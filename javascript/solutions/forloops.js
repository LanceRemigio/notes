// use a for loop to push the values 1 through 5 onto myArray

// const myArray = [];

// for (let i = 1; i <= 5; i++ ) { 
//     myArray.push(i);
// }
// console.log(myArray);

// use a for loop to to push odd numbers from 1 through 9 into an array (pushing the odd numbers)

// const myArray = [];

// for (let i = 1; i < 10; i += 2 ) { 
//     myArray.push(i);
// }
// console.log(myArray);
//

// Counting backwards to create an array of descending odd numbers.

// const myArray = [];

// for (let i = 9; i > 0; i -= 2) { 
//     myArray.push(i);
// }
// console.log(myArray);

// Declare and initialize a variable total to 0. Use a for loop to add the value of each element of the myArr array to total.

// const myArr = [2,3,4,5,6];
// let total = 0
// for (let i  = 0; i < myArr.length; i++) { 
//    total += myArr[i]; 
// }
// console.log(total);

// Modify function multiplyAll so that it returns the product of all the numbers in the sub-arrays of arr.

function multiplyAll (arr) { 
    let product = 1;
    for (let i=0 ; i < arr.length ; i++) { 
        for (let j =0; j < arr[i].length; j++) { 
            product *= arr[i][j];
        }
    }
    return product
}

// console.log(multiplyAll([[1, 2], [3, 4], [5, 6, 7]]))



