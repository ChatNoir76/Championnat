import sqlite3


class Singleton(object):
    instance = None

    class __Singleton:
        def __init__(self):
            self.__bddname = "test8.db"
            self.__conn = sqlite3.connect(self.__bddname)

        def get_instance(self):
            return self.__conn

        def __del__(self):
            print('Close DAO connection')
            self.__conn.close()

    def __new__(cls):  # _new_ est toujours une méthode de classe
        if not Singleton.instance:
            print('Open DAO connection')
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

    def __setattr__(self, attr, val):
        return setattr(self.instance, attr, val)
