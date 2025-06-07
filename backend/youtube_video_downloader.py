import os
from yt_dlp import YoutubeDL

def download_video(url, output_dir=r'.\media'):
    
    if output_dir is None:
        output_dir = os.getcwd()
    options = {
        "paths": {"home": output_dir},
        "outtmpl": {"default": "%(title)s.%(ext)s"},
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
    }
    with YoutubeDL(params=options) as ydl:
        video_title = ydl.extract_info(url).get("title")
        return video_title