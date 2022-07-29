from typing import Optional
import requests
import moviepy
import webbrowser
import locale
from settings import PEXELS_API_KEY as API_KEY

# https://docs.python.org/3/library/enum.html
# from enum import Enum
# class VideoOrientation(str, Enum):
#     LANDSCAPE = "landscape"
#     PORTRAIT = "portrait"
#     SQUARE = "square"

def search_videos(
    query: str, # Ocean, Tigers, Pears, etc.
    orientation: Optional[str] = None, # landscape, portrait, or square
    size: Optional[str] = None, # large: 4K, medium: FHD, small: HD
    locale: Optional[str] = None, # 'en-US', 'pt-BR'
    page: Optional[int] = None, # default: 1
    per_page: Optional[int] = None, # default: 15 | max: 80
):
    # https://www.pexels.com/api/documentation/#videos-search
    response = requests.get(
        url="https://api.pexels.com/videos/search",
        headers={"Authorization": API_KEY},
        params={
            "query": query,
            "orientation": orientation,
            "size": size,
            "locale": locale,
            "page": page,
            "per_page": per_page,
        },
    )

    if response.status_code != 200:
        raise Exception("Error fetching videos")

    return response.json()



def fetch_video_content(download_url: str) -> bytes:
    # https://www.pexels.com/api/documentation/#videos-search
    response = requests.get(
        url=download_url,
        headers={"Authorization": API_KEY},
    )

    if response.status_code != 200:
        raise Exception("Error fetching videos")

    return response.content


if __name__ == "__main__":
    search_results = search_videos(
        query="Ocean",
        orientation="portrait",
        size="large",
        locale="en-US",
        page=1,
        per_page=15,
    )

    for video in search_results["videos"]:
        for video_file in video["video_files"]:
            print(video_file)
            video_content = fetch_video_content(video_file["link"])

            locale.setlocale(category=video_content , locale=None)
            get_video_file = open(video_content , encoding=utf_8.getdefaultlocale()[1])
            full_video_content = get_video_file.read()
