##first you need to install "moviepy" package (pip install "moviepy")
import os
from moviepy.editor import *

##list all videos in the folder video
files = os.listdir("./video_folder")
if (len(files) == 0):
    print("Empty Folder !!!")
else:
    cpt_videos = 0
    for i in files:
        if (i.split(".")[-1] == "mp4"):
            print("******** Converting ("+str(i)+") ********")
            video = VideoFileClip("./video_folder/"+str(i))
            video.audio.write_audiofile("./audio_folder/"+i.split(".")[1]+".mp3")
            cpt_videos += 1
    if(cpt_videos != 0):
        print(f"*******Converstion successful (converted {cpt_videos} videos in total)")
    else:
        print(f"No (mp4) videos found in the directory !!!")



