r"""Exact conservation algebra of Pacioli's Venetian *Quaderno* & *Problem of Points* (1494).

Models *Part I, Distinctio IX, Tractatus X–XI* (fols. 197r–210v) of Fra Luca Pacioli's
*Summa de arithmetica, geometria, proportioni et proportionalita* (Venice, 1494):

1. **Venetian Money of Account** (*fol. 201v*): Exact rational arithmetic in the four
   ledger columns ``l[ire] s[oldi] g[rossi] p[icioli]`` (*a oro*, where
   :math:`1\text{ lira} = 10\text{ ducati} = 20\text{ soldi}`,
   :math:`1\text{ soldo} = 12\text{ grossi}`, :math:`1\text{ ducato} = 24\text{ grossi}`,
   :math:`1\text{ grosso} = 32\text{ piccoli}`).
2. **Skew-Symmetric Conservation Algebra of Double-Entry Bookkeeping**
   (*Particularis de computis et scripturis*, fols. 198v–210v): Models every *Giornale*
   entry ``Per <Debitore> // A <Creditore>`` as a directed edge in a conservation network
   with oriented incidence matrix :math:`B` (:math:`\mathbf{1}^T B = \mathbf{0}^T`) and
   skew-symmetric flow matrix :math:`F = -F^T`, proving the *Summa summarum* identity
   :math:`\sum \text{Dare} = \sum \text{Avere}`, Pacioli's *Cassa* non-negativity rule
   (fol. 201r), and *Bilancio del libro* closure via *Pro e Danno* :math:`\to` *Capitale*.
3. **The Problem of Points (*Giuoco della Balla & Balestrare*, fol. 197r–197v)**:
   Exact rational comparison between Pacioli's 1494 past-score proportionality rule and
   the 1654 Pascal–Fermat combinatorial expectation for two or more players.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import sympy as sp

__all__ = [
    "AccountSummary",
    "JournalEntry",
    "ProblemOfPointsResult",
    "QuadernoLedger",
    "TrialBalanceReport",
    "VenetianAmount",
    "build_venetian_merchant_quaderno_1493",
    "compare_problem_of_points",
]

PICCOLI_PER_GROSSO = 32
GROSSI_PER_SOLDO = 12
SOLDI_PER_LIRA = 20
GROSSI_PER_DUCATO = 24
PICCOLI_PER_SOLDO = GROSSI_PER_SOLDO * PICCOLI_PER_GROSSO  # 384
PICCOLI_PER_DUCATO = GROSSI_PER_DUCATO * PICCOLI_PER_GROSSO  # 768
PICCOLI_PER_LIRA = SOLDI_PER_LIRA * PICCOLI_PER_SOLDO  # 7680 (= 10 ducati)


@dataclass(frozen=True)
class VenetianAmount:
    """Exact Venetian money of account (``lire, soldi, grossi, piccoli`` *a oro*, fol. 201v)."""

    piccoli_total: sp.Integer

    @classmethod
    def from_lsgp(
        cls,
        lire: int = 0,
        soldi: int = 0,
        grossi: int = 0,
        piccoli: int = 0,
    ) -> VenetianAmount:
        """Construct an exact amount from ``(lire, soldi, grossi, piccoli)`` columns."""
        total = (
            sp.Integer(lire) * PICCOLI_PER_LIRA
            + sp.Integer(soldi) * PICCOLI_PER_SOLDO
            + sp.Integer(grossi) * PICCOLI_PER_GROSSO
            + sp.Integer(piccoli)
        )
        return cls(piccoli_total=total)

    @classmethod
    def from_ducati(
        cls,
        ducati: int = 0,
        grossi: int = 0,
        piccoli: int = 0,
    ) -> VenetianAmount:
        """Construct an exact amount from Venetian gold ducats (``24 grossi = 1 ducato``)."""
        total = (
            sp.Integer(ducati) * PICCOLI_PER_DUCATO
            + sp.Integer(grossi) * PICCOLI_PER_GROSSO
            + sp.Integer(piccoli)
        )
        return cls(piccoli_total=total)

    def to_lsgp(self) -> tuple[int, int, int, int]:
        """Decompose into canonical ``(lire, soldi, grossi, piccoli)`` columns."""
        sign = -1 if self.piccoli_total < 0 else 1
        rem = abs(int(self.piccoli_total))
        lire, rem = divmod(rem, PICCOLI_PER_LIRA)
        soldi, rem = divmod(rem, PICCOLI_PER_SOLDO)
        grossi, piccoli = divmod(rem, PICCOLI_PER_GROSSO)
        return (sign * lire, sign * soldi, sign * grossi, sign * piccoli)

    def to_ducati_rational(self) -> sp.Rational:
        """Express the exact value in Venetian gold ducats as a ``sympy.Rational``."""
        return sp.Rational(self.piccoli_total, PICCOLI_PER_DUCATO)

    def to_lire_rational(self) -> sp.Rational:
        """Express the exact value in Venetian *lire di grossi* as a ``sympy.Rational``."""
        return sp.Rational(self.piccoli_total, PICCOLI_PER_LIRA)

    def format_venetian(self) -> str:
        """Format in Pacioli's four-column Venetian ledger notation (``l. s. g. p.``)."""
        lire, soldi, grossi, piccoli = self.to_lsgp()
        return f"l. {lire} s. {soldi} g. {grossi} p. {piccoli}"

    def __add__(self, other: VenetianAmount) -> VenetianAmount:
        """Add two exact Venetian amounts."""
        return VenetianAmount(self.piccoli_total + other.piccoli_total)

    def __sub__(self, other: VenetianAmount) -> VenetianAmount:
        """Subtract two exact Venetian amounts."""
        return VenetianAmount(self.piccoli_total - other.piccoli_total)


@dataclass(frozen=True)
class JournalEntry:
    """Single Venetian *Giornale* entry ``Per <debit_account> // A <credit_account>``."""

    entry_no: int
    date: str
    debit_account: str
    credit_account: str
    amount: VenetianAmount
    narrative: str

    def format_giornale(self) -> str:
        """Render the entry in Pacioli's Venetian *Giornale* syntax (fol. 201r–201v)."""
        return (
            f"{self.entry_no}. ({self.date}) Per {self.debit_account} // A {self.credit_account} "
            f"— {self.narrative} [{self.amount.format_venetian()}]"
        )


@dataclass(frozen=True)
class AccountSummary:
    """T-account summary in the *Quaderno grande* (Dare on left, Avere on right)."""

    folio: int
    name: str
    kind: str
    dare_ducati: sp.Rational
    avere_ducati: sp.Rational
    net_dare_ducati: sp.Rational


@dataclass(frozen=True)
class TrialBalanceReport:
    """Exact *Summa summarum* and conservation verification of the *Quaderno*."""

    accounts: tuple[AccountSummary, ...]
    summa_dare_ducati: sp.Rational
    summa_avere_ducati: sp.Rational
    net_conservation_sum: sp.Rational
    is_balanced: bool
    cassa_non_negative: bool


@dataclass(frozen=True)
class ProblemOfPointsResult:
    """Comparison of Pacioli's 1494 rule vs. Pascal–Fermat 1654 expectation."""

    target_rounds: int
    current_scores: tuple[int, ...]
    total_stake_ducati: sp.Rational
    pacioli_shares: tuple[sp.Rational, ...]
    pascal_fermat_probabilities: tuple[sp.Rational, ...]
    pascal_fermat_shares: tuple[sp.Rational, ...]
    discrepancies: tuple[sp.Rational, ...]


class QuadernoLedger:
    """Directed-graph conservation model of Pacioli's *Quaderno grande* (Venice, 1494)."""

    def __init__(self) -> None:
        """Initialize an empty Venetian *Quaderno* with alphabetical *Repertorio*."""
        self._account_order: list[str] = []
        self._account_kinds: dict[str, str] = {}
        self._account_folios: dict[str, int] = {}
        self._entries: list[JournalEntry] = []

    @property
    def accounts(self) -> list[str]:
        """Ordered list of registered ledger accounts."""
        return list(self._account_order)

    @property
    def entries(self) -> list[JournalEntry]:
        """Chronological list of posted *Giornale* entries."""
        return list(self._entries)

    def register_account(self, name: str, kind: str = "real") -> int:
        """Register an account in the *Alfabeto / Repertorio* and return its *Quaderno* folio.

        Args:
            name: Account title (e.g., ``"Cassa de contanti"``, ``"Cavedal"``).
            kind: Account category (``"cassa"``, ``"capitale"``, ``"mercanzia"``,
                ``"personal"``, ``"nominal"``, ``"pro_e_danno"``, ``"bilancio"``).

        Returns:
            1-indexed *Quaderno* folio (*carta*) number.
        """
        if name in self._account_folios:
            return self._account_folios[name]
        folio = len(self._account_order) + 1
        self._account_order.append(name)
        self._account_kinds[name] = kind
        self._account_folios[name] = folio
        return folio

    def post(
        self,
        date: str,
        debit_account: str,
        credit_account: str,
        amount: VenetianAmount,
        narrative: str,
        *,
        debit_kind: str = "real",
        credit_kind: str = "real",
    ) -> JournalEntry:
        """Post a *Giornale* item ``Per <debit> // A <credit>`` to both *Quaderno* folios.

        Enforces Pacioli's Cap. 14 rule (fol. 202r): *mai si deue mettere cosa in dare
        che quella ancora non si ponga in hauere*.

        Args:
            date: Venetian entry date string.
            debit_account: Debtor account prefixed by ``Per``.
            credit_account: Creditor account prefixed by ``A``.
            amount: Strictly positive :class:`VenetianAmount`.
            narrative: Brief *Giornale* description distilled from the *Memoriale*.
            debit_kind: Category if ``debit_account`` is not yet registered.
            credit_kind: Category if ``credit_account`` is not yet registered.

        Returns:
            The recorded :class:`JournalEntry`.
        """
        if debit_account == credit_account:
            raise ValueError("Self-loop entry forbidden: debtor and creditor must be distinct.")
        if amount.piccoli_total <= 0:
            raise ValueError("Posted ledger amount must be strictly positive.")

        self.register_account(debit_account, kind=debit_kind)
        self.register_account(credit_account, kind=credit_kind)
        entry = JournalEntry(
            entry_no=len(self._entries) + 1,
            date=date,
            debit_account=debit_account,
            credit_account=credit_account,
            amount=amount,
            narrative=narrative,
        )
        self._entries.append(entry)
        return entry

    def incidence_matrix(self) -> sp.Matrix:
        r"""Return oriented vertex-edge incidence matrix :math:`B \in \{-1, 0, +1\}^{|V| \times |E|}`.

        For entry :math:`e` (``Per u // A v``), :math:`B_{u, e} = +1` (Dare) and
        :math:`B_{v, e} = -1` (Avere), so :math:`\mathbf{1}^T B = \mathbf{0}^T`.
        """
        n_acc = len(self._account_order)
        n_ent = len(self._entries)
        idx = {name: i for i, name in enumerate(self._account_order)}
        mat = sp.zeros(n_acc, n_ent)
        for col, ent in enumerate(self._entries):
            mat[idx[ent.debit_account], col] = sp.Integer(1)
            mat[idx[ent.credit_account], col] = sp.Integer(-1)
        return mat

    def weight_vector_ducati(self) -> sp.Matrix:
        r"""Return column vector :math:`w \in \mathbb{Q}^{|E|}` of transaction weights in ducats."""
        return sp.Matrix([ent.amount.to_ducati_rational() for ent in self._entries])

    def skew_symmetric_flow_matrix(self) -> sp.Matrix:
        r"""Return skew-symmetric pairwise flow matrix :math:`F \in \mathbb{Q}^{|V| \times |V|}`.

        Entry :math:`F_{i,j}` equals net ducats debited to account :math:`i` against credit
        to account :math:`j`, satisfying :math:`F^T = -F` identically.
        """
        n_acc = len(self._account_order)
        idx = {name: i for i, name in enumerate(self._account_order)}
        flow = sp.zeros(n_acc, n_acc)
        for ent in self._entries:
            i = idx[ent.debit_account]
            j = idx[ent.credit_account]
            val = ent.amount.to_ducati_rational()
            flow[i, j] += val
            flow[j, i] -= val
        return flow

    def trial_balance(self) -> TrialBalanceReport:
        """Compute Pacioli's *Summa summarum* and verify all conservation invariants."""
        dare: dict[str, sp.Rational] = {name: sp.Rational(0) for name in self._account_order}
        avere: dict[str, sp.Rational] = {name: sp.Rational(0) for name in self._account_order}

        for ent in self._entries:
            val = ent.amount.to_ducati_rational()
            dare[ent.debit_account] += val
            avere[ent.credit_account] += val

        summaries: list[AccountSummary] = []
        cassa_ok = True
        for name in self._account_order:
            d_val = dare[name]
            a_val = avere[name]
            net = d_val - a_val
            kind = self._account_kinds[name]
            if kind == "cassa" and net < 0:
                cassa_ok = False
            summaries.append(
                AccountSummary(
                    folio=self._account_folios[name],
                    name=name,
                    kind=kind,
                    dare_ducati=d_val,
                    avere_ducati=a_val,
                    net_dare_ducati=net,
                )
            )

        sum_dare = sum((s.dare_ducati for s in summaries), sp.Rational(0))
        sum_avere = sum((s.avere_ducati for s in summaries), sp.Rational(0))
        net_sum = sum((s.net_dare_ducati for s in summaries), sp.Rational(0))

        return TrialBalanceReport(
            accounts=tuple(summaries),
            summa_dare_ducati=sum_dare,
            summa_avere_ducati=sum_avere,
            net_conservation_sum=net_sum,
            is_balanced=(sum_dare == sum_avere and net_sum == 0),
            cassa_non_negative=cassa_ok,
        )

    def close_to_bilancio(
        self,
        date: str = "1493-12-31",
        pro_e_danno_account: str = "Pro e Danno",
        capitale_account: str = "Cavedal",
        bilancio_account: str = "Bilancio del libro",
    ) -> sp.Rational:
        """Execute Pacioli's Cap. 27 & Cap. 34 closing cycle (*Pro e Danno* -> *Cavedal* -> *Bilancio*).

        First sweeps all ``"mercanzia"`` (closed venture) and ``"nominal"`` accounts into
        *Pro e Danno*, transfers net profit/loss from *Pro e Danno* to *Cavedal* (Cap. 27),
        and finally closes all remaining open asset/liability/capital accounts into
        *Bilancio del libro* (Cap. 34), bringing every account's net balance to ``0``.

        Args:
            date: Closing date string.
            pro_e_danno_account: Profit-and-loss summary account name.
            capitale_account: Merchant's capital account name.
            bilancio_account: Final closing balance account name.

        Returns:
            Exact net profit (positive) or loss (negative) in ducats transferred to *Cavedal*.
        """
        self.register_account(pro_e_danno_account, kind="pro_e_danno")
        self.register_account(capitale_account, kind="capitale")
        self.register_account(bilancio_account, kind="bilancio")

        def _piccoli_net(acc_name: str) -> sp.Integer:
            tot = sp.Integer(0)
            for ent in self._entries:
                if ent.debit_account == acc_name:
                    tot += ent.amount.piccoli_total
                elif ent.credit_account == acc_name:
                    tot -= ent.amount.piccoli_total
            return tot

        # Step 1: Close nominal accounts into Pro e Danno
        for name in list(self._account_order):
            if self._account_kinds[name] == "nominal":
                net_p = _piccoli_net(name)
                if net_p > 0:
                    self.post(
                        date,
                        pro_e_danno_account,
                        name,
                        VenetianAmount(net_p),
                        f"Saldo di {name} in Pro e Danno",
                    )
                elif net_p < 0:
                    self.post(
                        date,
                        name,
                        pro_e_danno_account,
                        VenetianAmount(-net_p),
                        f"Utile di {name} in Pro e Danno",
                    )

        # Step 2: Close Pro e Danno into Cavedal (net credit in Pro e Danno = profit)
        ped_net = _piccoli_net(pro_e_danno_account)
        net_profit_ducati = sp.Rational(-ped_net, PICCOLI_PER_DUCATO)
        if ped_net < 0:
            self.post(
                date,
                pro_e_danno_account,
                capitale_account,
                VenetianAmount(-ped_net),
                "Utile netto portato a Cavedal (Cap. 27)",
            )
        elif ped_net > 0:
            self.post(
                date,
                capitale_account,
                pro_e_danno_account,
                VenetianAmount(ped_net),
                "Danno netto portato a Cavedal (Cap. 27)",
            )

        # Step 3: Close all remaining real/personal/capital balances into Bilancio del libro
        for name in list(self._account_order):
            if name == bilancio_account:
                continue
            net_p = _piccoli_net(name)
            if net_p > 0:
                self.post(
                    date,
                    bilancio_account,
                    name,
                    VenetianAmount(net_p),
                    f"Saldo debitore portato in {bilancio_account}",
                )
            elif net_p < 0:
                self.post(
                    date,
                    name,
                    bilancio_account,
                    VenetianAmount(-net_p),
                    f"Saldo creditore portato in {bilancio_account}",
                )

        return net_profit_ducati


def build_venetian_merchant_quaderno_1493() -> QuadernoLedger:
    """Construct a canonical Venetian *Quaderno* modeled on *Summa* fols. 201v–210r (Nov. 1493).

    Includes opening inventory of cash and gems against *Cavedal*, purchase of sugar
    and Ginger (*zenzer mechini*, fol. 201v item 7), credit sale to Martino da Foro,
    brokerage expense (*Spese de mercanzia*), partial cash settlement, and profit transfer.

    Returns:
        Populated :class:`QuadernoLedger` prior to final closing.
    """
    ledger = QuadernoLedger()
    ledger.register_account("Cassa de contanti", kind="cassa")
    ledger.register_account("Cavedal", kind="capitale")
    ledger.register_account("Gioie ligate e disligate", kind="mercanzia")
    ledger.register_account("Zenzer mechini", kind="mercanzia")
    ledger.register_account("Antonio da Cremona", kind="personal")
    ledger.register_account("Martino da Foro", kind="personal")
    ledger.register_account("Spese de mercanzia", kind="nominal")
    ledger.register_account("Utile de zenzer", kind="nominal")

    # 1. Opening cash inventory (fol. 201v, 8 Nov 1493): 500 ducats = l. 50 s. 0 g. 0 p. 0
    ledger.post(
        "1493-11-08",
        "Cassa de contanti",
        "Cavedal",
        VenetianAmount.from_ducati(500),
        "Contanti in oro e monete posto in cassa da inventario (fol. 201v)",
    )
    # 2. Opening gem inventory (fol. 201v, item 2): 240 ducats
    ledger.post(
        "1493-11-08",
        "Gioie ligate e disligate",
        "Cavedal",
        VenetianAmount.from_ducati(240),
        "Balassi, rubini e diamanti a comun corso da inventario",
    )
    # 3. Purchase of Mecca ginger half cash, half credit (Cap. 9, 9 modi del comprare): 180 ducats
    ledger.post(
        "1493-11-12",
        "Zenzer mechini",
        "Cassa de contanti",
        VenetianAmount.from_ducati(90),
        "Colli di zenzer mechini comprati parte a contanti",
    )
    ledger.post(
        "1493-11-12",
        "Zenzer mechini",
        "Antonio da Cremona",
        VenetianAmount.from_ducati(90),
        "Resto di zenzer mechini comprati a termine",
    )
    # 4. Weighing and Fondaco dei Tedeschi brokerage fee: 6 ducats 12 grossi (= 6.5 ducats)
    ledger.post(
        "1493-11-14",
        "Spese de mercanzia",
        "Cassa de contanti",
        VenetianAmount.from_ducati(6, 12, 0),
        "Sansaria di Messetaria e pesadori al Fondaco",
    )
    # 5. Sale of the entire lot of ginger to Martino da Foro for 230 ducats (cost 180 + gain 50)
    ledger.post(
        "1493-11-20",
        "Martino da Foro",
        "Zenzer mechini",
        VenetianAmount.from_ducati(180),
        "Costo dei colli di zenzer venduti a Martino da Foro",
    )
    ledger.post(
        "1493-11-20",
        "Martino da Foro",
        "Utile de zenzer",
        VenetianAmount.from_ducati(50),
        "Guadagno sopra la partita di zenzer mechini",
    )
    # 6. Partial cash collection from Martino da Foro: 150 ducats
    ledger.post(
        "1493-11-26",
        "Cassa de contanti",
        "Martino da Foro",
        VenetianAmount.from_ducati(150),
        "Contanti ricevuti a bon conto da Martino da Foro",
    )
    return ledger


@lru_cache(maxsize=None)
def _exact_win_probs(needs: tuple[int, ...]) -> tuple[sp.Rational, ...]:
    """Exact symmetric fair-trial winning probabilities for ``m`` players needing ``needs[i]`` points."""
    m = len(needs)
    for idx, rem in enumerate(needs):
        if rem <= 0:
            return tuple(sp.Rational(1 if j == idx else 0) for j in range(m))

    weight = sp.Rational(1, m)
    accum = [sp.Rational(0) for _ in range(m)]
    for winner in range(m):
        nxt = list(needs)
        nxt[winner] -= 1
        sub_probs = _exact_win_probs(tuple(nxt))
        for j in range(m):
            accum[j] += weight * sub_probs[j]
    return tuple(accum)


def compare_problem_of_points(
    target_rounds: int = 6,
    current_scores: tuple[int, ...] = (5, 3),
    total_stake_ducati: int | sp.Expr = 10,
) -> ProblemOfPointsResult:
    """Compare Pacioli's 1494 *balla* / *balestrare* division against Pascal–Fermat (1654).

    Covers both the classic two-player *giuoco della balla* on fol. 197r (e.g., ``(5, 3)``
    or ``(5, 2)`` playing to ``6`` for ``10`` ducats) and Problem 51 on fol. 197v
    (three crossbowmen *a balestrare* playing to ``6`` best shots for ``10`` ducats,
    interrupted at ``(4, 3, 2)``).

    Args:
        target_rounds: Winning score threshold (e.g., ``6``).
        current_scores: Tuple of positive/non-negative scores below ``target_rounds``.
        total_stake_ducati: Total pot in ducats (default ``10``).

    Returns:
        Exact :class:`ProblemOfPointsResult` with `sp.Rational` shares and discrepancies.
    """
    if len(current_scores) < 2:
        raise ValueError("At least two players are required.")
    if any(s < 0 or s >= target_rounds for s in current_scores):
        raise ValueError("Scores must satisfy 0 <= score < target_rounds.")
    score_sum = sum(current_scores)
    if score_sum <= 0:
        raise ValueError("At least one point must have been scored for Pacioli's rule.")

    stake = sp.Rational(sp.sympify(total_stake_ducati))
    pacioli = tuple(stake * sp.Rational(s, score_sum) for s in current_scores)

    needs = tuple(target_rounds - s for s in current_scores)
    pf_probs = _exact_win_probs(needs)
    pf_shares = tuple(stake * p for p in pf_probs)
    diffs = tuple(pf - pac for pf, pac in zip(pf_shares, pacioli, strict=True))

    return ProblemOfPointsResult(
        target_rounds=target_rounds,
        current_scores=tuple(current_scores),
        total_stake_ducati=stake,
        pacioli_shares=pacioli,
        pascal_fermat_probabilities=pf_probs,
        pascal_fermat_shares=pf_shares,
        discrepancies=diffs,
    )
