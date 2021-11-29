from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from menu import Menu
from show_ import Show

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

class ComponentSearch(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Buttons and Edit
        self.searchButton = Button('Search', self.buttonClicked)
        self.clearButton = Button('C', self.buttonClicked)
        self.previousButton = Button('<-', self.buttonClicked)
        self.nextButton = Button('->', self.buttonClicked)

        self.searchEdit = QLineEdit()
        self.consolEdit = QTextEdit()
        self.consolEdit.setReadOnly(True)
        self.pictureEdit = QLabel()

        self.pixmap = QPixmap()
        self.pixmap.load('default.jfif')
        self.name = 'default.jfif'
        self.picture = self.pixmap.scaled(400, 400)
        self.pictureEdit.setPixmap(self.picture)

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

        self.startCheck()

    def startCheck(self):
        self.menu = Menu()
        self.show_ = Show()

    def buttonClicked(self):
        component = self.searchEdit.text()
        key = self.sender().text()

        if key == 'Search':
            try:
                result = ''
                if component in self.menu.components_list:
                    self.name_result, self.comp_result = self.show_.showConsol(component)
                    result += "해당 성분이 포함된 음식" + "\n" * 2
                    for a in range(len(self.name_result)):
                        result += (self.name_result[a] + " : ")
                        for b in self.comp_result[a]:
                            result += b + ", "
                        result += "\n" * 2
                else:
                    raise
                self.consolEdit.setText(str(result))
            except:
                QMessageBox.warning(self, "입력을 초기화 합니다.", '해당 성분을 포함한 음식이 존재하지 않습니다.')
                self.searchEdit.setText('')
        elif key == '<-':
            self.imgNames = [ '13.png', '12.png', '11.png', '10.png', '9.png', '8.png',
                              '7.png', '6.png', '5.png', '4.png', '3.png', '2.png', '1.png', 'default.jfif' ]
            for i in range(len(self.imgNames)):
                if self.name == self.imgNames[i]:
                    previous_file_name = self.imgNames[0 if len(self.imgNames) - 1 == i else i + 1]
                    self.pixmap.load(previous_file_name)
                    self.picture = self.pixmap.scaled(400, 400)
                    self.pictureEdit.setPixmap(self.picture)
                    self.name = previous_file_name
                    break
        elif key == '->':
            self.imgNames = [ 'default.jfif', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png',
                              '8.png', '9.png', '10.png', '11.png', '12.png', '13.png' ]
            for i in range(len(self.imgNames)):
                if self.name == self.imgNames[i]:
                    next_file_name = self.imgNames[0 if len(self.imgNames) - 1 == i else i + 1]
                    self.pixmap.load(next_file_name)
                    self.picture = self.pixmap.scaled(400, 400)
                    self.pictureEdit.setPixmap(self.picture)
                    self.name = next_file_name
                    break
        elif key == 'C':
            self.searchEdit.setText('')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    search = ComponentSearch()
    search.show()
    sys.exit(app.exec_())
