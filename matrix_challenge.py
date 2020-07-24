# The matrix challenge:
# Given an integer n, complete the function MatrixA such that you return a n x n matrix. 
# A(i,j) = (i + j) mod n, where i,j start at 1

# Complete the function MatrixA
# Inputs:
#   - n, the side of the matrix 

# Outputs in the order specified
#   - A numpy array of size n x n which meets the conditions mentioned above.
import numpy as np

def matrixA(n):
    # Write your code here:

    #

if __name__ == "__main__":
    print("Matrix Challenge")
    # Check for test cases 
    inputs = [2,3,5]
    answers = [np.array([[0., 1.],[1., 0.]]),np.array([[2., 0., 1.],[0., 1., 2.],[1., 2., 0.]]),np.array([[2., 3., 4., 0., 1.],[3., 4., 0., 1., 2.],[4., 0., 1., 2., 3.],[0., 1., 2., 3., 4.],[1., 2., 3., 4., 0.]])]

    outputs = []
    for inp in inputs:
        try:
            outputs.append(matrixA(inp))
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