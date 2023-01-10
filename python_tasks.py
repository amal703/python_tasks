
                                                                          LOOP AND IF-ELSE
    
1. """Exercise 1: Print First 10 natural numbers using while loop"""

i=1
while(i<=10):
    print(i)
    i=i+1

========================================================================================================================================================================================================

2. """Write a program to print the following number pattern using a loop."""

j=1

while(j<=10):
    
    i=1
    while(i<=j):
        print(i,end=" ")
        
        i=i+1
    print("\n")    
    j=j+1
    
========================================================================================================================================================================================================
3. """Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number"""


sum = 0
n = int(input("Enter number "))

for i in range(1, n + 1, 1):

    sum=sum+i

print("Sum is: ", sum)
========================================================================================================================================================================================================

4. """ Write a program to print multiplication table of a given number"""

 n= 2

for i in range(1, 11, 1):
    
    result = n * i
    print(result)

========================================================================================================================================================================================================

5. """Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop"""

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:

    if(i>500):
        break
    elif(i>150):
        continue
    
    elif(i%5==0):
        print(i)

========================================================================================================================================================================================================
   
                                                                                            STRING
  
  
1.  """Write a program to create a new string made of an input string’s first, middle, and last character."""


           
str1 = "James"
res=str1[0]

red=str1[2]


rep=str1[4]


set=res+red+rep
print(set.upper())

========================================================================================================================================================================================================

2. """Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1."""

s1 = "Ault"
s2 = "Kelly"
x=s1[2:]
y=s1[:2]
print(y+s2+x)
========================================================================================================================================================================================================

3. """Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters."""

s1 = "America"
s2 = "Japan"

print(len(s1))
print(len(s2))

a=s1[0]
b=s2[0]
c=s1[3]
d=s2[2]
e=s1[6]
f=s2[4]

set=a+b+c+d+e+f
print(set)


========================================================================================================================================================================================================

4. """Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first."""
str1 = "PyNaTive"

small = []

big = []

for char in str1:
    if char.islower():
        small.append(char)
    else:
        big.append(char)

set_str =''.join(small + big)
print("Result=",set_str)
========================================================================================================================================================================================================

5. """Write a program to find the last position of a substring “Emma” in a given string."""

str1 = "Emma is a data scientist who knows Python. Emma works at google."

index=str1.rfind("Emma")
print("The result is=",index)




========================================================================================================================================================================================================

                                                                                                  LIST

1. """Reverse a list in Python"""

list1 = [100, 200, 300, 400, 500]

list1.reverse()
print(list1)


========================================================================================================================================================================================================

2. """You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item."""

list1 = [5, 10, 15, 20, 25, 50, 20]

list1[3] = 200
print(list1)

========================================================================================================================================================================================================

3. """Given a Python list, write a program to remove all occurrences of item 20."""

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)

========================================================================================================================================================================================================

4."""Given a list of numbers. write a program to turn every item of a list into its square."""

numbers = [1, 2, 3, 4, 5, 6, 7]
res = []
for i in numbers:

    res.append(i * i)
print(res)

========================================================================================================================================================================================================

5. """Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order."""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

========================================================================================================================================================================================================


                                                                                   INPUT AND OUTPUT


1. """Use the print() function to format the given words in the mentioned format. Display the ** separator between each string."""

print('My', 'Name', 'Is', 'James', sep='**')

========================================================================================================================================================================================================

2. """Convert Decimal number to octal using print() output formatting"""


num = 8
print("The result is =",'%o' % num)

========================================================================================================================================================================================================

3. """Accept a list of 5 float numbers as an input from the user"""

numbers = []

for i in range(0, 5):
    print("Enter number at location", i, ":")

    item = float(input())

    numbers.append(item)

print("User List:", numbers)
========================================================================================================================================================================================================

4. """Display float number with 2 decimal places using print()"""

num = 458.541315
print('%.3f' % num)

========================================================================================================================================================================================================

5. """Write a program to take three names as input from a user in the single input() function call."""

str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)

========================================================================================================================================================================================================

                                                                                          DICTONORIES
         
1. """Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value"""

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

d=dict(zip(keys,values))

print(d)

========================================================================================================================================================================================================

2. """Merge two Python dictionaries into one"""

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)

print(dict1)

========================================================================================================================================================================================================

3. """Print the value of key ‘history’ from the below dict"""

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])

========================================================================================================================================================================================================
4. """We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

Write a Python program to check if value 200 exists in the following dictionary."""

Dict1 = {'a': 100, 'b': 200, 'c': 300}
if 200 in Dict1.values():
    print("The value 200 is exist")
else:
    print("The value 200 not exist")

========================================================================================================================================================================================================
5. """Write a program to rename a key city to a location in the following dictionary."""


sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))
