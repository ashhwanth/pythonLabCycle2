def pyramid():	
	n=int(input("Enter number of rows"))
	for i in range(1,n+1):
		a=0
		for j in range(i):
			a=a+i
			print(a,end=" ")
		print(" ")
pyramid()
