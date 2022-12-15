import sys
from PyQt5.QtWidgets import *



widgets = [
            QCheckBox,
            QLabel,
            QLineEdit,
]

app = QApplication(sys.argv)
root = QWidget()
grid = QHBoxLayout()
toolbar = QToolBar("My main toolbar")
for w in widgets:
    grid.addWidget(w())
root.setLayout(grid)
#root.resize(250, 250)
root.setWindowTitle("Hello world!")
root.show()
if __name__ == '__main__':
    sys.exit(app.exec_())