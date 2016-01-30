# Created by Traburiss on 2016/1/27
import random

from people.judgment.jsb_judgment.standard_jsb_judgment import StandardJsbJudgment
from people.player.jsb_player.standard_jsb_player import StandardJsbPlayer


class SimpleJsbPlayer(StandardJsbPlayer):
    """
    classdocs
    """
    __sens__ = 1
    __like_level = [1, 1, 1]

    def __init__(self, play_id, name="no_name_jsb_player", like_level=None, sens=1):
        """
        Constructor
        """
        StandardJsbPlayer.__init__(self, name, play_id)
        self.set_sens(sens)
        self.set_like_level(like_level)

    def set_sens(self, sens=1):
        if sens <= 1:
            self.__sens__ = 1
        else:
            self.__sens__ = sens

    def set_like_level(self,  like_level=None):
        try:
            if not isinstance(like_level, list):
                like_level = [1, 1, 1]
            elif len(like_level) != 3:
                like_level = [1, 1, 1]
            else:
                for item in like_level:
                    if not isinstance(item, int):
                        like_level = [1, 1, 1]
                for position in range(len(like_level)):
                    if like_level[position] == 0:
                        like_level[position] = 1
        except BaseException as e:
            print(e)
            like_level = [1, 1, 1]
        self.__like_level = like_level

    def actions(self):
        jsb_code = random.randint(1, self.__like_level[0] + self.__like_level[1] + self.__like_level[2])
        if jsb_code <= self.__like_level[0]:
            jsb_code = 1
            jsb_name = "剪刀"
        elif jsb_code <= self.__like_level[0] + self.__like_level[1]:
            jsb_code = 2
            jsb_name = "石头"
        else:
            jsb_code = 3
            jsb_name = "布"
        self.set_action_result({self.PLAYER_NAME: self.get_name(),
                                self.GAME_TYPE: self.get_game_type(),
                                self.JSB_CODE: jsb_code,
                                self.JSB_NAME: jsb_name,
                                self.PLAYER_ID: self.get_play_id()})

    def game_tactics(self, other_action_results):
        j = StandardJsbJudgment("my_self")
        actions = [self.get_action_result()]
        if isinstance(other_action_results, dict):
            actions.append(other_action_results)
        elif isinstance(other_action_results, list):
            actions.extend(other_action_results)
        else:
            return
        j.ruling(actions)
        if j.get_result_code() == 2:
            for item in j.get_loser():
                if self.get_name() == item[self.PLAYER_NAME]:
                    switch_data = (self.__case_3, self.__case_1, self.__case_2)
                    switch_data[self.get_action_result()[self.JSB_CODE]-1]()
                    return
            for item in j.get_winner():
                if self.get_name() == item[self.PLAYER_NAME]:
                    switch_data = (self.__case_1, self.__case_2, self.__case_3)
                    switch_data[self.get_action_result()[self.JSB_CODE]-1]()
                    return

    def __case_1(self):
        self.__like_level[0] += self.__sens__

    def __case_2(self):
        self.__like_level[1] += self.__sens__

    def __case_3(self):
        self.__like_level[2] += self.__sens__
