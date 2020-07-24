# The Longest Word Challenge
# Given an list of words, return the length of the longest word

# Example:
# A = ["hello","my","name","is","bob"]
# Return 5 cause hello is the longest word and it is of length 5

# Inputs
#   - A List of words (Strings) 

# Outputs
#   - An integer representing the length of the longest word
def longest_word(A):
    # Write your code here:

    #

if __name__ == "__main__":
    print("Longest Word Challenge Challenge")
    # Check for test cases 
    inputs = [["hello","my","name","is","bob"],["this","coding","challenge","is","super","fun"],["thanks","henry","and","josh"]]
    answers = [5,9,6]

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