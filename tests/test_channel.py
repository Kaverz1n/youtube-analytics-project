import pytest

from src.channel import Channel


@pytest.fixture
def make_channel():
    return Channel("UCjay7c-KSW2nC8Grq_q8tHg")

@pytest.fixture
def make_two_channel():
    return (
        Channel('UC-OVMPlMA3-YCIeg4z5z23A'),
        Channel("UCjay7c-KSW2nC8Grq_q8tHg")
    )
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

def test_src(make_two_channel):
    chn_1, chn_2 = make_two_channel
    assert str(chn_1) == "MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)"
    assert str(chn_2) == "Scammers (https://www.youtube.com/channel/UCjay7c-KSW2nC8Grq_q8tHg)"

def test_add(make_two_channel):
    chn_1, chn_2 = make_two_channel
    assert chn_1 + chn_2 == 1_416_000

def test_sub(make_two_channel):
    chn_1, chn_2 = make_two_channel
    assert chn_2 - chn_1 == 1_364_000


def test_lt(make_two_channel):
    chn_1, chn_2 = make_two_channel
    assert (chn_1 < chn_2) == True
    assert (chn_2 < chn_1) == False

def test_le(make_two_channel):
    chn_1, chn_2 = make_two_channel
    assert (chn_1 <= chn_2) == True
    assert (chn_2 <= chn_1) == False


def test_gt(make_two_channel):
    chn_1, chn_2 = make_two_channel
    assert (chn_1 > chn_2) == False
    assert (chn_2 > chn_1) == True

def test_ge(make_two_channel):
    chn_1, chn_2 = make_two_channel
    assert (chn_1 >= chn_2) == False
    assert (chn_2 >= chn_1) == True

def test_eq(make_two_channel):
    chn_1, chn_2 = make_two_channel
    assert (chn_1 == chn_2) == False