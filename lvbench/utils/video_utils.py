from typing import Union
import cv2
from moviepy.editor import VideoFileClip
from pathlib import Path

def get_video_info(video_path: Union[str,Path]):
    if isinstance(video_path, str):
        video_path = Path(video_path)
    assert video_path.exists(), f"Video file {video_path} does not exist."

    # 使用 cv2 获取 FPS 和分辨率
    cap = cv2.VideoCapture(str(video_path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()

    # 使用 moviepy 获取视频时长
    video = VideoFileClip(str(video_path))
    duration = video.duration  # 时长以秒为单位
    duration_in_minutes = duration / 60  # 转换为分钟
    video.close()

    return {
        "duration_minutes": duration_in_minutes,
        "fps": fps,
        "resolution": {
            "width": width,
            "height": height
        }
    }
