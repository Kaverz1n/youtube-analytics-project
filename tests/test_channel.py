import pytest

from src.channel import Channel


@pytest.fixture
def make_channel():
    return Channel("AIzaSyDoZASHGsoIzkxWLAIIh79w6VB1g074nJE")


def test_class(make_channel):
    channel = make_channel
    assert isinstance(channel, object)


def test_init(make_channel):
    channel = make_channel
    assert channel.id == "AIzaSyDoZASHGsoIzkxWLAIIh79w6VB1g074nJE"
