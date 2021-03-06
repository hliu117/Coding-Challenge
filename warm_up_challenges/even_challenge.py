# The Even Challenge
# Given an integer x and you must return True if x is even and False if x is odd

# Inputs
#   - An integer x 

# Outputs
#   - True or False depending if the number is even or not
def is_even(x):
    # Write your code here:
    if x%2 == 1:
        return False
    else:     
        return True
    #

if __name__ == "__main__":
    print("Is Even Challenge")
    # Check for test cases 
    inputs = [2,3,11,12,26]
    answers = [True,False,False,True,True]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(is_even(inp))
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
        print("")

    if completed:
        print("Task Completed")
    else: 
        print("Task Not Complete")