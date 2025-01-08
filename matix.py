import numpy as np
#Puzzle:Find the sum of elements along the diagonal and flip the matrix
#Generate a random 4*4 matrix
matrix=np.random.randint(1,21,(4,4))
print("Original matrix")
print(matrix)

#Calculate the sum of diagonal
diagonal_sum=np.trace(matrix)
print(f"\nSum of diagonal elements {diagonal_sum}")

#Flip the matrix vertically and horizontally
flipped_matrix=np.flip(matrix)
print("\nFlipped matrix")
print(flipped_matrix)

#Identify the position of elements greater than 15
positions=np.argwhere(matrix>15)
print("\nPosition of elements greater than 15")
for pos in positions:
    print(f"Row {pos[0]+1}, Column{pos[1]+1}")