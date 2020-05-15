from model.dao.abstractdao import AbstractDAO
from model.dao.daoexception import DAOException
from model.match import Match

R_INSERT = """
INSERT INTO Match 
VALUES (null, ?, ?, ?)"""
R_INSERT2 = """
INSERT INTO Calendrier 
VALUES (?, ?, ?)"""
R_UPDATE = """
UPDATE Match 
SET
    date_match = ?,
    commentaire_match = ?,
    isplayed_match = ?
WHERE id_match = ?
"""
R_DELETE = """
DELETE FROM Match 
WHERE id_match = ?"""
R_READBYID = """
SELECT * 
FROM vMatch 
WHERE id_match = ?"""
R_READALL = """
SELECT * 
FROM vMatch
WHERE id_championnat = ?
"""
R_NEXTMATCH = """
SELECT *
FROM vMatch
WHERE isplayed_match = False and id_championnat = ?
LIMIT 1
"""
R_MATCHPLAYED = """
SELECT *
FROM vMatch
WHERE isplayed_match = True and id_championnat = ?
"""


class DaoMatch(AbstractDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def insert(self, o_match):
        if isinstance(o_match, Match):
            with self._conn as conn:
                try:
                    c = conn.cursor()
                    lparam = [o_match.datetime,
                              o_match.comment,
                              o_match.isplayed]
                    c.execute(R_INSERT, lparam)
                    index = c.lastrowid

                    pcalendrier = [o_match.idteam_home,
                                   index,
                                   o_match.idteam_outside]
                    c.execute(R_INSERT2, pcalendrier)
                    conn.commit()
                    o_match.id = index
                except Exception as ex:
                    conn.rollback()
                    DAOException(self, ex)

    def update(self, o_match):
        if isinstance(o_match, Match):
            lparam = [o_match.datetime,
                      o_match.comment,
                      o_match.isplayed,
                      o_match.id]
            rep = AbstractDAO._update(self, R_UPDATE, lparam)
            return rep

    def delete(self, o_match):
        if isinstance(o_match, Match):
            lparam = [o_match.id]
            rep = AbstractDAO._delete(self, R_DELETE, lparam)
            return rep

    def getById(self, id_match):
        lparam = [str(id_match)]
        rep = AbstractDAO._read(self, R_READBYID, lparam)
        return self.__fetch_to_object(rep, True)

    def getAll(self, o_competition):
        rep = AbstractDAO._read(self, R_READALL, [str(o_competition.id)])
        return self.__fetch_to_object(rep)

    def getNextMatch(self, o_competition):
        lparam = [o_competition.id]
        rep = AbstractDAO._read(self, R_NEXTMATCH, lparam)
        return self.__fetch_to_object(rep, True)

    def getMatchPlayed(self, o_competition):
        lparam = [o_competition.id]
        rep = AbstractDAO._read(self, R_MATCHPLAYED, lparam)
        return self.__fetch_to_object(rep)

    def __fetch_to_object(self, fetchresult, return_one=False):
        """
        fetch[0]: id_championnat
        fetch[1]: id_equipe
        fetch[2]: id_equipe_exterieur
        fetch[3]: id_match
        fetch[4]: date_match
        fetch[5]: commentaire_match
        fetch[6]: isplayed_match
        :param fetchresult:
        :param return_one:
        :return:
        """
        liste = []
        try:
            if len(fetchresult) > 0:
                for fetch in fetchresult:
                    obj = Match(fetch[1],
                                fetch[2],
                                fetch[4],
                                fetch[5],
                                fetch[6])
                    obj.id = fetch[3]
                    liste.append(obj)
                return liste if not return_one else liste[0]
            else:
                return None
        except Exception as ex:
            DAOException(self, ex)

