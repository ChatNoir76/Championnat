from model.abstractmodel import AbstractModel


class Team(AbstractModel):
    def __init__(self, id_competition, name, comment=None):
        super().__init__(self)
        self.__id_competition = id_competition
        self.__name = name
        self.__comment = comment

    @property
    def id_competition(self):
        return self.__id_competition

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value
