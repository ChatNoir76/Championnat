class CalendarGenerator(object):

    def __init__(self, teams, double_round=False):
        self.__double_round = double_round
        if len(teams) > 1:
            self.__teams = teams
            if len(self.__teams) % 2 == 1:
                self.__teams.append(None)  # to have pair teams

    def get_calendar(self):
        calendar = []  # list of tuple (teamhome - teamoutside)
        mixer = []

        for team in self.__teams:
            mixer.append(team)  # pivot fixe : team index 0

        for ar in range(0, 2 if self.__double_round else 1):
            for tour in range(1, len(self.__teams)):
                for i in range(0, int(len(mixer)/2)):
                    i1 = i
                    i2 = len(mixer)-1-i
                    if i == 0:
                        t_dom = mixer[i1 if ar == 0 else i2] if tour % 2 != 0 else mixer[i2 if ar == 0 else i1]
                        t_vis = mixer[i2 if ar == 0 else i1] if tour % 2 != 0 else mixer[i1 if ar == 0 else i2]
                    else:
                        t_dom = mixer[i1 if ar == 0 else i2] if i % 2 != 0 else mixer[i2 if ar == 0 else i1]
                        t_vis = mixer[i2 if ar == 0 else i1] if i % 2 != 0 else mixer[i1 if ar == 0 else i2]
                    if t_dom is not None and t_vis is not None:  # to exclude ghost team
                        calendar.append((t_dom, t_vis))
                # team rotation for the next tour
                team = mixer[1]
                del mixer[1]
                mixer.append(team)
        return calendar
