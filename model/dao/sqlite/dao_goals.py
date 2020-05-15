from model.dao.abstractdao import AbstractDAO
from model.dao.daoexception import DAOException
from model.goals import Goals

R_INSERT = """
INSERT INTO But 
VALUES (null, ?, ?, ?, ?, ?)"""
R_UPDATE = """
UPDATE But 
SET
    commentaire_but = ?,
    id_joueur_assistance = ?,
    id_joueur = ?
WHERE id_but = ?
"""
R_DELETE = """
DELETE FROM But 
WHERE id_but = ?"""
R_READBYID = """
SELECT * 
FROM vBut 
WHERE id_but = ?"""
R_READALL = """
SELECT * 
FROM vBut
"""
R_READBYMATCH = """
SELECT *
FROM vBut
WHERE id_match = ?
"""


class DaoGoals(AbstractDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def insert(self, o_goals):
        """
        Insert Goals Object
        :param o_goals: Goals Object
        """
        if isinstance(o_goals, Goals):
            lparam = [o_goals.comment,
                      o_goals.idplayer_ass,
                      o_goals.idplayer_scorer,
                      o_goals.idmatch,
                      o_goals.idequipe]
            rep = AbstractDAO._insert(self, R_INSERT, lparam)
            o_goals.id = rep

    def update(self, o_goals):
        """
        Update Goals Object
        :param o_goals: Goals Object
        :return: boolean, result of operation
        """
        if isinstance(o_goals, Goals):
            lparam = [o_goals.comment,
                      o_goals.idplayer_ass,
                      o_goals.idplayer_scorer,
                      o_goals.id]
            rep = AbstractDAO._update(self, R_UPDATE, lparam)
            return rep

    def delete(self, o_goals):
        """
        Delete Goals Object
        :param o_goals: Goals Object
        :return: boolean, result of operation
        """
        if isinstance(o_goals, Goals):
            lparam = [o_goals.id]
            rep = AbstractDAO._delete(self, R_DELETE, lparam)
            return rep

    def getById(self, id_goals):
        """
        Get Goals Object By it id
        :param id_goals: id of Goals Object
        :return: Goals Object
        """
        lparam = [id_goals]
        rep = AbstractDAO._read(self, R_READBYID, lparam)
        return self.__fetch_to_object(rep, True)

    def getAll(self, o_competition):
        """
        Get all Goals Object
        :return: list of Goals
        """
        rep = AbstractDAO._read(self, R_READALL, [o_competition.id])
        return self.__fetch_to_object(rep)

    def getByMatch(self, o_match):
        rep = AbstractDAO._read(self, R_READBYMATCH, [o_match.id])
        return self.__fetch_to_object(rep)

    def __fetch_to_object(self, fetchresult, return_one=False):
        """
        fetch[0]: id_championnat
        fetch[1]: id_but
        fetch[2]: commentaire_but
        fetch[3]: id_joueur_assistance
        fetch[4]: id_joueur
        fetch[5]: id_match
        fetch[6]: id_equipe
        :param fetchresult:
        :return:
        """
        liste = []
        try:
            if len(fetchresult) > 0:
                for fetch in fetchresult:
                    obj = Goals(fetch[4],
                                fetch[5],
                                fetch[6],
                                fetch[2],
                                fetch[3])
                    obj.id = fetch[1]
                    liste.append(obj)
                return liste if not return_one else liste[0]
            else:
                return None
        except Exception as ex:
            DAOException(self, ex)
