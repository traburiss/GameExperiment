# Created by Traburiss on 2016/3/14
from people.player.base_player import BasePlayer
from people.player.dj_player.memory.dj_player_memory import DjPlayerMemory


class MyDjPlayer(BasePlayer):

    def __init__(self):
        self.memory = DjPlayerMemory()
        self.face_state = ""

    def actions(self):
        pass

