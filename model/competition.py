from model.abstractmodel import AbstractModel


class Competition(AbstractModel):
    def __init__(self, name, ptswin, ptsnull, ptslose, tworound, comment=None):
        super().__init__(self)
        # competition model from championnat table
        self.__name = name  # name of the competition
        self.__pts_win = ptswin  # win point
        self.__pts_lose = ptslose  # loose point
        self.__pts_null = ptsnull  # equality point
        self.__two_round = tworound
        self.__comment = comment

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def pts_win(self):
        return self.__pts_win

    @pts_win.setter
    def pts_win(self, value):
        self.__pts_win = value

    @property
    def pts_lose(self):
        return self.__pts_lose

    @pts_lose.setter
    def pts_lose(self, value):
        self.__pts_lose = value

    @property
    def pts_null(self):
        return self.__pts_null

    @pts_null.setter
    def pts_null(self, value):
        self.__pts_null = value

    @property
    def tworound(self):
        return self.__two_round

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value
