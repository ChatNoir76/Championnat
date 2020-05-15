from model.dao.daofactory import DaoFactory as dao
from model.provider.modelfactory import ModelFactory as model
from service.calendar_generator import CalendarGenerator


class ServiceProvider(object):

    @classmethod
    def getCalendar(cls, teams, double_round=None):
        return CalendarGenerator(teams, double_round).get_calendar()

    @classmethod
    def saveCalendar(cls, calendar):
        for i, t in enumerate(calendar):
            match = model.getMatchProvider().get_new(comment='match number {}'.format(i + 1))
            dao.getMatch().insert(match, t[0], t[1])
