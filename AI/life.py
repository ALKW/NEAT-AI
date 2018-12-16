import neural_network as network
from game_environment import game
from game_environment import game_visual

#species determined by combination of traits; hidden_layer, hidden_width, and act_func
class Life:
    def __init__(self):
        #Array of all networks regardless of species
        self.individuals = []

        #list of lists. each list has a specific species
        self.species_list = []

    def feed_life(self):
        #Runs all networks through the 
        pass
    
    def classify_life(self):
        #goes through all elements in the list. If it does not have a species classify it and assign it to the appropriate list
        pass
    

#Have max heaps (species) of 20 individuals max. At each stage:
#   Delete 4 lowest performers. : -4 
#   Mate top 4 perfomers. : +6
#   Mutate Next top 4: +4

all_life = Life()
all_life.individuals = network.create_init_population_species(20)

test_network = network.create_random()
test_network.print_traits()