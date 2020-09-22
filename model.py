# importing of all elements and functions required to run rest of code
import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib
import sys


# Open the in.txt file with the CSV data so that it can be used by the Agents

with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
            
        environment.append(rowlist)
# changed values of elements below to numbers contained in the argv list
num_of_agents = sys.argv[1]
num_of_iterations = sys.argv[2]
neighbourhood = sys.argv[3]
agents = []
print("the number of agents is", num_of_agents)
print("the number of iterations is", num_of_iterations)
print("the number of neighbourhood is", neighbourhood)


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move the agents.
for j in range(num_of_iterations):
    # shuffling agents for each iteration to remove issue associated by 
    # artifacts
    random.shuffle(agents)
    for i in range(num_of_agents):
       agents[i].move()
       agents[i].eat()
       agents[i].share_with_neighbours(neighbourhood)

# this section writes the resulting area of the environment to a plot and 
# displays the agent locartions and the areas they have influenced
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# this section writes the data to a .txt file each time the process is run
with open ('out.txt', 'w') as f:
    f.write(str(environment))
    for row in environment:
        for value in row:
            f.write(str(value) + ", ")
        f.write("\n")