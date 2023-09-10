# Compare Scopes of the var and let Keywords

The `let` and the `var` keywords have different scopes. With `var`, it can be declared either globally or locally within a function. On the other hand, `let` is essentially the same but this time you can declare a variable with `let` and it will only be limited within a block, statement, or expression.

For example take:
```js
var numArray = [];
for (var i=0; i < 3 ; i++) { 
    numArray.push(i);
}
console.log(numArray);
console.log(i);
```
The output will display the array `[0,1,2]` and the variable `i` being assigned to `3`.

Another example is:
````js
var numArray = [];
var i;
for(i = 0; i < 3; i++) { 
    numArray.push(i);
}
console.log(numArray);
console.log(i);
````
This will have the same output as the example code before it, but this time `i` will always refer to the variable defined outside the for loop. This potentially have problems when we use the same variable in other functions which could lead to different, unexpected outputs. Another piece of code that can potentially have problems is the following:

````js
var printNumTwo;
for (var i =0; i < 3; i++) {
    if (i === 2) {
        printNumTwo = function() { 
            return i;
        };
    }
}
console.log(printNumTwo());
````
In this case, we would expect the output to be `2` instead of `3`. Instead, we get the the latter. This is because the variable `i` is declared globally which causes the function `printNumTwo` to output `3`. Replacing the keyword `var` with `let` will constrain any variable assignment within a statement, block, or expression. Consider the following:


````js
let printNumTwo;
for(let i =0; i < 3; i++) {
    if( i === 2) { 
        printNumTwo = function() { 
            return i;
        };
    };
}
console.log(printNumTwo());
console.log(i);
````
If we try to call the variable `i`, we will have an error saying that `i is not defined`.

By default, developers use `const` in all of their variables except for the case when they decide to reassign certain values for which they will use `let`. Note that using `const` does not mean that a variable cannot be mutable. It will only prevent the variable/object from being reassigned to another variable/identifier.

````js
const s = [5,6,7];
s = [1,2,3];
s[2] = 45;
console.log(s);
````
This will give off an error. This is because the array `s` declared with `const` are mutable but otherwise cannot be reassigned to a new array. 

# Prevent Object Mutation

In the last lesson, we observed that the `const` keyword does not really prevent data from being manipulated. However, this can be solved by using the `Object.freeze` function. It will throw off an error whenever an attempt is made to change an object.

````js
let obj = {
    name: "FreeCodeCamp",
    review: "Awesome"
};
Object.freeze(obj);
obj.review = "bad";
obj.newProp = "Test";
console.log(obj);
````
Note that our attempt to reassign the values of object gave us errors, preventing us from making any further changes to the object.

# Use Arrow Functions to Write Concise Anonymous Functions

We are not required to name our functions especially if the function is being passed as an argument to another function. Using ES6, we can shorten our code from
````js
const myFunc = function() {
    const myVar = "value";
    return myVar;
}
````
to 
````

````








