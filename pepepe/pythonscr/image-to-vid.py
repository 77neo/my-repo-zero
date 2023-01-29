import os
import cv2
from PIL import Image

def generate_video():
    video_name = 'video.avi'
    images = ["napoleon.jpg","napoleon.jpg","napoleon.jpg","napoleon.jpg","napoleon.jpg","napoleon.jpg","napoleon.jpg","napoleon.jpg",]
   
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') 

    # Array images should only consider 
    # the image files ignoring others if any 
    
    frame = cv2.imread(images[0])
    
    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

    # Appending the images to the video one by one 
    for image in images:
        video.write(cv2.imread(image))
        
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()
    video.release()  # releasing the video generated 
    
generate_video()


def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("ffmpeg -i {input} -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 {output}.mp4".format(input = avi_file_path, output = output_name))
    return True

convert_avi_to_mp4("video.avi", "video")