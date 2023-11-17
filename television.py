class Television():
    '''
        Controls a TV remote
    '''
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3


    def __init__(self) -> None:
        '''
            Initializes class with default values:
                status = false
                muted = false
                volume = 0
                channel = 0
        '''
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL
        self._prev = self._volume ## a temp variable that stores the previous volume while the TV is muted

    def power(self):
        '''
            Turns power on/off
        '''
        self._status = not(self._status)

    def mute(self):
        '''
            Mutes/unmutes and stores the previous volume
        '''
        if self._status == True:
            self._muted = not(self._muted)
            if(self._muted == True):
                self._prev = self._volume
                self._volume = self.MIN_VOLUME
            if(self._muted == False):
                self._volume = self._prev

    def channel_up(self):
        '''
            Increases channel. If channel passes max channel num, cycles back to minimum channel. 
        '''
        if self._status == True:
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL ## cycles channel back to min channel
            else:
                self._channel += 1

    def channel_down(self):
        '''
            Decreases channel. If channel passes min channel num, cycles back to max channel. 
        '''
        if self._status == True:
            if self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL ## cycles channel back to max channel
            else:
                self._channel -= 1

    def volume_up(self):
        '''
            Increases volume. If volume exceeds max, stays at max volume
        '''
        if self._status == True:
            ## turns off mute
            if self._muted == True:
                self.mute()

            if self._volume == self.MAX_VOLUME:
                self._volume = self.MAX_VOLUME ## stays on max volume 
            else:
                self._volume += 1

    def volume_down(self):
        '''
            Decreases volume. If volume exceeds min, stays at min volume
        '''
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