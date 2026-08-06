import os

def download_video(query, output_name):
    # Use local video instead of API
    video_path = "assets/background.mp4"
    
    if not os.path.exists(video_path):
        raise FileNotFoundError("No background video found in assets folder.")
    
    print("Using local background video.")
    return video_path