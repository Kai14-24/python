class Television:
    """"Here we have the base variable of how the tv starts"""
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialization the variable."""
        self.__status: bool = False
        self.__muted: bool  = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Method to turn on the tv."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Method to mute the tv channel."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Method to increase the tv channel."""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        """Method to decrease the tv channel."""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self) -> None:
        """Method to increase the volume."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Method to decrease the volume."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        volume_display = Television.MIN_VOLUME if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"
