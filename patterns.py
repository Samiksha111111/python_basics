# n=5
# for n in range(1,n+1):
#     for m in range(1,n+1):
#         print(m, end=" ")
#     print(" ")

# n=5
# digit=n
# for k in range(n,0,-1):
#     for m in range(1,k+1):
#         print(digit, end=" ")

#     print(" ")

# n=5
# m=0
# for k in range(n,0,-1):
#     m+=1
#     for c in range(1, k+1):
#         print(m, end=" ")
#     print(" ")

# n=5
# m=0
# for k in range(1, n+1):
#     m+=1
#     for c in range(1, k+1):
#         print(m, end=" ")
#     print(" ")

# n=7
# for k in range(n,0,-1):
#     for _ in range(1, k):
#         print(k, end=" ")
#     print(" ") 

# n=5
# num=1
# for r in range(1, n+1):
#     for c in range(2*r-1):
#         print(num, end=" ")
#         num+=1
#     print(" ")

n=7
for r in range(1,n+1):
    for c in range(r,0,-1):
        print(c, end=" ")
    print(" ")