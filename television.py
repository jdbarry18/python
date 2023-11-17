class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes a Television object with default values.
        """
        self.status: bool = False
        self.muted: bool = False
        self.volume: int = Television.MIN_VOLUME
        self.channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the television.
        """
        self.status = not self.status

    def mute(self) -> None:
        """
        Toggles the mute status of the television. If the TV is muted, it sets the volume to the minimum.
        """
        if self.status:
            self.muted = not self.muted
            if self.muted:
                self.volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Increases the channel of the television. If the TV is on the maximum channel, it wraps around to the minimum channel.
        """
        if self.status:
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel of the television. If the TV is on the minimum channel, it wraps around to the maximum channel.
        """
        if self.status:
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
            else:
                self.channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume of the television. If the TV is on the maximum volume, it remains at the maximum.
        """
        if self.status and not self.muted:
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume of the television. If the TV is on the minimum volume, it remains at the minimum.
        """
        if self.status and not self.muted:
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the television object.
        """
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'