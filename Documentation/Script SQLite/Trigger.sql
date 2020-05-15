drop trigger if exists equipe_before_delete;
create trigger equipe_before_delete before delete on Equipe
begin
	delete from Participant WHERE Participant.id_equipe = OLD.id_equipe;
end;

drop trigger if exists joueur_before_delete;
create trigger joueur_before_delete before delete on Joueur
begin
	delete from Composition WHERE Composition.id_joueur = OLD.id_joueur;
end;
