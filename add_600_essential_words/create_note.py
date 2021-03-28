from collections import defaultdict

from aqt import mw
from aqt.utils import showInfo, askUser, showWarning
from .settings import DECK_NAME, NOTE_NAME
from anki.notes import Note

from .settings import *


def create_note(word_detail:dict) -> None:
    did = mw.col.decks.id(DECK_NAME)
    m = mw.col.models.byName(NOTE_NAME)

    n = Note(col=mw.col,model=m)
    n._fmap = defaultdict(str, n._fmap)

    for k, v in word_detail.items():
        n[k] = v

    num_card = mw.col.add_note(n, did)
    return num_card

    
    
    
