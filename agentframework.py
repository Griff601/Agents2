import random

class Agent:
    def __init__(self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        for agent in agents:
            print(agent.x, agent.y)
    def move(self): 
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
    
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    def share_with_neighbours(self, neighbourhood):
        
        # Loop through the agents in self.agents .
        for agent in self.agents:
            if self == agent:
                # discounting self agent in loop
                continue
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(agent)
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Sum self.store and agent.store .
                sum = self.store + agent.store
                # Divide sum by two to calculate average.
                average = sum / 2
                # self.store = average
                self.store = average
                # agent.store = average
                agent.store = average
                print("sharing " + str(distance) + " " + str(average))
            
            # End if
        # End loop
                
    
    
    def distance_between(self, other_agent):
        return (((self.x - other_agent.x)**2) +
                ((self.y - other_agent.y)**2))**0.5

    @property
    def x(self):
        return self.__x
    @x.setter            
    def x(self, x):
        self.__x = x
        
    @property
    def y(self):
        return self.__y
    @y.setter            
    def y(self, y):
        self.__y = y
        
