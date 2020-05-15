import sys


class DAOException(Exception):
    def __init__(self, parent, error):
        print(sys.exc_info()[0])
        print('Parent Error : {}'.format(parent))
        print("ERROR {}:".format(error.args[0]))
        raise error
