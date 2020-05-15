from model.team import Team


class ModelProviderTeam(object):

    @staticmethod
    def get_new(id_competition, name, comment=None):
        obj = Team(id_competition, name, comment)
        return obj

    @staticmethod
    def get_paris_team(id_competition):
        obj = Team(id_competition, "Paris St Germain", "equipe test 1")
        return obj

    @staticmethod
    def get_lyon_team(id_competition):
        obj = Team(id_competition, "Olympique Lyonnais", "equipe test 2")
        return obj

    @staticmethod
    def get_marseille_team(id_competition):
        obj = Team(id_competition, "Olympique de Marseille", "equipe test 3")
        return obj

    @staticmethod
    def get_lille_team(id_competition):
        obj = Team(id_competition, "Lille", "equipe test 4")
        return obj
