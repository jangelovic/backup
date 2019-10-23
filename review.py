# John
# period 6

# variable declaration and assignment
myVariable = "John" # String variable
myNumber = 12 # int variable
MYDecimal = 12.6 # float variable

# Make a variable of type String
print("3 + 8 = " + str(3+ 8))

# while loops 
x= 1
while x <= 10:
	print(x)
	x += 1 
# challenge
y= 100
while y >= 1:
	print(y)
	y-=1

# string concatenation 
# example
string1 = "Hello "
string2 = "world "
print(string1 + string2 + "!")
# challenge
string1 = " My "
string2 = " favorite "
string3 = " movie "
string4 = " is "
string5 = " Spiter Man Homecoming "
print(string1 + string2 + string3 + string4 + string5 )

# input
yourName = input("What is your name? ")
print("Hello " + yourName)
# challenge 
yourName = input("What is your favorite song? ")
print("My favorite song is " + yourName)

# casting change one type into another 
myNum = input("Enter a number ") #myNum is a string
myNum = int(myNum) + 10 # myNum is now an int
print("The answer is " + str(myNum))
# challenge


# if and if/else
num = intput("What is your number: ")

if num > 100:
	print("Your number is more than 100")
elif num == 100:
	print("Your number is 100")
else:
	print("Your number is less than 100")

yourName = input("Is today your birthday? ")
print("If yes happy birthday")
