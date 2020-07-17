# Name of the challenge goes here as well as any inputs required and potential return type
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