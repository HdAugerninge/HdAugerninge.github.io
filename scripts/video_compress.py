import os
import argparse
import sys

try:
    import imageio_ffmpeg as ffmpeg_pkg
except ImportError:
    print("Error: 'imageio-ffmpeg' is not installed.")
    print("Please install it using: pip install imageio-ffmpeg")
    sys.exit(1)
import subprocess
import tempfile
import shutil

def optimize_videos(directory, duration=15, resize_width=480, crf=28):
    """
    Finds all .mp4 files in the specified directory and optimizes them for web use.
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
        # Check if already optimized (we'll skip files with '_optimized' if we used that, 
        # but here we overwrite, so we just process everything)
        
        try:
            ffmpeg_exe = ffmpeg_pkg.get_ffmpeg_exe()
            
            # Create a temporary file for the optimized version
            fd, temp_path = tempfile.mkstemp(suffix=".mp4")
            os.close(fd)
            
            print(f"\n--- Optimizing: {os.path.basename(mp4_path)} ---")
            
            # FFmpeg command for web-optimized MP4:
            # -an: Remove audio
            # -c:v libx264: H.264 codec
            # -crf: Compression level (23 default, 28 is high compression)
            # -preset slow: Better compression efficiency
            # -movflags +faststart: Optimized for web playback
            cmd = [
                ffmpeg_exe,
                "-y",
                "-ss", "0",
                "-t", str(duration),
                "-i", mp4_path,
                "-vf", f"scale={resize_width}:trunc(ow/a/2)*2",
                "-an",
                "-c:v", "libx264",
                "-crf", str(crf),
                "-preset", "slow",
                "-movflags", "+faststart",
                "-pix_fmt", "yuv420p", # Maximum compatibility
                temp_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise Exception(f"FFmpeg error: {result.stderr}")
            
            # Replace original with optimized version
            shutil.move(temp_path, mp4_path)
            print(f"Successfully optimized: {os.path.basename(mp4_path)}")
            print(f"New size: {os.path.getsize(mp4_path) / 1024:.1f} KB")
                
        except Exception as e:
            print(f"Error processing {mp4_path}: {e}")
            if 'temp_path' in locals() and os.path.exists(temp_path):
                os.remove(temp_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize .mp4 files for web (remove audio, compress, resize).")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to scan (default: current directory)")
    parser.add_argument("--duration", type=int, default=15, help="Max duration in seconds (default: 15)")
    parser.add_argument("--width", type=int, default=480, help="Resize to this width (default: 480)")
    parser.add_argument("--crf", type=int, default=28, help="Compression level 0-51. Higher = smaller file (default: 28)")
    parser.add_argument("-y", "--yes", action="store_true", help="Skip confirmation prompt")
    
    args = parser.parse_args()
    
    if not args.yes:
        print("!!! WARNING: This script will OVERWRITE original .mp4 files with optimized versions !!!")
        confirm = input("Are you sure you want to proceed? (y/n): ")
        if confirm.lower() != 'y':
            print("Aborted.")
            sys.exit(0)

    optimize_videos(
        args.directory, 
        duration=args.duration, 
        resize_width=args.width,
        crf=args.crf
    )
