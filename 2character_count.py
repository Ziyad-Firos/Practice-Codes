#Code to print character count in a string

# ab = input("Enter string : ")
ab = "HelloW"
count = {}
for char in ab:
    if char in count:
        count[char] +=1
    else:
        count[char] =1 
        
print(count)
