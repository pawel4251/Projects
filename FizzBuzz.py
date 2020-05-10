# FizzBuzz program to print numbers from n to m inclusive
#
# input parameters 'n' and 'm'
#
# output:
#
# if number is multiples of three print, "FIZZ" instead of number,
# if number is multiples of five print, "BUZZ" instead of number,
# if number is multiples of three and five, print "FIZZBUZZ" instead of number,
# in other case print number
#
def FizzBuzz():
    # Checking if input is number
    try:
        n = int(input("Please enter first number\n"))
    except ValueError:
        print("That was no valid number")
        return -1
    # Checking if input is number
    try:
        m = int(input("Please enter second number\n"))
    except ValueError:
        print("That was no valid number")
        return -2
    # check n value which should be greater than 1, lower than 10000 and lower than m.
    if n < 1 or n > 9999 or n >= m:
        print("Wrong first Value - Shall be in range [1-10000= and lower than second")
        return -4
    # check m value which should be greater than 1 and n and not greater than 10000.
    elif m < n or m > 10000 or m <= 1:
        print("Wrong second Value - Shall be in range (1-10000] and higher than first")
        return -1
    # Loop to detect divisibility
    for i in range(n, m+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz\n")
        elif i % 3 == 0:
            print("Fizz\n")
        elif i % 5 == 0:
            print("Buzz\n")
        else:
            print("{}\n".format(i))


# Function call
if __name__ == "__main__":
    FizzBuzz()