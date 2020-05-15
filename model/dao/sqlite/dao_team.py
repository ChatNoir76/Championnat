from model.dao.abstractdao import AbstractDAO
from model.dao.daoexception import DAOException
from model.team import Team

R_INSERT1 = """
INSERT INTO Equipe 
VALUES (null, ?, ?)"""
R_INSERT2 = """
INSERT INTO Participant 
VALUES (?, ?)"""
R_UPDATE = """
UPDATE Equipe 
SET
    nom_equipe = ?,
    commentaire_equipe = ?,
WHERE id_equipe = ?
"""
R_DELETE = """
DELETE FROM Equipe 
WHERE id_equipe = ?"""
R_READBYNAME = """
SELECT *
FROM vEquipe
WHERE nom_equipe = ?
"""
R_READBYID = """
SELECT * 
FROM vEquipe 
WHERE id_equipe = ?"""
R_READALL = """
SELECT * 
FROM vEquipe
WHERE id_championnat = ?
"""


class DaoTeam(AbstractDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def insert(self, o_team):
        if isinstance(o_team, Team):
            with self._conn as conn:
                try:
                    c = conn.cursor()
                    param_rq1 = [o_team.name,
                                 o_team.comment]
                    c.execute(R_INSERT1, param_rq1)
                    index = c.lastrowid
                    param_rq2 = [index,
                                 o_team.id_competition]
                    c.execute(R_INSERT2, param_rq2)
                    conn.commit()
                    o_team.id = index
                except Exception as ex:
                    conn.rollback()
                    DAOException(self, ex)

    def update(self, o_team):
        if isinstance(o_team, Team):
            lparam = [o_team.name,
                      o_team.comment,
                      o_team.id]
            rep = AbstractDAO._update(self, R_UPDATE, lparam)
            return rep

    def delete(self, o_team):
        if isinstance(o_team, Team):
            lparam = [o_team.id]
            rep = AbstractDAO._delete(self, R_DELETE, lparam)
            return rep

    def getById(self, id_team):
        lparam = [str(id_team)]
        rep = AbstractDAO._read(self, R_READBYID, lparam)
        return self.__fetch_to_object(rep, True)

    def getByName(self, str_team):
        lparam = [str_team]
        rep = AbstractDAO._read(self, R_READBYNAME, lparam)
        return self.__fetch_to_object(rep)

    def getAll(self, o_competition):
        rep = AbstractDAO._read(self, R_READALL, [str(o_competition.id)])
        return self.__fetch_to_object(rep)

    def __fetch_to_object(self, fetchresult, return_one=False):
        liste = []
        try:
            if len(fetchresult) > 0:
                for fetch in fetchresult:
                    obj = Team(fetch[0],
                               fetch[2],
                               fetch[3])
                    obj.id = fetch[1]
                    liste.append(obj)
                return liste if not return_one else liste[0]
            else:
                return None
        except Exception as ex:
            DAOException(self, ex)
