"""Batch extract faces from all .mp4/.mkv files in a folder.
"""
import os

import cv2
import face_recognition
import numpy as np
from PIL import Image


# Tune this this to memory.
BATCH_FRAMES = 10


def process_video(vid):
    print(f"Processing: {vid}")
    basename, _ = os.path.splitext(os.path.basename(vid))
    os.makedirs(f"{basename}_faces", exist_ok=True)
    if os.path.exists(f"{basename}.maga"):
        return
    video_capture = cv2.VideoCapture(vid)
    faces = 0
    frames = []
    while video_capture.isOpened():
        # Grab a single frame of video
        ret, frame_cv = video_capture.read()

        # Bail out when the video file ends
        if not ret:
            break

        frame = cv2.cvtColor(frame_cv, cv2.COLOR_BGR2RGB)
        frames.append(frame)
        print(".", end="", flush=""),
        # Tune this to GPU Memory Size.
        if len(frames) == BATCH_FRAMES:
            print("#", end="", flush="")
            batch_of_face_locations = face_recognition.batch_face_locations(
                frames, number_of_times_to_upsample=0
            )

            for idx, face_locations in enumerate(batch_of_face_locations):
                if len(face_locations) == 0:
                    continue
                face_encodings = face_recognition.face_encodings(
                    face_image=frames[idx], known_face_locations=face_locations
                )
                for face_encoding, face_location in zip(face_encodings, face_locations):
                    print("$", end="", flush=True)
                    top, right, bottom, left = face_location
                    # You can access the actual face itself like this:
                    face_image = frame[top:bottom, left:right]
                    pil_image = Image.fromarray(face_image)

                    pil_image.save(f"{basename}_faces/{basename}-{faces:08d}.jpg")

                    with open(f"{basename}_faces/{basename}-{faces:08d}.np", "wb") as b:
                        np.save(b, face_encoding, allow_pickle=False, fix_imports=False)

                    faces += 1
            print("", end="\n", flush=True)
            frames = []
    with open(f"{basename}.maga", "w") as F:
        F.write("MAGA!")


# Open video file
import glob

vids = glob.glob("*.mp4") + glob.glob("*.mkv")
for vid in vids:
    process_video(vid)
