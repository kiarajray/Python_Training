# Peanut Butter Jelly Time!                  

print "This program will tell you how many PB&J Sandwiches you can make!\nAssume each sandwich has a ratio of 2:1:1 bread:peanut butter:jelly"
try:
    bread = int(raw_input("Enter number of bread slices"))    
    peanut_butter = int(raw_input("Enter number of peanut butter"))
    jelly = int(raw_input("Enter number of jelly"))

    missing_ingredient = ""
    type_of_sammie = ""
    num_of_sammie = ""
    plural = ""

    if jelly == 0:
        missing_ingredient = "jelly"
        type_of_sammie = "peanut butter"
        num_of_sammie = peanut_butter
    if peanut_butter == 0:
        missing_ingredient = "peanut butter"
        type_of_sammie = "jelly"
        num_of_sammie = "jelly"
    if bread == 0:
        missing_ingredient = "bread"
    if bread%2 == 1 or bread == 1:
        openfaced = raw_input("Do you want all openfaced sandwiches?")
    if bread > 3:
        plural = "es"

    if jelly == 0 and bread >= 2:
        print "You're missing {0}, you can make {1} {2} sandwich{3}".format(missing_ingredient,min(bread/2,num_of_sammie),type_of_sammie, plural)
    elif peanut_butter == 0 and bread >= 2:
        print "You're missing {0}, you can make {1} {2} sandwich{3}".format(missing_ingredient,min(bread/2,num_of_sammie),type_of_sammie, plural)
    elif bread == 0 and peanut_butter > 1:
        print "You're missing bread, No PB&J's for you!\nBut...you can eat peanut butter out of the jar"
    elif bread == 0 and peanut_butter == 0 and jelly > 1:
        print "You're missing bread AND peanut butter! I guess you could just eat jelly"
    print missing_ingredient, type_of_sammie

    if bread == 1 and peanut_butter > 1 and jelly == 0:
        print "You're missing jelly, you can make 1 openfaced peanut butter sandwich"
    if bread == 1 and jelly > 1 and peanut_butter == 0:
        print "You're missing peanut butter, you can make 1 openfaced jelly sandwich"
    
    if bread%2 == 1 and bread > 1:
        if openfaced == "yes" or openfaced == "YES" or openfaced == "Yes" or openfaced == "Y" or openfaced == "y":
            print "You can make {0} openfaced sandwiches. Enjoy".format(min(bread, peanut_butter, jelly))
        else:
            if bread%2 == 1 and peanut_butter >= 1 and jelly >= 1:
                print "You can make {0} sandwiches and {1} openfaced sandwiches. Enjoy".format(min(bread/2, peanut_butter, jelly), bread%2)   
    else:
        if bread >= 2 and peanut_butter >= 1 and jelly >= 1:
            print "You can make {0} sandwich{1}".format(min(bread/2, peanut_butter, jelly), plural)
    
except:
    print "Invaild input. Enter a whole number"
