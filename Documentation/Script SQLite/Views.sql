drop view if exists vEquipe;
create view vEquipe
AS
select Participant.id_championnat, Equipe.*
FROM Equipe, Participant, Championnat
WHERE Equipe.id_equipe = Participant.id_equipe and Participant.id_championnat = Championnat.id_championnat
ORDER by id_equipe;

drop view if exists vJoueur;
create view vJoueur
AS
select vEquipe.id_championnat, Composition.id_equipe, Joueur.*
FROM Joueur, Composition, vEquipe
WHERE Joueur.id_joueur = Composition.id_joueur and Composition.id_equipe = vEquipe.id_equipe
ORDER by id_joueur;

drop view if exists vMatch;
create view vMatch
AS
select vEquipe.id_championnat, Calendrier.id_equipe, Calendrier.id_equipe_Exterieur, Match.*
FROM Match, Calendrier, vEquipe
WHERE Match.id_match = Calendrier.id_match and Calendrier.id_equipe = vEquipe.id_equipe
ORDER by id_match;

drop view if exists vBut;
create view vBut
AS
select DISTINCT *
FROM
	(select vMatch.id_championnat, But.*
	FROM vEquipe, vMatch, vJoueur, But
	WHERE vMatch.id_match = But.id_match and vEquipe.id_equipe = But.id_equipe
	ORDER by id_but)
