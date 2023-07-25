// Generates a random number within a specified max and minimum number
// function randomRange (myMin, myMax) { 
//     return Math.floor(Math.random() * (myMax - myMin + 1) + myMin);
// }

// console.log(randomRange(2,4));

// Using the parseint function to convert a binary number into an integer 

function convertToInteger (str) { 
    return parseInt(str, 2);
}

console.log(convertToInteger("10011"));
