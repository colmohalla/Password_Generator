'''
Problem Statement
Create a strong password generator which takes 4 inputs: letters, numbers, symbols,
num_of_passwords.
Each parameter is an integer. You must not have too many consecutive character
types in a row.
The resulting passwords must be printed as strings on separate lines.
'''
##################################################################################
### Helper Function ###
def split(password:list=[], num:int=1):
    '''
    function which splits a list into sublists depending on the num inputted.
    '''
    try:
        if type(num) != int or type(password) != list:
            return "Please input correct paramater type."
        elif num <= 0:
            return "Number must be at least 1."
        new_list = []
        length = len(password)
        for i in range(num): # for every item in our number range
            start = int(i*length/num) # find the start
            end = int((i+1)*length/num) # find the end
        new_list.append(password[start:end]) # slice the list and append to
                                            # our new list of lists
        return new_list
    except:
        return "Oops"

###################################################################################

### Password Generator ###
import random
def password_generator(letters:int=2, numbers:int=2, symbols:int=2,
        num_of_passwords:int=1 ) -> str:
    '''
    function that returns a randomized password based on inputs
    '''
    # put our characters in separate lists
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [] # new list
    try:
        # error handling
        if type(letters) != int or type(numbers) != int or type(symbols) != int or type(num_of_passwords) != int:
            return "Please input a number into the parameters."
        elif letters <= 0:
            return "Number must be at least 1."

        elif numbers <= 0:
            return "Number must be at least 1."

        elif symbols <= 0:
            return "Number must be at least 1."

        elif num_of_passwords <= 0:
            return "Number must be at least 1."

        else:
            for val in range(1, letters + 1): # loop through list
                password_list.append(random.choice(letters_list)) # append to password_list

            for val in range(1, symbols + 1):
                password_list += random.choice(symbols_list)

            for val in range(1, numbers + 1):
                password_list += random.choice(numbers_list)

            random.shuffle(password_list) # shuffle the list

            sub_lists = split(password_list, num_of_passwords) # use our split function to create our sublists
 
            strings = ('\n'.join(' '.join(i) for i in sub_lists)) # formats the string

            return strings
    except:
        return "Oops"
