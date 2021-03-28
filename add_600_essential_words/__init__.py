from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *

from .new_word_dialog import new_word_dialog
from .dictionary_search import dictionary_search
from .settings import NOTE_NAME
from .create_note import create_note

def add_600_ew() -> None:
    while True:
        word_detail = new_word_dialog(mw)
        if word_detail is None:
            break
        elif all(word_detail.values()):
            word_detail.update(dictionary_search(word_detail))
            create_note(word_detail)
            showInfo(f"Added word: \"{word_detail['Word']}\".")
        else:
            showInfo(f"All field can't be blank.")
    return None


action = QAction("Add 600 Essential Words IELTS", mw)
qconnect(action.triggered, add_600_ew)
mw.form.menuTools.addAction(action)