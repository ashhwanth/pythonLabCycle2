def factor():
    num = int(input("Enter the Number: "))
    print("\nFactors of", num)
    i = 1
    while i<=num:
        if num%i==0:
            print(i)
        i = i+1

factor()
