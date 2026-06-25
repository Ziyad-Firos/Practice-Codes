row, column = map(int, input("Enter row and column: ").split())

for i in range(row):
    if i == 0:
        print(" ___    "*column,sep="", end="\n")
    
    print("/   \\___"*(column-1),"/   \\",sep="", end="\n")
    print("\\___/   "*(column-1),"\\___/",sep="", end="\n")
"""


"""
        