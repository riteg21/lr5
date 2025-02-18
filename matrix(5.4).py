D_Matrixfirst = {(2, 1):4, (4, 4):2, (5, 6):9}
D_Matrixsecond = {(8, 3):4, (3, 4):2}

D_sum = {}

for (i,j), a in D_Matrixfirst.items():
    D_sum[(i,j)] = a
for (i,j), a in D_Matrixsecond.items():
    if (i,j) in D_sum:
        D_sum[(i,j)] += a    
else:
    D_sum[(i,j)] = a 
         
print(set(D_sum.items()))         
