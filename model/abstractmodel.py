class AbstractModel(object):
    def __init__(self, parent):
        self.__id = None
        self.__idcompetition = None
        self.__parent = parent.__class__.__name__

    def __str__(self):
        return 'ID:{} - Class:{}'.format(self.__id, self.__parent)

    def __hash__(self):
        return hash('{}{}'.format(self.__id, self.__parent))

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if self.__id is None:
            self.__id = value
