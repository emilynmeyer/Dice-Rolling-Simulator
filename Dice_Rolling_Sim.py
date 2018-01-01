#randomly choose a number between 1 and 6
#print that number
#ask user if they would like to role again

import random

high_roller = raw_input("How high would you like to roll?")
high_roller = int(high_roller)

x = 'y'
while x is 'y':
    print "Rolling the dice now!"
    print random.randint(1, high_roller)
    x = raw_input("Would you like to roll again? (y for yes)")

print "It was fun rolling with you! Come back soon :)"
