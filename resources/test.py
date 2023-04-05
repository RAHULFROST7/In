from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QApplication
import sys

class BrowserWidget(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.load(QUrl('https://webrtc.github.io/samples/src/content/devices/input-output/'))

        self.page = self.page()
        self.profile = QWebEngineProfile.defaultProfile()
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        self.page.setProfile(self.profile)

        self.page.setAudioCaptureEnabled(True)
        self.page.setVideoCaptureEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = BrowserWidget()
    widget.show()
    sys.exit(app.exec_())
