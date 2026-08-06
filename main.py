import argparse
import os

from modules.script_generator import generate_script
from modules.video_fetcher import download_video
from modules.video_editor import create_video
from modules.thumbnail_generator import create_thumbnail
from modules.metadata_generator import generate_metadata
from modules.voice_generator import generate_voice
from modules.uploader import upload_video

OUTPUT_DIR = "outputs"
ASSETS_DIR = "assets"


def ensure_directories():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(ASSETS_DIR, exist_ok=True)


def parse_args():
    parser = argparse.ArgumentParser(description="Build a short YouTube-style video automatically.")
    parser.add_argument("--topic", "-t", default="AI replacing jobs in 2030", help="Topic for the video, script, and metadata.")
    parser.add_argument("--query", "-q", default="AI robot future", help="Search query for a local background video.")
    parser.add_argument("--output", "-o", default="final_video", help="Base filename for outputs.")
    parser.add_argument("--language", "-l", default="en", help="Language code for text-to-speech.")
    parser.add_argument("--upload", action="store_true", help="Upload the finished video to YouTube after building it.")
    return parser.parse_args()


def save_metadata(title, description, tags, output_name):
    metadata_path = os.path.join(OUTPUT_DIR, f"{output_name}_metadata.txt")
    with open(metadata_path, "w", encoding="utf-8") as metadata_file:
        metadata_file.write(f"Title: {title}\n\n")
        metadata_file.write("Description:\n")
        metadata_file.write(f"{description}\n\n")
        metadata_file.write("Tags:\n")
        metadata_file.write(", ".join(tags))
    return metadata_path


def main():
    args = parse_args()
    ensure_directories()

    print("Generating script...")
    script = generate_script(args.topic)
    print("Script Generated ✅")
    print(script)

    print("Generating AI voice...")
    voice_path = generate_voice(script, language=args.language)
    print("Voice Generated ✅", voice_path)

    print("Finding background video...")
    video_path = download_video(args.query, args.output)
    print("Video source:", video_path)

    print("Creating final video...")
    final_video = create_video(video_path, script, args.output)
    print("Video Created ✅", final_video)

    print("Creating thumbnail...")
    thumbnail_path = create_thumbnail(args.topic, args.output)
    print("Thumbnail Created ✅", thumbnail_path)

    print("Generating metadata...")
    title, description, tags = generate_metadata(args.topic)
    metadata_path = save_metadata(title, description, tags, args.output)
    print("Metadata Generated ✅", metadata_path)

    if args.upload:
        print("Uploading to YouTube...")
        upload_video(final_video, title, description, tags)

    print("\n🎉 Automation complete! Check the outputs folder for the new files.")


if __name__ == '__main__':
    main()
