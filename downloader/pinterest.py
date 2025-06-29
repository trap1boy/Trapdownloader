# downloader/pinterest.py

import requests
import re

def download_pinterest(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        matches = re.findall(r'"contentUrl":"(https://[^"]+)"', response.text)
        if matches:
            return {"title": "Pinterest Image/Video", "url": matches[0]}
        else:
            return {"error": "محتوا پیدا نشد."}
    except Exception as e:
        return {"error": str(e)}
