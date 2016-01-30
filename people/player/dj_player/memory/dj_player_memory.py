# Created by Traburiss on 2016/3/14


class DjPlayerMemory(object):
    def __init__(self):
        self.situations = []
        self.steps = []
        self.win_style = 0

    def add_state(self, situation="", step=1):
        self.situations.append(situation)
        self.steps.append(step)

    def refresh_win_style(self, win_style=0):
        self.win_style = win_style
