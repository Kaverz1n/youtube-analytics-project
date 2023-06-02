import datetime

import pytest

from src.playlist import PlayList


@pytest.fixture
def make_playlist():
    playlist = PlayList('PLPmH-9rK0Yo3OLTC-7H19myF8BU39qRCZ')
    return playlist


def test_init(make_playlist):
    playlist = make_playlist
    assert playlist.title == 'БИОХАКИНГ И ЗДОРОВЬЕ 🤪😵🤪'
    assert playlist.url == 'https://www.youtube.com/playlist?list=PLPmH-9rK0Yo3OLTC-7H19myF8BU39qRCZ'


def test_repr(make_playlist):
    playlist = make_playlist
    assert repr(playlist) == "PlayList('PLPmH-9rK0Yo3OLTC-7H19myF8BU39qRCZ')"


def test_str(make_playlist):
    playlist = make_playlist
    assert str(playlist) == playlist.url
    assert str(playlist) == 'https://www.youtube.com/playlist?list=PLPmH-9rK0Yo3OLTC-7H19myF8BU39qRCZ'


def test_total_duration(make_playlist):
    playlist = make_playlist
    assert str(playlist.total_duration) == '7:17:59'
    assert isinstance(playlist.total_duration, datetime.timedelta)


def test_show_best_video(make_playlist):
    playlist = make_playlist
    assert playlist.show_best_video() == 'https://youtu.be/o8K_gZoKiqQ'