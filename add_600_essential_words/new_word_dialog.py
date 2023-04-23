from aqt.qt import (
    QDialog,
    Qt,
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QLineEdit,
    QDialogButtonBox,
)


def new_word_dialog(mw):
    dialog = QDialog(mw)
    dialog.setWindowTitle("Pull from Duolingo")
    dialog.setWindowModality(Qt.WindowModality.WindowModal)
    vbox = QVBoxLayout()
    label = QLabel("""<p>Please enter your <strong>Word</strong>.</p>""")
    label.setOpenExternalLinks(True)
    label.setWordWrap(True)
    vbox.addWidget(label)
    vbox.addSpacing(20)
    grid_layout = QGridLayout()
    field_labels = {}
    field_keys = ("Word", "Parts_of_speech", "Meaning", "Example")
    for _i, field_name in enumerate(field_keys):
        label = QLabel(f"{field_name}:")
        grid_layout.addWidget(label, _i, 0)
        field_labels[field_name] = QLineEdit()
        grid_layout.addWidget(field_labels[field_name], _i, 1)

    vbox.addLayout(grid_layout)
    button_box = QDialogButtonBox(
        QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
    )
    button_box.button(QDialogButtonBox.StandardButton.Ok).setAutoDefault(True)
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)
    vbox.addWidget(button_box)
    dialog.setLayout(vbox)
    dialog.show()
    accepted = dialog.exec()

    field_data = {k: fl.text() for k, fl in field_labels.items()}

    if accepted:
        return field_data
    else:
        return None
