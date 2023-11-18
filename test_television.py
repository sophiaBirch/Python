import unittest
from television import *

class TestTelevision(unittest.TestCase):

    tv1 = Television()
    tv2 = Television()
    tv3 = Television()
    tv4 = Television()
    tv5 = Television()
    tv6 = Television()
    
    def test_init(self):
        self.assertEqual(str(self.tv1), "Power = False, Channel = 0, Volume = 0")

    def test_power(self):
        self.tv1.power() ## turn tv on
        self.assertEqual(str(self.tv1), "Power = True, Channel = 0, Volume = 0")
        self.tv1.power() ## turn tv off
        self.assertEqual(str(self.tv1), "Power = False, Channel = 0, Volume = 0")
    
    def test_mute(self):

        ## power on, volume up 1, mute
        self.tv2.power()
        self.tv2.volume_up()
        self.tv2.mute()
        self.assertEqual(str(self.tv2), "Power = True, Channel = 0, Volume = 0")

        ## on and unmuted (using values from previous steps)
        self.tv2.mute()
        self.assertEqual(str(self.tv2), "Power = True, Channel = 0, Volume = 1")

        ## off and muted
        self.tv2.power()
        self.tv2.mute()
        self.assertEqual(str(self.tv2), "Power = False, Channel = 0, Volume = 1")

        ## off and unmuted
        self.tv2.mute()
        self.assertEqual(str(self.tv2), "Power = False, Channel = 0, Volume = 1")

    def test_channel_up(self):
        ## off and channel up
        self.tv3.channel_up()
        self.assertEqual(str(self.tv3), "Power = False, Channel = 0, Volume = 0")

        ## on, channel up
        self.tv3.power()
        self.tv3.channel_up()
        self.assertEqual(str(self.tv3), "Power = True, Channel = 1, Volume = 0")

        ## on, channel up past max
        self.tv3.channel_up()
        self.tv3.channel_up()
        self.tv3.channel_up()
        self.assertEqual(str(self.tv3), "Power = True, Channel = 0, Volume = 0")
    
    def test_channel_down(self):
        ## off and channel down
        self.tv4.channel_down()
        self.assertEqual(str(self.tv4), "Power = False, Channel = 0, Volume = 0")

        ## on, past minimum
        self.tv4.power()
        self.tv4.channel_down()
        self.assertEqual(str(self.tv4), "Power = True, Channel = 3, Volume = 0")

    def test_volume_up(self):
        ## off and volume up
        self.tv5.volume_up()
        self.assertEqual(str(self.tv5), "Power = False, Channel = 0, Volume = 0")

        ## on, volume up
        self.tv5.power()
        self.tv5.volume_up()
        self.assertEqual(str(self.tv5), "Power = True, Channel = 0, Volume = 1")

        ## on, muted, volume up
        self.tv5.mute()
        self.tv5.volume_up()
        self.assertEqual(str(self.tv5), "Power = True, Channel = 0, Volume = 2")

        ## on, volume up past max
        self.tv5.volume_up()
        self.assertEqual(str(self.tv5), "Power = True, Channel = 0, Volume = 2")
    
    def test_volume_down(self):
        ## off and volume down
        self.tv6.volume_down()
        self.assertEqual(str(self.tv6), "Power = False, Channel = 0, Volume = 0")

        ## on, to max, decreased
        self.tv6.power()
        self.tv6.volume_up()
        self.tv6.volume_up()
        self.tv6.volume_down()
        self.assertEqual(str(self.tv6), "Power = True, Channel = 0, Volume = 1")

        # on, muted, volume down
        self.tv6.volume_up()
        self.tv6.mute()
        self.tv6.volume_down()
        self.assertEqual(str(self.tv6), "Power = True, Channel = 0, Volume = 1")

        ## on decrease past min
        self.tv6.volume_down()
        self.tv6.volume_down()
        self.assertEqual(str(self.tv6), "Power = True, Channel = 0, Volume = 0")

if __name__ == "__main__":
    unittest.main()