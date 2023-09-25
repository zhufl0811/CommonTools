from ui.video_resize_task_item import Ui_Form
from PySide2.QtWidgets import QWidget
import ffmpeg
import os


class VideoResizeTaskItem(QWidget, Ui_Form):
    def __init__(self, filepath):
        super().__init__()
        self.setupUi(self)
        s = ffmpeg.probe(filepath, 'ffprobe')
        self.labelFileName.setText(os.path.basename(filepath))
        # self.labelVideoInfo.setText()
        self.pgsBar.setValue(0)
        self.get_video_info(s)

    def get_video_info(self, s):
        w = 0
        h = 0
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
                    w = item['width']
                    h = item['height']
                    codec_name = item['codec_name']
                    fps = round(float(item['nb_frames'])/float(item['duration']))
                    break
        size = f"{round(size/1024/1024,2)}Mb"
        info = f"{w}x{h},{duration}秒,{fps}fps,{codec_name},{size}"
        self.labelVideoInfo.setText(info)
