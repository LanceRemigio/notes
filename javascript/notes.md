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
We can count by even numbers. 

Suppose we start at i = 0. Then consider the following code

```
const ourArray = [];

for (let i = 0; i < 10; i +=2) { 
    ourArray.push(i);
}
```
Not only can we count forwards with for loops but we can also count backwards like with the while loop earlier.

We do this by changing our initialization, condition, and final expression.

Suppose we start at i = 10 and loop while i>0. Consider the following code
````
const ourArray = [];

for (let i = 10; i > 0; i -= 2 ) { 
    ourArray.push(i);
}
````
The output contains [10,8,6,4,2].

# Iterating Through an Array with a For Loop

A common task is to iterate through the elements of an array. We can do this by using a for loop.

```
const arr = [10,9,8,7,6];

for (let i = 0; i < arr.length; i++) { 
    console.log(arr[i]);
}
```
This code intializes the index i = 0 (the first position of the array) and iterates by counting by 1 while printing out each element of the array until it the i < arr.length condition is false.

# Nesting For loops

We can use a nested for loop to loop through a nested array. 


__Example:__

```
const arr = [ 
    [1,2], [3,4], [5,6]
];

for (let i = 0; i < arr.length; i++) { 
    for (let j = 0; j < arr[i].length; j++) { 
        console.log(arr[i][j]);
    }
}
```
Note that the inner loop checks the length of each subarray.

__Example:__ 

Let's create a function that will loop through each element in each subarray and return its product.

````
function multiplyAll (arr) { 
    let product = 1;
    for (let i=0 ; i < arr.length ; i++) { 
        for (let j =0; j < arr[i].length; j++) { 
            product *= arr[i][j];
        }
    }
    return product
}
````

# Iterate with Javascript Do...While Loops
The "do" part makes one pass of the code inside the loop with no restrictions, and then continue to run the loopo while a specific condition is true.

__Example:__ 

````
const OurArray = [];
let i = 0;

do {
    ourArray.push(i);
    i++;
} while (i < 5);
````
The code above just returns an array with elements from 0 through 4. Let's look at an example where the condition of the while loop fails to be satisfied.

````
const ourArray = []; 
let i = 5;

while (i < 5) {
  ourArray.push(i);
  i++;
}
````

Since the index i = 5, the code in the while loop will not execute, leaving our initialized array empty. Now let's take a look at the __Dowhile__ loop

````
const ourArray = [];
let i = 5;

do { 
    ourArray.push(i);
    i++;
} while (i<5);
````

The code above intializes our index i with 5 and initializes an empty array named __ourArray__. Then notice that our code executes the contents within the do statement (no condition check needed) and incrementsour index by 1. Since i is incremented to 6, our code then tries to execute the condition within the while statement but fails because the index is now greater than 5. Hence, we exit the loop and get a single element within the array. 

# Replace Loops using Recursion

Recursion is defined as a function that can be expressed in terms of itself. We can look at an example regarding the product of the first n elements of an array.

````
  function multiply(arr, n) {
    let product = 1;
    for (let i = 0; i < n; i++) {
      product *= arr[i];
    }
    return product;
  }
````
Notice how __multiply(arr, n) == multiply(arr, n-1) * arr[n-1]__ . Hence, we can rewrite the function above as follows 
````
  function multiply(arr, n) {
    if (n <= 0) {
      return 1;
    } else {
      return multiply(arr, n - 1) * arr[n - 1];
    }
  }
````

# Writing a function that looks up contacts 
Suppose we have the following object that stores contacts and their associated properties
````

````
````
function lookUpProfile(name, prop) {
    for (let i = 0  ; i < contacts.length ; i++) { 
        if (contacts[i].firstName === name  ) { 
               if (contacts[i].hasOwnProperty(prop) === true)  { 
                    return contacts[i][prop];
               } else { 
                    return "No such property";
               }  
        }  
    }
    return "No such contact";
     
}
````

Uses a for loop that 

# Generate Random Fractions with Javascript

We can use random numbers to simulate random behavior. Javascript contains a function __Math.random()__ that generates a random decimal between 0 (inclusive) and 1 (exclusive). This means that the function can return a 0 but never a 1. 

__Note__: Like storing values with the assingment operator, all function calls are resolved before the return statement is executed. Hence, we can return the value of the __Math.random()__ function. Hence, we have
````
function randomFraction() { 
    return Math.random();
}
````

# Generate Random Whole Numbers with Javascript

We can use the __Math.random()__ in addition to the __Math.floor()__ function to generate random whole numbers within a certain range.
````

function randomWholeNum () { 
    return Math.floor(Math.random() * 10)
}
````
The function above returns a random whole number in between 0 and 9 (can't reach 10 because number is always rounded down to the nearest whole number).











