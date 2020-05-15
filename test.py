from model.dao.daofactory import DaoFactory
from model.provider.modelfactory import ModelFactory
from service.service_provider import ServiceProvider


class Classement(object):
    def __init__(self, lteams):
        self.teams = {}  # team = (win, null, lose, BP, BC)
        for team in lteams:
            self.teams[team] = [0, 0, 0, 0, 0]

    def show(self):
        print('===============================')
        print('CLASSEMENT: ')
        for key, values in self.teams.items():
            print('{} {}'.format(key.name, values))
        print('===============================')

    def set_result(self, oteam1, score1, score2, oteam2):
        if score1 == score2:
            self.teams[oteam1][1] += 1
            self.teams[oteam2][1] += 1
        elif score1 > score2:
            self.teams[oteam1][0] += 1
            self.teams[oteam2][2] += 1
        else:
            self.teams[oteam1][2] += 1
            self.teams[oteam2][0] += 1
        self.teams[oteam1][3] += score1
        self.teams[oteam1][4] += score2
        self.teams[oteam2][3] += score2
        self.teams[oteam2][4] += score1


model = ModelFactory()
dao = DaoFactory()
service = ServiceProvider()
ch = dao.getCompetition().getById(1)
teams = dao.getTeam().getAll(ch)
monClassement = Classement(teams)
monClassement.show()

matchs = dao.getMatch().getMatchPlayed(ch)
for match in matchs:
    team_dom = dao.getTeam().getById(match.idteam_home)
    team_ext = dao.getTeam().getById(match.idteam_outside)
    score_dom = 0
    score_ext = 0
    goals = dao.getGoals().getByMatch(match)
    for goal in goals:
        if goal.idequipe == team_dom.id:
            score_dom += 1
        else:
            score_ext += 1
    monClassement.set_result(team_dom, score_dom, score_ext, team_ext)
    print('{} {} - {} {}'.format(team_dom.name, score_dom, score_ext, team_ext.name))
monClassement.show()


"""      
    def __update_result(self):
        self.listWidget_matchslist.addItem(self.__competition.get_lastresult())
        result = self.__competition.get_results()
        for row in range(len(result)):
            for column in range(len(result[row])):
                # print('row: {}, column: {} => data: {}'.format(row-1, column, result[row][column]))
                info = result[row][column]
                item = QTableWidgetItem('%s' % info)
                self.tableWidget_competitionresult.setItem(row, column, item)

    def __goal_window(self):
        dialog = GoalWindow(self)
        dialog.set_datas(self.__dico)
        btpressed = dialog.exec()
        if btpressed:
            self.__update_score(dialog.get_datas())

    def __update_score(self, goal_window_result):
        txtedit = self.textEdit_extscore if goal_window_result[0] else self.textEdit_domscore
        score = int(txtedit.toPlainText())
        score += 1
        txtedit.setText(str(score))
        team = self.__competition.get_teamofthenextmatch(not goal_window_result[0])
        self.listWidget_matchevent.addItem('GOAL for team {}'.format(team.get_name()))

    def __info_next_match(self):
        oTeam1 = self.__competition.get_teamofthenextmatch(True)
        oTeam2 = self.__competition.get_teamofthenextmatch(False)
        self.__dico.clear()
        self.__dico[oTeam1.get_name()] = oTeam1.get_players_list()
        self.__dico[oTeam2.get_name()] = oTeam2.get_players_list()
        self.textEdit_dom.setText(oTeam1.get_name())
        self.textEdit_vis.setText(oTeam2.get_name())
        self.textEdit_extscore.setText('0')
        self.textEdit_domscore.setText('0')
        for player in oTeam1.get_players_list():
            self.listWidget_domplayer.addItem(player.get_description())
        for player in oTeam2.get_players_list():
            self.listWidget_extplayer.addItem(player.get_description())
"""
"""
        # competition configuration
        self.__teams = {}  # key: team object, value:(victoire, null, défaite, but pour, but contre)
        self.__matchs = []  # Calendar => [n]: match number n, [n][0]: team1, [n][1]: team2
        self.__lastresult = ''

        # system configuration
        self.__isStarted = False  # to know if adding team is finished
        self.__mixer = 0  # gets modulo to mix team to create matches calendar
        self.__teams_list = []  # to create calendar
        self.__NOTEAM = 'teamnomatch'

    def description(self):
        texte = 'compétition: {} [{} équipes]'.format(self.__nom, len(self.__teams))
        for team, result in self.__teams.items():
            if team != self.__NOTEAM:
                score = result[0] * self.__pts_win
                score += result[1] * self.__pts_null
                score += result[2] * self.__pts_lose
                diff = result[3] - result[4]
                match = result[0] + result[1] + result[2]
                texte += "\n{} - {}pts ({}) att:{} nbMatchs:{}".format(team, score, diff, result[3], match)
        return texte

    def get_team_byindex(self, index):
        return tuple(self.__teams)[index]

    def get_lastresult(self):
        return self.__lastresult

    def get_totalmatch(self):
        total = 1
        return total * 2 if self.__two_legged else total

    def add_team(self, team):
        if not self.__isStarted:
            self.__teams[team] = [0, 0, 0, 0, 0]

    def delete_team(self, team):
        if not self.__isStarted:
            del self.__teams[team]

    def get_teamnumber(self):
        if self.__NOTEAM in self.__teams:
            return len(self.__teams) - 1
        else:
            return len(self.__teams)

    def get_matchnumber(self):
        return len(self.__matchs)

    def get_teamofthenextmatch(self, domicile=True):
        return self.__matchs[0][0 if domicile else 1]
        
**************************************************************************************************
**************************************************************************************************
    def get_results(self):
        liste = []
        for team, result in self.__teams.items():
            if team != self.__NOTEAM:
                score = result[0] * self.__pts_win
                score += result[1] * self.__pts_null
                score += result[2] * self.__pts_lose
                diff = result[3] - result[4]
                match = result[0] + result[1] + result[2]
                ligne = (team.get_name(),
                         score,
                         result[0],
                         result[1],
                         result[2],
                         match,
                         diff,
                         result[3],
                         result[4])
                liste.append(ligne)
        return sorted(liste, key=itemgetter(1, 3, 4), reverse=True)
**************************************************************************************************
**************************************************************************************************

    def next(self):
        if not self.__isStarted:
            self.start_competition()
        # run next match
        team1 = self.__matchs[0][0]  # get team1 object
        team2 = self.__matchs[0][1]  # get team2 object
        del self.__matchs[0]  # delete meeting
        current_match = Match(team1, team2)  # create match object from team of the meeting
        # print(current_match)
        self.__save_match_result(team1, team2, current_match.play_simulate(20))  # records result into competition
        return len(self.__matchs)  # return number of matches remaining (at zero => return false)

    def start_competition(self):
        if not self.__isStarted:  # competition start & block add team method
            self.__isStarted = True
            if len(self.__teams) % 2 == 1:
                self.__teams[self.__NOTEAM] = []
            self.__prepare_matchs_list()  # initialize matches calendar

    def __save_match_result(self, team1, team2, result):
        # print(result)
        self.__lastresult = '{} {}-{} {}'.format(team1.get_name(), result[0], result[1], team2.get_name())
        score1 = result[0]
        score2 = result[1]
        if score1 > score2:
            self.__scoring_team(team1, 1, 0, 0, score1, score2)
            self.__scoring_team(team2, 0, 0, 1, score2, score1)
        elif score1 < score2:
            self.__scoring_team(team1, 0, 0, 1, score1, score2)
            self.__scoring_team(team2, 1, 0, 0, score2, score1)
        else:
            self.__scoring_team(team1, 0, 1, 0, score1, score2)
            self.__scoring_team(team2, 0, 1, 0, score2, score1)

    def __scoring_team(self, team, victory, null, defeat, but_pour, but_contre):
        team_result = self.__teams.get(team)
        # (victoire, null, défaite, but pour, but contre)
        team_result[0] += victory
        team_result[1] += null
        team_result[2] += defeat
        team_result[3] += but_pour
        team_result[4] += but_contre
"""

"""def __prepare_matchs_list(self):
        meeting_day = len(self.__teams) - 1

        # load teams list
        for team in self.__teams.keys():
            self.__teams_list.append(team)

        while self.__mixer < meeting_day:
            for i in range(int(len(self.__teams_list) / 2)):
                team1 = self.__teams_list[i]
                team2 = self.__teams_list[len(self.__teams_list) - 1 - i]

                if i % 2 != 0:  # impair
                    self.__add_match(team1, team2)
                else:  # pair
                    if i == 0:
                        if self.__mixer % 2 == 0:
                            self.__add_match(team2, team1)
                        else:
                            self.__add_match(team1, team2)
                    else:
                        self.__add_match(team2, team1)

            self.__next_tour()
        # print("nb de match: {}".format(len(self.__matchs)))
"""
"""
    def __add_match(self, team1, team2):
        if team1 != self.__NOTEAM != team2:
            self.__matchs.append((team1, team2))

    def __next_tour(self):
        imax = len(self.__teams_list) - 1
        team = self.__teams_list[imax]
        del self.__teams_list[imax]
        self.__teams_list.insert(1, team)
        self.__mixer += 1"""
"""def __str__(self):
    return '{} VS {}'.format(self.team1, self.team2)

def play_simulate(self, rounder):

    score = [0, 0]
    # print('START')
    for r in range(1, rounder+1):
        # print('{}/{}'.format(r, rounder))
        def1 = random.randint(1, self.team1.get_defence())
        def2 = random.randint(1, self.team2.get_defence())

        for i in range(0, self.team1.get_attack()):
            att1 = random.randint(1, self.team2.get_defence())
            if att1 == def2:
                score[0] += 1
                # print('     team1 GOAL')

        for i in range(0, self.team2.get_attack()):
            att2 = random.randint(1, self.team1.get_defence())
            if att2 == def1:
                score[1] += 1
                # print('     team2 GOAL')

    # print('final score: {} - {}'.format(score[0], score[1]))
    return score"""