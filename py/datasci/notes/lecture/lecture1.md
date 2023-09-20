# Basic Computations, strings, and lists 

## This lecture covers
- Basic Arithmetic
- Strings
- Slice Notation
- Lists

## Data Types

- When doing operations with integers, python follows pemdas. 

- When assigning names to variables don't start with numbers or special characters. 

### Strings

#### Formatting Strings
- Can use single quotes and double quotes to make a string. 
You can format strings in the following way:
````python
num = 12
name = 'Sam'
'My number is {} and my name is {}'.format(num, name)
````
We can also pass in the variables into the curly braces.

````python
num = 12
name = 'Sam'
'My number is {one} and my name is {two}'.format(one = num, two =  name)
````

#### Grabbing characters from strings

Recall that strings are just a sequence of characters. We can treat them as lists and grab the  `nth` element by doing the following:
Let's say we want the third element of my name, then we would have
````python
s = 'Lance'
print(s[2])
````

#### Slice Syntax
We can specify a portion of a string we want to grab by using the slice notation. Say we have the letters of the alphabet again. 
````python
s = 'abcdefghijk'
````
Then we would have
````python
print(s[0:]) #grabs everything in the string
````
If we want a specific portion of our string then we would need

````python
print(s[:3]) # should return the string 'abc' (this is exclusive)
````
We can specify start point and end point of the portion we want to take from string.
````python
print(s[0:2]) # 
````
Notation should follow something like $0\leq i < 2$ where $i$ is the index of the string (if you want to think of it this way).

#### Lists

Some examples are 
````python
my_list = [1,2,3]
print(my_list) # returns the list of integers
````
We can have a list of strings and append elements to them via the `append` function
````python
str_list = ['a', 'b', 'c']
str_list.append('d')
print(str_list)
````
We can apply the same logic for splitting strings for splitting lists. We can also replace elementso of a list by specifying the index you want to replace and assigning it a new string value; that is, we have
````python
str_list[0] = "hey"
print(str_list[0]) # prints the 1st element of list
````
We can also nest a list within a list like the following
````python
nest = [1,2,3,[4,5,['target']]]
print(nest[3][2][0]) # Grabs the third element of the list within the list
````



