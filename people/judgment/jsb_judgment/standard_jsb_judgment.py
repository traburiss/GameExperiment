# Created by Traburiss on 2016/1/27
from people.judgment.base_judgment import BaseJudgment
from people.player.jsb_player.standard_jsb_player import StandardJsbPlayer


class StandardJsbJudgment(BaseJudgment):
    """
    classdocs
    """
    RESULT_CODE = "RESULT_CODE"
    RESULT_NAME = "RESULT_NAME"
    WINNER = "WINNER"
    LOSER = "LOSER"
    __this_result = {RESULT_CODE: 0, RESULT_NAME: "错误", WINNER: [], LOSER: []}

    def __init__(self, name="no_name_jsb_judgment"):
        """
        Constructor
        """
        BaseJudgment.__init__(self, name, "jsb")

    def ruling(self, player_actions):
        if isinstance(player_actions, list):
            player_points = [[], [], []]
            try:
                for item in player_actions:
                    if isinstance(item, dict):
                        player_points[item[StandardJsbPlayer.JSB_CODE] - 1].append(item)
                    else:
                        print("data error")
                        self.set_this_result()
                        return

                if len(player_points[0]) > 0 and len(player_points[1]) > 0 >= len(player_points[2]):
                    self.set_this_result(2, "分出胜负！", player_points[1], player_points[0])

                elif len(player_points[0]) > 0 >= len(player_points[1]) and len(player_points[2]) > 0:
                    self.set_this_result(2, "分出胜负！", player_points[0], player_points[2])

                elif len(player_points[0]) <= 0 < len(player_points[1]) and len(player_points[2]) > 0:
                    self.set_this_result(2, "分出胜负！", player_points[2], player_points[1])

                else:
                    self.set_this_result(1, "未分出胜负")

            except BaseException as e:
                print("data error" + str(e))
                self.set_this_result()
        else:
            print("data error")
            self.set_this_result()

    def set_this_result(self, code=0, name="错误", winner=(), loser=()):
        self.__this_result[self.RESULT_CODE] = code
        self.__this_result[self.RESULT_NAME] = name
        self.__this_result[self.WINNER] = winner
        self.__this_result[self.LOSER] = loser

    def get_this_result(self):
        return self.__this_result

    def get_result_code(self):
        return self.__this_result[self.RESULT_CODE]

    def get_result_name(self):
        return self.__this_result[self.RESULT_NAME]

    def get_winner(self):
        return self.__this_result[self.WINNER]

    def get_loser(self):
        return self.__this_result[self.LOSER]
