# Created by Traburiss on 2016/3/14
import string
from random import Random

import sqlite3

from Tools.my_dj_memory import MyDjMemory
from people.player.base_player import BasePlayer
from people.player.dj_player.memory.dj_player_memory import DjPlayerMemory


class MyDjPlayer(BasePlayer):
    __DB_NAME = "DJ.DB"

    def __init__(self, deep=10):
        super().__init__()
        self.memory = DjPlayerMemory()
        self.next_step = -1
        self.deep = deep

    def actions(self, face_state):
        self.get_batter_step(face_state, self.deep)
        pass

    # 获得数据库中的历史数据，匹配局面与落点，根据落点的胜负比得到最佳的落点，当无数据时，随机落子，施工中
    def get_game_history(self, face_state):
        result_step = -1
        win_times = 0
        lose_times = 0
        my_long_memory = MyDjMemory()
        my_memory_result = my_long_memory.search_by_face_state(face_state)
        if len(my_memory_result) == 0:
            result_step = self.random_step(face_state)
        else:
            for item in my_memory_result:
                if self.win_percent_compare(win_times, lose_times, item[3], item[4]) and self.win_percent(item[3], item[4]) > 0.1:
                    result_step = item[2]
                    win_times = item[3]
                    lose_times = item[4]
                else:
                    result_step = self.random_step(face_state)

        return result_step, win_times, lose_times

    # 调用数据库历史数据返回结果，根据deep参数迭代推算下一步，再去获取下一步的数据库局面结果，得到最优结果，施工中，
    def get_batter_step(self, face_state, deep):
        result_step = -1
        return result_step

    # 根据局面随机下一步
    @staticmethod
    def random_step(face_state):
        length = 0
        position = []
        for item in face_state:
            if item == "0":
                position.append(length)
            length += 1
        random = Random()
        c = random.randint(0, len(position)-1)
        return position[c]

    @staticmethod
    def win_percent(win_times, lose_times):
        if win_times == 0:
            return 0
        elif lose_times == 0:
            return 1
        else:
            return win_times/lose_times

    def win_percent_compare(self,win_times1, lose_times1, win_times2, lose_times2):
        return self.win_percent(win_times1, lose_times1) < self.win_percent(win_times2, lose_times2)
