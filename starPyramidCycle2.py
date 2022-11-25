row=int(input("Enter the number of rows"))
for i in range(row):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
for k in range(row,1,-1):
    for h in range(k-1):
        print("*",end=" ")
    print("\n")
