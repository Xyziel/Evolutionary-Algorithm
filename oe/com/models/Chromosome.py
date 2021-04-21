import random


class Chromosome:

    def __init__(self, *args):
        if len(args) == 2:
            beginning = args[0]
            end = args[1]
            self.__value = random.uniform(beginning, end)
        elif len(args) == 1:
            value = args[0]
            self.__value = value

    def get_value(self) -> float:
        return self.__value

    def set_value(self, value):
        self.__value = value


