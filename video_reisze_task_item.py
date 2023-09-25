from ui.video_resize_task_item import Ui_Form
from PySide2.QtWidgets import QWidget, QMessageBox
import ffmpeg
import os
import time
from threading import Thread


class VideoResizeTaskItem(QWidget, Ui_Form):

    ratio_choice = ['自定义', '3/4', '1/2', '1/3', '1/4', '1/5', '1/8', '1/10', '1/20']

    def __init__(self, filepath):
        super().__init__()
        self.setupUi(self)
        self.filepath = filepath
        self.video_info = ffmpeg.probe(self.filepath, 'ffprobe')
        self.w = 0
        self.h = 0
        self.init_ui()

    def init_ui(self):
        self.labelFileName.setText(os.path.basename(self.filepath))
        self.get_video_info(self.video_info)
        self.add_ratios()
        self.labelState.setText('未开始')

        self.comboBoxRatio.currentIndexChanged.connect(self.on_ratio_selected)
        self.btnStart.clicked.connect(self.on_start_clicked)

    def update_progress_bar(self, p):
        self.labelState.setText('进行中')
        while True:
            state = p.poll()
            if state is not None:
                if state == 0:
                    self.labelState.setText('已完成')
                else:
                    self.labelState.setText('任务失败')
                break
            time.sleep(1)

    def get_video_info(self, s):
        fps = 0
        size = 0
        duration = 0
        bit_rate = 0
        codec_name = ''
        if 'format' in s:
            f_info = s.get('format')
            duration = round(float(f_info.get('duration')), 1)
            size = float(f_info.get('size'))
            bit_rate = f_info.get('bit_rate')
        if 'streams' in s:
            for item in s.get('streams'):
                if item['codec_type'] == 'video':
                    self.w = int(item['width'])
                    self.h = int(item['height'])
                    codec_name = item['codec_name']
                    fps = round(float(item['nb_frames'])/float(item['duration']))
                    break
        size = f"{round(size/1024/1024,2)}Mb"
        info = f"{self.w}x{self.h},{duration}秒,{fps}fps,{codec_name},{size}"
        self.labelVideoInfo.setText(info)

    def add_ratios(self):
        for ratio in self.ratio_choice:
            self.comboBoxRatio.addItem(ratio)

    def on_ratio_selected(self):
        ratio = self.comboBoxRatio.currentText()
        if ratio == '自定义':
            self.lineEditResizeW.setEnabled(True)
            self.lineEditResizeH.setEnabled(True)
        else:
            self.lineEditResizeW.setDisabled(True)
            self.lineEditResizeH.setDisabled(True)
            r = eval(ratio)
            r_w = round(r * self.w)
            r_h = round(r * self.h)
            if r_w % 2 == 1:
                r_w += 1
            if r_h % 2 == 1:
                r_h += 1

            self.lineEditResizeW.setText(str(r_w))
            self.lineEditResizeH.setText(str(r_h))

    def on_start_clicked(self):
        if not self.lineEditResizeW.text() or not self.lineEditResizeH.text():
            QMessageBox.warning(self, "warning", "请输入正确的缩放宽高", QMessageBox.Close)
            return
        r_w = int(self.lineEditResizeW.text())
        r_h = int(self.lineEditResizeH.text())
        input_video = ffmpeg.input(self.filepath)
        v = input_video.video.filter('scale', f'{r_w}x{r_h}')
        a = input_video.audio
        suf = '.' + os.path.basename(self.filepath).split('.')[-1]
        out_path = os.path.join(
            os.path.dirname(self.filepath),
            self.filepath.replace(suf, f'_resize_{r_w}x{r_h}{suf}')
        )
        out = ffmpeg.output(v, a, out_path).overwrite_output()
        p = out.run_async()
        t = Thread(target=self.update_progress_bar, args=(p,))
        t.start()
