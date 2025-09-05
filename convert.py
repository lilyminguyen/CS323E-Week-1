import sys

# function to test other functions
def test_cases():
    # test convert()
    assert convert(45, 2) == "101101"
    assert convert(45, 8) == "55"

    # return the result
    return "all test cases passed"

# function to convert a decimal number to a different base less than 10
# Input: n : decimal number, b : base less than 10
# Output: a string representing number n in base b
def convert(n, b):
    # define an empty string
    s = ''

    # perform repeated division
    while n > 0:
        r = n % b
        s = str(r) + s
        n = n // b
    
    # return the result
    return s

def main():
    # test the defined function
    print (test_cases())

    # read input and print the results
    for line in sys.stdin:
        line = line.rstrip() # remove /n character
        line = line.split()

        # get the number and the base
        n = int(line[0])
        b = int(line[1])
        
        # convert number to base and print result
        print(convert(n, b)) 

main()