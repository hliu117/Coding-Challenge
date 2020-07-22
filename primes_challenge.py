# Primes Challenge:
# Given a number n, return a list, in order, of all the prime numbers that are less than n

# Complete the function findPrimes
# Inputs:
#   - n, find all primes that are less than this number

# Outputs in the order specified
#   - a list of primes less than n, in order smallest to largest
def findPrimes(n):
    primes = []
    number = 2
    while number < n:
        is_prime = True
        for p in primes:
            if number%p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        number += 1
    return primes

if __name__ == "__main__":
    print("Primes Challenge")
    # Check for test cases 
    inputs = [1,2,10,50,100]
    answers = [[],[],[2,3,5,7],[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47],[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(findPrimes(inp))
        except Exception as e:
            print("ERROR:",e)
            outputs.append(None)

    completed = True
    print("")
    for i, out in enumerate(outputs):
        if out == answers[i]:
            print("Test Case", i+1, "is correct")
        else:
            print("Test Case", i+1, "is incorrect..")
            print("Expected:", answers[i])
            print("Your Output:", out)
            completed = False
        print("\n")

    if completed:
        print("Task Completed")
    else: 
        print("Task Not Complete")