# Created by Traburiss on 2016/1/27


class BasePeople(object):
    """
    classdocs
    """

    def __init__(self, name="no_name", play_id=0):
        """
        Constructor
        """
        self.__name = name
        self.__play_id = play_id

    def set_name(self, name):
        self.__name = name

    def set_play_id(self, play_id):
        self.__play_id = play_id

    def get_name(self):
        return self.__name

    def get_play_id(self):
        return self.__play_id
