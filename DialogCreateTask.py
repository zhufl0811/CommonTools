from PySide2.QtWidgets import QDialog, QFileDialog
from ui.dialogcreatevideotask import Ui_DialogCreateVideoTask
import ffmpeg


class CreateVideoTask(QDialog, Ui_DialogCreateVideoTask):
    def __init__(self):
        super(CreateVideoTask, self).__init__()
        self.setupUi(self)
        self.btnSelectSrc.clicked.connect(self.select_src_clicked)

        # (
        #     ffmpeg
        #     .input(r'C:\Users\zfl\Downloads\老人与海.mp4')
        #     .hflip()
        #     .output(r'C:\Users\zfl\Downloads\老人与海_1.mp4')
        #     .run()
        # )

        # ffmpeg.input(r'C:\Users\zfl\Downloads\老人与海.mp4').hflip().output(r'C:\Users\zfl\Downloads\老人与海_1.mp4').run()

    def select_src_clicked(self):
        src_path, _ = QFileDialog.getOpenFileName(self, "选择视频文件", "", "")
        self.lineEditVideoSrc.setText(src_path)

    def select_dst_clicked(self):
        pass

    # def