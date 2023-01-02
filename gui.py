from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QPushButton
)

import sys
app = QApplication(sys.argv)
app.setStyle('macos')

window = QWidget()
window.setWindowTitle("Eco Tech Mac - Lock Check")
window.setFixedSize(300, 150)

layout = QVBoxLayout()

"""
'lock check' only run function used to determine lock status and return as json.
'lock check + audit' run lock check functions, and additional system info audit functions and return as json.
"""
dropdown = QComboBox()
dropdown.addItem('lock check')
dropdown.addItem('lock check + audit')

button = QPushButton('Select')

layout.addWidget(QLabel('select option:'))
layout.addWidget(dropdown)
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec()
