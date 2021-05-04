from moviepy.editor import VideoFileClip, concatenate_videoclips
import requests
import os


a = os.path.join(os.getcwd(), 'teste123')
os.mkdir(a)


url = 'https://production.assets.clips.twitchcdn.net/AT-cm%7C1123209676.mp4?sig=6c0711542d09875dec46c6d3f4c38806228bc4c3&token=%7B%22authorization%22%3A%7B%22forbidden%22%3Afalse%2C%22reason%22%3A%22%22%7D%2C%22clip_uri%22%3A%22%22%2C%22device_id%22%3A%226MEEURB4czL4io4WZtHZbxgaLBNs9XCJ%22%2C%22expires%22%3A1619968431%2C%22user_id%22%3A%2260144112%22%2C%22version%22%3A2%7D'

r = requests.get(url, allow_redirects=True)
open('./clips/testeClipDownload.mp4', 'wb').write(r.content)

clip1 = VideoFileClip("./clips/video1.mp4")
clip2 = VideoFileClip("./clips/video2.mp4")
final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("./clips/my_concatenation.mp4")