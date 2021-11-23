from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import menu, show

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() +5)
        size.setWidth(max(size.width(), size.height()))
        return size

class ComponentSearch(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)

        # Buttons and Edit
        self.searchButton = Button('Search', self.buttonClicked)
        self.clearButton = Button('C', self.buttonClicked)
        self.previousButton = Button('<-', self.buttonClicked)
        self.nextButton = Button('->', self.buttonClicked)

        self.searchEdit = QLineEdit()
        self.consolEdit = QTextEdit()
        self.pictureEdit = QTextEdit()

        #picture = QPixmap()

        # Grid Creation and Placement
        pictureLayout = QGridLayout()
        searchLayout = QGridLayout()
        consolLayout = QGridLayout()
        nextLayout = QGridLayout()

        pictureLayout.addWidget(self.pictureEdit, 1, 0, 4, 1)
        searchLayout.addWidget(self.searchEdit, 1, 2)
        searchLayout.addWidget(self.searchButton, 1, 3)
        searchLayout.addWidget(self.clearButton, 1, 4)
        consolLayout.addWidget(self.consolEdit, 2, 2, 3, 3)
        nextLayout.addWidget(self.previousButton, 5, 0)
        nextLayout.addWidget(self.nextButton, 5, 1)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(pictureLayout, 1, 0, 4, 1)
        mainLayout.addLayout(nextLayout, 5, 0, 5, 1)
        mainLayout.addLayout(searchLayout, 1, 2, 1, 3)
        mainLayout.addLayout(consolLayout, 2, 2, 3, 3)

        self.setLayout(mainLayout)

        self.setWindowTitle("Allergy Component Checker")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        if key == 'Search':
            try:
                result = show.showConsol(self.display.text())
                self.consolEdit.setText(result)
            except:
                QMessageBox.warning(self, '해당 성분을 포함한 음식이 존재하지 않음', "입력을 초기화 합니다.")
                self.display.setText('')
        elif key == 'C':
            self.display.setText('')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    search = ComponentSearch()
    search.show()
    sys.exit(app.exec_())