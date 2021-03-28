from aqt.qt import *
from collections import defaultdict


def new_word_dialog(mw):
    d = QDialog(mw)
    d.setWindowTitle("Pull from Duolingo")
    d.setWindowModality(Qt.WindowModal)
    vbox = QVBoxLayout()
    l = QLabel("""<p>Please enter your <strong>Word</strong>.</p>""")
    l.setOpenExternalLinks(True)
    l.setWordWrap(True)
    vbox.addWidget(l)
    vbox.addSpacing(20)
    g = QGridLayout()
    field_labels = {}
    field_keys = ("Word", "Parts_of_speech", "Meaning", "Example")
    for _i, field_name in enumerate(field_keys):
        label = QLabel(_(f"{field_name}:"))
        g.addWidget(label, _i, 0)
        field_labels[field_name] = QLineEdit()
        g.addWidget(field_labels[field_name], _i, 1)

    vbox.addLayout(g)
    bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    bb.button(QDialogButtonBox.Ok).setAutoDefault(True)
    bb.accepted.connect(d.accept)
    bb.rejected.connect(d.reject)
    vbox.addWidget(bb)
    d.setLayout(vbox)
    d.show()
    accepted = d.exec_()

    field_data = { k: fl.text() for k, fl in field_labels.items() }

    if accepted:
        return field_data
    else:
        return None