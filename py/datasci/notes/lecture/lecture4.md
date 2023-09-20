# Lecture 4

- Map functions
- Lambda Expressions



## Using the map function

Suppose we have the following function
````python
def times2(var):
    return var*2
````

Say we want to square every number in the list `seq = [2,4,6,8,10]` using the function above. We can usually do this with the for loop, but instead we can use the `map` built-in function to do this same task. The map function takes in two arguments. The first takes in a function and the second a list.

````python
print(map(times2, seq))
````

## Lambda Expressions

Lambda expressions can make our code shorter by writing functions in a short-hand way. The function above can be written in the following way:
````python
lambda var: var*2
````
and slightly modifying our map function above by writing:
````python
list(map(lambda num: num*2, seq))
````

## Filter function

The filter function returns a boolean value based on what function (or lambda function) you put in and list. If we want to grab a random list of numbers and returns a list of even numbers, then we could implement the following code:
````python
seq = [1,2,3,4,5]
filter(lamda num: num%2 == 0 , seq) # returns a boolean value if elements meet the condition
````
If we try to cast this code into a list then we would get a list of numbers that are even; that is, 
````python
list(filter(lambda num: num%2 ==0 , seq)) # returns [2,4]
````

# A Few Methods

Suppose we have the string 
````python
s = 'hello my name is Sam'
````
Using the `.` operator, we can use the `lower()` method to turn all the characters in the string `s` in to lowercase. On the other hand, `upper()` turns all the characters into uppercase.

The `split()` method seperates all the words of a string into a list based on what value is passed in to it. The default value is the whitespace `""`.

We can use `pop()` method to remove the last element of a list and return it. We can reassign the result of this method to a new variable.

## In Operator

We can check if an element is inside of a list by using the `in` operator. An example is:
````python
'x' in ['x', 'y', 'z'] # returns true
````
We have false if we have the following code:
````python
'x' in [1,2,3] # returns false
````

## Tuple Unpacking

Suppose we have a list of tupples:
````python
x = [(1,2), (3,4), (5,6)]
````
We can use tuple unpacking to print the elements within tuples in the list `x`.
````python
for a,b in x: 
    print(a) # prints out the first element in each tuple in x
    print(b) # prints out the second element in each tuple in x
````
