n = int(input("Enter value of n: "))

for i in range(2*n - 1):
         
    if i<n:
        j = i
    else:
        j = 2*n - 2 - i
        
    count = j//2+1
    for k in range(count):
            
        if i % 2 == 0:
            print("*  ",end="")
        else:
            print("  *",end="")
    print()










# n = int(input("Enter value of n: "))

# for i in range(2*n - 1):
         
#     if i<n:
#         j = i
#     else:
#         j = 2*n - 2 - i
        
#     count = j//2+1
    
#     if i % 2 == 0:
#         print("*  " * count)
#     else:
#         print("  *" * count)













#n = int(input("Enter value of n: "))

# for i in range(2*n - 1):
    
#     if i<n:
#         j = i
#     else:
#         j = 2*n - 2 - i
        
#     count = j//2+1
    
#     if i % 2 == 0:
#         print("*  " * count)
#     else:
#         print("  *" * count)
        

    
    

    
# n = int(input("Enter value of n: "))

# for i in range(n):
#     for j in range(0, i+1, 2):
#         if i%2 == 0:            
#             print("*", end="  ")
#         else:
#             print("  ", end="*")
#     print()
# for i in range(n-2, -1, -1):
#     for j in range(0,i+1, 2):
#         if i%2 != 0:
#             print("  ", end="*")
#         else:            
#             print("*", end="  ")
#     print()