// Using Arrow Functions to Write Concise Anonymous Functions
// We can convert the following code into function arrow notation 
// var magic = function() { 
//     return new Date();
// }


// const magic = () => {
//     return new Date();
// }


//Write Arrow Functions with Parameters

// we can translate the following code with the arrow notation


// var myConcat = function(arr1, arr2) {
//   return arr1.concat(arr2);
// };
// We can write this two ways
// const myConcat = (arr1,arr2) => {
//     return arr1.concat(arr2)
// } 
// const myConcat = (arr1,arr2) => arr1.concat(arr2);

// Set Default Parameters for Your Functions

const increment = (number, value = 1) => number + value;

console.log(increment(2));
