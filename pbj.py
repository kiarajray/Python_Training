# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
print "First Goal"
bread = int(raw_input("Enter number of bread slices"))
peanut_butter = int(raw_input("Enter number of peanut butter"))
jelly = int(raw_input("Enter number of jelly"))
if bread > 2 and peanut_butter > 1 and jelly > 1:
    print "You can make a sandwich"
else:
    print "No sandwich for you"
# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make
print "Second Goal"
bread = 400
peanut_butter = 100
jelly = 250
if bread >= 2 and peanut_butter >= 1 and jelly >= 1:
    print "You can make {0} sandwichs".format(min(bread/2, peanut_butter, jelly))
else:
    print "No sandwich for you"


# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )
print "Third Goal"
bread = 409
peanut_butter = 100
jelly = 250
if bread%2 == 1:
    openfaced = raw_input("Do you want all openfaced sandwiches?")
    if openfaced == "yes" or openfaced == "YES" or openfaced == "Yes":
            print "You can make {0} openfaced sandwiches".format(min(bread, peanut_butter, jelly))
    else:
        if bread%2 == 1 and peanut_butter >= 1 and jelly >= 1:
            print "You can make {0} sandwiches and {1} openfaced sandwiches".format(min(bread/2, peanut_butter, jelly), bread%2)   
        else:
            print "No sandwich for you"
else:
    if bread >= 2 and peanut_butter >= 1 and jelly >= 1:
            print "You can make {0} sandwiches".format(min(bread/2, peanut_butter, jelly))
    else:
        print "No sandwich for you"
                    
    
# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches
# To satisfy the fourth goal:
# Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly,
# print a message that tells you that you can make a peanut butter sandwich
# Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches
# and a certain number of peanut butter sandwiches
print "Fourth Goal"
bread = int(raw_input("Enter number of bread slices"))
peanut_butter = int(raw_input("Enter amount of peanut butter"))
jelly = int(raw_input("Enter amount of jelly"))

if jelly == 0 or bread == 0 or peanut_butter == 0:
    print "You're missing ingredients"
if jelly == 0:
    print "You're missing jelly"
elif peanut_butter == 0:
    print "You're missing peanut butter"
elif bread == 0:
    print "You're missing bread"
print "You have to make {0} peanut butter sandwiches".format(min(bread/2, peanut_butter))
full_sandwich = min(bread/2, peanut_butter, jelly)
if bread >= 2 and peanut_butter >= 1 and jelly >= 1:
    print "You can make {0} sandwiches and {1} peanut butter sandwiches".format(full_sandwich,min((peanut_butter-jelly),(bread/2 - full_sandwich)))
    


# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich
#but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.
print "Fifth Goal"
bread = int(raw_input("Enter number of bread slices"))
peanut_butter = int(raw_input("Enter amount of peanut butter"))
jelly = int(raw_input("Enter amount of jelly"))

if bread/2 > 0 and peanut_butter > 0 and jelly == 0:
    print "You can make a peanut butter sandwich but you should take a hard, honest look at your life.\nWow, your program is kinda judgy"
else:
    print "You can make pb&j sandwiches, so maybe your life is together"

# What are the step-by-steps to recreate this?
# First, you need variables to store your information.  Remember, variables are just containers for your information that you give a name.

# You need three ingredients to make a PB&J, so you'll want three different variables:
# 		How much bread do you have? (make this a number that reflects how many slices of bread you have)
#		How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)

# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)

# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients

# Based on the results of that conditional, display a message.

# To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"

# To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before

# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py

# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches

# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.
