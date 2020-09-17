import csv
import matplotlib
import agentframework
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
            
        environment.append(rowlist)
       
#print(environment)

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
        

