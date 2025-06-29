# downloader/youtube.py

from yt_dlp import YoutubeDL

def download_youtube(url):
    try:
        ydl_opts = {
            "format": "best[ext=mp4]/best",
            "quiet": True
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title"),
                "url": info.get("url")
            }
    except Exception as e:
        return {"error": str(e)}
