#write your python code here
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


ranNums = [] #name your list and make sure it is empty!

randomNum = input("Enter number of choice: ")


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for index in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    ranNums.append(randint(1,50)) #this adds a random number between 1-50 to the list

print("Generated List: ", ranNums) #print the list!

print("Searching for number: ", randomNum)

comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found

for index in ranNums:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if index == randomNum:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found

if randomNum[0] in ranNums:
    print("Number",randomNum,"is found in the list after", comparisons, "comparison/s!")
else:
    print("Number",randomNum,"not found in the list after", comparisons, "comparison/s!")

ranNums.sort()
print("Sorted List: ", ranNums)

def calsum(ranNums):
    total=0
    for number in ranNums:
        total += number
    return total
result = calsum(ranNums)

print("The sum of the values is ", result) #sum of the values

max4=max(ranNums)
min4=min(ranNums)

print("The biggest number is: ", max4) #max number
print("The smallest number is: ", min4) #min number

binarylist = [bin(x)[2:] for x in ranNums] #numbers into binary
print(binarylist)

Relist = [] #Reverse Order list
for index in range(len(ranNums) -1, -1, -1):
    Relist.append(ranNums[index])
print("Numbers in reverse order: ", Relist)



