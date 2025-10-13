#Write a Python program that writes out a table of the function sin(x) vs. x, 
#where x is tabulated between 0 and 2pi with a thousand entries. 
#Follow the basic Python program structure, including a main program function.

#Made by Zane M
#Finished on 10/10/25

#Commonly Used Abr
import matplotlib.pyplot as plt
import numpy as np

def SinGraph():
	end = 2 * np.pi
	xValues = np.linspace(0, end, num = 1000)
	yValues = np.sin(xValues)
	#sinNeg = np.linspace(-1, 1, num = 1000)
	#print(xValues)
	#print(yValues)
	#print(sinNeg)

	plt.plot(xValues, yValues, color='blue', label='sin(x)')
	#plt.plot(sinNeg, color='red', label='x')
	plt.title('sin(x) vs x: 0 to 2pi')
	plt.xlabel('x (radians)')
	plt.ylabel('sin(x)')
	plt.legend()
	plt.grid(True)
	plt.show()

def main():
	SinGraph()

if __name__ == "__main__":
	main()


