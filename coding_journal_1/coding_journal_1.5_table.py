#Write a Python program that writes out a table of the function sin(x) vs. x 
#where x is tabulated between 0 and 2pi with a thousand entries. 
#Follow the basic Python program structure, including a main program function.

import numpy as np

def SinTable():
	end = 2 * np.pi

	#creates an array with 1000 entries
	xValues = np.linspace(0, end, num = 1000)

	#creates a second array with 1000 entries
	sinValues = np.sin(xValues)

	#Read the string breakdown below to understand how this works
	print(f"{'x':<15} {'sin(x)':<15}")

	#output 30 dashes
	print("-" * 30)

	#Starts two counters x, s inside both arrays going at the same time
	#Similar to nesting mutiple for loops in C++, but it is in the header this time

	for x, s in zip(xValues, sinValues):

		#f with "" desginates f string
			#Can use {} to print direct values from Python
		#print x and s with the following formatting
			#< alligns it to the left
			#15 limits the total characters of x or s to 15 total characters (. & - included)
			#.6 rounds the values to 6 places 
			#Seperating the values puts a space between them in the table

		print(f"{x:<15.6f} {s:<15.6f}")

def main():
	SinTable()

if __name__ == "__main__":
	main()