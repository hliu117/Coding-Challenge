# Name of the challenge goes here as well as any inputs required and potential return type
import numpy as np

def MatrixA(n):
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A[i,j] = (i+1+j+1)%n
    return A

if __name__ == "__main__":
    # Check for test cases 
    inputs = [2,3,5]
    answers = [np.array([[0., 1.],[1., 0.]]),np.array([[2., 0., 1.],[0., 1., 2.],[1., 2., 0.]]),np.array([[2., 3., 4., 0., 1.],[3., 4., 0., 1., 2.],[4., 0., 1., 2., 3.],[0., 1., 2., 3., 4.],[1., 2., 3., 4., 0.]])]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(MatrixA(inp))
        except Exception as e:
            print("ERROR:",e)
            outputs.append(None)

    completed = True
    print("\n")
    for i, out in enumerate(outputs):
        if (out == answers[i]).all():
            print("Test Case", i+1, "is correct")
        else:
            print("Test Case", i+1, "is incorrect..")
            print("Expected:\n", answers[i])
            print("Your Output:\n", out)
            completed = False
        print("\n")

    if completed:
        print("Task Completed")
    else: 
        print("Task Not Complete")