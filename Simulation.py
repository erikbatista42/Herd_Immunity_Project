import random
import sys
random.seed(42)
from person import *
from logger import *


class Simulation(object):

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)

        # TODO: Create a Logger object and bind it to self.logger.  You should use this
        # logger object to log all events of any importance during the simulation.  Don't forget
        # to call these logger methods in the corresponding parts of the simulation!
        self.logger = Logger(self.file_name)

        # This attribute will be used to keep track of all the people that catch
        # the infection during a given time step. We'll store each newly infected
        # person's .ID attribute in here.  At the end of each time step, we'll call
        # self._infect_newly_infected() and then reset .newly_infected back to an empty
        # list.

        self.newly_infected = []
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.

    def _create_population(self, initial_infected):
        infectedPeople = []
        vaccinatedPeople = []
        unvaccinatedPeople = []
        restOfThePopulation = self.population_size - initial_infected
        randomNum = random.uniform(0, 1)

        for infectedPerson in range(0, initial_infected):
            infectedPerson = Person(self.next_person_id, False, virus_name)
            infectedPeople.append(infectedPerson)
            self.population.append(infectedPerson)
            self.next_person_id += 1
        for person in range(0, restOfThePopulation):
            if randomNum < vacc_percentage:
                # person is vaccinated
                person = Person(self.next_person_id, True, None)
                vaccinatedPeople.append(person)
                self.population.append(person)
                self.next_person_id += 1
            elif randomNum > vacc_percentage:
                # person is not vaccinated
                person = Person(self.next_person_id, False, None)
                unvaccinatedPeople.append(person)
                self.population.append(person)
                self.next_person_id += 1
        return(len(self.population))

    def _simulation_should_continue(self):
        deadPeople = []
        continueSimulation = True
        for person in self.population:
            if person.is_alive == False:
                deadPeople.append(person)

        if len(deadPeople) == self.population_size:  # the entire pop. is dead
            continueSimulation = False
        elif self.current_infected == 0:  # no infected people left
            continueSimulation = False
        else:  # otherwise continue simulation
            continueSimulation = True

    def run(self):
        # TODO: Finish this method.  This method should run the simulation until
        # everyone in the simulation is dead, or the disease no longer exists in the
        # population. To simplify the logic here, we will use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # This method should keep track of the number of time steps that
        # have passed using the time_step_counter variable.  Make sure you remember to
        # the logger's log_time_step() method at the end of each time step, pass in the
        # time_step_counter variable!
        time_step_counter = 0
        # TODO: Remember to set this variable to an intial call of
        # self._simulation_should_continue()!
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)
            should_continue = self._simulation_should_continue()
        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self):
        # TODO: Finish this method!  This method should contain all the basic logic
        # for computing one time step in the simulation.  This includes:
            # - For each infected person in the population:
            #        - Repeat for 100 total interactions:
            #             - Grab a random person from the population.
            #           - If the person is dead, continue and grab another new
            #                 person from the population. Since we don't interact
            #                 with dead people, this does not count as an interaction.
            #           - Else:
            #               - Call simulation.interaction(person, random_person)
            #               - Increment interaction counter by 1.
        pass

    def interaction(self, person, random_person):
        # TODO: Finish this method! This method should be called any time two living
        # people are selected for an interaction.  That means that only living people
        # should be passed into this method.  Assert statements are included to make sure
        # that this doesn't happen.
        assert person1.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated == True:
            # random person is vaccinated
            self.logger.log_interaction(person, random_person, False, True, False)
            pass
        elif random_person.infection != None:
            # random person is already infected
            self.logger.log_interaction(person, random_person, False, False, True)
            pass
        elif (random_person.is_vaccinated == False) and (random_person.infection == None):
            # random person is not vaccinated, but is healthy then gets infected by person
            randomNum = random.uniform(0, 1)
            if randomNum < self.basic_repro_num:
                self.newly_infected.append(random_person._id)
                random_person.infection = self.virus_name
            self.logger.log_interaction(person, random_person, True, False, False)
        else:
            # no interaction
            self.logger.log_interaction(person, random_person, None, random_person.is_vaccinated,
                                        random_person.infection)

    def _infect_newly_infected(self):
        for infectedId in self.newly_infected:
            for person in self.population:
                if infectedId == person._id:
                    person.infection = self.virus_name
                    self.current_infected += 1
                    self.total_infected += 1
        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    print(simulation._create_population(initial_infected))
    simulation.run()
