# Concatenating Strings with the Plus Equals Operator

We can use the += operator to *concatenate* a string onto the end of an existing string variable. 

__Note:__ Remember that concatenation does not add any spaces in between strings, so you'll need to add them yourself.

Example:

```
let ourStr = "I come first. ";
ourStr += "I come second.";
console.log(ourStr);
```

# Iterate with Javascript For Loops

You can run code multiple times using a for loop because it runs for a specified amount of times. The syntax can be done as the following 
for (a; b; c), where a is the initialization statement, b is the condition, and c is the final expression.

__Example:__

```
const ourArray = [];
for (let i = 0; i < 5; i++) { 
    ourArray.push(i);
}
```
The code above will return the table [0,1,2,3,4].

Now let's use a for loop to create a table of numbers from 1 through 5.

```
const myArray = [];

for (let i = 1; i <= 5; i++ ) { 
    myArray.push(i);
}
```
# Iterate Odd Numberes With a For Loop 

We can change our fina-expression to count by even numbers.

Suppose we start at i = 0.


