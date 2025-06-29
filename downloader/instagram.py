# downloader/instagram.py

import requests
import re

def download_instagram(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        video_url = re.search(r'"video_url":"([^"]+)"', response.text)
        if video_url:
            return {"title": "Instagram Video", "url": video_url.group(1).replace("\\u0026", "&")}
        else:
            return {"error": "ویدیو پیدا نشد."}
    except Exception as e:
        return {"error": str(e)}
