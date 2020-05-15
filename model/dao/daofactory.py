from model.dao.singleton import Singleton
from model.dao.sqlite.dao_competition import DaoChampionnat
from model.dao.sqlite.dao_goals import DaoGoals
from model.dao.sqlite.dao_match import DaoMatch
from model.dao.sqlite.dao_player import DaoPlayer
from model.dao.sqlite.dao_team import DaoTeam


class DaoFactory(object):
    __connexion = Singleton().get_instance()

    @classmethod
    def getCompetition(cls):
        return DaoChampionnat(cls.__connexion)

    @classmethod
    def getTeam(cls):
        return DaoTeam(cls.__connexion)

    @classmethod
    def getPlayer(cls):
        return DaoPlayer(cls.__connexion)

    @classmethod
    def getGoals(cls):
        return DaoGoals(cls.__connexion)

    @classmethod
    def getMatch(cls):
        return DaoMatch(cls.__connexion)
