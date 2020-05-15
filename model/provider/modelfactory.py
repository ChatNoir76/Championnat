from model.provider.modelprovidercompetition import ModelProviderCompetition
from model.provider.modelprovidergoals import ModelProviderGoals
from model.provider.modelprovidermatch import ModelProviderMatch
from model.provider.modelproviderplayer import ModelProviderPlayer
from model.provider.modelproviderteam import ModelProviderTeam


class ModelFactory(object):

    @classmethod
    def getCompetitionProvider(cls):
        return ModelProviderCompetition()

    @classmethod
    def getTeamProvider(cls):
        return ModelProviderTeam()

    @classmethod
    def getPlayerProvider(cls):
        return ModelProviderPlayer()

    @classmethod
    def getMatchProvider(cls):
        return ModelProviderMatch()

    @classmethod
    def getGoalsProvider(cls):
        return ModelProviderGoals()
