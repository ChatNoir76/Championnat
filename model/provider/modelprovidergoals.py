from model.goals import Goals


class ModelProviderGoals(object):

    @staticmethod
    def get_new(id_player_scorer, idmatch, idequipe, id_player_ass=None, comment=None):
        obj = Goals(id_player_scorer, idmatch, idequipe, comment, id_player_ass)
        return obj
