

# template for calling functions in another file
def print_function():
    print("I'm in another file :)")

###################################################################################
### Exercise 1 ###
def firsts(s:str):
    '''
    Function that removes any duplication of characters in s
    '''

    display = [] # empty list
    s = str(s)
    if type(s) == str:
        for i in s: # for every element in s
            if i not in display: # if i is not already in display,
                display.append(i) # append it. This results in no duplication
        return "".join (display) # cast to string

##################################################################################
### Exercise 2 ###
def F(s1, s2):
    try:
        r = [] # empty list assigned to variable r
        i = 0 # counter
        while i < len(s1):
            j = 0
            while j < len(s2):
                if s1[i] == s2[j]: # if both elements are the same
                    r += [s1[i]] # add to empty list
                    break
                j += 1
            i += 1
        return r
    except:
        return "Oops"

###################################################################################
### Exercise 3 ###
def iter_factorial( n:int ):
    '''
    Function that gives the factorial of a given integer
    iter_factorial(0) will return 1
    '''

    if type(n) != int:
        return "Oops"
    else:
        count = 1 # start at 1
        for i in range(1, n+1): # for each element in the range between 1 and n+1
            count *= i # multiply the count by i and store it

        return count

###################################################################################
#
### Exercise 4 ###
def removeVowels(sentence:str):
    '''
    Function that removes vowels from a string
    '''
    try:
        vowels = "aeiou"
        filtered_list = [] # empty list
        i = 0 # counter
        if type(sentence) != str:
            return "Oops"
        else:
            while i < len(sentence)-1: # while i is less than the length of the sentence -1
                if sentence[i] not in vowels: # if it is not in vowels
                    filtered_list.append(sentence[i]) # append it to our empty list
                i += 1
            return "".join (filtered_list) # cast it back to a string
    except:
        return "Oops"

###################################################################################
##
### Exercise 5 ###

def hailstone(n:int):
    '''
    Function that generates the hailstone sequence of a
    given positive number n and returns the sequence as a list
    '''
    try:
        filtered_list = [] # empty string
        if type(n) != int:
            return "Oops"
        else:
            while n > 1: # number must be greater than 1
                filtered_list.append(n) # append number to empty list
                if n % 2 == 0: # if the number is divisible by 2 w/o a remainder
                    n = (n//2) # divide by 2
                else:
                    n = (n*3+1) # else, we multiply by 3, + 1
            filtered_list.append(n) # append the number to our empty list
            return filtered_list
    except:
        return "Oops"
###################################################################################
###
### Exercise 6 ###

def chooseLargest(a, b):
    '''
    Function that returns the largest of a and b
    '''
    try:
        results = [] # empty list
        i = 0 # counter
        while i < len(a):
            results.append(max(a[i], b[i])) # append the greater of the two to our results list
            i += 1
        return results
    except:
        return "Oops"
###################################################################################
###
### Exercise 7 ###
def loop_the_loop(a1, a2):
    try:
        new_loop = [] # empty list
        i = 0 # counter
        while i < len(a1):
            j = 0
            while j < len(a2):
                new_loop.append(a1[i]+ a2[j]) # append added elements to new_loop
                j += 1
            i += 1
        return new_loop
    except:
        return "Oops"

###################################################################################
