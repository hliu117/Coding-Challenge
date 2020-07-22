# The Scrambled challenge:
# Given two words a and b return True if b is a perfect scramble of the word a. 
# A perfect scramble means that both words have to be the same length and all letters of the 
# word b are used in the word a

# Complete the function scrambled
# Inputs:
#   - a, a word
#   - b, a word that may or may not be a perfect scramble of word a

# Outputs in the order specified
#   - A boolean True or false, depending whether or not the word b is a scrambled version of the word a
def scrambled(a,b):
    pass

if __name__ == "__main__":
    print("Scrambled Challenge")
    # Check for test cases 
    inputs = [("great","greater"),("josh","hsoj"),("henry","yenry")]
    answers = [False,True,False]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(scrambled(*inp))
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