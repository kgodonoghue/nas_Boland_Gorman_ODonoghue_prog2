from math import *
import numpy
import numpy as np
import matplotlib . pyplot as plt
from decimal import *
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import time
from matplotlib import rcParams

#diag zero check #default is no which is 1/switch to zero is it is
diagZero=1
#diag zero check #default is no which is 1/switch to zero is it is
diagDom=1

ip_name = input("Please enter full input filename including extension: ")

if ip_name == "":

    ip_name = "nas_Sor.in"

    print(ip_name, " selected as input filename")

else:

    print("Default ",ip_name, " selected as input filename")

 

# User prompted for output filename. If no value entered default nas_Sor.out selected.    

op_name = input("Please enter full output filename including extension: ")

if op_name == "":

    op_name = "nas_Sor.out"

    print(op_name, " selected as output filename")

else:

    print("Default ",op_name, " selected as output filename")

##


## Reading in file and storing as matrix 

with open(ip_name,'r') as infile:

    n = int(infile.readline())

    A = np.zeros((n,n))

    b = np.zeros((n,1))

    mat_temp = infile.readlines()

    

    for row in range(n+1):

        if row != n:

            for col in range(n):

                # Now have this reading in one element at a time. Easy to pass into the CSR storage format

                A[row,col] = float(mat_temp[row].strip().split("\t")[col])

        else:

            # b read in as a column vector            

            b[0:,0] = mat_temp[row].strip().split("\t")

 

print("File as matrix ---------")    

print(A)

print(b)

##


## FUNCTION DEFINITION
# This of course returning CSR with convention that first element is 0 rather than 1. Python implementation
def csr_store(B,diagZero,diagDom):
    # Obtain size of matrix. Cycling through each row    
    val = []
    col = []
    rowStart = [] 
    
      
    for i in range(B.shape[0]):
        
        
        # Set this to zero at start of each new row. Used to populate rowStart vector        
        startCheck = 0
        
        # Iterating through each column
        for j in range(B.shape[0]):
            #diagonally zero check
            if (i==j) and B[i,j] == 0:
                diagZero=0
            #diagonally dominant check  
            if (i==j) and (B[i,j]-(sum(B[i,0:len(B)])-B[i,j])<=0) and (B[i,j]-(sum(B[0:len(B),j])-B[i,j])<=0):
                diagDom=0
            
            # Ignore zero entries
            if B[i,j] != 0:
                
                # When first entry in a row reached iterate check value
                startCheck += 1
                # Appending relevant values to val and col vectors
                val.append(B[i,j])
                col.append(j)
                
                # Here if startCheck is 1 then new rowStart value needs to be appended
                if startCheck == 1:
                    rowStart.append(len(val)-1)
                    
    # Finally append the last value to row start, namely the length of the val vector
    rowStart.append(len(val))
    # Output is returned as a dictionary that can be referenced by the various different key values    
    return{'val':val, 'col':col, 'rowStart':rowStart,'diagZero':diagZero,'diagDom':diagDom}
    


                  
# run the sparse sor
csr = csr_store(A,diagZero,diagDom)
print(csr)
    