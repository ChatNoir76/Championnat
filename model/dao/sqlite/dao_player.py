from model.dao.abstractdao import AbstractDAO
from model.dao.daoexception import DAOException
from model.player import Player

R_INSERT = """
INSERT INTO Joueur 
VALUES (null, ?, ?, ?, ?)"""
R_INSERT2 = """
INSERT INTO Composition 
VALUES (?, ?, ?)"""
R_READ_CH_INDEX = """
SELECT id_championnat
FROM vJoueur
WHERE id_equipe = ?
"""
R_UPDATE = """
UPDATE Joueur 
SET
    nom_joueur = ?,
    prenom_joueur = ?,
    datenaissance_joueur = ?,
    commentaire_joueur = ?,
    WHERE id_joueur = ?
"""
R_DELETE = """
DELETE FROM Joueur 
WHERE id_joueur = ?"""
R_READBYNAME = """
SELECT * 
FROM vJoueur 
WHERE id_championnat = ? and nom_joueur = ?"""
R_READBYID = """
SELECT * 
FROM vJoueur 
WHERE id_joueur = ?"""
R_READALL = """
SELECT * 
FROM vJoueur
WHERE id_championnat = ?"""
R_READBYTEAM = """
SELECT * 
FROM vJoueur
WHERE id_equipe = ?
"""


class DaoPlayer(AbstractDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def insert(self, o_player, comment=None):
        if isinstance(o_player, Player):
            with self._conn as conn:
                try:
                    c = conn.cursor()
                    param_rq1 = [o_player.lname,
                                 o_player.fname,
                                 o_player.birthdate,
                                 o_player.comment]
                    c.execute(R_INSERT, param_rq1)
                    index = c.lastrowid

                    param_rq2 = [o_player.idteam,
                                 index,
                                 comment]
                    c.execute(R_INSERT2, param_rq2)
                    conn.commit()
                    o_player.id = index
                except Exception as ex:
                    conn.rollback()
                    DAOException(self, ex)

    def update(self, o_player):
        if isinstance(o_player, Player):
            lparam = [o_player.lname,
                      o_player.fname,
                      o_player.birthdate,
                      o_player.comment,
                      o_player.id]
            rep = AbstractDAO._update(self, R_UPDATE, lparam)
            return rep

    def delete(self, o_player):
        if isinstance(o_player, Player):
            lparam = [str(o_player.id)]
            rep = AbstractDAO._delete(self, R_DELETE, lparam)
            return rep

    def getById(self, id_player):
        if id_player is not None:
            lparam = [str(id_player)]
            rep = AbstractDAO._read(self, R_READBYID, lparam)
            return self.__fetch_to_object(rep, True)

    def getByTeam(self, o_team):
        if o_team is not None:
            lparam = [str(o_team.id)]
            rep = AbstractDAO._read(self, R_READBYTEAM, lparam)
            return self.__fetch_to_object(rep)

    def getAll(self, o_competition):
        if o_competition is not None:
            param = [str(o_competition.id)]
            rep = AbstractDAO._read(self, R_READALL, param)
            return self.__fetch_to_object(rep)

    def __fetch_to_object(self, fetchresult, return_one=False):
        """
        fetch[0] : id_championnat
        fetch[1] : id_equipe
        fetch[2] : id_joueur
        fetch[3] : nom_joueur
        fetch[4] : prenom_joueur
        fetch[5] : datenaissance_joueur
        fetch[6] : commentaire_joueur
        :param fetchresult:
        :param return_one:
        :return:
        """
        liste = []
        try:
            if len(fetchresult) > 0:
                for fetch in fetchresult:
                    obj = Player(fetch[1],
                                 fetch[3],
                                 fetch[4],
                                 fetch[5],
                                 fetch[6])
                    obj.id = fetch[2]
                    liste.append(obj)
                return liste if not return_one else liste[0]
            else:
                return None
        except Exception as ex:
            DAOException(self, ex)
