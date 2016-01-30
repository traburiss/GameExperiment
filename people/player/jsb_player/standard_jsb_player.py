# Created by Traburiss on 2016/1/27
import random

from people.player.base_player import BasePlayer


class StandardJsbPlayer(BasePlayer):
    """
    classdocs
    """
    PLAYER_NAME = "PlayerName"
    GAME_TYPE = "GameType"
    JSB_CODE = "JSBCode"
    JSB_NAME = "JSBName"
    PLAYER_ID = "PlayerID"

    __GAME_TYPE_NAME = "jsb"

    def __init__(self, name, play_id):
        """
        Constructor
        """
        BasePlayer.__init__(self, name, self.__GAME_TYPE_NAME, play_id)
        self.__action_result = {self.PLAYER_NAME: "no_name",
                                self.GAME_TYPE: self.__GAME_TYPE_NAME,
                                self.JSB_CODE: 0,
                                self.JSB_NAME: "未出招",
                                self.PLAYER_ID: play_id}

    def actions(self):
        jsb_code = random.randint(1, 3)
        if jsb_code == 1:
            jsb_name = "剪刀"
        elif jsb_code == 2:
            jsb_name = "石头"
        else:
            jsb_name = "布"
        self.__action_result = {self.PLAYER_NAME: self.get_name(),
                                self.GAME_TYPE: self.get_game_type(),
                                self.JSB_CODE: jsb_code,
                                self.JSB_NAME: jsb_name,
                                self.PLAYER_ID: self.get_play_id()}

    def get_action_result(self):
        return self.__action_result

    def set_action_result(self, action_result):
            self.__action_result = action_result
