import datetime
from Module.Generate import Generate

class Code_Core():

    def __init__(self):
        try:
            self.Generate = Generate()
        except Exception as Errr:
            raise Errr
        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')