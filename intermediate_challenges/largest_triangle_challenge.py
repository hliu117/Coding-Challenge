# The Largest Triangle challenge:
# Given a list of integers, return perimeter of the largest triangle that can be made using those integers. Each integer in the list can only be used once. If no triangle can be created then you should return None. 

# Example 1
# [1,2,4] -> return 7
# Example 2
# [4,2] -> return -1

# Complete the function scrambled
# Inputs:
#   - A, List[int] - Note: This list is not ordered in any particular way 

# Outputs in the order specified
#   - the perimeter of the largest triangle that can be created
def largest_triangle(A):
    # Write your code here:

    #

if __name__ == "__main__":
    print("Largest Triangle Challenge")
    # Check for test cases
    inputs = [[1,2,3,4],[1,2,3],[4,2,3,1],[0,1],[2,3,3,6]]
    answers = [9,-1,9,-1,8]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(largest_triangle(inp))
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