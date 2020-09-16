import cv2
import numpy as np
import os
from django.conf import settings
from scenedetect import VideoManager
from scenedetect import SceneManager
from scenedetect.detectors import ContentDetector

def find_scenes(videoURL):
    threshold=30.0
    video_path=settings.MEDIA_ROOT
    video_path=video_path.replace('\\','/')

    
    video_manager = VideoManager([video_path+videoURL])
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))

   
    base_timecode = video_manager.get_base_timecode()
    #base_timecode = video_manager.get(cv2.CAP_PROP_POS_MSEC)
    video_manager.set_downscale_factor()

    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    scene_list = scene_manager.get_scene_list(base_timecode)
    
    return scene_manager.get_scene_list(base_timecode)


def readvid(videoURL, frames, title):
    path_root=settings.MEDIA_ROOT
    path_root=path_root.replace('\\','/')
    new_dir_path=path_root+videoURL
    new_dir_path=os.path.splitext(new_dir_path)[0]

    cap=cv2.VideoCapture(path_root+videoURL)

    if not (os.path.isfile(path_root+videoURL)):
        print("없음")
        return #에러메세지 보내주고 팝업띄워야함
    
    frame= cap.read()

    try_3times=0
    while (not cap.isOpened()):
        frame= cap.read()
        waitKey(1)
        try_3times=try_3times+1
        if try_3times>=3 :
            return

    cut_nums=len(frames)
    idx=0
    cnt=0
    frame_num=0
    while (cap.isOpened()):
        ret, frame= cap.read()
        if ret :
            frame_num=frame_num+1
            if frames[idx][1].get_frames() == frame_num:
                idx=idx+1
                if frames[idx][1].get_seconds()-frames[idx][0].get_seconds() < 1:
                    continue
                if idx>=cut_nums:
                    idx=idx-1
                    break
                if not os.path.isdir(new_dir_path):
                    os.mkdir(new_dir_path)
                cv2.imwrite(new_dir_path + '/' + title + '_' + str(cnt) +'.jpg',frame)
                cnt=cnt+1
                cv2.waitKey(1)

        else :
            print('비디오 읽기 오류')
            break

    cap.release()
    cv2.destroyAllWindows()
    return
    