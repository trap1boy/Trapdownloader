# downloader/tiktok.py

import requests
import re

def download_tiktok(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        video_url = re.search(r'"downloadAddr":"([^"]+)"', response.text)
        if video_url:
            return {"title": "TikTok Video", "url": video_url.group(1).replace("\\u0026", "&")}
        else:
            return {"error": "ویدیو پیدا نشد."}
    except Exception as e:
        return {"error": str(e)}
