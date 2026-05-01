import os
from PIL import Image, ImageOps

def optimize_images(root_dir, max_size=(1280, 1280), quality=80):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_path = os.path.join(subdir, file)
                webp_path = os.path.splitext(file_path)[0] + '.webp'
                
                # Force re-processing to fix rotation issues
                try:
                    with Image.open(file_path) as img:
                        # Fix orientation based on EXIF data
                        img = ImageOps.exif_transpose(img)
                        
                        # Convert to RGB if necessary
                        if img.mode in ('RGBA', 'P'):
                            img = img.convert('RGB')
                        
                        # Resize
                        img.thumbnail(max_size, Image.Resampling.LANCZOS)
                        
                        # Save as WebP
                        img.save(webp_path, 'WEBP', quality=quality)
                        print(f"Optimized: {file} -> {os.path.basename(webp_path)}")
                        
                except Exception as e:
                    print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resources_dir = os.path.join(base_dir, 'resources')
    optimize_images(resources_dir)
