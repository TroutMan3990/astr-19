#Write a Python program that declares a class describing your favorite animal. 
#Have the data members of the class represent the following physical parameters of the animal: 
#length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool). 
#Write an initialization function that sets the values of the data members when an instance of the class is created. 
#Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.

#Made by Zane M
#Finished on 10/9/25

def FavoriteAnimal():

	class Animal:
		def __init__(self, name, arms, legl, eyes, tail, furry):
			self.name = name
			self.arms = arms
			self.legl = legl
			self.eyes = eyes
			self.tail = tail
			self.furry = furry

	cockatiel = Animal("Cockatiel", 2, 5.5, 2, True, True)
	brownbear = Animal("Brown Bear", 4, 2.5, 2, True, True)

	print (cockatiel.name)
	print ('A cockatiel has', cockatiel.arms)
	print ('A cockatiels legs are ', cockatiel.legl, 'mm')
	print ('A cockatiel has', cockatiel.eyes, 'eyes')
	print (cockatiel.tail, 'a cockatiel has a tail')
	print (cockatiel.furry, 'cockatiels are furry animals')

def main():
	FavoriteAnimal()

if __name__ == "__main__":

	main()
