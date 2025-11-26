"""
run the main app
"""
from .pacioli import Pacioli


def run() -> None:
    reply = Pacioli().run()
    print(reply)
