import cv2 as cv
import os
from typing import List
import numpy as np

PATH_TO_VIDEO = 'Dataset/video/'
PATH_TO_SAVE_IMAGE = 'Dataset/images/'


def get_video_data(path: str = PATH_TO_VIDEO) -> List:
    """Get list video file name
    Args:
        path (str): path to video data

    Returns:
        List: pathes from video-data
    """
    data = os.listdir(path = path)
    return data

def resize_image(image: np.ndarray, size = (640, 640)) -> np.ndarray:
    """Resize image

    Args:
        image (np.ndarray): image
        size (tuple, optional): size. Defaults to (640, 640).

    Returns:
        np.ndarray: resize image
    """
    if image is not None:
        return cv.resize(image, size)
    else:
        print(f'Currnet image is None!')

def save_image(image: np.ndarray, fileName:str, count: int, path: str = PATH_TO_SAVE_IMAGE) -> None:
    """Save image

    Args:
        image (np.ndarray): image from video
        fileName (str): filename
        count (int): counts images
        path (str, optional): path to save image. Defaults to PATH_TO_SAVE_IMAGE.

    Returns:
        _type_: None
    """
    if image is not None:
        fileName += '.' + str(count) + '.jpg'
        cv.imwrite(filename = path + fileName, img= image)
        print(f"Image : {path + fileName} saved!")
    else:
        print(f"Error save image!")
        return None
        
        


def cutting_video(path: str, skip_step: int = 0, resize: bool = False) -> None:
    """Get frame from video and save cutting frame

    Args:
        path (str): path to video file
        skip_step (int): skip count frame
        resize (bool): key from resize image
    """
    path = PATH_TO_VIDEO + path
    cap = cv.VideoCapture(path)
    step = 0
    count = 0
    if (cap.isOpened()== False):
        print("Error opening video file!")
        return
    
    while(cap.isOpened):
        ret, frame = cap.read()
        
        if ret == True and step == skip_step:
            step = 0
            if resize:
                frame = resize_image(frame)
                
            save_image(frame, fileName= "street1", count = count)
            count+=1
        else:
            step += 1
            
        if ret == False:
            break

    print('All data is completed!')

            
paths_from_video = get_video_data()
cutting_video(path = paths_from_video[1], skip_step = 15, resize= False)