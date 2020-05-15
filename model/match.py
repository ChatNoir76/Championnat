from model.abstractmodel import AbstractModel


class Match(AbstractModel):
    def __init__(self, id_team_home, id_team_outside, datetime=None, comment=None, isplayed=False):
        super().__init__(self)
        self.__idteam_home = id_team_home
        self.__idteam_outside = id_team_outside
        self.__datetime = datetime
        self.__comment = comment
        self.__isplayed = isplayed

    @property
    def idteam_home(self):
        return self.__idteam_home

    @property
    def idteam_outside(self):
        return self.__idteam_outside

    @property
    def datetime(self):
        return self.__datetime

    @datetime.setter
    def datetime(self, value):
        self.__datetime = value

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value

    @property
    def isplayed(self):
        return self.__isplayed

    @isplayed.setter
    def isplayed(self, value):
        self.__isplayed = value


