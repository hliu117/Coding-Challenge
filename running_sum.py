# The running sum challenge:
# Given a list of integers, return a running sum of the provided list.
# For example if the following list is provided:
# [1,2,3,4,5,6,7,8,9,10] the output should be [1,3,6,10,15,21,28,36,45,55]

# Complete the function running sum
# Inputs:
#   - nums an list of integers of size n 

# Outputs in the order specified
#   - a list of integers containing the running sum of the input list of integers 
def running_sum(nums):
    # Write your code here
    output = [None]*len(nums)
        
    sum = 0
    
    for x in range(len(nums)):
        sum = sum + nums[x]
        output[x] = sum
    return output
    #

if __name__ == "__main__":
    print("Running Sum Challenge")
    # Check for test cases 
    inputs = [[1,2,3,4,5,6,7,8,9,10],[0,0,0,0,0,-1,-1,50],[1,-1,1,-1,1,-1]]
    answers = [[1,3,6,10,15,21,28,36,45,55],[0,0,0,0,0,-1,-2,48],[1,0,1,0,1,0]]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(running_sum(inp))
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