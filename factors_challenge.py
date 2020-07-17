# return all factor pairs of a given number, is the number is prime just return "prime":
# return a list of factor pairs, where each factor pair is a tuple of two numbers i.e. [(a,b),(c,d),(e,f),...]
# each tuple should have the two numbers in order i.e. (2,3) not (3,2)
# the list should be ordered lexographically, so in ascending order of the first number of each tuple
def Factorize(x):
    factor_pairs = []
    y = 2
    while y <= x**(1/2):
        if x%y == 0:
            factor_pairs.append((y,int(x/y)))
        y += 1
    if len(factor_pairs) == 0:
        return "prime"
    return factor_pairs

if __name__ == "__main__":
    # Check for test cases 
    inputs = [1,3,6,16,36]
    answers = ["prime","prime",[(2, 3)],[(2, 8), (4, 4)],[(2, 18), (3, 12), (4, 9), (6, 6)]]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(Factorize(inp))
        except Exception as e:
            print("ERROR:",e)
            outputs.append(None)

    completed = True
    print("\n")
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