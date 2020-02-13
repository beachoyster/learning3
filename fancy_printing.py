# the point of this lesson is to get comfortable with format characters for print
# Why do you care about this? when you write to databases, you format strings like this
# Why do you care about writing to databases? A lot of programs write and recall stuff from databases


my_name = 'Jimminy Bonks'
my_age = 53
my_height = 74 #inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))



#0. What data types are %d and %s for respectively?



#1. Change all the variables so there isn’t the my_ in front.
#    Make sure you change the name everywhere, not just where you used = to set them.



#2. Try more format characters. %r is a very useful one. It’s like saying “print this no matter what.”



#3. Search online for all the Python format characters.



#4. Try to write some variables that convert the inches and pounds to centimeters and kilos.
#   Do not just type in the measurements. Work out the math in Python.

