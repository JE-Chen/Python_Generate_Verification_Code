import datetime

from Module.Generate import GenerateVerificationCode


class VerificationCodeCore:

    def __init__(self):
        try:
            self.GenerateVerificationCode = GenerateVerificationCode()
        except Exception as error:
            raise error
        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')
