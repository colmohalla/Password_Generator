
# template for calling functions in another file
def print_function():
    print("I'm in another file :)")


def to_english(n:int)->str:
    ''''
    function that takes in an integer and returns the english word of said integer
    assumption: numbers will range from -999 to 999
    '''
    to_nineteen = ["zero", "one ", "two ", "three ", "four ","five ", "six ",
    "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
    "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen "]
    tens =["", "ten", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety "] # first item is blank due to indexing
    try:
        if n < -999 or n > 999: # number must be between -999 and 999
            return "Number is out of range."
        elif n < 0: # use recursion for minus numbers
            return "Minus "+ to_english(-n)
        elif n < 20: # if number is under 20, just return item from first list
            return to_nineteen[n].capitalize()
        elif n < 100: # if number between this range
            return tens[n // 10].capitalize() + to_nineteen[n % 10].lower() # divide item by 10 and concantenate to remainder
        elif n < 1000:
            return to_nineteen[n // 100].capitalize() + "hundred and " + to_english(n % 100).lower() # divide by one hundred for first digit, use recursion for next two digits
    except:
        return "Oops"
        
print(to_english(10001))
print(to_english(-10001))
print(to_english(875))
print(to_english(2))