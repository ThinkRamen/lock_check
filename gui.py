from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QComboBox, QLabel
)

import sys
app = QApplication(sys.argv)
app.setStyle('macos')

window = QWidget()
window.setWindowTitle("Lock Check")
window.setFixedSize(250, 250)

layout = QVBoxLayout()
dropdown = QComboBox()
layout.addWidget(QLabel('select: '))
layout.addWidget(dropdown)

window.setLayout(layout)
window.show()
app.exec()
