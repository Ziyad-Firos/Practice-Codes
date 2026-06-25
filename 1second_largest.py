#Python code to print the 2nd largest number

nums= list(map( int,input(" Enter the numbers :").split()))

sorted(nums)
first=0
second=0
for i in range(len(nums)):
    if nums[i] > first:
        second = first
        first =nums[i]
    elif nums[i] > second:
        second = nums[i]
print("The second largest number is:", second)


#instead of 2, k

# nums = list(map(int, input ("Enter val : ").split()))
# nums = list(set(nums))
# nums.sort(reverse = True)
# k = int(input("  "))
# print(nums[k-1])
