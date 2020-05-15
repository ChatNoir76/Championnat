from model.dao.abstractdao import AbstractDAO
from model.player import Player

R_PLAYERS_GOALS = """
select * from view_goal where id_but = ?
"""


class DaoService(AbstractDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def get_players_from_goal(self, o_goal):
        lparam = [str(o_goal.id)]
        rep = AbstractDAO._read(self, R_PLAYERS_GOALS, lparam)
        liste = []
        for p in range(1, len(rep[0]), 5):
            pl = Player(rep[0][p+1], rep[0][p+2], rep[0][p+3], rep[0][p+4])
            pl.id = rep[0][p]
            liste.append(pl)
        return liste
