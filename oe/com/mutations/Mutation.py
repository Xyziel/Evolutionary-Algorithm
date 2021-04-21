from abc import ABC, abstractmethod

from oe.com.models import Population


class Mutation(ABC):

    def __init__(self, mutate_probability: float):
        self.mutate_probability = mutate_probability

    @abstractmethod
    def mutate(self, population: Population, beginning: float = None, end: float = None):
        pass

