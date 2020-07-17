# The lcm challenge:
# Given two integers x and y, find the lowest common multiple of these two numbers

# Complete the function lcm
# Inputs:
#   - x an integer
#   - y an integer

# Outputs in the order specified
#   - lcm, the lowest common multiple of the two input numbers 

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
        print("")

    if completed:
        print("Task Completed")
    else: 
        print("Task Not Complete")