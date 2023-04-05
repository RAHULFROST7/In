import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtMultimedia import QCamera,QCameraInfo
from PyQt5.QtMultimedia import QAudioInput, QAudioDeviceInfo,QAudioFormat


class BrowserFrame(QFrame):
    def __init__(self):
        super().__init__()

        # create a QWebEngineView widget and add it to the frame
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://meet.google.com/jkr-zxmb-vkq'))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)
        self.setFixedSize(1200, 1000)

        # create a navbar and add it to the frame
        navbar = QToolBar()
        self.layout.addWidget(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
        

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://meet.google.com/"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(1900, 1000)


        # create a horizontal layout
        self.layout = QHBoxLayout()

        # create a frame and add it to the layout
        self.frame1 = BrowserFrame()
        self.layout.addWidget(self.frame1)

        # add a stretch factor to move the frame to the left
        self.layout.addStretch(1)

        # create another frame and add it to the layout
        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.layout.addWidget(self.frame2)

        # set the layout as the central widget of the main window
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
