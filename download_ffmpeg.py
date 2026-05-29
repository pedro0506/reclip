import urllib.request
import zipfile
import io
import os

url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
dest_dir = r"d:\Trabalho\psdev\SAAS\ReClip"

print(f"Downloading FFmpeg from {url}...")
try:
    with urllib.request.urlopen(url) as response:
        zip_data = response.read()
    print("Download completed. Extracting ffmpeg.exe and ffprobe.exe...")
    with zipfile.ZipFile(io.BytesIO(zip_data)) as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename.endswith("ffmpeg.exe") or file_info.filename.endswith("ffprobe.exe"):
                # Extract file and save to dest_dir
                filename = os.path.basename(file_info.filename)
                target_path = os.path.join(dest_dir, filename)
                with zip_ref.open(file_info) as source_file, open(target_path, "wb") as target_file:
                    target_file.write(source_file.read())
                print(f"Extracted {filename} to {target_path}")
    print("Done!")
except Exception as e:
    print(f"Error occurred: {e}")

