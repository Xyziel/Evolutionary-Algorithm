from oe.com.models.Chromosome import Chromosome


class Population:

    def __init__(self):
        self.__population = []
        self.__size = 0
        self.__number_of_variables = 0

    def create_random_population(self, size: int, number_of_variables: int, beginning: float, end: float):
        self.__size = size
        self.__number_of_variables = number_of_variables
        self.__population = [[Chromosome(beginning, end) for _ in range(number_of_variables)] for _ in range(size)]

    def get_population(self) -> list:
        return self.__population

    def get_population_as_numbers(self) -> list:
        return [[self.__population[i][j].get_value() for j in range(self.__number_of_variables)]
                for i in range(self.__size)]

    def get_size(self) -> int:
        return self.__size

    def get_number_of_variables(self) -> int:
        return self.__number_of_variables

    def add_chromosomes(self, chromosomes: list):
        self.__population.append(chromosomes)
        self.__size += 1
        self.__number_of_variables = len(chromosomes)

    def __add__(self, another_population):
        for chromosomes in another_population.get_population():
            self.add_chromosomes(chromosomes)
        return self
