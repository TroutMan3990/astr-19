#Write a Python that prints the sum of two floating point numbers, 
#the difference between two integers 
#and the product of a floating point number and an integer. 
#In each case, have the program print out the data type of the resulting answer.

#Made by Zane Mitchell

def FloatingPointMath():
	#Int Difference
	x = 10 - 5
	print(x)
	print(type(x))


	#Floating Point + Int Product
	y = 20.5 * 2
	print(y)
	print(type(y))

def main():
	FloatingPointMath()

if __name__== "__main__":
	main()
