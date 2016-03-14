# Created by Traburiss on 2016/3/14
from people.player.base_player import BasePlayer
from people.player.dj_player.memory.dj_player_memory import DjPlayerMemory


class MyDjPlayer(BasePlayer):
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
        return result_step, win_times, lose_times

    # 调用数据库历史数据返回结果，根据deep参数迭代推算下一步，再去获取下一步的数据库局面结果，得到最优结果，施工中，
    def get_batter_step(self, face_state, deep):
        result_step = -1
        return result_step
