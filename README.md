# YouTube MP3/OGG Downloader

Công cụ Python để tải nhạc từ YouTube thành **MP3 128kbps mono** và tùy
chọn chuyển đổi sang **OGG**.

## Yêu cầu

-   Python 3.7+
-   [yt-dlp](https://github.com/yt-dlp/yt-dlp)
-   [FFmpeg](https://ffmpeg.org/) (bắt buộc để convert âm thanh)

Cài đặt các thư viện cần thiết:

``` bash
pip install yt-dlp
```

Cài đặt FFmpeg (Linux/macOS):

``` bash
sudo apt install ffmpeg
```

Windows: tải [FFmpeg bản build sẵn](https://ffmpeg.org/download.html) và
thêm vào **PATH**.
Nếu bạn ko biết tải: [Hướng dẫn ở đây](https://www.youtube.com/watch?v=JR36oH35Fgg)

------------------------------------------------------------------------

## Cách sử dụng

1.  Tạo file `links.txt` chứa danh sách link YouTube cần tải, mỗi link
    một dòng.\
    Ví dụ:

        https://www.youtube.com/watch?v=dQw4w9WgXcQ
        https://www.youtube.com/watch?v=Rpyj6T7QBOQ

2.  Chạy script:

    ``` bash
    python main.py
    ```

3.  Tool sẽ:

    -   Tải từng link về dưới dạng **MP3 128kbps mono** trong thư mục
        `downloads/`.
    -   Hỏi bạn có muốn chuyển tất cả sang **OGG** không.
        -   Nếu chọn `y`, file OGG sẽ được lưu vào thư mục
            `downloads_ogg/`.
        -   Nếu chọn `n`, bỏ qua bước convert.

------------------------------------------------------------------------

## Cấu trúc thư mục

    project/
    │── main.py
    │── links.txt
    │── downloads/        # Lưu file MP3
    │── downloads_ogg/    # Lưu file OGG (nếu convert)

------------------------------------------------------------------------

## Lưu ý

-   Một số video có thể bị lỗi do chặn tải xuống hoặc vấn đề bản quyền.
-   Nếu bị lỗi `FFmpegAudioConvertorPP`, hãy chắc chắn rằng **FFmpeg**
    đã được cài đặt và nhận diện trong PATH.

------------------------------------------------------------------------

✅ Giờ bạn chỉ cần chuẩn bị `links.txt` rồi chạy `main.py` là xong!
