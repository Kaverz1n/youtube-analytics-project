import pytest

from src.channel import Channel


@pytest.fixture
def make_channel():
    return Channel("UCjay7c-KSW2nC8Grq_q8tHg")


def test_class(make_channel):
    channel = make_channel
    assert isinstance(channel, object)


def test_init(make_channel):
    channel = make_channel
    assert channel.channel_id == "UCjay7c-KSW2nC8Grq_q8tHg"

def test_channel_id(make_channel, capsys):
    channel = make_channel
    channel.channel_id = "dFdfdfsdfgdf"
    output = capsys.readouterr()
    assert output.out == "Ошибка\n"