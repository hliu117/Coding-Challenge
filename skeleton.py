# Name of the challenge goes here as well as any inputs required and potential return type
def challenge_name(x,y):
    return x, y

if __name__ == "__main__":
    print("Enter Challenge Name")
    # Check for test cases 
    inputs = [(1,2),(5,6)]
    answers = [(1,2),(5,6)]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(challenge_name(*inp))
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