# The Average Challenge:
# Given a list of integers A, find the average of the array. This number should not be rounded at all

# Inputs
#   - A a list of integers

# Outputs
#   - the average of the array
def average(A):
    return sum(A)/len(A)

if __name__ == "__main__":
    print("Average Challenge")
    # Check for test cases 
    inputs = [[10,10,10,10],[2,4,6,8],[3,6,9,15],[-1,5,-7,0,3]]
    answers = [10,5,8.25,0]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(average(inp))
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