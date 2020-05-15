drop view if exists view_goal;
create view view_goal
AS
select *
from
	(SELECT bt3.id_but, bt1.*
	FROM joueur_event as bt2, But as bt3, Joueur as bt1
	WHERE bt1.id_joueur = bt2.id_joueur and bt2.id_but = bt3.id_but) as scorer
,
	(SELECT bt1.*
	FROM joueur_event as bt2, But as bt3, Joueur as bt1
	WHERE bt1.id_joueur = bt2.id_joueur_assistance and bt2.id_but = bt3.id_but) as assistance