"""Scholarly English translations (using GEOMETOR semantic RST directives and roles)
and Critical Commentary / Translation Notes for Part I, Sections 1 & 2 (Chapters I-XXIII)
of Fra Luca Pacioli's Compendio de Divina Proportione (1509).
"""

from __future__ import annotations
from typing import Dict, Any

CHAPTERS_1_TO_23: Dict[int, Dict[str, str]] = {
    1: {
        "title_en": (
            "Epistle on the Divine Proportion to the Most Excellent Prince Ludovico Maria Sforza Anglo, "
            "Duke of Milan, Ornament of Peace and War, by Brother Luca Pacioli of Borgo Sansepolcro "
            "of the Order of Minorites, Professor of Sacred Theology"
        ),
        "body_en": """\
In the course of the years of our salvation 1498, on the ninth day of February, Most Exalted Duke, when I was present before Your Excellency within the impregnable citadel of Your illustrious city of Milan—the most worthy seat of Your customary residence—at that laudable and scientific duel attended by so many most celebrated and wise men of every rank, both religious and secular, in whom Your magnificent court continually abounds:

Among their number, besides the Most Reverend Lordships of Bishops, Protonotaries, and Abbots, there were from our sacred Seraphic Order the Reverend Father and sublime theologian Magister Gometius, the most worthy herald of Sacred Scripture Brother Domenico surnamed Ponzone, and the Most Reverend Father Magister Francesco Busti, currently appointed Regent of our worthy convent in Milan. And among the laymen there was first my especial patron, the Illustrious Lord Galeazzo Sanseverino, son-in-law of Your Ducal Highness and most valiant Captain General, second to none in arms today and a diligent follower of our mathematical disciplines. There were also egregious orators of the most illustrious powers, and the supreme masters of medicine and astronomy: the most renowned and acute investigator of Serapion, Avicenna, and the celestial bodies, and interpreter of future things, Ambrogio da Rosate; the most learned healer of all ailments, Aloisio Marliani; and the most perceptive observer of every branch of medicine, Gabriele Pirovano; together with Nicolò Cusano, greatly admired and venerated by all the aforesaid in every subject mentioned above, and Andrea da Novara, most skilled in the same professions; as well as other distinguished and most learned Doctors of Both Laws, and counselors, secretaries, and chancellors of Your most ornate magistracy.

In their company were the most perspicacious architects and engineers and tireless inventors of new things: Leonardo da Vinci, our Florentine compatriot, who in sculpture, bronze-casting, and painting verifies his surname against all rivals—as is manifest in the admirable and stupendous equestrian statue, whose height from the crown of the head to the level ground is 12 *braccia*, that is, $37\\frac{4}{5}$ times the length of the line :g:`ab` printed here, while its entire bronze mass amounts to nearly 200,000 pounds (where each pound consists of twelve common ounces), dedicated to the most blessed and unconquered memory of Your father, and wholly free from any envy of the steeds of Phidias and Praxiteles on Monte Cavallo; and likewise in the graceful simulacrum of the ardent desire for our salvation [*The Last Supper*], painted by his own hand in the worthy and devout place of bodily and spiritual refection of the sacred Temple of the Graces [*Santa Maria delle Grazie*], before which Apelles, Myron, Polykleitos, and the rest must today clearly yield. Nor is he satisfied with these, for having already brought to completion with all diligence his worthy book on painting and human movements, he now strives with every study to bring to due completion his inestimable work on local motion, percussion, weights, and all forces, that is, accidental weights. And beside him was Giacomo Andrea da Ferrara, as dear to him as a brother, the most accurate follower of the works of Vitruvius, yet in no way diminished in his singular military skill.

There Your Highness, with golden and mellifluous words, declared that he who is endowed with any virtue and willingly communicates it to others is worthy of the highest commendation before God and the world; for from this there arises charity toward one's neighbor and praise and honor to oneself, in imitation of the sacred saying: *Quam sine fictione didici, et sine invidia communico* ("That which I learned without guile, I communicate gladly without envy," Wisdom 7:13). The meaning of those most sweet words fixed itself so firmly in my mind that nothing was ever carved more durably in marble.

And although it was already almost innate in me by nature to practice the like toward everyone—especially in those faculties wherewith the Most High in His immense bounty was pleased to endow me above others, namely the necessary sciences and most worthy mathematical disciplines—nevertheless, already weary from laborious toils both by day and by night, bodily as well as spiritual (all of which is openly manifest to anyone who diligently examines our great work [*Summa de Arithmetica, Geometria, Proportioni et Proportionalita*] compiled on similar disciplines and faculties and dedicated to Your Highness's magnanimous kinsman Guidobaldo, Duke of Urbino, together with the other matters treated in its Fifth Distinction), I had already resolved, along with others, to withdraw to a sheltered haven and reckon up my years.

Yet, greatly stirred by Your words, I took breath again upon the deserted shore; and as a seasoning to every other work of ours composed in these faculties, and for the supreme and delightful savor of all the aforesaid sciences and mathematical disciplines, for Your Ducal Highness and for the utility of Your reverent subjects, as well as for the adornment and perfect ornament of Your most worthy library—decked with an innumerable multitude of volumes in every faculty and doctrine—I resolved to compose this brief compendium and most useful treatise entitled *On the Divine Proportion*. Together with it I have arranged all the material models of the geometric bodies contained herein, which will arouse no less admiration in everyone who visits Your library than all the other volumes and worthy treasures preserved therein, inasmuch as these forms have hitherto remained hidden from living men.

In this work we shall speak of high and sublime things that are truly the touchstone and assaying-cup (*cimento e copella*) of all the aforesaid sciences and disciplines, and from which every other speculative, scientific, practical, and mechanical operation derives; without knowledge and presupposition of which it is impossible to understand or perform any human work well, as will be demonstrated. Wherefore Your Ducal Highness, with Your acute intelligence, will exhort Your courtiers and other reverent subjects to peruse it with delight, supreme pleasure, and most useful fruit. For these are not old wives' tales (*faule anili*) or other ridiculous and false jests, nor mendacious and incredible poetic inventions that feed the ears with mere smoke. For although false things, according to the Philosopher [Aristotle], may be useful to us through their kinship with the true consequences that follow from them—just as the reverse is opposite to the obverse—much more will true things be useful and profitable to us, since from them nothing but truth proceeds.

And among true things, as Aristotle and Averroes affirm, our mathematical sciences are the truest and stand in the first degree of certainty (*in primo gradu certitudinis*), while all the natural sciences follow after them. Let this suffice as an introduction and argument for what follows. Hence it clearly appears, Most Exalted Duke, that all other sciences are matters of opinion, and that these alone deserve to be called certainties. Among physicians, for instance—Avicenna, Galen, Hippocrates, and the rest—it happens that one says the life of man resides in the heart, another in the brain, and another in the blood, each adducing many reasons and arguments in corroboration. Thus it is never good to forsake things that are certain for those that are doubtful, since the latter are called vain by the wise; whence the verse: *Non debent certa pro vanis relinqui* ("Certain things must not be forsaken for vain ones"). With all humility and due reverence toward Your Ducal Highness, to whom I continually and most highly commend myself: *Quae felicissime ad vota valeat* ("May You prosper most happily according to Your wishes").""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **The Scientific Duel of February 9, 1498**: Pacioli opens Part I with a vivid eyewitness account of a *laudabile e scientifico duello* (an academic disputation) held on February 9, 1498 in the Castello Sforzesco of Milan before Duke Ludovico Maria Sforza ("il Moro", 1452–1508). This courtly gathering brings together Franciscan Scholastic theologians, military commanders, court physicians, astrologers, jurists, and Renaissance artist-engineers.
2. **Franciscan & Courtly Prosopography**:
   - **Magister Gometius**: Gomez de Lisboa (d. 1513), Portuguese Franciscan theologian at Pavia and Milan, later Vicar General of the Conventual Franciscans.
   - **Domenico Ponzone** and **Francesco Busti**: Prominent Milanese Franciscan preachers and regents of the Convent of San Francesco Grande.
   - **Galeazzo Sanseverino** (c. 1460–1525): Son-in-law of Ludovico Sforza, Captain General of the Milanese armies, and Pacioli's personal patron in Milan (to whom one of the three manuscript copies of *De Divina Proportione* was presented).
   - **Court Physicians & Astrologers**: Ambrogio Varese da Rosate (court astrologer and physician to Ludovico Sforza), Aloisio Marliani, Gabriele Pirovano, Nicolò Cusano (a Milanese physician, not the Cardinal Nicholas of Cusa who died in 1464), and Andrea da Novara.
3. **Leonardo da Vinci's Works in Milan**:
   - **The Sforza Equestrian Monument**: Pacioli records the exact dimensions of Leonardo's colossal clay model for the monument to Francesco Sforza: 12 Milanese *braccia* from the horse'spoll (*cervice*, misprinted *cerulee* in 1509) to the ground, which Pacioli calibrates directly against a printed reference segment :g:`ab` on Folio 0017r ($37\\frac{4}{5}$ times :g:`ab`), and an estimated bronze casting weight of 200,000 Milanese *libbre* (at 12 ounces per pound).
   - **The Last Supper (*Cenacolo*)**: Described as *el ligiadro de l'ardente desiderio de nostra salute simulacro* ("the graceful simulacrum of the ardent desire for our salvation", alluding to Luke 22:15, *Desiderio desideravi hoc pascha manducare vobiscum*) in the refectory of Santa Maria delle Grazie.
   - **Leonardo's Treatises**: Pacioli provides priceless documentary testimony that by 1498 Leonardo had already completed a treatise on painting and human movements (*libro de pictura e movimenti humani*) and was actively writing a treatise on mechanics: local motion, percussion, weights, and accidental forces (*del moto locale, dele percussioni e pesi e dele forze tutte*).
   - **Giacomo Andrea da Ferrara**: Architect and commentator on Vitruvius, closely bound to Leonardo as a brother (*suo quanto fratello*, misprinted *quarto fratello* in the 1509 edition, as Winterberg notes). He was executed by the French in May 1500 after the fall of Milan.
4. **Epistemological Primacy of Mathematics**: Pacioli cites Averroes's commentary on Aristotle's *Metaphysics* II (Book $\\alpha$, comm. 14–16): mathematical demonstrations occupy the "first degree of certainty" (*in primo gradu certitudinis*), whereas natural philosophy and medicine (exemplified by the classical controversy between Aristotle/Avicenna on the heart, Galen on the brain/liver, and Empedocles/Critias on the blood as the seat of life) remain subject to probable dispute.""",
    },
    2: {
        "title_en": (
            "Preface of the Reverend Father Magister Luca Pacioli of Borgo Sansepolcro, of the Order of "
            "Minorites and Professor of Sacred Theology, to the Compendium on the Divine Proportion "
            "drawn from the Mathematical Disciplines"
        ),
        "body_en": """\
*Propter admirari coeperunt philosophari* ("On account of wonder men began to philosophize," Aristotle, *Metaphysics* I.2, 982b12). The authority of the "Master of those who know" [Aristotle; cf. Dante, *Inferno* IV.131] holds, Most Exalted Duke, that knowledge took its beginning from sight; just as he affirms in another place, saying: *Quod nihil est in intellectu quin prius sit in sensu*—that is, nothing is in the intellect that has not first offered itself in some way to the senses. And among our senses, the wise conclude that sight is the noblest; whence even among the common people it is not undeservedly said that the eye is the first portal through which the intellect understands and tastes.

As is recorded in that place, when the priests of Egypt beheld the moon eclipsed, they stood in great wonder; and seeking the cause, they discovered through true science that this occurs naturally through the interposition of the earth between the sun and the moon, wherewith they remained satisfied. From that time forward, as their successors progressively refined their inquiries with the light of the five intellectual windows [the five senses], they filled an innumerable multitude of volumes with their profound sciences for our utility, inasmuch as one thought bursts forth from another (*l'uno pensier da l'altro scoppia*; Dante, *Inferno* XXIII.10), so that many others were born therefrom.

Reflecting within myself upon this, I resolved to take up the pen for this most useful compendium chosen from the mathematical sciences, and together with it, with my own hands, to fashion materially in their proper forms the solid bodies belonging thereto for the common utility, and to offer them along with the present compendium to Your Ducal Highness. On account of their unwonted aspect—like something descended from heaven in our own days—I do not doubt that Your graceful and perspicacious intellect will take the greatest pleasure therein, especially when, by that same light and with no less investigation than the ancient Egyptians applied to the eclipse, You discover with the aid and support of the present treatise the causes and sweetest harmony of such forms.

Wherefore I am certain that if in the past Your Highness has shown Yourself generous and munificent toward those who possessed even a part of such sciences and disciplines, in the future You will show Yourself far more magnanimous and bountiful still, and—what is more—will exhort with all diligent care Your dear courtiers, reverent subjects, and other well-wishers to acquire them. For these mathematical sciences are the foundation and ladder (*fondamento e scala*) for arriving at knowledge of every other science, because they stand in the first degree of certainty, as the Philosopher affirms when he says: *Mathematicae enim scientiae sunt in primo gradu certitudinis et naturales sequuntur eas* ("For the mathematical sciences are in the first degree of certainty, and the natural sciences follow them").

Without knowledge of them, it is impossible to understand any other science well. Moreover, in the Book of Wisdom (11:21) it is written: *Quod omnia consistunt in numero, pondere et mensura*—that is, everything that unfolds throughout the lower and upper universe is necessarily subject to number, weight, and measure; and in these three things Aurelius Augustine in *De Civitate Dei* says that the Supreme Artificer is most highly praised, because in them *fecit stare ea quae non erant* ("He caused to stand fast the things that were not").

Through Your loving exhortation, I perceive that many who are ignorant of such sweet fruit of utility will awaken from their torpor and mental slumber, and will devote themselves wholly to inquiring into it with every study and solicitude; and this will cause the age itself to be renewed in our time, and men to arrive with greater reality and swiftness at perfection in whatever science they study.

Furthermore, beyond renown and worthy commendation, it will increase no small probity in Your Ducal Highness's exalted dominion among Your dear courtiers and beloved subjects, making them ever prepared for its defense—no less than the noble, ingenious geometer and most worthy architect Archimedes did for his own homeland. He, as is written, by his new and varied inventions of machines long preserved the city of Syracuse safe and unharmed against the assault and warlike might of the Romans, until Marcus Marcellus sought to storm it by stealth.

Indeed, by daily experience it is not hidden from Your Ducal Highness (even as for many years Your illustrious father's memory [Francesco Sforza] was the author, preceptor, and standard thereof for all Italy and for both Transalpine and Cisalpine Gaul) that the defense of great and small commonwealths—otherwise called the military art—cannot be practiced egregiously with honor and profit without knowledge of Geometry, Arithmetic, and Proportion. Nor can any worthy army assigned to a siege or defense ever be said to be fully provided for unless there is found within it a dedicated engineer and deviser of new machines, such as we have just mentioned in the great geometer Archimedes at Syracuse.

If one examines carefully all artillery and siege engines in general—take whichever you will, such as bastions and other ramparts, bombards, *briccole*, trebuchets (*trabocchi*), mangonels, *rompheae*, ballistae, catapults, battering rams (*arieti*), and tortoises (*testudines*)—they will always be found to be fabricated and formed by the power of numbers, measure, and their proportions. What else are citadels (*rocche*), towers, ravelins, walls, outworks (*antemuri*), moats, bastioned keeps (*turrioni*), battlements (*merli*), mantlets, and other fortifications in towns, cities, and castles, if not pure geometry and proportions, poised and adjusted with due levels and plumb-lines (*archipendoli*)?

Through nothing else were the ancient Romans so victorious, as Vegetius, Frontinus, and other egregious authors write, than through their great care and diligent preparation of engineers and commanders by land and sea, whose sufficiency is impossible without the mathematical disciplines—namely Arithmetic, Geometry, and Proportions—as the ancient histories of Livy, Dionysius, Pliny, and others make clear and manifest. From these sources Roberto Valturio, the most skilled citizen of Rimini, drew all the machines he set forth in his worthy work entitled *De re militari* (*De instrumentis bellicis*), dedicated to the Illustrious Lord Sigismondo Pandolfo [Malatesta]. And the most blessed memory of Your Highness's close kinsman Federico da Montefeltro, Most Illustrious Duke of Urbino, caused all those machines and instruments—letter for letter as the said author of Rimini sets them forth in his book, and many more besides—to be carved in order by the hands of most worthy stonecutters and sculptors in a frieze of living and beautiful stone all around the base of the stupendous edifice of his noble and admirable Palace in Urbino. Thus too one reads in the *Commentaries* of Julius Caesar concerning his ingenious bridge [across the Rhine]; and even to this day, in the worthy Umbrian city of Todi, in the church of San Fortunato—our sacred convent—there still hang publicly a great multitude of huge hempen cables which the illustrious memory of Your father [Francesco Sforza] duly arranged for a bridge across the Tiber to win his famous victory.

By no other means, moreover, did our most subtle Doctor [John Duns] Scotus arrive at the loftiest speculations of Sacred Theology than through knowledge of the mathematical disciplines, as appears throughout his sacred works—especially if one examines the question in the Second Book of his *Sentences* where he inquires whether an angel has a proper and determinate place (*locus determinatus*) for its existence, wherein he clearly shows that he understood the entire sublime volume of our most perspicacious Megarian philosopher Euclid.

For no other reason, likewise, do all the texts of the "Prince of those who know" [Aristotle]—the *Physics*, *Metaphysics*, *Posterior Analytics*, and the rest—appear difficult, save through ignorance of the aforesaid disciplines. For no other reason is there a scarcity of good astronomers, save for the lack of arithmetic, geometry, proportions, and proportionalities; so that nine out of ten govern their judgments by tables, almanacs (*tacuini*), and other calculations made by Ptolemy, Albumasar, Alfraganus, Geber [Jabir ibn Aflah], King Alfonso, Giovanni Bianchini, Prosdocimo [de' Beldomandi], and others, which through the carelessness of copyists are often corrupted and vitiated; and consequently, trusting in them, they fall into the greatest and most manifest errors, to no small harm and prejudice of those who rely upon them.

The supreme subtlety of all municipal laws, too, consists—as experts therein have often explained to me—in adjudicating alluvial deposits and circumluvions of waters (*alluvioni e circumluvioni de l'acque*) caused by excessive flooding. On this subject their eminent chief, Bartolus of Sassoferrato, composed a special treatise entitled *Tyberiadis* [*De fluminibus*], in the preface of which he greatly extolled Geometry and Arithmetic, affirming that he had learned them from a friar of our Order named Brother Guido, Professor of Sacred Theology, in that treatise on what the Tiber sometimes gives and takes away through its flooding, especially in the region from Perugia toward Deruta—wherein, citing step by step our most perspicacious philosopher Euclid with rectilinear and curvilinear geometric figures, he guided his inquiry and brought it to a conclusion with the greatest subtlety.

I say nothing of the sweet and gentle harmony of music, nor of the supreme beauty and intellectual comfort of perspective, nor of the most skillful disposition of architecture, together with the description of the maritime and terrestrial universe [cosmography] and the doctrine of celestial bodies and aspects, because from what has already been said their dependence is clear. To spare the reader tedium, I pass over many other practical and speculative sciences along with all the mechanical arts necessary in human affairs, none of which can be acquired or maintained in due order without the aid of these disciplines.

Therefore one should not wonder if good mathematicians are few in our times: for the scarcity of good teachers is the cause thereof, together with gluttony, sleep, and idle feather-beds (*la gola, il sonno e l'oziose piume*; Petrarch, *Canzoniere* VII.1), and in part the weakness of more recent minds. Whence among the wise it is magisterially customary to say as a common proverb: *Aurum probatur igni et ingenium mathematicis*—that is, fire proves the goodness of gold, and the mathematical disciplines prove the excellence of the intellect. This means in substance that a keen intellect is most suited to mathematics, since these sciences are of the greatest abstraction and subtlety, having always to be considered apart from sensible matter; and truly they are, as the Tuscan proverb says, those that "split a hair in mid-air" (*spaccano el pelo in l'aire*).

For this reason the ancient and divine philosopher Plato not undeservedly denied entry into his celebrated Gymnasium [the Academy] to those unskilled in geometry, placing an inscription high above its main portal in large, legible letters with these formal words: *Nemo huc geometriae expers ingrediatur*—that is, let no one who is not a good geometer enter here. This he did because within geometry every other hidden science is found. Filled before him with its sweetest delight, that most diligent contemplator of nature, Pythagoras, upon discovering the property of the right angle (:just:`I.47`)—as is read of him and as Vitruvius recounts (*De architectura* IX.praef.6)—sacrificed a hundred oxen to the gods with the greatest festivity and jubilation, as will be told below.

Let this suffice at present in commendation of the mathematical sciences, the number of whose students in this Your illustrious city already begins to grow day by day through the grace of Your Ducal Highness, thanks to the assiduous public lectures recently instituted by You and the progress of the egregious auditors, as I expound to them clearly and with all diligence (in their judgment), according to the grace granted me therein by the Most High, the sublime volume of the aforesaid Euclid in the sciences of Arithmetic and Geometry, Proportions and Proportionalities. Having already brought its first ten Books to a most worthy conclusion—always interweaving our practical applications with his theory for their greater utility and fuller understanding—I now dedicate the remainder of my time to the present completion of this treatise.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Dantean and Petrarchan Echoes**: Pacioli weaves vernacular literary classics directly into his Scholastic Latin-Italian prose:
   - *el maistro de color ch'sano* ("the Master of those who know", Aristotle) is a direct quotation of Dante, *Inferno* IV.131.
   - *l'uno pensier da l'altro scoppia* ("one thought bursts forth from another") quotes Dante, *Inferno* XXIII.10.
   - *la gola, sonno e otiose piume* ("gluttony, sleep, and idle feather-beds") quotes the opening line of Petrarch's famous sonnet *La gola e 'l sonno e l'oziose piume Hanno del mondo ogni vertù sbandita* (*Rerum vulgarium fragmenta* VII).
2. **Material Models of the Polyhedra**: Pacioli explicitly states that he fashioned with his own hands (*de mia propria mano materialmente*) three-dimensional models of the regular and dependent polyhedra to accompany the treatise in the Ducal Library at Pavia/Milan. In May 1506, the Venetian Republic recorded Pacioli's presentation of three sets of sixty polyhedra fashioned in lightweight wood.
3. **Roberto Valturio and the Urbino Frieze**: Pacioli links classical military engineering (Archimedes at Syracuse, Caesar's Rhine bridge, Vegetius, Frontinus) to Roberto Valturio's *De re militari* (written c. 1455 for Sigismondo Pandolfo Malatesta of Rimini, printed at Verona in 1472) and the celebrated stone bas-reliefs (*Formelle dell'Arte della Guerra*, carved by Ambrogio Barocci after designs by Francesco di Giorgio Martini) that adorned the bench-frieze around the facade of Federico da Montefeltro's Ducal Palace in Urbino.
4. **Duns Scotus, Bartolus of Sassoferrato, and Euclid**:
   - **John Duns Scotus** (*Ordinatio* / *Opus Oxoniense* II, dist. 2, p. 2, q. 5–6) used geometric arguments on the divisibility of the continuum from Euclid's *Elements* to analyze angelic location (*ubi angelicum*) and motion.
   - **Bartolus of Sassoferrato** (1313–1357) composed his treatise *De fluminibus seu Tyberiadis* (1355) while watching the bends of the Tiber near Perugia; as Bartolus himself records in his prologue, he was assisted in the geometric division of alluvial islands and riverbeds by the Franciscan theologian and mathematician **Guido da Perpignano / Guido de Perusio**, citing Euclid's *Elements*.
5. **Pacioli's Public Chair of Mathematics in Milan**: Appointed by Ludovico Sforza in 1496, Pacioli notes at the end of Chapter II that he has just completed lecturing publicly through Books I–X of Euclid's *Elements* (incorporating practical algebra and arithmetic alongside Campanus's theoretical propositions) and is now devoting the remainder of his term to Books XI–XV and *De Divina Proportione*.""",
    },
    3: {
        "title_en": (
            "The Preface Being Ended, There Follows an Explanation of What Is Meant by This Name 'Mathematical'"
        ),
        "body_en": """\
This word *Mathematical*, Most Exalted Duke, is Greek, derived from $\\mu\\alpha\\theta\\eta\\mu\\alpha\\tau\\iota\\kappa\\acute{o}\\varsigma$ (*mathematikos* / $\\mu\\alpha\\theta\\eta\\tau\\acute{o}\\varsigma$), which in our tongue signifies *disciplinable* ("capable of being taught and learned"). And for our purpose, by the mathematical sciences and disciplines are understood **Arithmetic**, **Geometry**, **Astrology** [Astronomy], **Music**, **Perspective**, **Architecture**, and **Cosmography**, together with every other science dependent upon these.

Nevertheless, the wise commonly take only the first four—namely Arithmetic, Geometry, Astronomy, and Music [the classical *Quadrivium*]—and call the others *subalternate*, that is, dependent upon these four. So hold Plato, Aristotle, Isidore in his *Etymologies*, and Severinus Boethius in his *Arithmetic* (*De institutione arithmetica* I.1).

Yet our own judgment—however weak and lowly it may be—compels us to reckon them as either **three** or **five**: namely Arithmetic, Geometry, and Astronomy, excluding Music from the four for as many reasons as they exclude Perspective from the five; or else adding Perspective to the aforesaid four for as many reasons as they add Music to our three.

If they say that Music satisfies hearing, one of the natural senses, Perspective satisfies sight—which is all the more noble inasmuch as it is the first portal to the intellect. If they say that Music attends to sonorous number (*numerus sonorus*) and to the measure imported into the time of its prolations, Perspective attends to natural number according to its every definition and to the measure of the visual ray (*linea visuale*). If the former refreshes the soul through harmony, the latter delights it greatly through due distance and variety of colors. If the former considers its harmonic proportions, the latter considers both arithmetic and geometric proportions.

In short, Most Exalted Duke, up to this very hour and for many years now this question has contended within my head, and no one has yet made clear to me why there should be four rather than three or five. Still, I judge that so many wise men do not err, even if their sayings do not uproot my ignorance.

Alas, who is there that, beholding a graceful figure well disposed with its due lineaments, to which nothing seems lacking save breath alone, does not judge it a thing rather divine than human? Painting imitates nature as closely as anything can possibly be said to do. This appears manifestly before our eyes in the aforesaid simulacrum of the ardent desire for our salvation [*The Last Supper*], wherein it is impossible to imagine the Apostles more alive at the sound of the voice of infallible Truth when He said: *Unus vestrum me traditurus est* ("One of you is about to betray me," Matthew 26:21)—where with actions and gestures toward one another, in living and afflicted astonishment, they seem truly to speak, so worthily has our Leonardo disposed it with his graceful hand!

So too we read in Pliny concerning paintings (*Natural History* XXXV.65) about Zeuxis and Parrhasius: when they entered into a contest in the same art, challenging each other with the brush, Zeuxis painted a basket of grapes set among vine-leaves and placed it in public, whereupon the birds were deceived and flew down to peck at it as though it were real. Parrhasius then painted a linen curtain; and when he too had set his work in public, Zeuxis, believing it to be a real curtain covering his rival's painting, said to Parrhasius: "Draw back the curtain and let everyone see your work, as mine was seen!"—and thus he was vanquished, confessing that whereas he had deceived birds, irrational animals, Parrhasius had deceived a rational being and a master of the art itself.

Perhaps, then, my great delight and supreme love for perspective (though I myself am unpracticed in the brush) does not deceive me; for universally there is no gentle spirit in whom painting does not awaken delight, seeing that it draws to itself both rational and irrational creatures alike. Wherefore I shall abide by this opinion until someone shows me otherwise: that there are either three principal mathematical sciences with the others subalternate, or else five if Music is numbered among them, since it seems to me that Perspective must on no account be placed behind it, being worthy of no less praise. And since this is no article of faith, I am certain I shall be indulged therein. Let this suffice concerning the meaning of the said name.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **The Lacuna for the Greek Word in the 1509 Printing**: In the 1509 Paganini edition (Folio 0021r), the compositor left a blank space after *derivato da* for the Greek word $\\mu\\alpha\\theta\\eta\\mu\\alpha\\tau\\iota\\kappa\\acute{o}\\varsigma$ (or $\\mu\\alpha\\nu\\theta\\acute{\\alpha}\\nu\\omega$ / $\\mu\\acute{\\alpha}\\theta\\eta\\mu\\alpha$), which Pacioli regularly glosses in his *Summa* and his 1509 edition of Euclid as *disciplinabile*.
2. **Reforming the Quadrivium — Perspective as a Liberal Art**: Chapter III is one of the defining documents of the Italian Renaissance elevation of the visual arts from *artes mechanicae* to *artes liberales*. Challenging Boethius's canonical fourfold *Quadrivium* (Arithmetic, Music, Geometry, Astronomy), Pacioli argues on strictly parallel epistemological and mathematical grounds that *Prospectiva* (linear perspective and the science of visual rays, pioneered by Piero della Francesca, Leon Battista Alberti, and Leonardo da Vinci) stands on an equal footing with Music:
   - **Sense Hierarchy**: Sight (*el vedere*, the *prima porta al intellecto*) is nobler than hearing (*l'udito*).
   - **Mathematical Object**: Measure of the visual ray (*linea visuale*) and natural number vs. sonorous number (*numero sonoro*) and musical time (*tempo de sue prolationi*).
   - **Proportional Scope**: Arithmetic and geometric proportions of foreshortening vs. harmonic proportions.
3. **Second Ekphrasis of Leonardo's *Last Supper***: Pacioli specifies the exact dramatic moment depicted by Leonardo in the refectory of Santa Maria delle Grazie: Christ's words *Unus vestrum me traditurus est* (Matthew 26:21), capturing the Apostles' *acti e gesti* ("actions and gestures", corresponding directly to Leonardo's theory of *moti mentali* expressed through bodily movements).""",
    },
    4: {
        "title_en": (
            "On Those Things Which the Reader Must Observe for the Understanding of This Treatise"
        ),
        "body_en": """\
Furthermore, for the avoidance of difficulty in what follows, let the reader note that whenever we cite "the first of the first" (:just:`I.1`), "the fourth of the second" (:just:`II.4`), "the tenth of the fifth" (:just:`V.10`), "the twentieth of the sixth" (:just:`VI.20`), and so on up to the fifteenth Book, the first number is always to be understood as the number of the proposition (*conclusione*), and the second number as the number of the Book of our philosopher Euclid, whom we follow in all things as the *archimandrite* [supreme leader] of these faculties. That is, to say "by the fifth of the first" (:just:`I.5`) means "by the fifth proposition of his first Book," and so likewise for the other particular books of his complete work on the *Elements* and first principles of Arithmetic and Geometry. When, however, an authority adduced by us is drawn from another work of his [such as the *Optics* or *Catoptrics*] or from another author, we shall name that work and that author explicitly.

Moreover, because of the many varied characters and abbreviations that are customarily employed in such faculties—especially by us, just as is required in every other profession: for medicine uses its own symbols for scruples, ounces, drachms, and handfuls (*manipoli*); silversmiths and jewelers use theirs for grains, pennyweights (*denari*), and carats; astrologers use theirs for Jupiter, Mercury, Saturn, the Sun, the Moon, and the rest; and merchants likewise use theirs for pounds (*lire*), shillings (*soldi*), groats (*grossi*), and pence (*denari*) for the sake of brevity, solely to avoid prolixity in writing and reading, since otherwise they would fill much paper with ink—in the same way we too, in the mathematical sciences and in algebra (that is, speculative practice, *pratica speculativa*), employ characters that denote the unknown (*cosa*, $x$), its square (*censo*, $x^2$), its cube (*cubo*, $x^3$), and the other algebraic powers, as contained in our aforesaid work [*Summa de Arithmetica*]. Some of these we shall also use in the present treatise, namely those which we have set forth in the Table at the beginning of the book [Folio 0011r, e.g., *R.* for *Radice* (root), *p.* for *più* (plus), *m.* for *meno* (minus)].

Likewise, let the reader observe that these terms—namely **multiplication** (*multiplicatione*), **product** (*producto*), and **rectangle** (*rectangolo*)—signify one and the same thing [for $a \\cdot b$ is the area of the rectangle contained by segments $a$ and $b$]. And similarly, **square of a quantity** (*quadrato de una quantità*) and **power of a quantity** (*potentia d'alcuna quantità*, $\\delta\\acute{\\upsilon}\\nu\\alpha\\mu\\iota\\varsigma$) are one and the same thing: for the *power* of a line refers to its square, by the last proposition of the First Book (:just:`I.47`), and the utmost that a line can produce in power (*più che possa la linea*) is its square. These equivalences must be kept in mind throughout our discourse, lest any equivocation arise in the meaning of the words.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Citation Convention (`la prima del primo`)**: Pacioli codifies the standard medieval and Renaissance citation formula for Euclid's *Elements* (in the fifteen-book Campanus of Novara edition, where Book XIV is Hypsicles' treatise on the dodecahedron and icosahedron, and Book XV is the late-antique treatise on inscribing the five Platonic solids in one another). Note that propositional numbering in the Campanus Latin edition occasionally differs by one or two from the modern Heiberg Greek text (notably in Books VI, X, XIII, and XIV); in our critical commentary we cross-reference both the Campanus number cited by Pacioli and the standard Heiberg/GEOMETOR G-Index identifier.
2. **Algebraic Abbreviations (*Cosa, Censo, Cubo*)**: Pacioli connects the symbolic syncopation of Renaissance Italian abacus algebra (*R.* = *radice*, *p.* = *più*, *m.* = *meno*, *co.* = *cosa*, *ce.* = *censo*, *cu.* = *cubo*) to the professional notation systems of apothecaries, goldsmiths, astrologers, and merchants.
3. **Geometric-Arithmetical Isomorphism**: Pacioli explicitly equates the arithmetical operations of *multiplicatione* / *producto* ($a \\cdot b$) and *quadrato* ($a^2$) with their Euclidean Book II geometric counterparts: *rectangolo* (the rectangle contained by two segments) and *potentia* (the square on a segment, rendering the Greek $\\delta\\acute{\\upsilon}\\nu\\alpha\\mu\\iota\\varsigma$, as in the Pythagorean Theorem, :just:`I.47`, *l'ultima del primo*).""",
    },
    5: {
        "title_en": (
            "On the Fitting Title of the Present Treatise"
        ),
        "body_en": """\
It seems to me, Most Exalted Duke, that the fitting title of our treatise ought to be *On the Divine Proportion* (*De la Divina Proportione*). And this is on account of many similar correspondences (*convenientie*) belonging to God Himself that I find in our proportion, whereof we intend to treat in this our most useful discourse. Among these correspondences, we shall take four—and a fifth—as sufficient for our purpose:

.. subclause:: First Correspondence: Unity

   The **first correspondence** is that it is **one alone** and no more; and it is impossible to assign to it any other species or differences. And this **Unity** (*unità*) is the supreme epithet of God Himself, according to the entire theological and philosophical school.

.. subclause:: Second Correspondence: The Holy Trinity

   The **second correspondence** is that of the **Holy Trinity**: namely, just as *in divinis* one and the same substance resides among three Persons—Father, Son, and Holy Spirit—so one and the same proportion of this kind must always be found among **three terms** [the whole $a+b$, the major part $a$, and the minor part $b$, where $(a+b) : a = a : b$], and can never be found in either more or fewer, as will be explained.

.. subclause:: Third Correspondence: Ineffability and Irrationality

   The **third correspondence** is that just as God cannot be properly defined nor made intelligible to us through words, so this our proportion can never be assigned by any intelligible [rational] number nor expressed by any rational quantity, but always remains hidden and secret (*occulta e secreta*), and is called by mathematicians **irrational** (*irrationale*).

.. subclause:: Fourth Correspondence: Immutability and Omnipresence

   The **fourth correspondence** is that just as God can never change, and is **all in all and all in every part** (*tutto in tutto e tutto in ogni parte*), so our present proportion, in every continuous and discrete quantity—whether great or small—is always one and the same and ever invariable, and can in no wise be altered, nor apprehended otherwise by the intellect, as our discourse will demonstrate.

.. subclause:: Fifth Correspondence: Formal Being of Heaven and the Five Regular Bodies

   A **fifth correspondence** may not undeservedly be joined to the aforesaid four: namely, just as God confers being (*l'essere*) upon the Celestial Virtue—otherwise called the **Fifth Essence** (*quinta essentia*)—and through it upon the other four simple bodies, that is, the four elements **Earth**, **Water**, **Air**, and **Fire**, and through these confers being upon every other thing in nature; so too this our sacred proportion gives formal being (*l'esser formale*)—according to ancient Plato in his *Timaeus* (53c–56c)—to Heaven itself, assigning to it the figure of the body called the **Dodecahedron** (*Duodecedron*), otherwise known as the body of twelve pentagons, which, as will be shown below, cannot possibly be formed without our proportion.

And similarly, it assigns to each of the other elements its own proper form, in no way coinciding with one another:
- to **Fire**, the pyramidal figure called the **Tetrahedron** (*Tetracedron*);
- to **Earth**, the cubic figure called the **Hexahedron** (*Exacedron*);
- to **Air**, the figure called the **Octahedron** (*Octocedron*); and
- to **Water**, the figure called the **Icosahedron** (*Ycocedron*).

These forms and figures are all called by the wise the **Regular Bodies** (*corpi regulari*), as will be told separately of each below; and then, through these, it gives form to infinitely many other bodies called **Dependent Bodies** (*corpi dependenti*). Nor is it possible for those five regular bodies to be proportioned to one another, or to be understood as circumscribable by a sphere (:just:`XIII.13`–:just:`XIII.18`), without our said proportion, all of which will appear below. Although many other correspondences could be adduced, let these suffice for the fitting naming of the present compendium.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Coining the Name *Divina Proportione***: Prior to Pacioli's treatise, Euclid's division of a line in extreme and mean ratio (:just:`VI.def.3`, $\\ddot{\\alpha}\\kappa\\rho\\omicron\\varsigma \\kappa\\alpha\\grave{\\iota} \\mu\\acute{\\epsilon}\\sigma\\omicron\\varsigma \\lambda\\acute{\\omicron}\\gamma\\omicron\\varsigma$) was known in medieval Latin exclusively by Gerard of Cremona's and Campanus of Novara's rendering *proportio habens medium et duo extrema* ("proportion having a mean and two extremes"). Chapter V is the historic locus where Pacioli christens the ratio $\\phi = \\frac{1+\\sqrt{5}}{2}$ the **Divine Proportion** (*Divina Proportione*), grounding the name in five Scholastic-Platonic analogies:
   1. **Unicity**: Unlike multiplex or superparticular ratios ($2:1, 3:1, 3:2, 4:3, \\dots$), which form infinite families of species, extreme and mean ratio is unique (*una sola e non più*).
   2. **Trinitarian Structure**: Continuous proportion requires a minimum of three terms ($a+b : a :: a : b$), mirroring the *una substantia in tribus personis* of Trinitarian theology.
   3. **Apophatic Ineffability**: The incommensurability of $\\phi$ (:just:`XIII.6`) is compared to negative (apophatic) theology: just as God transcends finite verbal definition, $\\phi$ transcends rational numerical expression (*occulta e secreta*).
   4. **Self-Similarity and Invariance**: Echoing the Neoplatonic and Augustinian maxim that God is *totus in toto et totus in qualibet parte*, $\\phi$ remains invariant across all scales and self-replicates upon subdivision or addition (:just:`XIII.4`, :just:`XIV.2`).
   5. **Cosmological Formative Principle (Plato's *Timaeus*)**: Combining Aristotle's *De Caelo* (the celestial *quinta essentia*) with Plato's *Timaeus* 53c–56c (Tetrahedron = Fire, Cube = Earth, Octahedron = Air, Icosahedron = Water, Dodecahedron = the Cosmos/Heaven), Pacioli argues that because the regular pentagon and dodecahedron—and the mutual proportions of all five Platonic solids inscribed in a single sphere (:just:`XIII.13`–:just:`XIII.18`)—depend essentially on $\\phi$, the Divine Proportion is the formal geometric principle of cosmic order.""",
    },
    6: {
        "title_en": (
            "On Its Worthy Commendation"
        ),
        "body_en": """\
This our proportion, Most Exalted Duke, is worthy of as great prerogative and excellence as could ever be uttered regarding its infinite power; inasmuch as without knowledge of it very many things most worthy of admiration could never come to light either in philosophy or in any other science.

This gift is assuredly granted to it by the invariable nature of higher principles, as the great philosopher Campanus, our most famous mathematician, declares in his commentary upon the tenth proposition of the Fourteenth Book (:just:`XIV.10`)—especially when we behold that it is this very proportion which attunes so great a diversity of solids, whether in magnitude, in multitude of faces (*basi*), or in figures and forms, to one another with a certain **irrational symphony** (*con certa irrationale simphonia fra loro accordi*), as will be understood in the course of our treatise when we set forth the stupendous effects of a line divided according to it, which ought truly to be called not natural, but **divine**. Of these effects, the first in their enumeration is the following.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Campanus of Novara on Book XIV, Proposition 10 (*Irrationale Simphonia*)**: Pacioli translates and adapts a celebrated passage from Campanus of Novara's 13th-century commentary on Book XIV, Proposition 10 of Euclid's *Elements* (a corollary added by Campanus to Hypsicles' *Book XIV* comparing the dodecahedron and icosahedron inscribed in the same sphere). Campanus marveled at the *mirabilis potentia lineae secundum proportionem habentem medium duoque extrema divisae*, writing: *"Cui cum plurima admiranda conveniant, hoc praecipue... ex invariabili natura superiorum principiorum sibi adest, ut tam diversa solida, tum magnitudine, tum basium numero, tum etiam figura, irrationali quadam symphonia rationabiliter conciliet"* ("To which, though very many admirable properties belong, this above all is present to it from the invariable nature of higher principles: that it rationally reconciles solids so diverse in magnitude, in number of bases, and in figure, by a certain irrational symphony").""",
    },
    7: {
        "title_en": (
            "On the First Effect of a Line Divided According to Our Proportion"
        ),
        "body_en": """\
.. enunciation::

   When a straight line is divided according to the proportion having a mean and two extremes—for by this other name the wise call our aforesaid proportion—if to its **greater part** be added the **half of the whole line** so proportionally divided, it will necessarily follow that the **square of their sum** is always **quintuple** (that is, five times as great as) the **square of the said half of the whole** (:just:`XIII.1`).

Before proceeding further, we must explain how the said proportion is to be understood and interposed among quantities, and how it is named by the wisest authors in their volumes. I say, therefore, that it is called *proportio habens medium et duo extrema*—that is, "the proportion having a mean and two extremes"—which is a proper attribute (*propria passione*) of every ternary [triplet of terms]. For whatever ternary be assigned, it will always have a mean together with its two extremes, since a mean is never understood without extremes.

In this manner Euclid teaches how to divide a quantity in the nineteenth [thirtieth] proposition of the Sixth Book (:just:`VI.30`), having first defined in the third definition of the Sixth Book (:just:`VI.def.3`) how such a division is to be understood; although in his Second Book, in the eleventh proposition (:just:`II.11`), he already demonstrated how to divide a line with the very same virtue and power, without however naming "proportion" until he had passed through the Fifth Book; and Campanus also adduces it among numbers in the sixteenth proposition of the Ninth Book (:just:`IX.16`). Let this suffice regarding its designation.

How Its Mean and Its Extremes Are to Be Understood
--------------------------------------------------

Having understood how our proportion is called by its particular name, it remains to explain how the said mean and extremes are to be understood in any quantity whatever, and how they must be conditioned so that the said Divine Proportion may be found among them.

To this end, one must know—as is set forth in the Fifth Book—that between any three terms of one and the same kind (*de un medesimo genere*) there are necessarily two relations or ratios (*habitudini o vogliam dire proportioni*): namely, one between the first term and the second, and another between the second term and the third.

.. assertion:: Numerical Example of Continuous Proportion

   For example, let there be three quantities of the same kind (for otherwise no ratio is understood to exist between them, :just:`V.def.3`): let the first be :g:`a` and equal to $9$ in number, the second :g:`b` and equal to $6$, and the third :g:`c` and equal to $4$. I say that between them there are two ratios: one from :g:`a` to :g:`b`, that is, from $9$ to $6$, which among common ratios we call in our work [*Summa*] **sesquialtera** ($1\\frac{1}{2} : 1$), which occurs whenever the greater term contains the lesser once and a half; for $9$ contains $6$ and also $3$, which is half of $6$, and for this reason it is called *sesquialtera*.

   (Since we do not intend here to treat of ratios in general—having treated and explained them fully and at length, together with proportionalities, in our aforesaid work—I shall not trouble to expand upon them here; rather, let everything said of them in general, with their definitions and divisions, always be presupposed, and let our present discourse be devoted solely to this unique proportion, since no one has hitherto treated of it with so extensive and useful a development.)

   Now returning to our undertaking concerning the three quantities: there is likewise from the second term :g:`b` to the third term :g:`c`—that is, from $6$ to $4$—a second ratio, which is similarly *sesquialtera* ($6 : 4 = 3 : 2$). Whether such ratios in general be similar or dissimilar we do not care at present; our sole intent is to make clear that among three terms of the same kind two ratios are necessarily found.

I say likewise that our **Divine Proportion** observes the very same conditions: namely, between its three terms—the mean and the two extremes—it invariably contains two ratios that are always of one and the same denomination (:just:`V.def.5`). In other proportions, whether continuous or discontinuous, this can happen in infinitely many varied ways: for sometimes among their three terms the ratio will be *dupla* ($2:1$), sometimes *tripla* ($3:1$), and so on running through all the common species. Between the mean and the extremes of this our proportion, however, it is impossible for the ratio ever to vary, as will be told.

Whence this was deservedly the **fourth correspondence** with the Supreme Artificer. And in that it is numbered among the other proportions without species or further difference, while preserving the conditions of their definitions, we may liken it to **our Savior**, who came not to destroy the Law, but to fulfill it (Matthew 5:17), and conversed among men, making Himself subject and obedient to Mary and Joseph (Luke 2:51). Even so, this our proportion, sent down from heaven, accompanies the other proportions in definition and conditions, and does not degrade them, but rather magnifies them more amply, holding the principate of unity among all quantities indifferently and never changing—even as our holy Severinus [Boethius] says of the Great God: *Stabilisque manens dat cuncta moveri* ("And remaining steadfast, He gives all things to be moved," *De consolatione philosophiae* III, m. 9).

.. assertion:: Defining Condition of the Divine Proportion

   Wherefore, in order to recognize it among occurring quantities, one must know that among its three terms it is invariably found disposed in **continuous proportionality** in this manner: namely, that the **product of the lesser extreme and the sum of the lesser extreme and the mean** is equal to the **square of the mean**:

   $$b(b + a) = a^2$$

   Consequently, by the tenth definition of the Fifth Book (:just:`V.def.10`), the said **sum** ($a + b$) will necessarily be its **greater extreme**. And whenever three quantities of any kind whatever are found thus ordered, they are said to be according to the **proportion having a mean and two extremes** (:just:`VI.def.3`); and its greater extreme is always the sum of the lesser extreme and the mean.

   Hence we may say that the said greater extreme is the **whole quantity** divided into those two parts—namely, the lesser extreme ($b$) and the mean ($a$)—under that condition. From this it must be noted that the said proportion cannot be rational, nor can the lesser extreme and the mean ever be denominated by any rational number when the greater extreme is rational; for they will always be irrational (:just:`XIII.6`), as will be openly shown below. And in this third way it accords with God, as stated above.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Proposition Citations in Chapter VII**:
   - **First Effect (:just:`XIII.1`)**: If a line $AB = a+b$ is cut in extreme and mean ratio at $C$ with greater segment $AC = a$, and $AD = \\frac{1}{2}AB$ is added to $AC$, then $CD^2 = 5 \\cdot AD^2$, i.e., $(a + \\frac{a+b}{2})^2 = 5(\\frac{a+b}{2})^2$.
   - **Campanus VI.19 = Heiberg :just:`VI.30`**: Pacioli cites *la 19. del 6.* ("the 19th of the 6th"), which is the numbering of *Elements* VI.30 ("To cut a given finite straight line in extreme and mean ratio") in the medieval Latin edition of Campanus of Novara, preceded by :just:`VI.def.3`.
   - **:just:`II.11`**: Euclid's geometric construction in Book II ("To cut a given straight line so that the rectangle contained by the whole and one of the segments is equal to the square on the remaining segment"), which constructs the golden section by areas prior to the theory of proportions in Book V.
   - **Campanus :just:`IX.16`**: In Campanus's commentary on *Elements* IX.16 ("If two numbers be prime to one another, the second will not be to any other number as the first is to the second"), Campanus proves as a corollary that no three integers can stand in extreme and mean ratio (since if $a+b : a = a : b$ in lowest terms, $a$ and $b$ would be coprime, yet $a+b$ and $a$ would also be coprime, contradicting IX.16).
2. **Christological and Boethian Analogies**: Pacioli extends the theological analogies of Chapter V with a Christological comparison (Christ fulfilling the Mosaic Law, Matthew 5:17, and submitting to Mary and Joseph, Luke 2:51) and quotes the famous Neoplatonic hymn *O qui perpetua mundum ratione gubernas* from Boethius's *Consolation of Philosophy* (Book III, metrum 9, line 3): *stabilisque manens dat cuncta moveri* ("remaining unmoved, He gives all things to move").""",
    },
    8: {
        "title_en": (
            "How a Quantity Divided According to the Proportion Having a Mean and Two Extremes Is to Be Understood"
        ),
        "body_en": """\
We must know, once these things have been well noted, that to divide a quantity according to the proportion having a mean and two extremes means to make of it **two unequal parts** such that the **product of the lesser part and the whole undivided quantity** is equal to the **square of the greater part**, as our Philosopher declares in the third definition of the Sixth Book (:just:`VI.def.3`):

$$(a + b) \\cdot b = a^2$$

Therefore, even if a problem should never explicitly mention dividing a quantity "according to the proportion having a mean and two extremes," but should merely ask to make of it two parts so conditioned that the product of one part and the whole quantity equals the square of the other part, anyone who understands well and is expert in the art must reduce the problem to this our proportion, since it cannot be interpreted otherwise.

.. assertion:: Algebraic Division of $10$ in the Divine Proportion

   For example, suppose someone should say: *"Make of $10$ two such parts that when one part is multiplied by $10$, it produces as much as the other part multiplied by itself."*

   Operating upon this case and others like it according to the rules given by us in the speculative practice called *Algebra and Almucabala*—known by another name as the *Rule of the Thing* (*Regola dela Cosa*)—set forth in our aforesaid work [*Summa*, Distinctio VIII], the problem is found to be solved thus:
   - One part, namely the **lesser part**, is $15 - \\sqrt{125}$ (*15 m. R. 125*);
   - The other, namely the **greater part**, is $\\sqrt{125} - 5$ (*R. 125 m. 5*).

   These parts, thus written, are irrational, and in the art they are called **apotomes** (*residui*), of which our Philosopher assigns six species in the seventy-ninth [seventy-third] proposition of the Tenth Book (:just:`X.73`).

   In common speech, the said parts are pronounced thus: the lesser is "fifteen minus the square root of one hundred twenty-five," which means: take the square root of $125$, which is a little more than $11$ [$\\approx 11.18034$], and subtract it from $15$, leaving a little more than $3$, or let us say a little less than $4$ [$\\approx 3.81966$]. And the greater part is pronounced "the square root of $125$ minus $5$," which means: take the square root of $125$, which is a little more than $11$ as said, and subtract $5$ from it, leaving a little more than $6$, or let us say a little less than $7$ [$\\approx 6.18034$], for the said greater part.

   (As for such operations of multiplying, adding, subtracting, and dividing apotomes [*residui*], binomials [*binomii*], and roots [*radici*], as well as all other rational and irrational quantities, whole numbers and fractions, in every way—since we have demonstrated them in full in our aforesaid work [*Summa*], I do not trouble to repeat them here, attending only to stating new things and not reiterating those already told.)

.. assertion:: Verification of Continuous Proportionality

   When any quantity is thus divided, we shall always have **three terms** ordered in continuous proportionality:
   1. The first is the **whole divided quantity**, that is, the **greater extreme**, as here in the proposed case $10$;
   2. The second is the **greater part**, that is, the **mean**, namely $\\sqrt{125} - 5$;
   3. The third is the **lesser part**, that is, the **lesser extreme**, namely $15 - \\sqrt{125}$.

   Between these three terms there is one and the same ratio: namely, from the first to the second as from the second to the third ($10 : (\\sqrt{125} - 5) = (\\sqrt{125} - 5) : (15 - \\sqrt{125})$), and conversely from the third to the second as from the second to the first.

   And multiplying the lesser extreme ($15 - \\sqrt{125}$) by the greater extreme ($10$) produces the exact same result as multiplying the mean ($\\sqrt{125} - 5$) by itself: for both products equal

   $$150 - \\sqrt{12500}$$

   just as our proportion requires!

.. qed::

   Wherefore $10$ is said to be divided according to the proportion having a mean and two extremes, its greater part being $\\sqrt{125} - 5$ and its lesser part $15 - \\sqrt{125}$, both of which are necessarily irrational, as is proved by the sixth proposition of the Thirteenth Book (:just:`XIII.6`), as well as in the eleventh of the Second (:just:`II.11`) and the sixteenth of the Ninth (:just:`IX.16`). Let this serve for the knowledge of a quantity thus divided.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Pacioli's Canonical Numerical Exemplar ($a + b = 10$)**: Throughout Chapters VIII–XXII (and later in the polyhedral measurements), Pacioli adopts $10$ as the standard rational whole divided in extreme and mean ratio. Setting the greater part $a = x$ (*una cosa*) and the lesser part $b = 10 - x$, the defining equation $10(10 - x) = x^2$ gives the quadratic equation $x^2 + 10x = 100$ (*censo e cose equale a numero*). By al-Khwarizmi's rule in *Algebra et Almucabala*:
   $$a = \\sqrt{\\left(\\frac{10}{2}\\right)^2 + 100} - \\frac{10}{2} = \\sqrt{125} - 5$$
   $$b = 10 - (\\sqrt{125} - 5) = 15 - \\sqrt{125}$$
2. **Arithmetic of Apotomes (*Residui*, :just:`X.73`)**: Pacioli writes radicals in pure single-radical form so that $10 \\cdot \\sqrt{125} = \\sqrt{100 \\cdot 125} = \\sqrt{12500}$. Thus:
   - Product of extremes: $10 \\cdot (15 - \\sqrt{125}) = 150 - \\sqrt{12500}$.
   - Square of the mean: $(\\sqrt{125} - 5)^2 = 125 + 25 - 2 \\cdot 5\\sqrt{125} = 150 - \\sqrt{12500}$.
   Notice also that in line 24 of the 1509 print (and Winterberg's transcription), `15 m. R. 125` was twice misprinted as `o. m. R. 125`; our translation restores the mathematically exact `15 - \\sqrt{125}`.
3. **Campanus X.79 = Heiberg :just:`X.73`**: In Euclid's Book X, an apotome ($\\dot{\\alpha}\\pi\\omicron\\tau\\omicron\\mu\\acute{\\eta}$, rendered *residuum* by Gerard of Cremona and Campanus) is defined in :just:`X.73` (which is Proposition 79 in Campanus's numbering because Campanus counted several lemmas as numbered propositions), followed by the six species of apotomes in X.79–84 (Campanus X.85–90). Specifically, $\\sqrt{125} - 5$ is a *fourth apotome* (*residuum quartum*), and $15 - \\sqrt{125}$ is a *first apotome* (*residuum primum*).""",
    },
    9: {
        "title_en": (
            "What the Root of a Number and of Any Other Quantity Is"
        ),
        "body_en": """\
Because in the course of our treatise we shall frequently have occasion to speak of **Roots** (*Radici*), it seems fitting to explain briefly here what that term signifies, even though we have treated of it at length in every way in our great work [*Summa*].

.. enunciation::

   I say, nevertheless, that the **root** (*radice*) of a quantity is likewise a quantity which, when multiplied by itself, produces that quantity of which it is said to be the root; and that multiplication made into itself is called the **square** (*quadrato*) of the said root.

Thus we say that the root of $9$ is $3$, the root of $16$ is $4$, and the root of $25$ is $5$, and so in other cases; while $9$, $16$, and $25$ are called **squares** (*quadrati*).

From this it must be known that there are certain quantities which do not have a root that can be named exactly by a number: for instance, $10$ has no number which, multiplied by itself, makes $10$ exactly; and the same is true of $11$, $12$, $13$, and others like them.

Wherefore there arise two kinds of roots:
- One is called **discrete** (*discreta*), or let us say **rational** (*rationale*), which is a root that can be assigned exactly by a number, just as the root of $9$ is $3$;
- The other is called **surd** (*sorda*), which is one that cannot be given exactly by a number, as we have said of the root of $10$ and others.

These latter are called by another name **irrational** (*irrationali*), because all quantities that cannot be assigned exactly by a number [or ratio of integers] are called irrational in the art, whereas those that can be given by a number are called **rational** (*rationali*). And let this suffice for our purpose concerning roots.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Terminology of Roots (*Radix discreta* vs. *Radix surda*)**: Pacioli provides a concise glossary for courtly readers unfamiliar with abacus algebra. The Latin/Italian term *radice sorda* ("deaf" or "mute" root, rendering the Arabic *jadhr asamm*, which in turn translated the Greek $\\alpha\\lambda\\omicron\\gamma\\omicron\\varsigma$, "without ratio" or "inexpressible") denotes an irrational square root such as $\\sqrt{10}$ or $\\sqrt{125}$ (:just:`X.def.3`).""",
    },
    10: {
        "title_en": (
            "Sequel to the First Proposed Effect"
        ),
        "body_en": """\
Once these things have been well noted, let us return to its **first proposed effect** [Chapter VII] and make it clear with evident examples. For its elucidation, let us resume the very same case of $10$ adduced above, without troubling ourselves with other laborious quantities, since the very same property that is stated here occurs invariably in every quantity whatever. And for the fuller understanding of Your Highness, we shall pursue all the remaining effects by way of Arithmetic, while presupposing throughout that the rigorous scientific proofs of everything contained in our treatise are assigned geometrically with all care by our philosopher Euclid in the propositions we shall cite, according to the requirements of the conclusions.

.. assertion:: Arithmetical Demonstration of the First Effect (:just:`XIII.1`)

   I say, therefore, that when $10$ is divided according to our proportion, its **greater part** is $\\sqrt{125} - 5$. If to this greater part, in accordance with the said First Effect, we add $5$—that is, the **half of the whole $10$**—their sum will make $\\sqrt{125}$ exactly; because that $- 5$ (*meno 5*) is restored and filled up (*se vene a restorare e a rempire*) by the $+ 5$ (*più 5*), the half of $10$:

   $$(\\sqrt{125} - 5) + 5 = \\sqrt{125}$$

   When this sum, namely $\\sqrt{125}$, is multiplied by itself, it makes $125$ for its square. And this $125$ is **five times** the square of the half of $10$, which half is $5$ and its square is $25$:

   $$(\\sqrt{125})^2 = 125 = 5 \\times 25 = 5 \\times 5^2$$

   Whence $125$ is exactly **quintuple** to the said $25$, the square of the said half of $10$, just as was stated.

.. qed::

   And this effect holds good in every quantity of whatever nature it may be, as the first proposition of the Thirteenth Book (:just:`XIII.1`) of our guide [Euclid] openly demonstrates.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. ***Restorare e rempire* (*al-jabr*)**: Notice Pacioli's technical use of the verb *restorare* ("to restore"): adding $+5$ cancels the subtracted $-5$ in $\\sqrt{125} - 5$, which is the literal meaning of the Arabic *al-jabr* (*restauratio*, restoring a deficient or subtracted quantity).
2. **Correlation with Euclid :just:`XIII.1`**: Algebraically, since $a = \\sqrt{5\\left(\\frac{a+b}{2}\\right)^2} - \\frac{a+b}{2}$, adding $\\frac{a+b}{2}$ immediately isolates $\\sqrt{5}\\left(\\frac{a+b}{2}\\right)$, whose square is $5\\left(\\frac{a+b}{2}\\right)^2$. Thus Pacioli illuminates why Euclid begins Book XIII with :just:`XIII.1`: it is the geometric equivalent of completing the square on the golden ratio quadratic equation.""",
    },
}

CHAPTERS_1_TO_23.update({
    11: {
        "title_en": (
            "On Its Second Essential Effect"
        ),
        "body_en": """\
.. enunciation::

   If a quantity be divided into two parts, and to one of them be added a quantity such that the **square of this sum** is **quintuple** the **square of the added quantity**, it follows of necessity that the said added quantity is the **half of the first quantity** divided into those two parts, and that the part to which it was added is its **greater part**, and that the whole first quantity is divided into those two parts according to our proportion (:just:`XIII.2`).

.. assertion:: Numerical Demonstration

   For example, let $15 - \\sqrt{125}$ and $\\sqrt{125} - 5$ be taken as the two integral parts of a quantity [namely $10$], and to one of them—namely $\\sqrt{125} - 5$—let $5$ be added as a third quantity. Their sum will be $\\sqrt{125}$, whose square is $125$; while the square of the added quantity ($5$) is $25$. Whence $125$ is **quintuple** to $25$, the square of the added quantity:

   $$125 = 5 \\times 25$$

   I say that $\\sqrt{25}$, namely $5$, is the **half of the first quantity** divided into those two parts; and that the part to which it was added ($\\sqrt{125} - 5$) is the **greater part** of the said first quantity ($10$) divided according to our proportion having a mean and two extremes.

.. qed::

   And this is the converse of the preceding effect, just as the second proposition of the Thirteenth Book (:just:`XIII.2`) concludes geometrically.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Converse of the First Effect (:just:`XIII.2`)**: In Euclid's *Elements* Book XIII, Proposition 2 states: "If the square on a straight line be five times the square on a segment of it, then when the double of the said segment is cut in extreme and mean ratio, the greater segment is the remaining part of the original straight line." Pacioli formulates this directly as the converse of Chapter VII/X: if $(a + c)^2 = 5c^2$ where $a + b = 2c$, then $c = \\frac{a+b}{2}$ and $a$ is the major golden segment of $a+b$.""",
    },
    12: {
        "title_en": (
            "On Its Third Singular Effect"
        ),
        "body_en": """\
.. enunciation::

   If a quantity be divided according to our proportion, and to its **lesser part** be added the **half of the greater part**, the **square of their sum** will always be **quintuple** the **square of the half of the said greater part** (:just:`XIII.3`).

.. assertion:: Numerical Demonstration

   For example, let $10$ be the quantity divided according to our Divine Proportion, so that one part—namely the greater ($a$)—is $\\sqrt{125} - 5$, and the lesser ($b$) is $15 - \\sqrt{125}$.

   I say that if to $15 - \\sqrt{125}$, which is the lesser part, we add the half of $\\sqrt{125} - 5$, which is the greater part, the sum of the lesser part and the said half, when multiplied by itself, will be **five times** the square of the half of the said greater part. And this appears as follows:

   1. The half of the greater part ($\\sqrt{125} - 5$) is:

      $$\\frac{a}{2} = \\sqrt{31\\frac{1}{4}} - 2\\frac{1}{2}$$

   2. Adding this to $15 - \\sqrt{125}$, which is the lesser part ($b$), yields:

      $$b + \\frac{a}{2} = (15 - \\sqrt{125}) + \\left(\\sqrt{31\\frac{1}{4}} - 2\\frac{1}{2}\\right) = 12\\frac{1}{2} - \\sqrt{31\\frac{1}{4}}$$

   3. Multiplying $12\\frac{1}{2} - \\sqrt{31\\frac{1}{4}}$ by $12\\frac{1}{2} - \\sqrt{31\\frac{1}{4}}$ produces:

      $$\\left(b + \\frac{a}{2}\\right)^2 = 187\\frac{1}{2} - \\sqrt{19531\\frac{1}{4}}$$

      and this is called the **square of the sum**.

   4. Next, let the half of the said greater part also be squared—that is, multiply $\\sqrt{31\\frac{1}{4}} - 2\\frac{1}{2}$ by $\\sqrt{31\\frac{1}{4}} - 2\\frac{1}{2}$—which will make:

      $$\\left(\\frac{a}{2}\\right)^2 = 37\\frac{1}{2} - \\sqrt{781\\frac{1}{4}}$$

      and this is called the **square of the half of the greater part**, which is converterly one-fifth ($\\frac{1}{5}$) of the square of the sum:

      $$5 \\times \\left(37\\frac{1}{2} - \\sqrt{781\\frac{1}{4}}\\right) = 187\\frac{1}{2} - \\sqrt{25 \\times 781\\frac{1}{4}} = 187\\frac{1}{2} - \\sqrt{19531\\frac{1}{4}}$$

.. qed::

   Consequently, the said square of the sum is **quintuple** the square of the half of the said greater part of $10$ thus divided. And this power is to be highly esteemed along with the others, as is proved geometrically in full by the third proposition of the Thirteenth Book (:just:`XIII.3`) of our author.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Radical Arithmetic in Chapter XII (:just:`XIII.3`)**: Pacioli's step-by-step calculation with apotomes is a tour de force of Renaissance abacus algebra:
   - Halving $\\sqrt{125}$ requires dividing the radicand by $2^2 = 4$: $\\frac{1}{2}\\sqrt{125} = \\sqrt{\\frac{125}{4}} = \\sqrt{31\\frac{1}{4}}$.
   - Subtracting $\\sqrt{125} - \\sqrt{31\\frac{1}{4}} = 2\\sqrt{31\\frac{1}{4}} - \\sqrt{31\\frac{1}{4}} = \\sqrt{31\\frac{1}{4}}$ gives $b + \\frac{a}{2} = (15 - 2\\frac{1}{2}) - \\sqrt{31\\frac{1}{4}} = 12\\frac{1}{2} - \\sqrt{31\\frac{1}{4}}$.
   - Squaring $12\\frac{1}{2} - \\sqrt{31\\frac{1}{4}}$ gives $(12\\frac{1}{2})^2 + 31\\frac{1}{4} - 2(12\\frac{1}{2})\\sqrt{31\\frac{1}{4}} = 156\\frac{1}{4} + 31\\frac{1}{4} - \\sqrt{625 \\times 31\\frac{1}{4}} = 187\\frac{1}{2} - \\sqrt{19531\\frac{1}{4}}$.
   - Squaring $\\frac{a}{2} = \\sqrt{31\\frac{1}{4}} - 2\\frac{1}{2}$ gives $31\\frac{1}{4} + 6\\frac{1}{4} - \\sqrt{25 \\times 31\\frac{1}{4}} = 37\\frac{1}{2} - \\sqrt{781\\frac{1}{4}}$.
   - Multiplying by $5$ scales the rational part by $5$ ($5 \\times 37\\frac{1}{2} = 187\\frac{1}{2}$) and the radicand by $5^2 = 25$ ($25 \\times 781\\frac{1}{4} = 19531\\frac{1}{4}$).""",
    },
    13: {
        "title_en": (
            "On Its Fourth Ineffable Effect"
        ),
        "body_en": """\
.. enunciation::

   If a quantity is divided according to our Divine Proportion, and to the **whole of the said quantity** be added its **greater part**, then the **said sum** and the **said greater part** will be the parts of another [second] quantity similarly divided; and the **greater part of this second divided quantity** will always be the **entire first quantity** (cf. :just:`XIII.5` [Campanus XIII.4]).

.. assertion:: Numerical Demonstration

   For example, let the quantity divided according to our unique proportion be $10$, so that its greater part is $\\sqrt{125} - 5$ and its lesser part is $15 - \\sqrt{125}$.

   If to $10$, the first quantity, we add $\\sqrt{125} - 5$, its greater part, they will make a second quantity, namely:

   $$(a + b) + a = 10 + (\\sqrt{125} - 5) = \\sqrt{125} + 5$$

   And I say that this second quantity, namely $\\sqrt{125} + 5$, is similarly divided according to our proportion into the two said parts: namely, into $\\sqrt{125} - 5$ (which was the greater part of the first quantity and is now the **lesser part** of this second quantity) and into $10$ (which was the whole first quantity and is now the **greater part** of this second quantity).

   This appears manifestly as follows: the product of $\\sqrt{125} - 5$ (which was the greater part of the first and is now the lesser part of this second) into the whole of this second quantity, namely $\\sqrt{125} + 5$, makes the exact same amount as the square of the mean—or let us say the greater part—of this second quantity, which is $10$; for both products make $100$ exactly, as is required by the said proportion:

   $$(\\sqrt{125} - 5)(\\sqrt{125} + 5) = 125 - 25 = 100 = 10^2$$

.. qed::

   Which power the fourth proposition of the Thirteenth Book (Campanus XIII.4 = Heiberg :just:`XIII.5`) likewise manifests to us geometrically.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Campanus XIII.4 vs. Heiberg :just:`XIII.5` (Ordering Inversion in Book XIII)**: In Campanus of Novara's Latin edition of *Elements* Book XIII, Heiberg's Propositions 4 and 5 are transposed! Specifically:
   - **Campanus XIII.4** (= Heiberg :just:`XIII.5`): If a straight line $AB$ is cut in extreme and mean ratio at $C$ (with greater segment $AC$), and $AD = AC$ is added to $AB$, then the whole $BD = AB + AC$ is cut in extreme and mean ratio at $A$, with greater segment $AB$.
   - **Campanus XIII.5** (= Heiberg :just:`XIII.4`): If a straight line $AB$ is cut in extreme and mean ratio, the sum of the squares on the whole $AB$ and the lesser segment $BC$ is triple the square on the greater segment $AC$.
   Pacioli follows Campanus's numbering strictly in Chapters XIII and XIV: Chapter XIII gives Heiberg :just:`XIII.5` (citing *la quarta del terzodecimo*), and Chapter XIV gives Heiberg :just:`XIII.4` (citing *la quinta del 13.*).
2. **Difference of Squares Identity**: Notice how cleanly the product of the conjugate binomial and apotome evaluates: $(\\sqrt{125} - 5)(\\sqrt{125} + 5) = 125 - 25 = 100 = 10^2$.""",
    },
    14: {
        "title_en": (
            "On Its Fifth Marvelous Effect"
        ),
        "body_en": """\
.. enunciation::

   If a quantity be divided according to our said proportion, the **sum of the square of the lesser part and the square of the entire undivided quantity** will always be **triple** the **square of the greater part** (:just:`XIII.4` [Campanus XIII.5]):

   $$b^2 + (a + b)^2 = 3a^2$$

.. assertion:: Numerical Demonstration

   For example, let $10$ be the divided quantity, where, as we have said, one part is $15 - \\sqrt{125}$ (namely the lesser, $b$) and the other is $\\sqrt{125} - 5$ (namely the greater, $a$).

   I say that when the square of $15 - \\sqrt{125}$ is added to the square of $10$ (the whole quantity), their sum will be **triple**—that is, three times as great as—the square of the greater part, namely of $\\sqrt{125} - 5$:

   1. The square of the lesser part ($15 - \\sqrt{125}$) is:

      $$b^2 = (15 - \\sqrt{125})^2 = 225 + 125 - 30\\sqrt{125} = 350 - \\sqrt{112500}$$

   2. The square of the whole quantity ($10$) is $100$, which, added to $350 - \\sqrt{112500}$, makes:

      $$b^2 + (a + b)^2 = 450 - \\sqrt{112500}$$

      for the said sum.

   3. Meanwhile, the square of the greater part ($\\sqrt{125} - 5$) is:

      $$a^2 = (\\sqrt{125} - 5)^2 = 150 - \\sqrt{12500}$$

      which is manifestly one-third ($\\frac{1}{3}$) of the said sum! For when $150 - \\sqrt{12500}$ is multiplied by $3$, it makes:

      $$3a^2 = 3 \\times 150 - \\sqrt{9 \\times 12500} = 450 - \\sqrt{112500}$$

.. qed::

   Therefore the said sum is **triple** the said square, just as we stated; which effect the fifth proposition of the Thirteenth Book (Campanus XIII.5 = Heiberg :just:`XIII.4`) concludes geometrically.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Algebraic Identity Behind the Fifth Effect (:just:`XIII.4`)**: Since $b(a+b) = a^2$ and $b = (a+b) - a$, we have:
   $$b^2 + (a+b)^2 = b^2 + (a+b)^2 = (a+b)^2 - 2(a+b)b + b^2 + 2(a+b)b = a^2 + 2a^2 = 3a^2$$
   In Pacioli's single-radical notation, multiplying $\\sqrt{12500}$ by $3$ brings $3^2 = 9$ inside the radical: $\\sqrt{9 \\times 12500} = \\sqrt{112500}$.""",
    },
    15: {
        "title_en": (
            "On Its Sixth Inexpressible Effect"
        ),
        "body_en": """\
.. enunciation::

   It is impossible for any **rational quantity** to be divided according to our said proportion without **each of its parts** being an **irrational line called an apotome** (*residuo*, :just:`XIII.6`).

.. assertion:: Numerical Demonstration

   For example, let $10$ be the rational quantity that is to be divided according to the proportion having a mean and two extremes. I say that of necessity each of its parts must be an **apotome** (*residuo*):
   - One part, namely the lesser, will be $15 - \\sqrt{125}$;
   - The other, namely the greater, will be $\\sqrt{125} - 5$.

.. qed::

   Wherefore it appears that each part is an apotome (*residuo*)—for so such lines are called in the art according to the seventy-ninth [seventy-third] proposition of the Tenth Book (:just:`X.73`). And this effect we have from the sixth proposition of the Thirteenth Book (:just:`XIII.6`).""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Euclid :just:`XIII.6` and :just:`X.73`**: Proposition 6 of Book XIII proves that if a rational straight line is cut in extreme and mean ratio, each of the segments is an irrational straight line called an *apotome* ($\\dot{\\alpha}\\pi\\omicron\\tau\\omicron\\mu\\acute{\\eta}$, defined in :just:`X.73`, Campanus X.79). Pacioli calls this the "inexpressible" or "innominable" (*innominabile*) effect because neither segment can ever be named by a rational number when the whole is rational.""",
    },
    16: {
        "title_en": (
            "On Its Seventh Inestimable Effect"
        ),
        "body_en": """\
.. enunciation::

   If the **side of an equilateral hexagon** be joined in a single line to the **side of an equilateral decagon**, both being understood as inscribed in one and the same circle, their **sum** will always be a quantity divided according to our said proportion, and its **greater part** will be the **side of the hexagon** (:just:`XIII.9`).

.. assertion:: Numerical Demonstration

   For example, let the side of an equilateral hexagon inscribed in a circle be $\\sqrt{125} - 5$, and let the side of the equilateral decagon in the very same circle be $15 - \\sqrt{125}$. (The diameter of this circle, which is double the side of the hexagon by :just:`IV.15`, will be $2(\\sqrt{125} - 5) = \\sqrt{500} - 10$.)

   I say that the sum of $\\sqrt{125} - 5$ and $15 - \\sqrt{125}$, which equals $10$, is divided according to our proportion, and that its **greater part** is $\\sqrt{125} - 5$ [the hexagon side] and its **lesser part** is $15 - \\sqrt{125}$ [the decagon side], just as we have repeatedly shown in the division of $10$.

.. qed::

   And this is manifest geometrically by the ninth proposition of the Thirteenth Book (:just:`XIII.9`).""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Hexagon and Decagon Inscribed in the Same Circle (:just:`XIII.9`)**: By :just:`IV.15.p`, the side $s_6$ of the regular hexagon inscribed in a circle of radius $R$ is equal to the radius itself ($s_6 = R$, so the diameter is $2R = 2(\\sqrt{125}-5) = \\sqrt{500}-10$). Proposition 9 of Book XIII proves that when $s_6$ and the side $s_{10}$ of the regular decagon inscribed in the same circle are placed in a straight line, the whole line $s_6 + s_{10}$ is cut in extreme and mean ratio, and $s_6$ is the greater segment:
   $$(s_6 + s_{10}) : s_6 = s_6 : s_{10} = \\phi$$""",
    },
    17: {
        "title_en": (
            "On the Eighth Effect, the Converse of the Preceding"
        ),
        "body_en": """\
.. enunciation::

   If a line be divided according to the proportion having a mean and two extremes, then for that circle in which the **greater part** is the **side of the inscribed hexagon**, the **lesser part** will always be the **side of the regular decagon** inscribed in the very same circle (:just:`XIII.9`).

.. assertion:: Numerical Demonstration and Ptolemaic Application

   For example, if the divided line is $10$, its **greater part**, which is $\\sqrt{125} - 5$, will always be the side of the equilateral hexagon of a circle whose diameter is double $\\sqrt{125} - 5$, namely $\\sqrt{500} - 10$ (:just:`IV.15`). I say that in that very same circle, the **lesser part**, $15 - \\sqrt{125}$, will be the side of the equilateral decagon inscribed therein.

.. qed::

   Of this converse **Ptolemy** makes great use in the ninth [tenth] chapter of the First Book (*prima dictione*) of his *Almagest* to demonstrate the lengths of the chords of circular arcs (*la quantità dele corde degli archi del cerchio*); and it is similarly demonstrated openly in the commentary upon the aforesaid ninth proposition of the Thirteenth Book (:just:`XIII.9`) geometrically.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Ptolemy's *Almagest* Book I, Ch. 9/10 (Calculation of the Table of Chords)**: Pacioli cites Gerard of Cremona's Latin translation of Ptolemy's *Almagest* (*Dictio prima*, cap. 9 in manuscript/printed divisions corresponding to Heiberg Book I, Ch. 10, *De magnitudine rectarum linearum quae in circulo ducuntur*). To construct his trigonometric table of chords, Ptolemy divides the diameter into $120$ parts (so the radius / hexagon chord $\\text{crd}(60^\\circ) = 60$), and uses :just:`XIII.9` and :just:`XIII.10` simultaneously to compute the chord of $36^\\circ$ (the side of the regular decagon, $\\text{crd}(36^\\circ) = \\sqrt{5 \\cdot 30^2} - 30 = \\sqrt{4500} - 30 \\approx 37;4,55$) and the chord of $72^\\circ$ (the side of the regular pentagon).""",
    },
    18: {
        "title_en": (
            "On Its Ninth Effect, Surpassing All the Others"
        ),
        "body_en": """\
.. enunciation::

   If an **equilateral pentagon** be formed in a circle, and opposite two of its adjacent angles two straight lines [diagonals] be subtended from the endpoints of their sides, those two lines will of necessity **divide one another according to our proportion**, and **each of their greater parts** will always be equal to the **side of the said pentagon** (:just:`XIII.8`).

.. assertion:: Geometric and Numerical Demonstration

   For example, let the equilateral pentagon be :g:`abcde`, and from the endpoints :g:`c` and :g:`a` let the chord :g:`ac` be drawn subtending the angle :g:`b`; and from the endpoints :g:`b` and :g:`e` let the other chord :g:`be` be drawn subtending the angle :g:`a`.

   I say that these two lines :g:`ac` and :g:`be` divide one another at the point :g:`f` according to the proportion having a mean and two extremes (:just:`XIII.8`), and the **greater part** of each is exactly equal to the **side of the said pentagon**:
   - Of the line :g:`ac`, the greater part is :g:`cf`, and the lesser part is :g:`af`;
   - Of the line :g:`be`, the greater part is :g:`ef`, and the lesser part is :g:`bf`;
   - And each of these greater parts (:g:`cf` and :g:`ef`) is always equal to the side of the said pentagon (:g:`ab` $= $ :g:`bc` $= $ :g:`cd` $= $ :g:`de` $= $ :g:`ea`).

   By mathematicians these two lines (:g:`ac` and :g:`be`) are called by another name the **chords of the pentagonal angle** (*corde del'angolo pentagonico*).

   Thus, if each of the said chords (:g:`ac` and :g:`be`) were $10$ (for they are equal when their pentagon in the circle is equilateral and equiangular):
   - :g:`cf` would be $\\sqrt{125} - 5$, and :g:`af` would be $15 - \\sqrt{125}$;
   - The part :g:`ef` would similarly be $\\sqrt{125} - 5$, and :g:`bf` would be $15 - \\sqrt{125}$;
   - And the **side of the pentagon** itself would likewise be $\\sqrt{125} - 5$!

.. qed::

   All of this the eighth [and eleventh] proposition of the Thirteenth Book (:just:`XIII.8`, :just:`XIII.11`) demonstrates geometrically in a beautiful manner. And through this effect, from knowledge of the **side** of the pentagon we can arrive at knowledge of all its **diagonals** (*corde*) and all their parts; and conversely, from knowledge of the **diagonals** we can arrive at knowledge of the **side** and of the segments of the said diagonals—operating arithmetically and geometrically just as we have taught in our aforesaid work [*Summa*] how to handle them with all diligence by means of binomials (*binomii*) and other irrational lines, whereof our Philosopher treats in his Tenth Book, and which he demonstrates for a line in the eleventh of the Second (:just:`II.11`) and the twenty-ninth [thirtieth] of the Sixth (:just:`VI.30`). Thus one easily arrives at the knowledge of the one from the other in every way, which is a thing of the greatest utility in our scientific and speculative inquiries.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Intersecting Diagonals of the Regular Pentagon (:just:`XIII.8` and :just:`XIII.11`)**: Proposition 8 of Book XIII proves that if two diagonals :g:`ac` and :g:`be` of an equilateral and equiangular pentagon :g:`abcde` intersect at :g:`f`, both diagonals cut one another in extreme and mean ratio ($ac : cf = cf : af$ and $be : ef = ef : bf$), and their greater segments equal the pentagon's side ($cf = ef = ab$). Pacioli also cites :just:`XIII.11` (which proves that the side of the regular pentagon inscribed in a circle with rational diameter is the irrational line called a *minor*, $\\dot{\\varepsilon}\\lambda\\acute{\\alpha}\\sigma\\sigma\\omega\\nu$, constructed from a fourth binomial and fourth apotome) because his *Libellus* (Tractatus I) and *Summa* extensively use :just:`XIII.8` and :just:`XIII.11` together to calculate all dimensions of the pentagon and dodecahedron.""",
    },
    19: {
        "title_en": (
            "On Its Tenth Supreme Effect"
        ),
        "body_en": """\
.. enunciation::

   If a quantity be divided according to the aforesaid proportion, **all the effects and relations** that can arise from it and its parts proceed **identically in ratio, number, species, and genus** from **any other quantity** so divided (:just:`XIV.2`).

.. assertion:: Geometric and Numerical Demonstration

   For example, let there be two lines thus divided: namely, one line :g:`ab` divided at :g:`c` whose greater part is :g:`ac`, and another line :g:`de` divided at :g:`f` whose greater part is :g:`df`. And what we say of these two lines, we understand likewise of infinitely many others, which can easily be assigned by way of Arithmetic:
   - Setting :g:`ab` $= 10$, its greater part :g:`ac` will be $\\sqrt{125} - 5$, and its lesser part :g:`cb` will be $15 - \\sqrt{125}$;
   - Setting :g:`de` $= 12$, its greater part :g:`df` will be $\\sqrt{180} - 6$, and its lesser part :g:`fe` will be $18 - \\sqrt{180}$.

   I say that everything that can ever happen to one of the said lines when compared, multiplied, divided, or manipulated in any other way whatever, happens identically to the other:
   - The ratio of each whole line to its greater part is the very same (:g:`ab` $:$ :g:`ac` $=$ :g:`de` $:$ :g:`df`);
   - The ratio of each whole line to its lesser part is the very same (:g:`ab` $:$ :g:`cb` $=$ :g:`de` $:$ :g:`fe`);
   - And conversely, from each of their parts to the wholes, and likewise in the product of one into its parts and conversely, and in division and subtraction.

   Thus the ratio of $10$ to its greater part $\\sqrt{125} - 5$ is the exact same as the ratio of $12$ to its greater part $\\sqrt{180} - 6$; and the ratio of the sum of $10$ and $\\sqrt{125} - 5$ to $\\sqrt{125} - 5$ is the exact same as the ratio of the sum of $12$ and $\\sqrt{180} - 6$ to $\\sqrt{180} - 6$.

.. qed::

   In short, taken and inverted to infinity, howsoever much and in whatsoever manner—by **alternation** (*permutata*, :just:`V.16`), **inversion** (*conversa*, :just:`V.7.p`), **composition** (*congionta*, :just:`V.18`), **separation** (*disgionta*, :just:`V.17`), **conversion** (*eversa*, :just:`V.19.p`), and **equality** (*equa proportionalita*, :just:`V.22`)—they will always agree in one and the same denomination and in the same intensive effects. This without fail demonstrates the **greatest harmony** in all quantities thus divided, as will appear below in the regular and dependent bodies; and all of this the second proposition of the Fourteenth Book (:just:`XIV.2`, Campanus's lemma) concludes geometrically in substance.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Universal Similarity of Golden-Divided Lines (Campanus Lemma to :just:`XIV.2`)**: In Hypsicles' *Book XIV* of the *Elements*, Proposition 2 proves that the same circle circumscribes both the pentagon of the dodecahedron and the triangle of the icosahedron inscribed in the same sphere. In his commentary on XIV.2, Campanus of Novara inserted and proved a fundamental lemma (often cited in medieval and Renaissance mathematics simply as part of XIV.2): **if two straight lines are cut in extreme and mean ratio, they are cut similarly** ($AB : AC = DE : DF$ and $AC : CB = DF : FE$).
2. **The Six Operations of Book V**: Pacioli enumerates the six canonical Scholastic operations on proportions from Book V of Euclid's *Elements*:
   - *Permutata* (*alternando*, :just:`V.16`): $a : b = c : d \\implies a : c = b : d$
   - *Conversa* (*invertendo*, :just:`V.7.p`): $a : b = c : d \\implies b : a = d : c$
   - *Congionta* (*componendo*, :just:`V.18`): $a : b = c : d \\implies (a+b) : b = (c+d) : d$
   - *Disgionta* (*dividendo*, :just:`V.17`): $a : b = c : d \\implies (a-b) : b = (c-d) : d$
   - *Eversa* (*convertendo*, :just:`V.19.p`): $a : b = c : d \\implies a : (a-b) = c : (c-d)$
   - *Equa proportionalita* (*ex aequali*, :just:`V.22`).""",
    },
    20: {
        "title_en": (
            "On Its Eleventh Most Excellent Effect"
        ),
        "body_en": """\
.. enunciation::

   If the **side of an equilateral hexagon** be divided according to our Divine Proportion, its **greater part** will of necessity always be the **side of the regular decagon** circumscribed by the very same circle as the hexagon (:just:`XIV.3` [Campanus corollary to :just:`XIII.9`]).

.. assertion:: Numerical Demonstration

   For example, if the side of the equilateral hexagon be $10$, and it be divided in the manner stated, its **greater part** will be $\\sqrt{125} - 5$, which I say is the exact **side of the decagon** inscribed in the very same circle, whose diameter will be $20$ (:just:`IV.15`). And this is concluded by the third proposition of the Fourteenth Book (Campanus XIV.3 / :just:`XIII.9`).

.. qed::

   Whence, manifestly, once the side of either polygon is known, the side of the other is easily found; and likewise, given the diameter of the circle, or its circumference, or its area, or any part thereof, we can always arrive through it at the knowledge of either the hexagon or the decagon from the other, and conversely in every way for the circle, hexagon, decagon, and also the equilateral triangle—operating arithmetically and geometrically, which is a most useful thing, just as was stated above in the Ninth Effect [Chapter XVIII] concerning the pentagon.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Direct Calculation of the Decagon from the Radius ($R = 10$)**: Whereas Chapters XVI and XVII took $s_6 + s_{10} = 10$ (so that the radius $R = s_6 = \\sqrt{125} - 5$), Chapter XX takes the hexagon side (the circle's radius $R$) itself as $10$ (so the circle's diameter is $20$). Since $(s_6 + s_{10}) : s_6 = s_6 : s_{10}$ (:just:`XIII.9`), $s_6$ is divided in extreme and mean ratio when a segment equal to $s_{10}$ is marked off from it: thus the side of the inscribed decagon is simply the major golden segment of the radius ($s_{10} = \\sqrt{125} - 5$). Note that Pacioli uses *circumscripto dal medesimo cerchio* in the sense of "surrounded/encompassed by the same circle" (i.e., inscribed within the circle).""",
    },
    21: {
        "title_en": (
            "On Its Twelfth Almost Incomprehensible Effect"
        ),
        "body_en": """\
.. enunciation::

   If a quantity be divided according to our said proportion, the **square root of the sum of the square of the whole quantity and the square of its greater part** will stand in the exact same ratio to the **square root of the sum of the square of the said whole quantity and the square of its lesser part** as the **side of the cube** stands to the **side of the triangle of the twenty-base body [the icosahedron]**, when both bodies are circumscribed by one and the same sphere (:just:`XIV.9`):

   $$\\frac{\\sqrt{(a + b)^2 + a^2}}{\\sqrt{(a + b)^2 + b^2}} = \\frac{s_{\\text{cube}}}{s_{\\text{icosahedron}}}$$

.. assertion:: Numerical Demonstration with Universal Roots (*Radici Legate*)

   For example, let $10$ be the quantity divided according to the proportion having a mean and two extremes, so that one part—namely the greater ($a$)—is, as has been said many times, $\\sqrt{125} - 5$, and the lesser ($b$) is $15 - \\sqrt{125}$.

   1. Let the said whole quantity ($10$) be squared—that is, multiplied by itself—which will make $100$.
   2. Let its greater part ($\\sqrt{125} - 5$) also be squared, which multiplied by itself will make $150 - \\sqrt{12500}$.
   3. And let its lesser part ($15 - \\sqrt{125}$) also be squared, which multiplied by itself makes $350 - \\sqrt{112500}$.
   4. Now to the square of the greater part ($150 - \\sqrt{12500}$) let the square of the whole quantity ($100$) be added, which will make:

      $$(a + b)^2 + a^2 = 250 - \\sqrt{12500}$$

   5. And let the same square of the whole quantity ($100$) be added to the square of the lesser part ($350 - \\sqrt{112500}$), which will make:

      $$(a + b)^2 + b^2 = 450 - \\sqrt{112500}$$

   Now I say that the ratio of the **square root of the first sum**—namely $\\sqrt{250 - \\sqrt{12500}}$, formed from the square of the whole quantity and the square of the greater part—to the **square root of the second sum**—namely $\\sqrt{450 - \\sqrt{112500}}$, formed from the square of the whole quantity and the square of its lesser part—is **precisely the ratio of the side of the cube to the side of the triangle of the twenty-base body [icosahedron]**, when both of the said bodies are circumscribed or surrounded by one and the same sphere!

   These roots of sums [nested radicals] are called in geometry **lines having power over the said sums** (*linee potenti sopra dicti congionti*): that is, $\\sqrt{250 - \\sqrt{12500}}$ means a line whose *power* or square is equal to that exact sum ($250 - \\sqrt{12500}$); and similarly $\\sqrt{450 - \\sqrt{112500}}$ means a quantity whose power or square is equal to $450 - \\sqrt{112500}$.

   By practicing algebraists (*pratici*), such roots are called by another name **universal roots** (*radici universali*) or **bound roots** (*radici legate*), as appears in our aforesaid work [*Summa de Arithmetica*], in the Third Treatise of its Eighth Distinction, beginning at folio 120 of the said volume. These quantities belong to the most subtle investigation and pertain to speculative practice (*pratica speculativa*), as is shown at length in that volume; and, Most Exalted Prince, it is impossible to express them in any simpler or lower terms (*con più depresse denotationi*).

.. qed::

   And this entire speculative effect is demonstrated geometrically by the ninth proposition of the Fourteenth Book (Campanus XIV.9), together with several others adduced in that place by Campanus.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Mathematical Verification of the Twelfth Effect (Campanus XIV.9)**:
   - Let a sphere have diameter $D$. By :just:`XIII.15`, the edge of the inscribed cube satisfies $s_{\\text{cube}}^2 = \\frac{1}{3}D^2$.
   - By :just:`XIII.16.p` and :just:`XIII.18`, the edge of the inscribed icosahedron satisfies $s_{\\text{icosa}}^2 = \\frac{5 - \\sqrt{5}}{10}D^2$.
   - Meanwhile, in Pacioli's formula with $a+b = 10$, $a = \\sqrt{125}-5$, and $b = 15-\\sqrt{125}$:
     - $(a+b)^2 + a^2 = 250 - \\sqrt{12500} = 250 - 50\\sqrt{5} = 50(5 - \\sqrt{5})$.
     - By the Fifth Effect (Chapter XIV, :just:`XIII.4`), $(a+b)^2 + b^2 = 3a^2 = 450 - \\sqrt{112500} = 3 \\times 50(3 - \\sqrt{5})$!
     - Wait: notice that $\\frac{\\sqrt{(a+b)^2 + b^2}}{\\sqrt{(a+b)^2 + a^2}} = \\frac{\\sqrt{3a^2}}{\\sqrt{(a+b)^2 + a^2}} = \\frac{\\sqrt{3} \\cdot a}{\\sqrt{(a+b)^2 + a^2}}$. Since $(a+b)^2 + a^2$ is the square of the hypotenuse of a right triangle with legs $a+b$ (radius of the pentagon's/icosahedron's defining circle) and $a$ (the decagon side), by :just:`XIII.10` ($s_5^2 = s_6^2 + s_{10}^2$), $\\sqrt{(a+b)^2 + a^2}$ is the **side of the pentagon** ($s_{\\text{icosa}}$) inscribed in the circle of radius $a+b$, while $a$ is the decagon side!
   - In Campanus's Latin text of Book XIV, Proposition 9 proves this exact relation between the cube edge and icosahedron edge via the segments of a line cut in extreme and mean ratio.
2. **Universal / Bound Roots (*Radici Universali / Radici Legate*)**: Pacioli introduces the Renaissance algebraic term *radice universale* or *radice legata* (written *R.V.* in the *Summa*, Distinctio VIII, Tractatus 3, f. 120r), where the radical sign governs an entire binomial or apotome ($\\sqrt{250 - \\sqrt{12500}}$).""",
    },
    22: {
        "title_en": (
            "On Its Thirteenth Most Worthy Effect"
        ),
        "body_en": """\
.. enunciation::

   For its **thirteenth effect**, it is no small matter of wonder that without its aid one can never construct the **equilateral and equiangular pentagon**—that is, the figure of five equal sides adduced above in the Ninth Effect and to be adduced again below—and that without the said pentagon, as will be told, it is impossible either to form or to imagine the **noblest body above all the others**, called the **Dodecahedron** (*duodecedron*)—that is, the body of twelve equilateral and equiangular pentagons, otherwise called the body of twelve pentagonal bases—whose form, as will be told, the divine **Plato** [in his *Timaeus*] attributed for the most fitting reasons to the **Fifth Essence**, namely to **Heaven** (:just:`IV.10`, :just:`IV.11`, :just:`XIII.17`).

.. assertion:: Euclid's Deductive Architecture in Books II, IV, V, and VI

   To this end, our Philosopher in the **tenth proposition of the Fourth Book** (:just:`IV.10`) teaches us how to construct an **isosceles triangle** of this condition: namely, that **each of the two angles at its base is double the remaining angle** [at the apex, i.e., $72^\\circ, 72^\\circ, 36^\\circ$].

   And he did this because, when we wish to know how to form the equilateral and equiangular pentagon, and to **inscribe** and **circumscribe** it in and about a circle—that is, to form it both inside and outside a given circle with exactness—it would have been impossible unless he had first taught us how to construct the said triangle, as appears from the eleventh and twelfth propositions of the said Fourth Book (:just:`IV.11`, :just:`IV.12`).

   Now, in order to construct the said triangle, it is of necessity required to **divide a line according to our Divine Proportion**, as he shows us in the said tenth proposition of the Fourth Book (:just:`IV.10`).

   It is true that in that place (:just:`IV.10`) Euclid does not state in words that the said line is divided "according to the said proportion and its conditions," because he had not yet given us knowledge of what a **proportion** is—which topic he reserves for his **Fifth Book**! For it is never his custom to introduce into his demonstrations subsequent doctrines of which knowledge has not yet been given; rather, he uses **only antecedent propositions**, and this rigorous deductive order is maintained throughout all fifteen of his Books.

.. qed::

   Therefore, for the purpose of the said triangle in :just:`IV.10`, he does not say "divide the said line according to the proportion having a mean and two extremes," but says instead: **"by the eleventh proposition of the Second Book (:just:`II.11`), divide it into two such parts that the square of one part is equal to the product [rectangle] of the other part and the whole line"**—which in substance and power means nothing other than dividing it according to our Divine Proportion, as appears from the third definition of the Sixth Book (:just:`VI.def.3`) and the twenty-ninth [thirtieth] proposition of the same Book (:just:`VI.30`), and as we ourselves explained above when we clarified how its mean and its extremes are to be understood under the First Effect [Chapter VII].""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **The Golden Triangle (:just:`IV.10`) and the Pentagon (:just:`IV.11`–:just:`IV.12`)**: In :just:`IV.10`, Euclid constructs the $72^\\circ\\text{–}72^\\circ\\text{–}36^\\circ$ isosceles triangle by dividing the leg $AB$ at $C$ via :just:`II.11` so that $AB \\cdot BC = AC^2$, and placing $BD = AC$ as the base. In :just:`IV.11` he inscribes this golden triangle into a circle and bisects the two $72^\\circ$ base angles to obtain the five vertices of the regular pentagon.
2. **Pacioli's Insight into Euclid's Axiomatic Method**: Chapter XXII contains a remarkably lucid analysis of the architecture of Euclid's *Elements*—one that directly anticipates modern historiography of Greek mathematics (and connects directly to the GEOMETOR G-Index dependency graph!). Pacioli explains why Euclid proves the golden section twice—first by geometric areas in :just:`II.11` ($AB \\cdot BC = AC^2$) and again by proportions in :just:`VI.30` ($AB : AC = AC : BC$): because :just:`IV.10`–:just:`IV.11` (the regular pentagon) stands in Book IV *prior* to Eudoxus's general theory of proportions in Book V, Euclid could not legally invoke ratios in Book IV without violating his strict deductive rule of using only *antecedenti* (previously proved propositions) and never *sequenti*!""",
    },
    23: {
        "title_en": (
            "How, Out of Reverence for Our Salvation, the Said Effects Conclude"
        ),
        "body_en": """\
It does not seem fitting to me, Most Exalted Duke, to extend my discourse at present to any more of its infinite effects—for paper would not suffice for the ink needed to express them all! Rather, we have chosen **only these thirteen** from among the rest out of reverence for the **Twelvefold Company** (*la turba duodena*, the Twelve Apostles) and its Most Holy Head, our Redeemer **Christ Jesus**.

For having bestowed upon this proportion the name **Divine**, it is fitting that its effects should likewise come to a close with the **number of our salvation**: namely, the **Thirteen Articles** [of the Creed] and the **Twelve Apostles together with our Savior**—toward which sacred college I perceive Your Ducal Highness bears a singular devotion, having caused it to be arrayed in the aforesaid most sacred Temple of the Graces [*Santa Maria delle Grazie*] by our aforesaid **Leonardo** with his graceful brush [*The Last Supper*].

Nevertheless, in the following chapters we shall not cease to adduce still further effects as occasion requires, inasmuch as—as will be told—without this proportion it is impossible either to form or to imagine the harmony and worthy agreement among themselves of all the **Five Regular Bodies** and their **Dependent Bodies**, for the sake of which we have set forth the thirteen effects already stated, so that what follows from them may be rendered all the clearer.""",
        "notes": """\
Historical and Philological Commentary
--------------------------------------

1. **Numerological Closure ($13 = 1 + 12$) and Leonardo's *Cenacolo***: Pacioli brings Section 2 (Chapters VII–XXIII, the Thirteen Effects of the Divine Proportion) to a close by linking the number **13** to the 13 Articles of the Scholastic Apostles' Creed and to Christ surrounded by the Twelve Apostles ($1 + 12 = 13$). In a masterstroke of courtly rhetoric, he ties this theological-mathematical structure directly back to Ludovico Sforza's patronage of Leonardo da Vinci's *Last Supper* in the refectory of Santa Maria delle Grazie (already praised in Chapters I and III), where Christ and the twelve Apostles form a visible thirteenfold harmonic composition before the viewer's eyes.""",
    },
})
