# Name of the challenge goes here as well as any inputs required and potential return type
import numpy as np

def mazeMatrix(n):
    # Write your code here:

    #

if __name__ == "__main__":
    print("Maze Matrix Challenge")
    # Check for test cases 
    inputs = [1,4,5]
    answers = [np.array([[1.]]),np.array([[1.,2.,9.,10.],[4.,3.,8.,11.],[5.,6.,7.,12.],[16.,15.,14.,13.]]),np.array([[ 1.,2.,9.,10.,25.],[ 4.,3.,8.,11.,24.],[ 5.,6.,7.,12.,23.],[16.,15.,14.,13.,22.],[17.,18.,19.,20.,21.]])]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(mazeMatrix(inp))
        except Exception as e:
            print("ERROR:",e)
            outputs.append(None)

    completed = True
    print("")
    for i, out in enumerate(outputs):
        if (out == answers[i]).all():
            print("Test Case", i+1, "is correct")
        else:
            print("Test Case", i+1, "is incorrect..")
            print("Expected:\n", answers[i])
            print("Your Output:\n", out)
            completed = False
        print("")

    if completed:
        print("Task Completed")
    else: 
        print("Task Not Complete")