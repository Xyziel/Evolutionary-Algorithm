import random

from oe.com.models import Population, Chromosome
from oe.com.selections.Selection import Selection


class TournamentSelection(Selection):

    def __init__(self, k: int):
        self.__number_of_groups = k

    def select_parents(self, population: Population, values: list, maximum: bool) -> Population:
        # winners of the tournament
        selected_parents = Population()
        population_size = population.get_size()
        # indexes that will be chosen to certain groups
        indexes = [i for i in range(population_size)]
        group_sizes = [population_size // self.__number_of_groups for _ in range(self.__number_of_groups)]

        # if there is not perfect division some groups need to be bigger
        if population_size % self.__number_of_groups != 0:
            remainder = population_size % self.__number_of_groups
            i = 0
            while remainder > 0:
                group_sizes[i] += 1
                remainder -= 1
                i += 1

        chromosomes = []
        for i in range(self.__number_of_groups):
            best_index = random.choice(indexes)
            # print("BEST:")
            # print(best_index)
            indexes.remove(best_index)
            for j in range(group_sizes[i] - 1):
                index = random.choice(indexes)
                # print("index:")
                # print(index)
                if maximum:
                    if values[best_index] < values[index]:
                        best_index = index
                else:
                    if values[best_index] > values[index]:
                        best_index = index
                indexes.remove(index)
                # print("indexes:")
                # print(indexes)
                chromosomes = population.get_population()[best_index]
            selected_parents.add_chromosomes(chromosomes)

        return selected_parents
