from model.match import Match


class ModelProviderMatch(object):

    @staticmethod
    def get_new(id_team_home, id_team_outside, datetime=None, comment=None, isplayed=False):
        obj = Match(id_team_home, id_team_outside, datetime, comment, isplayed)
        return obj
