'''
    Television testing module
'''

import pytest
from television import *

class Test:
    '''
        Test class
    '''

    def setup_method(self):
        '''
            Initializes television object
        '''
        self.tv = Television()

    def teardown_method(self):
        '''
            Removes television object
        '''
        del self.tv

    def test_init(self):
        '''
            Tests proper initalization
        '''
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        '''
            Tests power state
        '''
        self.tv.power() # turn self.tv on
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.power() # turn self.tv off
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        '''
            Tests mute state
        '''
        # power on, volume up 1, mute
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

        # on and unmuted (using values from previous steps)
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"

        # off and muted
        self.tv.power()
        self.tv.mute()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 1"

        # off and unmuted
        self.tv.mute()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up(self):
        '''
            Tests channel switching up
        '''
        # off and channel up
        self.tv.channel_up()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

        # on, channel up
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 1, Volume = 0"

        # on, channel up past max
        for _ in range(3):
            self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        '''
            Tests channel switching down
        '''
        # off and channel down
        self.tv.channel_down()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

        # on, past minimum
        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        '''
            Test volume up
        '''
        # off and volume up
        self.tv.volume_up()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

        # on, volume up
        self.tv.power()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"

        # on, muted, volume up
        self.tv.mute()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"

        # on, volume up past max
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        '''
            Tests volume down
        '''
        # off and volume down
        self.tv.volume_down()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

        # on, to max, decreased
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"

        # on, muted, volume down
        self.tv.volume_up()
        self.tv.mute()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"

        # on decrease past min
        self.tv.volume_down()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
