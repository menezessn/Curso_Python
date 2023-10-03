
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout, 
                               QGridLayout, QMainWindow )#widgets são coisas que estão na janela



class MyWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.button = self.make_button('Primeiro')
        self.button.clicked.connect(self.segunda_acao_marcada)

        self.button2 = self.make_button("Segundo")
        self.button3 = self.make_button('Terceiro')

        # button2.show() // abre duas janelas quando eu coloco apenas o botão como widget

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha Janela')
        self.grid_layout  = QGridLayout()
        self.grid_layout.addWidget(self.button,1,1)
        self.grid_layout.addWidget(self.button2,1,2 )
        self.grid_layout.addWidget(self.button3,3,1 ,1,2)
        self.central_widget.setLayout(self.grid_layout)
        #status bar 
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Show Message')

        #MenuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Qualquer coisa')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.muda_mensagem_status_bar)

        self.segunda_action = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(self.segunda_acao_marcada)
        self.segunda_action.hovered.connect(self.segunda_acao_marcada)

    @Slot()
    def muda_mensagem_status_bar(self):
            self.status_bar.showMessage('O meu slot foi executado')
        

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado', self.segunda_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text) 
        btn.setStyleSheet('font-size: 40px; color:red')
        return btn

if __name__ == '__main__':
    app = QApplication(sys.argv) #o app em si 
    window = MyWindow()
    window.show()
    app.exec() #inicia o loop da aplicação


