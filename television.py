class Television():
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3


    def __init__(self) -> None:
        
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL
        self._prev = self._volume

    def power(self,):
        self._status = not(self._status)

    def mute(self):
        if self._status == True:
            self._muted = not(self._muted)
            if(self._muted == True):
                self._prev = self._volume
                self._volume = self.MIN_VOLUME
            if(self._muted == False):
                self._volume = self._prev

    def channel_up(self):
        if self._status == True:
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL ## cycles channel back to min channel
            else:
                self._channel += 1

    def channel_down(self):
        if self._status == True:
            if self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL ## cycles channel back to max channel
            else:
                self._channel -= 1

    def volume_up(self):
        if self._status == True:
            ## turns off mute
            if self._muted == True:
                self.mute()

            if self._volume == self.MAX_VOLUME:
                self._volume = self.MAX_VOLUME ## stays on max volume 
            else:
                self._volume += 1

    def volume_down(self):
        if self._status == True:
            ## turns off mute
            if self._muted == True:
                self.mute()

            if self._volume == self.MIN_VOLUME:
                self._volume = self.MIN_VOLUME #stays on min volume
            else:
                self._volume -= 1

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"