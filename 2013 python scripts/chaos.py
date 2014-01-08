#!/usr/local/bin/python
#chaotic behavior
def main():
	print("chaotic fxn")
	z = eval(input("Enter number between 0 and 1: "))
	for i in range(100):
		z = 3.3 * z * (1-z)
		print(z)
main()