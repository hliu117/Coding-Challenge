# The Duplicate Number Challenge (FINAL BOSS)
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Example 
# Input: [1,3,4,2,2]
# Output: 2

# Inputs
#   - An List of ints
# Outputs
#   - Duplicate number in the list of ints 
def findDuplicate(nums):
    # Write your code here:

    #

if __name__ == "__main__":
    print("Duplicate Number Challenge")
    # Check for test cases 
    inputs = [[2,5,9,6,9,3,8,9,7,1]]
    answers = [9]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(findDuplicate(inp))
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