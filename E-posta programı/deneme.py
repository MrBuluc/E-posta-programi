import sys
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        menubar = self.menuBar()

        dosya = menubar.addMenu('Dosya')
        düzenle = menubar.addMenu('Düzenle')

        dosya_ac = QAction('Dosya Aç', self)
        dosya_ac.setShortcut('Ctrl+O')
        dosya_kaydet = QAction('Dosya Kaydet', self)
        dosya_kaydet.setShortcut('ctrl+S')
        cıkıs = QAction('Cıkıs Yap', self)
        cıkıs.setShortcut('Ctrl+Q')

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cıkıs)

        ara_ve_değiştir = düzenle.addMenu('Ara ve Değiştir')

        ara = QAction('Ara', self)
        değiştir = QAction('Değiştir', self)
        temizle = QAction('Temizle', self)

        ara_ve_değiştir.addAction(ara)
        ara_ve_değiştir.addAction(değiştir)
        düzenle.addAction(temizle)

        #cıkıs.triggered.connect(self.CıkısYap)

        self.show()

    def CıkısYap(self):
        qApp.quit()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())