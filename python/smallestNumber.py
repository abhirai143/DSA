a = int(input("Enter the value for a :"))
b = int(input("Enter the value for b :"))
c = int(input("Enter the value for c :"))
#comparing integer ‘a’ with other two integer
if a<=b and a<=c:
	print("a is smallest")
#comparing integer ‘b’ with other two integer
elif b<=a and b<=c:
	print("b is smallest")
#comparing integer ‘c’ with other two integer
elif c<=a and c<=b:
	print("c is smallest")
