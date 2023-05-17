import os

from googleapiclient.discovery import build

API_KEY = os.getenv("YT_API_KEY")
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, id: str) -> None:
        self.id = id

    def print_info(self) -> None:
        channel = YOUTUBE.channels().list(
            id=self.id,
            part='snippet,statistics'
        ).execute()
        print(channel)
