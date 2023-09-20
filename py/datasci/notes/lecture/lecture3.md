# Lecture 3:

- For Loops
- While Loops
- List Comprehensions
- Functions


## For loops
Suppose we have the sequence of numbers `seq = [1,2,3,4,5]`. Say we want to print out each element in this list. We want to use a `for loop` for this operation; that is, 
````python
for i in seq: 
    print(i) 
````
We can specify values we want to grab from a list by using the `range` function. We can implement this in the following way:
````python
for x in range(0,5):
    print(x)
````
By default, the starting number is the index `0`.

## While Loops
We can also write `while loops` which are pieces of code that executes only when a certain condition is true.
````python
i = 1 
while i < 5:
    print('i is: {}'.format(i))
    i += 1
````

## List Comprehension

Say, we have the following list `x = [1,2,3,4]` and suppose we want to append the square of each element in the list into a new list. We can do this in the following way:
````python
out = []
for i in x:
    out.append(i**2)
print(out) # prints [1,4,9,16]
````
We can save space by shortening the code above by using list comprehension:

```python
[i**2 for i in x]
```

## Functions

We can reuse code by puttting it into a function! The syntax goes as follows:
````python
def my_func(param1):
    return param1
````
We can have default values by implementing the following code:
````python
def my_func(name='default'):
    return 'hello' + name
````
To call functions, we can insert our parameters, write `out_func = my_func(param1)`, and return the output of the function. We can insert doc strings into a function in order to document what our function does. It is basically a really long comment.
````python
def square(num):
    """
    This is a doc string. This function squares a number.
    """
    return i**2
````

