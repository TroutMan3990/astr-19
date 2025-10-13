#Write a Python program that defines a function f(x) that returns x*3 + 8. 
#In the main function of the program, call f(x) with x = 9 and print the result.  
#Use an if statement that executes if the result is larger than 27 and prints “YAY!”.

#Written by Zane M

def FunctionMath():
	string_input = input('Input X\n')
	x = int(string_input)
	f = x * 3 + 8
	print('Result of function =', f)

	if f > 27:
		print('YAY!')

def main():
	FunctionMath()

if __name__ == "__main__":
	main()