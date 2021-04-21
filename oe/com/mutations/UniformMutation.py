import random

from oe.com.models import Population
from oe.com.mutations.Mutation import Mutation


class UniformMutation(Mutation):

    def mutate(self, population: Population, beginning: float, end: float):
        for chromosomes in population.get_population():
            if random.uniform(0, 1) <= self.mutate_probability:
                index = random.randint(0, population.get_number_of_variables() - 1)
                value = random.uniform(beginning, end)
                chromosomes[index].set_value(value)
