# The Skipping Product Challenge
# Given an list of ints, return a list of the products of all integers in the list excluding the current in the calculation of that product.

# Example:
# A = ["hello","my","name","is","bob"]
# Return 5 cause hello is the longest word and it is of length 5

# Inputs
#   - A List of words (Strings) 

# Outputs
#   - An integer representing the length of the longest word
def skipping_product(A):
    # Write your code here:
    output = []
    product = 1
    for num in A:
        product *= num

    for num in A:
        output.append(product/num)
    
    return output
    #

if __name__ == "__main__":
    print("Skipping Product Challenge")
    # Check for test cases 
    inputs = [[1,2,3,4,5,6,7,8,9,10]]
    answers = [[3628800.0, 1814400.0, 1209600.0, 907200.0, 725760.0, 604800.0, 518400.0, 453600.0, 403200.0, 362880.0]]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(skipping_product(inp))
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