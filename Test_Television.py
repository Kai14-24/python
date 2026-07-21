import pytest
from television import Television

class test:
    def setup_method(self):
        self.tv_1 = Television()

    def teardown_method(self):
        del self.tv_1

    def test_init(self):
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv_1.power()
        assert self.tv_1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv_1.power()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        pass

    def test_channel_up(self):
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tv_1.channel_up()
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == "Power = True, Channel = 2, Volume = 0"

    def test_channel_down(self):
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == "Power = true, Channel = 3, Volume = 0"
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == "Power = true, Channel = 2, Volume = 0"

    def test_volume_up(self):
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == "Power = true, Channel = 2, Volume = 1"
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == "Power = true, Channel = 2, Volume = 2"

    def test_volume_down(self):
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == "Power = true, Channel = 1, Volume = 2"
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == "Power = true, Channel = 1, Volume = 1"