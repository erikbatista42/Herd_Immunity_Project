import random


class Person(object):
    '''
    Person objects will populate the simulation.
    _____Attributes______:

    ** _id: Int.  A unique ID assigned to each person.

    ** is_vaccinated: Bool.  Determines whether the person object is vaccinated against
        the disease in the simulation.

    ** is_alive: Bool. All person objects begin alive (value set to true). *Changed
        to false if person object dies from an infection.
    infection:  None/Virus object.  Set to None for people that are not infected.
    '''

    def __init__(self, _id, is_vaccinated, infected=None):
        # TODO:  Finish this method.  Follow the instructions in the class documentation
        # to set the corret values for the following attributes.

        # - self.alive should be automatically set to true during instantiation.
        # - all other attributes for self should be set to their corresponding parameter passed during instantiation.

        # - If person is chosen to be infected for first round of simulation, then the object should create a Virus object and set it as the value for self.infection.  Otherwise, self.infection should be set to None.
        # ^ ...What??

        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = None
        self.mortality_rate = 0

    def did_survive_infection(self):
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # for resolve_infection.  If person dies, set is_alive to False and return False.
        if self._id and self.is_alive == False:
            return False
        # If person lives, set is_vaccinated = True, infected = None, return True.
        elif self.is_alive == True:
            self.is_vaccinated = True
            self.infected = None
            print("{0} lives and is vaccinated".format(self._id))
            return True
        # - Only called if infection attribute is not None.
        # - Takes no inputs.
        # - Generates a random number between 0 and 1.
        # - Compares random number to mortality_rate attribute stored in person's infection attribute.
        # - If random number is smaller, person has died from disease. is_alive is changed to false.
        # - If random number is larger, person has survived disease.  Person's is_vaccinated attribute is changed to True, and set self.infected to None.
        print("running")
        if self.infected != None:
            random_Number = random.uniform(0, 1)
            print(123)
            if random_Number < mortality_rate:
                self.is_alive = False
                print("Person is dead")
            elif self.random_Number > self.mortality_rate:
                self.is_alive = True
                self.is_vaccinated = true
                self.infected = None
        # pass


erik = Person("erik", True)
erik.did_survive_infection()
