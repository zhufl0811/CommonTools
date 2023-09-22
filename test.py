import ffmpeg
import time
# video_format = "flv"
# server_url = "http://127.0.0.1:8080"
# s = ffmpeg.probe(r'C:\Users\zfl\Downloads\老人与海.mp4', 'ffprobe')
# print(s)
# process = (
#     ffmpeg
#     .input(r'C:\Users\zfl\Downloads\老人与海.mp4')
#     .output(
#         server_url,
#         codec = "copy", # use same codecs of the original video
#         listen=1, # enables HTTP server
#         f=video_format)
#     .global_args("-re") # argument to act as a live stream
#     .run()
# )
input_video = ffmpeg.input(r'C:\Users\zfl\Downloads\老人与海.mp4')
v = input_video.video.filter('framerate', '10').filter('scale', '960x540').filter('rotate', 'PI/6')
a = input_video.audio
out = ffmpeg.output(v, a, r'C:\Users\zfl\Downloads\老人与海x.mp4').overwrite_output()
p = out.run_async()
p.wait()