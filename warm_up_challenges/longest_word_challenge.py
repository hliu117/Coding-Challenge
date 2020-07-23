# The Longest Word Challenge
# Given an list of words, return the length of the longest word

# Inputs
#   - A List of words (Strings) e.g. ["hello","my","name","is","bob"]

# Outputs
#   - An integer representing the length of the longest word
def longest_word(x):
    # Write your code here:
    if x % 2 == 0:
        return True 
    return False
    #

if __name__ == "__main__":
    print("Is Even Challenge")
    # Check for test cases 
    inputs = [2,3,11,12,26]
    answers = [True,False,False,True,True]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(longest_word(inp))
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