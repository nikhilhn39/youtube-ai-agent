import os
import numpy as np
from moviepy.editor import (
    VideoFileClip,
    CompositeVideoClip,
    AudioFileClip,
    ImageClip,
    CompositeAudioClip
)
from PIL import Image, ImageDraw, ImageFont


# --------- CREATE TEXT IMAGE ----------
def create_text_image(text, width=1080, height=1920):
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 70)
    except:
        font = ImageFont.load_default()

    lines = []
    words = text.split()
    line = ""

    for word in words:
        test_line = line + word + " "
        w, h = draw.textsize(test_line, font=font)
        if w < width - 150:
            line = test_line
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    y_text = height // 2
    for line in lines:
        w, h = draw.textsize(line, font=font)
        draw.text(
            ((width - w) / 2, y_text),
            line,
            font=font,
            fill="white"
        )
        y_text += h + 15

    return np.array(img)


# --------- MAIN VIDEO FUNCTION ----------
def create_video(video_path, script_text, output_name):

    print("Loading video...")
    video = VideoFileClip(video_path).resize((1080, 1920))

    if not os.path.exists("assets/voice.mp3"):
        raise FileNotFoundError("Voice file not found.")

    print("Loading AI voice...")
    voice = AudioFileClip("assets/voice.mp3")

    duration = voice.duration
    video = video.subclip(0, min(video.duration, duration))
    video = video.set_duration(duration)

    # 🔥 Split script into sentences
    sentences = [s.strip() for s in script_text.split(".") if s.strip()]
    sentence_duration = duration / len(sentences)

    subtitle_clips = []
    start_time = 0

    for sentence in sentences:
        text_img = create_text_image(sentence)
        txt_clip = (
            ImageClip(text_img)
            .set_start(start_time)
            .set_duration(sentence_duration)
        )
        subtitle_clips.append(txt_clip)
        start_time += sentence_duration

    final = CompositeVideoClip([video] + subtitle_clips)

    # 🎵 Background Music (Optional)
    if os.path.exists("assets/background_music.mp3"):
        bg = AudioFileClip("assets/background_music.mp3").volumex(0.2)
        bg = bg.set_duration(duration)
        final_audio = CompositeAudioClip([voice, bg])
    else:
        final_audio = voice

    final = final.set_audio(final_audio)

    print("Rendering final video...")
    final.write_videofile(
        f"outputs/{output_name}.mp4",
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )

    return f"outputs/{output_name}.mp4"