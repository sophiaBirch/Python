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
        self._status:bool = False
        self._muted:bool = False
        self._volume:int = self.MIN_VOLUME
        self._channel:int = self.MIN_CHANNEL
        self._prev:int = self._volume ## a temp variable that stores the previous volume while the TV is muted

    def power(self) -> None:
        '''
            Turns power on/off
        '''
        self._status:bool = not(self._status)

    def mute(self) -> None:
        '''
            Mutes/unmutes and stores the previous volume
        '''
        if self._status == True:
            self._muted:bool = not(self._muted)
            if(self._muted == True):
                self._prev:int = self._volume
                self._volume:int = self.MIN_VOLUME
            if(self._muted == False):
                self._volume:int = self._prev

    def channel_up(self) -> None:
        '''
            Increases channel. If channel passes max channel num, cycles back to minimum channel. 
        '''
        if self._status == True:
            if self._channel == self.MAX_CHANNEL:
                self._channel:int = self.MIN_CHANNEL ## cycles channel back to min channel
            else:
                self._channel += 1

    def channel_down(self) -> None:
        '''
            Decreases channel. If channel passes min channel num, cycles back to max channel. 
        '''
        if self._status == True:
            if self._channel == self.MIN_CHANNEL:
                self._channel:int = self.MAX_CHANNEL ## cycles channel back to max channel
            else:
                self._channel -= 1

    def volume_up(self) -> None:
        '''
            Increases volume. If volume exceeds max, stays at max volume
        '''
        if self._status == True:
            ## turns off mute
            if self._muted == True:
                self.mute()

            if self._volume == self.MAX_VOLUME:
                self._volume:int = self.MAX_VOLUME ## stays on max volume 
            else:
                self._volume += 1

    def volume_down(self) -> None:
        '''
            Decreases volume. If volume exceeds min, stays at min volume
        '''
        if self._status == True:
            ## turns off mute
            if self._muted == True:
                self.mute()

            if self._volume == self.MIN_VOLUME:
                self._volume:int = self.MIN_VOLUME #stays on min volume
            else:
                self._volume -= 1

    def __str__(self) -> str:
        '''
            Returns: a string with the status of tv elements:
                Power (boolean)
                Channel (int)
                Volume (int)
            
        '''
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"