from PySide2.QtWidgets import QApplication, QMainWindow
from ui.mainwindow import Ui_MainWindow
# from qt_material import apply_stylesheet
from functools import partial


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.function_map = {
            'video_resize':{
                'nav_btn':self.btnNavVideoResize,
                'page':self.pageVideoResize
            },
            'video_format':{
                'nav_btn':self.btnNavVideoFormat,
                'page':self.pageVideoFormat
            },
            'video_2audio':{
                'nav_btn':self.btnNavVideoAudio,
                'page':self.pageVideo2Audio
            }
        }
        for key, value in self.function_map.items():
            value['nav_btn'].clicked.connect(partial(self.switch_tab, key))

    def switch_tab(self, f_name):
        self.stackedWidget.setCurrentWidget(self.function_map[f_name]['page'])
        # for key, value in self.function_map.items():
        #     if key == f_name:
        #         value['nav_btn'].setProperty('class', 'success')
        #     else:
        #         value['nav_btn'].setProperty('class', 'small_button')


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    # apply_stylesheet(app, theme='light_red.xml', invert_secondary=True)
    win.show()
    app.exec_()