# Alternating Concatenation Challenge:
# you are given two lists: create a new list which takes alternating elements from the original two lists i.e. [1,2],[3,4] ----> [1,3,2,4]
# furthermore, the given lists may not be the same length; in this case simply add the remaining elements of the longer list to the end of your new list
# i.e. [1,2],[3,4,5,6] ----> [1,3,2,4,5,6]
# the list given in the first argument starts: i.e. the first element of the output list is the first element of a, given lists a,b

# Complete the function alternateConcat
# Inputs:
#   - a,b: the two lists to be combined

# Outputs in the order specified
#   - the single combined list
def alternateConcat(a,b):
    # Write your code here:

    #

if __name__ == "__main__":
    print("Alternating Concat Challenge")
    # Check for test cases 
    inputs = [([1,2],[3,4]),([1,2,3],['a','b','c']),([1,2,3,4,5,6],['a','b','c']),([1,2,3],['a','b','c','d','e','f'])]
    answers = [[1, 3, 2, 4],[1, 'a', 2, 'b', 3, 'c'],[1, 'a', 2, 'b', 3, 'c', 4, 5, 6],[1, 'a', 2, 'b', 3, 'c', 'd', 'e', 'f']]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(alternateConcat(*inp))
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