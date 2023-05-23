import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    API_KEY = os.getenv("YT_API_KEY")
    YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, id: str) -> None:
        self.__channel_id = id

        data = self.__get_data()
        self.title = data['items'][0]['snippet']['title']
        self.description = data['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = int(data['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(data['items'][0]['statistics']['videoCount'])
        self.view_count = int(data['items'][0]['statistics']['viewCount'])

    def __str__(self):
        '''
        Возвращает название канала и ссылку
        в удобном формате
        :return: описание канала с ссылкой
        '''
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        '''
        Складывает подписчиков двух каналов
        :return: результат сложения подписчиков
        '''
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        '''
        Вычитаем подписчиков двух каналов
        :return: результат вычитания подписчиков
        '''
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        '''
        Сравнивает подписчиков двух каналов
        :return: True, если у первого канала меньше
        подписчиков, в противном случае False
        '''
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        '''
        Сравнивает подписчиков двух каналов
        :return: True, если у первого канала меньше
        или такое же кол-во подписчиков,
        в противном случае False
        '''
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        '''
        Сравнивает подписчиков двух каналов
        :return: True, если у первого канала больше
        подписчиков, в противном случае False
        '''
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        '''
        Сравнивает подписчиков двух каналов
        :return: True, если у первого канала больше
        или такое же кол-во подписчиков,
        в противном случае False
        '''
        return self.subscriber_count >= other.subscriber_count

    def __eq__(self, other):
        '''
        Сравнивает подписчиков двух каналов
        :return: True, если у обоих каналов
        одинаковое кол-во подписчиков,
        иначе False
        '''
        return self.subscriber_count == other.subscriber_count

    def print_info(self) -> None:
        '''
        Выводит словарь с данными о канале
        '''
        channel = Channel.YOUTUBE.channels().list(
            id=self.__channel_id,
            part='snippet,statistics'
        ).execute()
        print(channel)

    def __get_data(self):
        '''
        Возвращает данные о канале в формате словаря
        :return: данные о канале
        '''
        channel = Channel.YOUTUBE.channels().list(
            id=self.__channel_id,
            part='snippet,statistics'
        ).execute()

        return channel

    def __get_attr_dict(self):
        '''
        Формирует словарь состоящий из атрибутом класса
        :return: словарь с атрибутами класса
        '''
        attr_dict = {}
        attr_dict['id'] = self.__channel_id
        attr_dict['title'] = self.title
        attr_dict['description'] = self.description
        attr_dict['url'] = self.url
        attr_dict['subscriber_count'] = self.subscriber_count
        attr_dict['video_count'] = self.video_count
        attr_dict['view_count'] = self.view_count

        return attr_dict

    def to_json(self, file_url):
        '''
        Записывает аттрибуты класса в формате JSON
        в указанный файл
        '''
        with open(file_url, 'w', encoding='UTF-8') as file:
            j_data = json.dumps(self.__get_attr_dict(), ensure_ascii=False)
            file.write(j_data)

    @classmethod
    def get_service(cls):
        '''
        Возвращает обьект для работы с
        YouTube API
        :return: обьект для работы с YT API
        '''
        return cls.YOUTUBE

    @property
    def channel_id(self):
        '''
        Возвращает id канала
        :return: id канала
        '''
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value):
        print("Ошибка")
