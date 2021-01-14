#!/usr/bin/env python3

import os

import cv2
import mmcv
import numpy as np
import torch
import tqdm
from facenet_pytorch import MTCNN
from PIL import Image
from PIL import ImageDraw


def main(input_file):
    base_out = os.path.splitext(input_file)[0]
    output_file = f"{base_out}_faces.mp4"
    if os.path.exists(output_file):
        raise Exception(f"Exists: {output_file}")

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Running on device: {device}")

    mtcnn = MTCNN(keep_all=True, device=device)

    video = mmcv.VideoReader(input_file)

    frames_tracked = []
    for frame in tqdm.tqdm(video, position=0):
        frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # Detect faces
        boxes, _ = mtcnn.detect(frame)
        # Draw faces
        frame_draw = frame.copy()
        draw = ImageDraw.Draw(frame_draw)
        if boxes is not None:
            for box in boxes:
                draw.rectangle(box.tolist(), outline=(255, 0, 0), width=6)
        # Add to frame list
        frames_tracked.append(frame_draw)

    dim = frames_tracked[0].size
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_tracked = cv2.VideoWriter(output_file, fourcc, 30.0, dim)
    for frame in frames_tracked:
        video_tracked.write(cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR))
    video_tracked.release()


import sys

if len(sys.argv) < 2:
    print(f"Usage:\n    python {sys.argv[0]} video_file.mp4")
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1])
