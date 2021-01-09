from scenedetect import VideoManager
from scenedetect import SceneManager
from cv2 import cv2
import os

from scenedetect.detectors import ContentDetector

ROOT = "./videos/"

def find_scenes(video_name, threshold=30.0):
    # Create our video & scene managers, then add the detector.
    video_manager = VideoManager([ROOT+video_name])
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))

    # Base timestamp at frame 0 (required to obtain the scene list).
    base_timecode = video_manager.get_base_timecode()

    # Improve processing speed by downscaling before processing.
    video_manager.set_downscale_factor()

    # Start the video manager and perform the scene detection.
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)

    # Each returned scene is a tuple of the (start, end) timecode.
    return scene_manager.get_scene_list(base_timecode)

def capture(timecode, video_manager, folder_name):
    video_manager.seek(timecode)
    r, img = video_manager.retrieve()
    if r:
        fname = "./images/%s/%d.jpg" % (folder_name, timecode.get_frames())
        print(fname)
        cv2.imwrite(fname, img)
        

def get_frames(video_name, scenes):
    count = 0
    folder_name = video_name[:-4]
    for scene in scenes:
        start, end = scene
        video_manager = VideoManager([ROOT+video_name]) 
        video_manager.start()
        # mid = start + ((end-start).get_seconds() / 2.0)
        capture(start, video_manager, folder_name)
        # capture(mid, video_manager, folder_name)
        capture(end, video_manager, folder_name)


    video_manager.release()

def get_trailer_frames():
    video_names = os.listdir(ROOT)
    # print(video_names)

    for video_name in video_names:
        os.mkdir("./images/" + video_name[:-4])
        scenes = find_scenes(video_name)
        # print(scenes)
        get_frames(video_name, scenes)

get_trailer_frames()

