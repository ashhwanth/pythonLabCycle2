str=input("Enter the string")
dict={}
def strcount():
    for i in str:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
strcount()
