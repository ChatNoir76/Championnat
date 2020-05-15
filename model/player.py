from model.abstractmodel import AbstractModel


class Player(AbstractModel):
    def __init__(self, id_team, lname, fname, birthdate=None, comment=None):
        super().__init__(self)
        self.__idteam = id_team
        self.__lname = lname
        self.__fname = fname
        self.__bdate = birthdate
        self.__comment = comment

    @property
    def idteam(self):
        return self.__idteam

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, value):
        self.__lname = value

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, value):
        self.__fname = value

    @property
    def birthdate(self):
        return self.__bdate

    @birthdate.setter
    def birthdate(self, value):
        self.__bdate = value

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value

    @property
    def description(self):
        return '{} {}'.format(self.__fname, self.__lname)
