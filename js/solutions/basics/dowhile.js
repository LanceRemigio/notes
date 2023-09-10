// Change the __while__ loop in the code to a __do..while__ loop so the loop will push the only number 10 to myArray, and i will be equal to 11 when your code has finished running.

const myArray = [];
let i = 10;

do { 
    myArray.push(i);
    i++;
} while (i < 5);

console.log(myArray);
console.log(i);
