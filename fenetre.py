from operator import itemgetter

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QAction, QLineEdit, QTableWidgetItem
from view.ui.Ui_main import Ui_MainWindow
from model.dao.daofactory import DaoFactory as dao
from model.provider.modelfactory import ModelFactory as model
from service.service_provider import ServiceProvider as service
from view.uiaddplayer import AddPlayerWindow
from view.uigoal import GoalWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    on_changed_competition = pyqtSignal(object)
    on_changed_teams = pyqtSignal(list)
    on_changed_players = pyqtSignal(list)
    on_changed_current_team = pyqtSignal(object)
    on_changed_current_player = pyqtSignal(object)
    on_changed_competition_begin = pyqtSignal(bool)
    on_changed_current_match = pyqtSignal(object)

    @staticmethod
    def __clear_listwidget(item):
        item.blockSignals(True)
        item.clear()
        item.blockSignals(False)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # PROPERTY [from model object]
        self.__competition = None
        self.__teams = None
        self.__current_team = None
        self.__players = None
        self.__current_player = None
        self.__competition_begin = False
        self.__current_match = None
        # INITIALIZATION
        self.__initialize_static_objects()
        self.__initialize_events()

    def __initialize_static_objects(self):
        # === TABLE HEADER ===
        self.__tableheaders = ['team name', 'Pts', 'Winned', 'Egality', 'Losed', 'played', 'diff', 'BP', 'BC']
        self.tableWidget_competitionresult.setColumnCount(len(self.__tableheaders))
        self.tableWidget_competitionresult.setHorizontalHeaderLabels(self.__tableheaders)

    def __initialize_events(self):
        # === CONNECT SIGNAL TO SLOT ===
        self.tabWidget.currentChanged.connect(self.__event_tab_selection_changed)
        # PROPERTY
        self.on_changed_players.connect(self.__after_changed_property_players)
        self.on_changed_teams.connect(self.__after_changed_property_teams)
        self.on_changed_competition.connect(self.__after_changed_property_competition)
        self.on_changed_current_team.connect(self.__after_changed_property_current_team)
        self.on_changed_current_player.connect(self.__after_changed_property_current_player)
        self.on_changed_competition_begin.connect(self.__after_changed_property_competition_begin)
        self.on_changed_current_match.connect(self.__update_view_for_current_match)
        # LISTWIDGET
        self.listWidget_teamslist.currentRowChanged.connect(self.__event_selected_team)
        self.listWidget_playerslist.currentRowChanged.connect(self.__event_selected_player)
        # MENU
        self.actionStandard_Competition.triggered.connect(self.__event_create_competition)
        self.__menu_open_competitions()  # auto generate event [autolink with self.__event_load_competition]
        self.actionStart.triggered.connect(self.__start_competition)
        # BUTTON
        self.pushButton_addplayer.clicked.connect(self.__event_bt_addplayer)
        self.pushButton_deleteplayer.clicked.connect(self.__event_bt_deleteplayer)
        self.pushButton_addteam.clicked.connect(self.__event_bt_addteam)
        self.pushButton_deleteteam.clicked.connect(self.__event_bt_deleteteam)
        self.pushButton_cm_goal.clicked.connect(self.__event_bt_after_goals)
        self.pushButton_cm_endmatch.clicked.connect(self.__event_bt_after_save_match)

    # ================
    # === PROPERTY ===
    # ================
    def get_competition_begin(self):
        return self.__competition_begin

    def set_competition_begin(self, value):
        self.__competition_begin = value
        if value is not None:
            self.on_changed_competition_begin.emit(value)

    def get_competition(self):
        return self.__competition

    def set_competition(self, value):
        self.__competition = value
        if value is not None:
            self.on_changed_competition.emit(value)

    def get_teams(self):
        return self.__teams

    def set_teams(self, value):
        self.__teams = value
        if value is not None:
            self.on_changed_teams.emit(value)

    def get_players(self):
        return self.__players

    def set_players(self, value):
        self.__players = value
        if value is not None:
            self.on_changed_players.emit(value)

    def get_current_team(self):
        return self.__current_team

    def set_current_team(self, value):
        self.__current_team = value
        if value is not None:
            self.on_changed_current_team.emit(value)

    def get_current_player(self):
        return self.__current_player

    def set_current_player(self, value):
        self.__current_player = value
        if value is not None:
            self.on_changed_current_player.emit(value)

    def get_current_match(self):
        return self.__current_match

    def set_current_match(self, o_match):
        if o_match is not None:
            self.__current_match = o_match
            self.on_changed_current_match.emit(o_match)
        else:
            self.__current_match = None

    # ====================================
    # === ===
    # ====================================
    def __refresh_tab1(self):
        self.__teams = None
        self.__current_team = None
        self.__players = None
        self.__current_player = None
        self.on_changed_competition.emit(self.get_competition())

    # ==========================
    # === VIEW CURRENT MATCH ===
    # ==========================
    def __update_result_after_match_finished(self):
        self.progressBar_competitionlevel.setValue(dao.getMatch().getMatchPlayed(self.get_competition()))
        matchs = dao.getMatch().getAll()

    def __update_view_for_current_match(self, o_match):
        self.__clear_listwidget(self.listWidget_domplayer)
        self.__clear_listwidget(self.listWidget_extplayer)
        self.__clear_listwidget(self.listWidget_matchevent)
        if o_match is not None:
            o_tdom = dao.getTeam().getById(o_match.idteam_home)
            o_tvis = dao.getTeam().getById(o_match.idteam_outside)
            self.textEdit_dom.setText(o_tdom.name)
            self.textEdit_vis.setText(o_tvis.name)
            self.textEdit_domscore.setText('0')
            self.textEdit_extscore.setText('0')
            playerteamdom = dao.getPlayer().getByTeam(o_tdom)
            for player in playerteamdom:
                self.listWidget_domplayer.addItem(player.description)
            playerteamext = dao.getPlayer().getByTeam(o_tvis)
            for player in playerteamext:
                self.listWidget_extplayer.addItem(player.description)
            # if there are goal
            listgoal = dao.getGoals().getByMatch(o_match)
            if listgoal is not None:
                for goal in listgoal:
                    oteam = dao.getTeam().getById(goal.idequipe)
                    oscorer = dao.getPlayer().getById(goal.idplayer_scorer)
                    oass = dao.getPlayer().getById(goal.idplayer_ass)
                    self.__update_view_after_goals(oteam, oscorer, oass)

    def __update_view_after_goals(self, oteam, oscorer, oass):
        text = 'GOAL for {}\n\tscorer: {}\n\tass: {}\n==============='.format(
            oteam.name,
            oscorer.description if oscorer is not None else 'own goal',
            oass.description if oass is not None else 'none')
        team_dom = dao.getTeam().getById(self.get_current_match().idteam_home)
        txtedit = self.textEdit_domscore if oteam == team_dom else self.textEdit_extscore
        score = int(txtedit.toPlainText())
        score += 1
        txtedit.setText(str(score))
        self.listWidget_matchevent.addItem(text)

    # ====================================
    # === EVENT AFTER CHANGED PROPERTY ===
    # ====================================
    # update view after competition_begin modification  [property]
    def __after_changed_property_competition_begin(self, compet_start):
        self.pushButton_deleteplayer.setEnabled(not compet_start)
        self.pushButton_deleteteam.setEnabled(not compet_start)
        self.actionStart.setEnabled(not compet_start)
        if compet_start:
            self.progressBar_competitionlevel.setMaximum(len(dao.getMatch().getAll(self.get_competition())))
            self.tableWidget_competitionresult.setRowCount(len(self.get_teams()))
            match = dao.getMatch().getNextMatch(self.get_competition())
            self.set_current_match(match)

    # update view after competition modification  [property]
    def __after_changed_property_competition(self, o_competition):
        if o_competition is not None:
            self.setWindowTitle(o_competition.name)
            self.set_teams(dao.getTeam().getAll(o_competition))
            self.tabWidget.setEnabled(True)
        else:
            self.tabWidget.setEnabled(False)

    # update view after teams modification  [property]
    def __after_changed_property_teams(self, teams_list):
        # Clear list
        self.__clear_listwidget(self.listWidget_teamslist)
        if teams_list is not None:
            # Update list
            for team in teams_list:
                self.listWidget_teamslist.addItem(team.name)

    # update view after players modification  [property]
    def __after_changed_property_players(self, p_players):
        # reset view config
        self.__clear_listwidget(self.listWidget_playerslist)
        self.pushButton_deleteplayer.setEnabled(False)
        # update list of players
        if p_players is not None:
            for player in p_players:
                self.listWidget_playerslist.addItem(player.description)

    # action after current_team modification [property]
    def __after_changed_property_current_team(self, team):
        self.__clear_listwidget(self.listWidget_playerslist)
        # get players for the team
        if team is not None:
            self.set_players(dao.getPlayer().getByTeam(team))
            self.pushButton_addplayer.setEnabled(True)
            self.pushButton_addplayer.setText("Add Player to {}".format(team.name))
        else:
            self.pushButton_addplayer.setEnabled(False)

    # action after current_player modification [property]
    def __after_changed_property_current_player(self, player):
        self.pushButton_deleteplayer.setEnabled(player is not None)
        self.pushButton_deleteplayer.setText(
            "Delete player {}".format(player.description if player is not None else ""))

    # =====================
    # === EVENT FOR TAB ===
    # =====================
    def __event_tab_selection_changed(self, index):
        self.__clear_listwidget(self.listWidget_matchslist)
        if index == 1:
            matchs = dao.getMatch().getMatchPlayed(self.get_competition())
            if matchs is not None:
                self.progressBar_competitionlevel.setValue(len(matchs))
            teams = dao.getTeam().getAll(self.get_competition())
            monClassement = Classement(teams)
            if matchs is not None:
                for match in matchs:
                    team_dom = dao.getTeam().getById(match.idteam_home)
                    team_ext = dao.getTeam().getById(match.idteam_outside)
                    score_dom = 0
                    score_ext = 0
                    goals = dao.getGoals().getByMatch(match)
                    if goals is not None:
                        for goal in goals:
                            if goal.idequipe == team_dom.id:
                                score_dom += 1
                            else:
                                score_ext += 1
                        monClassement.add_score(team_dom, score_dom, score_ext, team_ext)
                        self.listWidget_matchslist.addItem('{} {} - {} {}'.format(
                            team_dom.name, score_dom, score_ext, team_ext.name))
            self.__update_result(monClassement)

    def __update_result(self, classement):
        self.tableWidget_competitionresult.clearContents()
        result = classement.get_result()
        for row in range(len(result)):
            for column in range(len(result[row])):
                # print('row: {}, column: {} => data: {}'.format(row-1, column, result[row][column]))
                info = result[row][column]
                item = QTableWidgetItem('%s' % info)
                self.tableWidget_competitionresult.setItem(row, column, item)

    # =============================================
    # === EVENT AFTER SELECTION FROM LISTWIDGET ===
    # =============================================
    # action after selected team in the listwidget
    def __event_selected_team(self, index):
        # loading current team object
        self.set_current_team(self.get_teams()[index] if index != -1 else None)
        self.set_current_player(None)

    # action after selected player in the listwidget
    def __event_selected_player(self, index):
        # loading current player object
        players = self.get_players()
        if players is not None:
            self.set_current_player(players[index])

    # ========================
    # === EVENT OF BUTTONS ===
    # ========================
    # action after clicked on button ADDPLAYER
    def __event_bt_addplayer(self, checked):
        dialog = AddPlayerWindow(self)
        result = dialog.exec()
        if result:
            team = self.get_current_team()
            if dialog.get_lname() != "":
                player = model.getPlayerProvider().get_new(team.id, dialog.get_lname(), dialog.get_fname())
            else:
                player = model.getPlayerProvider().get_randomplayer(team.id)
            dao.getPlayer().insert(player)
            self.__refresh_tab1()
            self.set_current_team(team)

    # action after clicked on button DELETEPLAYER
    def __event_bt_deleteplayer(self, checked):
        if dao.getPlayer().delete(self.get_current_player()):
            self.set_current_player(None)

    # action after clicked on button ADDTEAM
    def __event_bt_addteam(self, checked):
        message = 'please can you input the name of the team?'
        text, yespressed = QInputDialog.getText(None, "Add team", message, QLineEdit.Normal, "")
        if yespressed and text is not None:
            o = model.getTeamProvider().get_new(self.get_competition().id, text)
            dao.getTeam().insert(o)
            self.__refresh_tab1()
            self.set_current_team(o)

    # action after clicked on button DELETETEAM
    def __event_bt_deleteteam(self, checked):
        if dao.getTeam().delete(self.get_current_team()):
            self.__refresh_tab1()

    # action after clicked on button GOALS
    def __event_bt_after_goals(self):
        match = self.get_current_match()
        oteamdom = dao.getTeam().getById(match.idteam_home)
        playersdom = dao.getPlayer().getByTeam(oteamdom)
        oteamvis = dao.getTeam().getById(match.idteam_outside)
        playersext = dao.getPlayer().getByTeam(oteamvis)

        dialog = GoalWindow(self, oteamdom, playersdom, oteamvis, playersext)
        btpressed = dialog.exec()
        if btpressed:
            oteam, oscorer, oass = dialog.get_datas()
            but = model.getGoalsProvider().get_new(oscorer.id if oscorer is not None else None,
                                                   match.id,
                                                   oteam.id,
                                                   oass.id if oass is not None else None)
            dao.getGoals().insert(but)
            self.__update_view_after_goals(oteam, oscorer, oass)

    # action after clicked on button SAVE MATCH
    def __event_bt_after_save_match(self):
        match = self.get_current_match()
        match.isplayed = True
        dao.getMatch().update(match)
        nextmatch = dao.getMatch().getNextMatch(self.get_competition())
        self.set_current_match(nextmatch)

    # =========================
    # === EVENT MENU / FILE ===
    # =========================
    # generate event for open action
    def __menu_open_competitions(self):
        competitions = dao.getCompetition().getAll()
        if competitions is not None:
            for competition in competitions:
                name = competition.name
                idenreg = competition.id
                obj = QAction(name, self)
                obj.triggered.connect(lambda chk, item=idenreg: self.__event_load_competition(item))
                self.menuOpen.addAction(obj)

    # action after selected competition in open menu
    def __event_load_competition(self, p_index):
        # loading existing competition
        compet = dao.getCompetition().getById(p_index)
        self.set_competition(compet)
        if dao.getMatch().getAll(self.get_competition()) is not None:
            print('la competition a déjà commencé')
            self.set_competition_begin(True)

    # action after selected new standard competition in new menu
    def __event_create_competition(self):
        # create competition with user's name
        name, bt = QInputDialog.getText(None, 'New competition', "Enter your competition's name:", text='choose')
        if bt:
            c = model.getCompetitionProvider().get_standard_competition(name)
            dao.getCompetition().insert(c)
            self.set_competition(c)

    # action after selected start competition in the menu
    def __start_competition(self):
        calendar = service.getCalendar(self.get_teams(), self.get_competition().tworound)
        for i, team in enumerate(calendar):
            match = model.getMatchProvider().get_new(team[0].id, team[1].id, comment='match number {}'.format(i + 1))
            dao.getMatch().insert(match)
        self.set_competition_begin(True)


class Classement(object):
    def __init__(self, lteams):
        self.teams = {}  # team = (win, null, lose, BP, BC)
        self.pts_win = 3
        self.pts_null = 1
        self.pts_lose = 0
        for team in lteams:
            self.teams[team] = [0, 0, 0, 0, 0]

    def get_result(self):
        result = []
        for key, values in self.teams.items():
            pts = values[0] * self.pts_win + values[1] * self.pts_null + values[2] * self.pts_lose
            played = values[0] + values[1] + values[2]
            diff = values[3] - values[4]
            result.append([key.name, pts, values[0], values[1], values[2], played, diff, values[3], values[4]])
        return sorted(result, key=itemgetter(1, 3, 4), reverse=True)

    def add_score(self, oteam1, score1, score2, oteam2):
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
