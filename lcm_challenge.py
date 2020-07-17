# Name of the challenge goes here as well as any inputs required and potential return type
def lcm(x,y):
    if x < y:
        x, y = y, x
    lcm = x
    while True:
        if lcm % y == 0:
            break
        else:
            lcm = lcm + x
    return lcm

if __name__ == "__main__":
    # Check for test cases 
    inputs = [(1,2),(8,2),(5,6),(55,51)]
    answers = [2,8,30,2805]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(lcm(*inp))
        except Exception as e:
            print("ERROR:",e)
            outputs.append(None)

    completed = True
    print("\n")
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