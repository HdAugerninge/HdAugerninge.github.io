import os
import argparse
import sys

try:
    from moviepy.editor import VideoFileClip
except ImportError:
    print("Error: 'moviepy' is not installed.")
    print("Please install it using: pip install moviepy")
    sys.exit(1)

def convert_videos_to_gifs(directory, duration=10, delete_original=True, resize_width=480):
    """
    Finds all .mp4 files in the specified directory and converts them to .gif.
    """
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    mp4_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".mp4"):
                mp4_files.append(os.path.join(root, file))

    if not mp4_files:
        print(f"No .mp4 files found in '{directory}'.")
        return

    print(f"Found {len(mp4_files)} videos to process.")

    for mp4_path in mp4_files:
        gif_path = os.path.splitext(mp4_path)[0] + ".gif"
        
        print(f"\n--- Processing: {os.path.basename(mp4_path)} ---")
        try:
            with VideoFileClip(mp4_path) as clip:
                # Determine end time for subclip
                end_time = min(duration, clip.duration)
                
                # Extract subclip
                gif_clip = clip.subclip(0, end_time)
                
                # Resize to keep GIF file size reasonable
                if resize_width and clip.w > resize_width:
                    gif_clip = gif_clip.resize(width=resize_width)
                
                # Write GIF with optimized settings
                print(f"Writing GIF to: {gif_path}")
                gif_clip.write_gif(gif_path, fps=10, logger=None)
            
            print(f"Successfully created: {os.path.basename(gif_path)}")
            
            if delete_original:
                os.remove(mp4_path)
                print(f"Deleted original: {os.path.basename(mp4_path)}")
                
        except Exception as e:
            print(f"Error processing {mp4_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find all .mp4 files in a folder and replace them with a max 10s long GIF.")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to scan (default: current directory)")
    parser.add_argument("--keep", action="store_true", help="Keep original .mp4 files instead of deleting them")
    parser.add_argument("--duration", type=int, default=10, help="Max duration of the GIF in seconds (default: 10)")
    parser.add_argument("--width", type=int, default=480, help="Resize GIF to this width in pixels (default: 480)")
    
    args = parser.parse_args()
    
    # Warning for destructive action
    if not args.keep:
        print("!!! WARNING: This script will DELETE original .mp4 files after conversion !!!")
        confirm = input("Are you sure you want to proceed? (y/n): ")
        if confirm.lower() != 'y':
            print("Aborted.")
            sys.exit(0)

    convert_videos_to_gifs(
        args.directory, 
        duration=args.duration, 
        delete_original=not args.keep,
        resize_width=args.width
    )
