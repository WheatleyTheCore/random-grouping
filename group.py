import csv
import random


allPeople = []
groupA = []
groupB = []

def printGroup(group):
    if (group == groupA):
        print('------------Group A----------')
    if (group == groupB):
        print("------------Group B----------")


    for name in group:
        print(name)

#put everyone in people.csv into an array
with open('people.csv', 'r') as file:
    reader = csv.reader(file)

    for name in reader:
        allPeople.append(name)

#shuffle the peeps
random.shuffle(allPeople)

#split people into groups
for i, name in enumerate(allPeople):
    if (i % 2 == 0):
        groupA.append(name)
    else:
        groupB.append(name)

#print to console
printGroup(groupA)
printGroup(groupB)


#write to file
f = open("groups.text", "w")
f.write("------------Group A-------------\n")
for name in groupA:
    f.write(name[0] + '\n')
f.write('------------Group B-------------\n')
for name in groupB:
    f.write(name[0] + '\n')
f.close()
