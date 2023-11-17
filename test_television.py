import pytest
from television import Television

def test_television_init():
    tv = Television()
    assert not tv.status
    assert not tv.muted
    assert tv.volume == Television.MIN_VOLUME
    assert tv.channel == Television.MIN_CHANNEL

def test_television_power():
    tv = Television()
    tv.power()
    assert tv.status
    tv.power()
    assert not tv.status

def test_television_mute():
    tv = Television()
    tv.mute()
    assert not tv.muted
    tv.power()
    tv.mute()
    assert tv.muted

def test_television_channel_up():
    tv = Television()
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL + 1
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL + 2
    tv.channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL

def test_television_channel_down():
    tv = Television()
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL
    tv.channel = Television.MIN_CHANNEL + 1
    tv.channel_down()
    assert tv.channel == Television.MIN_CHANNEL
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL

def test_television_volume_up():
    tv = Television()
    tv.volume_up()
    assert tv.volume == Television.MIN_VOLUME + 1
    tv.volume_up()
    assert tv.volume == Television.MIN_VOLUME + 2
    tv.volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv.volume == Television.MAX_VOLUME

def test_television_volume_down():
    tv = Television()
    tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME
    tv.volume = Television.MIN_VOLUME + 1
    tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME
    tv.volume = Television.MAX_VOLUME
    tv.volume_down()
    assert tv.volume == Television.MAX_VOLUME - 1

if __name__ == '__main__':
    pytest.main()