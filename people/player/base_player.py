# Created by Traburiss on 2016/1/27
from abc import abstractclassmethod

from people.base_people import BasePeople


class BasePlayer(BasePeople):
    """
    class docs
    """

    def __init__(self, name="no_name_player", game_type="base_type", play_id=0):
        """
        Constructor
        """
        BasePeople.__init__(self, name, play_id)
        self.__game_type = game_type

    def set_game_type(self, game_type):
        self.__game_type = game_type

    def get_game_type(self):
        return self.__game_type

    @abstractclassmethod
    def actions(self):
        pass
