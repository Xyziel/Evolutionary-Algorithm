import random

from oe.com.crossovers.Crossover import Crossover
from oe.com.models import Population, Chromosome


class HeuristicCrossover(Crossover):

    def cross(self, parents: Population, new_gen_size: int) -> Population:
        new_gen = Population()
        while new_gen.get_size() < new_gen_size:
            if random.uniform(0, 1) <= self.cross_probability:
                k = 0
                # loop while is needed so k will not be 0 - random() returns [0.0, 1.0)
                while k == 0:
                    k = random.random()

                tmp_parents = parents.get_population_as_numbers().copy()
                # print(tmp_parents)
                parent1 = random.choice(tmp_parents)
                # remove parent1 from the list so it cannot be chosen
                tmp_parents.remove(parent1)
                parent2 = random.choice(tmp_parents)

                i = 0
                while (parent1[0] > parent2[0]) or (parent1[1] > parent2[1]):
                    i += 1
                    if i > 20:
                        return Population()
                    tmp_parents = parents.get_population_as_numbers().copy()
                    parent1 = random.choice(tmp_parents)
                    # remove parent1 from the list so it cannot be chosen
                    tmp_parents.remove(parent1)
                    parent2 = random.choice(tmp_parents)

                child1 = [k * (parent2[j] - parent1[j]) + parent1[j] for j in range(parents.get_number_of_variables())]
                child = [Chromosome(child1[i]) for i in range(parents.get_number_of_variables())]
                new_gen.add_chromosomes(child)

        return new_gen