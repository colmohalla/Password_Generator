import random

def print_function():
    print("I'm in another file :)")

###################################################################################
############################
def ships(numShip:int=2)-> list:
    '''
    function that randomly returns between 1 and 5 ships from a list
    assumption - numShip will be inputted as an integer
    '''
    try:
        ships = ["Enterprise", "Galactica", "Rocinante", "Serenity", "Razorcrest"] # make a list of our ships


        if numShip < 1 or numShip > 5: # otherwise out of range
            return "Only 1 to 5 ships available"
        elif numShip == 2:
            return random.sample(ships, 2) # returning random ships depending on number inputted

        elif numShip == 3:
            return random.sample(ships, 3)

        elif numShip == 4:
            return random.sample(ships, 4)

        else:
            return ships
    except:
        return "Oops"
###################################################################################
##########################

def crews(ships:int=2,crew:list=["captain","first-mate", "mechanic" ])->list:
    '''
    function that will assign a crew to a number of ships
    assumption - a number of ships will be inputted and then a crew will be
    assigned to each
    '''
    names = ["Albert Fish","Jim Jones","Jeffrey Dahmer", "Jack the Ripper", "Ed Gein","Kurt Cobain","Layne Staley", "Dave Grohl", "Chris Cornell", "Eddie Vedder",
    "Tony Stark", "Steve Rogers", "Peter Parker", "Stephen Strange", "Bruce Banner", "Arthur Fleck", "Harley Quinn", "Christopher Smith", "Rick Sanchez",
    "Philip Glass", "Geralt Riviera ", "Piper Stephens", "Sven", "Johnny OnionRings", "Dennis Reynolds", "Jimmy McCarthy", "Rick O'Connell", "Edward Nigma" ]
    try:
        crew_list = [] # first empty list
        for ship in range(0, ships): # for every ship
            sub_list = [] # second empty list
            crew_members = len(crew) # so that we can cycle through the members list
            for member in range(crew_members): #for every member in our crew

                sub_list.append(random.choice(names)) # we append a random choice to the second list from our list of names

                crew_list.append(sub_list) # then we append this list to our outer empty list.
            return crew_list
    except:
        return "Oops"
###################################################################################
###########################################
def destinations(ships:int)->list:
    '''
    function that will randomly assign destinations based on number of ships
    inputted
    assumption - number of ships will be inputted
    '''
    destinations = ["Mars", "Venus", "Jupiter", "Tatooine", "Saturn", "Pluto",
    "Uranus", "Tubbercurry","Mercury", "Jakku", "Krypton", "Coruscant","Discworld",
    "Hoth", "Vulcan", "Naboo", "Mystara", "Mongo", "Gor", "Daxam","Battleworld", "Arrakis", "Alderaan", "Arcadia", "Bardakia", "Caliban", "Cerebrus",
    "Ebola 9","Erabus Prime", "Ergo", "Fantasy Planet", "Felucia","Frontius", "Labura", "Pallas", "Pirri", "Omicron Persei 8"]
    try:
        destination_list = [] # empty list
        for ship in range(0, ships): # for each ship given
            destination_list.append(random.choice(destinations)) # append random destination to list
        return destination_list
    except:
        return "Oops"
###################################################################################
###########################################
def recur_func(num:int=5)->str:
    '''
    recursive function which counts from num to 1. Default value 5
    assumption - will return a string of 5,4,3,2,1 to be used in countDown()
    '''
    try:
        print(num, end=" ") # to make sure everything is printed on one line we use end=
        if num > 1: # if the number is greater than 1
            return str(recur_func(num - 1)) # call our function, num-1
    except:
        return "Oops"
###################################################################################
###########################################
def countDown(ships:list,destinations:list=[])-> str:
    '''
    function which will count down each ship to its destination
    assumption1 - output will be a string
    assumption2 - both parameters will be inputted as lists
    '''
    ret_string = "" # empty string
    try:
        for index in range(len(ships)): # get the index of all the items in the ships list
            index == destinations[index] # so that the ships and destinations lists correspond

            if index+1 % 3 == 1: # use the modulus to determine which index is which
                loop = "for loop"
                # for val in range(0,5,-1):
                string = "5, 4, 3, 2, 1 - " + str(ships[index]) + " has blasted off to " + str(destinations[index]) + " using a " + loop + "\n"
                ret_string += string
            if index+1 % 3 == 2:
                loop = "while loop"
                # count = 5
                # while count > 0:
                string = "5, 4, 3, 2, 1 - " + str(ships[index]) + " has blasted off to " + str(destinations[index]) + " using a " + loop + "\n"
                ret_string += string
 

            if index+1 % 3 == 0:
                loop = "recursion"
                string = recur_func() + str(ships[index]) + "has blasted to" + str(destinations[index]) + "using" + loop + "\n" # call our recur_func()
                ret_string += string

        return ret_string
    except:
        return "Oops"

###################################################################################
###########################################
def printout(ships:list, crews:list, destinations:list, format:str="capatalise")->str:
    '''
    function will print out the ships, their crews and destinations in a special
    format assumption - all parameters, except "format", will be inputted as lists,
    outputted as strings
    '''
    try:
        ret_string = ""                             # empty list
        for ship in ships:                          # for every ship
            member = crews.pop()                    # remove items and return them
            destination = destinations.pop()        # also for destinations
            string = str(ship) + " has a crew of " +str(member) + " and is on route to " + str(destination) + "\n" # create our string

            ret_string += string                    # add to our empty string
        if format == "capatalise":                  # take care of the formatting
            ret_string = ret_string.capitalize()

        elif format == "upper":
            ret_string = ret_string.upper()
        elif format == "lower":
            ret_string = ret_string.lower()
        return ret_string
    except:
        return "Oops"
###################################################################################
###########################################
def toInfinityAndBeyond():
    '''
    '''
    # an example of how I could call the helper functions is shown below
    # variables for ships, crews and destinations
    my_ships = []
    my_crews = []
    my_destinations = []
    my_numShips = 3
 # save 3 ships
    my_ships = ships(my_numShips) # this would result in 3 of the ships randomly selected
    
 # save 1 crew members for each ship
    my_crews = crews(my_ships, ["captain"]) # of the crew, the captains from each would be selected

 # save 1 destination for each ship
    my_destinations = destinations(my_ships)

 # each of the ships needs to blast off, so lets count them down
    print(countDown(ships, my_destinations))

 # produce a string we can return
    return printout(my_ships, my_crews, my_destinations, "lower")