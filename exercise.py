import random

generations = 0
parents, babies = (20, 10)
while babies < 100 and (parents + babies) > 0:
    generations += 1
    # add a generation to the generation counter
    birthrate = random.randint(0,3)
    eatrate = random.randint(0,3)
    newbirths = parents*birthrate
    parentseaten = babies*eatrate
    print('{0} new babies were born'.format(newbirths))
    print('{0} parents were eaten'.format(parentseaten))
    parents, babies = (parents - parentseaten, babies+newbirths)
    print('**** there are {0} parents and {1} babies'.format(parents, babies))

if (parents + babies) < 0:
    print("babies ate all the parents")
else:
    print("more than a 100 parents and babies!")

print("{0} generations elapsed".format(generations))

# 1) add a note like in line 7 above each line of code to describe what it is doing
