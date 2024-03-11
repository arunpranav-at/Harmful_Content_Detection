import cv2
import os,sys
import numpy as np
from datetime import datetime
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import glob
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MAINFOLDER.image_text_detection import image_text_detection as extract_text_from_image

def find_latest_video(video_folder):
    list_of_files = glob.glob(os.path.join(video_folder, '*'))  # Adjust pattern if needed for video files
    if not list_of_files:
        return None
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def create_session_folder(parent_dir, session_name=None):
    if not session_name:
        session_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_path = os.path.join(parent_dir, session_name)
    os.makedirs(session_path, exist_ok=True)
    return session_path

def video_to_frames(video_path, frames_dir):
    video_capture = cv2.VideoCapture(video_path)
    success, frame = video_capture.read()
    frame_count = 0
    saved_frame_count = 0
    save_next_frame = False
    
    while success:
        if save_next_frame:
            frame_file = os.path.join(frames_dir, f"frame_{saved_frame_count}.jpg")
            cv2.imwrite(frame_file, frame)
            saved_frame_count += 1
            save_next_frame = False
        else:
            if(frame_count%60==0):
                save_next_frame = True

        success, frame = video_capture.read()
        frame_count += 1

    video_capture.release()
    print(f"Total frames: {frame_count}, Saved frames: {saved_frame_count}")

# extracting text from each image parallely
def extract_text_from_images(images_dir):
    image_files = glob.glob(os.path.join(images_dir, "*.jpg"))
    # num_workers = min(multiprocessing.cpu_count(), 8)  # Adjust max workers if needed
    text_list = set()
    for image_file in image_files:
        text_list.add(extract_text_from_image(image_file))
    return "".join(list(text_list))
            

def main():
    video_folder = "D:\\gdg_wtm_hackathon\\github\\gdg-hackathon\\MAINFOLDER\\video"
    frames_base_dir = "D:\\gdg_wtm_hackathon\\github\\gdg-hackathon\\MAINFOLDER\\frames"

    video_path = find_latest_video(video_folder)
    if video_path:
        print(f"Processing latest video: {video_path}")
        session_name = datetime.now().strftime("%Y%m%d_%H%M%S")
        images_session_dir = create_session_folder(frames_base_dir, session_name)
        video_to_frames(video_path, images_session_dir)
        return extract_text_from_images(images_session_dir)
    else:
        print("No video files found in the specified directory.")

if __name__ == "__main__":
    main()
