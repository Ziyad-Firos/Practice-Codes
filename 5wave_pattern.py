n = input("Enter value of n: ")
largest = 0
nums = []
for i in n:
    if int(i) > largest:
        largest = int(i)
    nums.append(int(i))
    
for j in range(largest):
    for k in range(len(nums)):
        if nums[k] >= largest - j:
            print("*", end="")
        else:
            print(" ", end="")
    print()    
# print("The largest number is:", largest)
# print(nums)