import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib



with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
            
        environment.append(rowlist)


num_of_agents = 10
num_of_iterations = 100
agents = []
neighbourhood = 20

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move the agents.
for j in range(num_of_iterations):
    # shuffling agents for each iteration
    random.shuffle(agents)
    for i in range(num_of_agents):
       agents[i].move()
       agents[i].eat()
       agents[i].share_with_neighbours(neighbourhood)

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

with open ('out.txt', 'w') as f:
    f.write(str(environment))
    for row in environment:
        for value in row:
            f.write(str(value) + ", ")
        f.write("\n")