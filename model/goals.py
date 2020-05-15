from model.abstractmodel import AbstractModel


class Goals(AbstractModel):
    def __init__(self, id_player_scorer, idmatch, idequipe, comment=None, id_player_ass=None):
        super().__init__(self)
        self.__idplayer_scorer = id_player_scorer
        self.__idplayer_ass = id_player_ass
        self.__idmatch = idmatch
        self.__idequipe = idequipe
        self.__comment = comment

    @property
    def idplayer_scorer(self):
        return self.__idplayer_scorer

    @property
    def idplayer_ass(self):
        return self.__idplayer_ass

    @property
    def idmatch(self):
        return self.__idmatch

    @property
    def idequipe(self):
        return self.__idequipe

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value
