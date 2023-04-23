from collections import defaultdict

from aqt import mw
from aqt.utils import showInfo
from .settings import DECK_NAME, NOTE_NAME
from anki.notes import Note


def create_model():
    models = mv.col.models

    new_model = models.new(NOTE_NAME)

    field_names = ["Meaning", "Word", "Parts_of_speech", "IPA", "Sound_US", "Example"]

    for field_name in field_names:
        field = models.newField(field_name)
        models.addField(new_model, field)

    template = models.new_template("Card Oxford")
    template["qfmt"] = """{{Meaning}}<div>{{type:Word}}</div>"""
    template[
        "afmt"
    ] = """{{Meaning}}<hr id="answer"><div>{{type:Word}}</div><i>{{Parts_of_speech}}</i><div class="sound">{{Sound_US}}/{{IPA}}/</div>{{Example}}"""
    models.addTemplate(new_model, template)
    models.add(new_model)

    return new_model


def create_note(word_detail: dict) -> bool:
    col = mw.col
    deck = col.decks.by_name(DECK_NAME)
    did = deck["id"]
    if did is None:
        showInfo(f"You must create desk name: {DECK_NAME}")
        return False
    m = col.models.by_name(NOTE_NAME)
    if m is None:
        m = create_model()
    if m:
        n = Note(col=col, model=m)
        n._fmap = defaultdict(str, n._fmap)

        for k, v in word_detail.items():
            n[k] = v

        _num_card = col.add_note(n, did)
        return True
    return False
