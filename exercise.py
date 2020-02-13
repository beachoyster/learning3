import random

print("i could have code like this")
print("this will run")

parents, babies = (50, 10)
while babies < 100 and (parents + babies) > 0:
    birthrate = random.randint(0,3)
    eatrate = random.randint(0,5)
    newbirths = parents*birthrate
    print('{0} new babies were born'.format(newbirths))
    print('{0} parents were eaten'.format(eatrate))
    parentseaten = babies*eatrate
    parents, babies = (parents - parentseaten, babies+newbirths)
    print('**** there are {0} parents and {1} babies'.format(parents, babies))

if (parents + babies) < 0:
    print("babies ate all the parents")
else
    print("more than a 100 parents and babies!")



