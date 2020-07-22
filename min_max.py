# The max min challenge:
# Given a list of items; find the largest and smallest integer in a list. 

# Example
# [1,2,3,4,5,6,7,8,9,10] return 10,1,1,1

# Complete the function min_max 
# Inputs:
#   - List of items

# Outputs in the order specified
#   - The largest number in the list
#   - The number of instances the largest number occurs in the list
#   - The smallest number in the list 
#   - The number of instances the smallest number occurs in the list    
def min_max(x):
    # Write your code here

    # Set initial values to the first int
    for i in x:
        if(type(i) == int):
            min = i
            max = i
            min_count = 0
            max_count = 0
            break

    for i in x:
        if type(i) == int:
            if i > max:
                max = i
                max_count = 1
            elif i == max:
                max_count += 1

            if i < min:
                min = i
                min_count = 1
            elif i == min:
                min_count += 1

    return max,max_count,min,min_count
    #

if __name__ == "__main__":
    print("Min Max Challenge")
    # Test Cases
    inputs = [[1,2,3,4,5,6,7,8,9,10],[10,10,50,60,10,10,100,100,50],[100,'abc',100,99,100],['abc',100,90,100,90]]
    answers = [(10,1,1,1),(100,2,10,4),(100,3,99,1),(100,2,90,2)]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(min_max(inp))
        except Exception as e:
            print("ERROR:",e)
            outputs.append(None)

    completed = True
    print("")
    for i, out in enumerate(outputs):
        if out == answers[i]:
            print("Test Case", i+1, "is correct")
        else:
            print("Test Case", i+1, "is incorrect")
            print("Expected:", answers[i])
            print("Your Output:", out)
            completed = False
        print("")

    if completed:
        print("Task Completed")
    else: 
        print("Task Not Complete")