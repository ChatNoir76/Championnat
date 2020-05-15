from PyQt5.QtWidgets import QDialog
from view.ui.Ui_goal import Ui_Dialog_goal


class GoalWindow(QDialog, Ui_Dialog_goal):

    C_NONE = 'NONE'
    C_OWNGOAL = 'OWN GOALS'

    def __init__(self, parent, team_dom, players_dom, team_vis, players_ext):
        super(GoalWindow, self).__init__(parent)
        self.setupUi(self)
        self.__datas = []
        self.__datas.append((team_dom, players_dom))
        self.__datas.append((team_vis, players_ext))
        self.__team = None
        self.__scorer = None
        self.__assistance = None
        # event
        self.comboBox_team.currentIndexChanged.connect(self.__event_team_selected)
        self.comboBox_goalscorer.currentIndexChanged.connect(self.__event_scorer_selected)
        self.comboBox_assistance.currentTextChanged.connect(self.__event_assistance_changed)
        self.__initialize_combobox_team()

    def __initialize_combobox_team(self):
        for team, players in self.__datas:
            self.comboBox_team.addItem(team.name)

    def __event_assistance_changed(self, text):
        iteam = self.comboBox_team.currentIndex()
        players = self.__datas[iteam][1]
        self.__assistance = None
        for player in players:
            if player.description == text:
                self.__assistance = player

    def __event_scorer_selected(self, index):
        self.comboBox_assistance.clear()
        iteam = self.comboBox_team.currentIndex()
        players = self.__datas[iteam][1]
        if index < len(players):
            for i, player in enumerate(players):
                if index != i:
                    self.comboBox_assistance.addItem(player.description)
                else:
                    self.__scorer = player
            self.comboBox_assistance.addItem(self.C_NONE)
            self.comboBox_assistance.setEnabled(True)
        else:
            self.comboBox_assistance.setEnabled(False)
            self.__scorer = None
            self.__assistance = None

    def __event_team_selected(self, index):
        self.comboBox_goalscorer.clear()
        self.__team = self.__datas[index][0]
        if index > -1:
            for player in self.__datas[index][1]:
                self.comboBox_goalscorer.addItem(player.description)
        self.comboBox_goalscorer.addItem(self.C_OWNGOAL)

    def get_datas(self):
        return tuple((self.__team, self.__scorer, self.__assistance))
