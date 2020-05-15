from datetime import datetime

from model.dao.daofactory import DaoFactory as dao
from model.provider.modelfactory import ModelFactory as model
from service.service_provider import ServiceProvider as service

o = len(dao.getCompetition().getAll())
if o == 0:
    chp = model.getCompetitionProvider().get_standard_competition("ma competition")
    dao.getCompetition().insert(chp)
    team1 = model.getTeamProvider().get_new("Liverpool")
    dao.getTeam().insert(team1, chp)
    team2 = model.getTeamProvider().get_new("Chelsea")
    dao.getTeam().insert(team2, chp)
    team3 = model.getTeamProvider().get_new("Arsenal")
    dao.getTeam().insert(team3, chp)
    team4 = model.getTeamProvider().get_new("Manchester")
    dao.getTeam().insert(team4, chp)
    pl1 = model.getPlayerProvider().get_randomplayer()
    pl2 = model.getPlayerProvider().get_randomplayer()
    dao.getPlayer().insert(pl1, team1, team1.name)
    dao.getPlayer().insert(pl2, team1, team1.name)
    pl3 = model.getPlayerProvider().get_randomplayer()
    pl4 = model.getPlayerProvider().get_randomplayer()
    dao.getPlayer().insert(pl3, team2, team2.name)
    dao.getPlayer().insert(pl4, team2, team2.name)
    pl5 = model.getPlayerProvider().get_randomplayer()
    pl6 = model.getPlayerProvider().get_randomplayer()
    dao.getPlayer().insert(pl5, team3, team3.name)
    dao.getPlayer().insert(pl6, team3, team3.name)
    pl7 = model.getPlayerProvider().get_randomplayer()
    pl8 = model.getPlayerProvider().get_randomplayer()
    dao.getPlayer().insert(pl7, team4, team4.name)
    dao.getPlayer().insert(pl8, team4, team4.name)

    teams = [team1, team2, team3, team4]

    calendar = service.getCalendar(teams)
    service.saveCalendar(calendar)

else:
    chp = dao.getCompetition().getByName("ma competition")
    team1 = dao.getTeam().getByName("Liverpool", chp)
    team2 = dao.getTeam().getByName("Chelsea", chp)
    team3 = dao.getTeam().getByName("Arsenal", chp)
    team4 = dao.getTeam().getByName("Manchester", chp)

    pl1 = dao.getPlayer().getByTeam(team1)[0]
    pl2 = dao.getPlayer().getByTeam(team1)[1]
    pl3 = dao.getPlayer().getByTeam(team2)[0]
    pl4 = dao.getPlayer().getByTeam(team2)[1]
    pl5 = dao.getPlayer().getByTeam(team3)[0]
    pl6 = dao.getPlayer().getByTeam(team3)[1]
    pl7 = dao.getPlayer().getByTeam(team4)[0]
    pl8 = dao.getPlayer().getByTeam(team4)[1]

    teams = [team1, team2, team3, team4]
































