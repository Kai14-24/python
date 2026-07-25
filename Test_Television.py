import pytest
from television import Television

class TestTelevision:
    def setup_method(self) -> None:
        """this deg set up the method for each test"""
        self.tv_1 = Television()

    def teardown_method(self) -> None:
        """this does a clea up before the test start"""
        del self.tv_1

    def test_init(self) -> None:
        """this tests the init method or the initiation of the tv"""
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self) -> None:
        """this tests the power function of the tv"""
        self.tv_1.power()
        assert self.tv_1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv_1.power()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self) -> None:
        """this tests the mute function of the tv"""
        self.tv_1.power()
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv_1.mute()
        assert self.tv_1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv_1.mute()
        assert self.tv_1.__str__() == "Power = True, Channel = 0, Volume = 1"

    def test_channel_up(self) -> None:
        """this tests the channel_up function of the tv"""
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv_1.power()
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == "Power = True, Channel = 2, Volume = 0"

    def test_channel_down(self) -> None:
        """this tests the channel_down function of the tv"""
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv_1.power()
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == "Power = True, Channel = 3, Volume = 0"
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == "Power = True, Channel = 2, Volume = 0"

    def test_volume_up(self) -> None:
        """this tests the volume_up function of the tv"""
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv_1.power()
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self) -> None:
        """this tests the volume_down function of the tv"""
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == "Power = True, Channel = 0, Volume = 2"
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == "Power = True, Channel = 0, Volume = 1"
