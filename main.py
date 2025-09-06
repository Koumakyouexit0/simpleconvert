import yt_dlp
import os
import subprocess
import shutil

def download_mp3(url, output_path="."):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)   # tải video
        filename = ydl.prepare_filename(info)         # tên file gốc (.webm, .m4a,…)
        mp3_file = os.path.splitext(filename)[0] + ".mp3"

    # convert sang mono + 128kbps 
    if os.path.exists(mp3_file):
        temp_output = mp3_file.replace(".mp3", "_mono.mp3")
        subprocess.run([
            "ffmpeg", "-y", "-i", mp3_file,
            "-ac", "1", "-b:a", "128k",
            temp_output
        ])
        os.remove(mp3_file)
        os.rename(temp_output, mp3_file)
        print(f"✔ {os.path.basename(mp3_file)} đã convert sang mono 128kbps")

    return mp3_file

def convert_to_ogg(mp3_files, ogg_folder="downloads_ogg"):
    if not os.path.exists(ogg_folder):
        os.makedirs(ogg_folder)

    for mp3_file in mp3_files:
        if os.path.exists(mp3_file):
            output_path = os.path.join(
                ogg_folder, os.path.splitext(os.path.basename(mp3_file))[0] + ".ogg"
            )
            print(f"Đang convert {os.path.basename(mp3_file)} → {os.path.basename(output_path)}")
            subprocess.run([
                "ffmpeg", "-y", "-i", mp3_file,
                "-ac", "1", "-b:a", "128k",
                output_path
            ])

if __name__ == "__main__":
    input_file = "links.txt"
    output_folder = "downloads"
    ogg_folder = "downloads_ogg"

    with open(input_file, "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip()]

    print(f"Tìm thấy {len(links)} link trong {input_file}")
    downloaded_mp3 = []

    for link in links:
        try:
            print(f"Đang tải: {link}")
            mp3_file = download_mp3(link, output_folder)
            downloaded_mp3.append(mp3_file)
        except Exception as e:
            print(f"Lỗi với link {link}: {e}")

    choice = input("Bạn có muốn convert tất cả MP3 sang OGG không? (y/n): ").strip().lower()
    if choice == "y":
        convert_to_ogg(downloaded_mp3, ogg_folder)
        print(f"✅ Toàn bộ file OGG đã được lưu trong thư mục: {ogg_folder}")
    else:
        print("❌ Bỏ qua convert OGG.")

