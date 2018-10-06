import random
from simulation import *


class Person():

    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = None

    def did_survive_infection(self):
        randomNum = 0
        if self.infection != None:
            randomNum = random.uniform(0, 1)
            if randomNum < Simulation.mortality_rate:
                self.is_alive = False
                return False
            elif randomNum > Simulation.mortality_rate:
                self.is_vaccinated = True
                self.infection = None
                return True
