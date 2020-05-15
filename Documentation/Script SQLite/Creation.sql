------------------------------------------------------------
--        Script SQLite
------------------------------------------------------------


------------------------------------------------------------
-- Table: Championnat
------------------------------------------------------------
CREATE TABLE Championnat(
	id_championnat             INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
	nom_championnat            TEXT NOT NULL ,
	pts_win_championnat        INTEGER NOT NULL ,
	pts_null_championnat       INTEGER NOT NULL ,
	pts_lose_championnat       INTEGER NOT NULL ,
	two_legged_championnat     INTEGER NOT NULL ,
	commentaire_championnat    TEXT
);


------------------------------------------------------------
-- Table: Joueur
------------------------------------------------------------
CREATE TABLE Joueur(
	id_joueur               INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
	nom_joueur              TEXT NOT NULL ,
	prenom_joueur           TEXT ,
	datenaissance_joueur    NUMERIC ,
	commentaire_joueur      TEXT
);


------------------------------------------------------------
-- Table: Equipe
------------------------------------------------------------
CREATE TABLE Equipe(
	id_equipe             INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
	nom_equipe            TEXT NOT NULL ,
	commentaire_equipe    TEXT
);


------------------------------------------------------------
-- Table: Match
------------------------------------------------------------
CREATE TABLE Match(
	id_match             INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
	date_match           NUMERIC ,
	commentaire_match    TEXT ,
	isplayed_match       INTEGER NOT NULL
);


------------------------------------------------------------
-- Table: But
------------------------------------------------------------
CREATE TABLE But(
	id_but                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
	commentaire_but         TEXT ,
	id_joueur_assistance    INTEGER ,
	id_joueur               INTEGER ,
	id_match                INTEGER NOT NULL ,
	id_equipe               INTEGER NOT NULL

	,CONSTRAINT But_Joueur_FK FOREIGN KEY (id_joueur) REFERENCES Joueur(id_joueur)
	,CONSTRAINT But_Match0_FK FOREIGN KEY (id_match) REFERENCES Match(id_match)
	,CONSTRAINT But_Equipe1_FK FOREIGN KEY (id_equipe) REFERENCES Equipe(id_equipe)
);


------------------------------------------------------------
-- Table: Composition
------------------------------------------------------------
CREATE TABLE Composition(
	id_equipe                  INTEGER NOT NULL ,
	id_joueur                  INTEGER NOT NULL ,
	commentaire_composition    TEXT,
	CONSTRAINT Composition_PK PRIMARY KEY (id_equipe,id_joueur)

	,CONSTRAINT Composition_Equipe_FK FOREIGN KEY (id_equipe) REFERENCES Equipe(id_equipe)
	,CONSTRAINT Composition_Joueur0_FK FOREIGN KEY (id_joueur) REFERENCES Joueur(id_joueur)
);


------------------------------------------------------------
-- Table: Participant
------------------------------------------------------------
CREATE TABLE Participant(
	id_equipe         INTEGER NOT NULL ,
	id_championnat    INTEGER NOT NULL,
	CONSTRAINT Participant_PK PRIMARY KEY (id_equipe,id_championnat)

	,CONSTRAINT Participant_Equipe_FK FOREIGN KEY (id_equipe) REFERENCES Equipe(id_equipe)
	,CONSTRAINT Participant_Championnat0_FK FOREIGN KEY (id_championnat) REFERENCES Championnat(id_championnat)
);


------------------------------------------------------------
-- Table: Calendrier
------------------------------------------------------------
CREATE TABLE Calendrier(
	id_equipe              INTEGER NOT NULL ,
	id_match               INTEGER NOT NULL ,
	id_equipe_Exterieur    INTEGER NOT NULL,
	CONSTRAINT Calendrier_PK PRIMARY KEY (id_equipe,id_match,id_equipe_Exterieur)

	,CONSTRAINT Calendrier_Equipe_FK FOREIGN KEY (id_equipe) REFERENCES Equipe(id_equipe)
	,CONSTRAINT Calendrier_Match0_FK FOREIGN KEY (id_match) REFERENCES Match(id_match)
	,CONSTRAINT Calendrier_Equipe1_FK FOREIGN KEY (id_equipe_Exterieur) REFERENCES Equipe(id_equipe)
);


