import pytest
from television import *

# Fixture for creating a new Television instance for each test
@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power(tv):
    tv.power() # turn tv on
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power() # turn tv off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute(tv):
    # power on, volume up 1, mute
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # on and unmuted (using values from previous steps)
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # off and muted
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

    # off and unmuted
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

def test_channel_up(tv):
    # off and channel up
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # on, channel up
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    # on, channel up past max
    for _ in range(3):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down(tv):
    # off and channel down
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # on, past minimum
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up(tv):
    # off and volume up
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # on, volume up
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # on, muted, volume up
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # on, volume up past max
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down(tv):
    # off and volume down
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # on, to max, decreased
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # on, muted, volume down
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # on decrease past min
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
