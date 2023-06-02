import pytest

from src.video import Video, PLVideo


@pytest.fixture
def make_video():
    return Video("g8tN2LDkpDo")


@pytest.fixture
def make_pl():
    return PLVideo('rLkg_9Muqhc', 'PLPmH-9rK0Yo3OLTC-7H19myF8BU39qRCZ')


def test_init(make_video):
    video = make_video
    assert video.video_id == "g8tN2LDkpDo"
    assert video.title == "🇺🇸GTA в реальной жизни. Лос-Анджелес"
    assert video.url == "https://youtu.be/g8tN2LDkpDo"


def test_str(make_video):
    video = make_video
    assert str(video) == "🇺🇸GTA в реальной жизни. Лос-Анджелес"


def test_repr(make_video):
    video = make_video
    assert repr(video) == "Video('g8tN2LDkpDo')"


def test_pl(make_pl):
    video_playlist = make_pl
    assert video_playlist.playlist_id == 'PLPmH-9rK0Yo3OLTC-7H19myF8BU39qRCZ'
    assert str(video_playlist) == 'ДЕПРЕССИЯ - Не игнорируй эти симптомы!'
