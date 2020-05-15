from model.competition import Competition
from model.dao.abstractdao import AbstractDAO
from model.dao.daoexception import DAOException

R_INSERT = """
INSERT INTO Championnat 
VALUES (null, ?, ?, ?, ?, ?, ?)"""
R_UPDATE = """
UPDATE Championnat 
SET
    nom_championnat = ?,
    pts_win_championnat = ?,
    pts_null_championnat = ?,
    pts_lose_championnat = ?,
    two_legged_championnat = ?,
    commentaire_championnat = ?
WHERE id_championnat = ?
"""
R_DELETE = """
DELETE FROM Championnat 
WHERE id_championnat = ?"""
R_READBYNAME = """
SELECT * 
FROM Championnat 
WHERE nom_championnat = ?"""
R_READBYID = """
SELECT * 
FROM Championnat 
WHERE id_championnat = ?"""
R_READALL = """
SELECT * 
FROM Championnat"""


class DaoChampionnat(AbstractDAO):

    def __init__(self, conn):
        super().__init__(conn)

    def getByName(self, oname):
        lparam = [oname]
        rep = AbstractDAO._read(self, R_READBYNAME, lparam)
        return self.__fetch_to_object(rep, True)

    def insert(self, obj):
        if isinstance(obj, Competition):
            lparam = [obj.name,
                      obj.pts_win,
                      obj.pts_null,
                      obj.pts_lose,
                      obj.tworound,
                      obj.comment]
            index = AbstractDAO._insert(self, R_INSERT, lparam)
            obj.id = index

    def update(self, obj):
        if isinstance(obj, Competition):
            lparam = [obj.name,
                      obj.pts_win,
                      obj.pts_null,
                      obj.pts_lose,
                      obj.tworound,
                      obj.comment,
                      obj.id]
            rep = AbstractDAO._update(self, R_UPDATE, lparam)
            return rep

    def delete(self, obj):
        if isinstance(obj, Competition):
            lparam = [obj.id]
            rep = AbstractDAO._delete(self, R_DELETE, lparam)
            return rep

    def getById(self, oid):
        lparam = [str(oid)]
        rep = AbstractDAO._read(self, R_READBYID, lparam)
        return self.__fetch_to_object(rep, True)

    def getAll(self):
        rep = AbstractDAO._read(self, R_READALL)
        return self.__fetch_to_object(rep)

    def __fetch_to_object(self, fetchresult, return_one=False):
        liste = []
        try:
            if len(fetchresult) > 0:
                for fetch in fetchresult:
                    obj = Competition(fetch[1],
                                      fetch[2],
                                      fetch[3],
                                      fetch[4],
                                      fetch[5],
                                      fetch[6])
                    obj.id = fetch[0]
                    liste.append(obj)
                return liste if not return_one else liste[0]
            else:
                return None
        except Exception as ex:
            DAOException(self, ex)
