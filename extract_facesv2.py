#!/usr/bin/env python3

import os

import cv2
import numpy as np
import tqdm
import torch
from facenet_pytorch import MTCNN
import mmcv
from PIL import Image
from PIL import ImageDraw


def main(input_file):
    basename = os.path.splitext(input_file)[0]
    if os.path.exists(f"{basename}.maga"):
        return
    output_folder = f"{basename}_faces"
    os.makedirs(output_folder, exist_ok=True)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Running on device: {device}")

    mtcnn = MTCNN(keep_all=True, device=device)

    video = mmcv.VideoReader(input_file)

    frames_tracked = []
    face_count = 0
    for frame in tqdm.tqdm(video, position=0):
        frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # Detect faces
        boxes, _ = mtcnn.detect(frame)
        # Draw faces
        frame_draw = frame.copy()
        draw = ImageDraw.Draw(frame_draw)
        if boxes is not None:
            for box in tqdm.tqdm(boxes, position=1):
                pt1 = box.tolist()[:2]
                pt2 = box.tolist()[2:4]
                face = frame.crop(pt1+ pt2)
                output_path = os.path.join(output_folder, f"{basename}-{face_count:08d}.jpg")
                face.save(output_path)
                face_count+=1
    with open(f"{basename}.maga", "w") as f:
        f.write("MAGA!")
import sys

if len(sys.argv) < 2:
    print(f"Usage:\n    python {sys.argv[0]} video_file.mp4")
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1])
