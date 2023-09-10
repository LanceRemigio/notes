// const myArray = [1,2,3,4,5];

//   function multiply(arr, n) {
//     if (n <= 0) {
//       return 1;
//     } else {
//       return multiply(arr, n - 1) * arr[n - 1];
//     }
//   }

// console.log(multiply(myArray, 5));

// function sum(arr,n) { 
//     if (n <= 0 ) { 
//         return 0;
//     } else { 
//         return sum(arr, n - 1 ) + arr[n-1]; 
//     }
// }

// console.log(sum([1], 0));
// console.log(sum([2,3,4], 2 ));
// console.log(sum([2,3,4,5], 3));

// Print out an array of numbers using recursion

// function rangeOfNumbers(startNum, endNum) { 
//     let arr = [];
//     if (startNum == endNum) { 
//         return arr.push(startNum);
//     } else { 
//         return rangeOfNumbers(startNum + 1 , endNum );
//     }
// }

// console.log(rangeOfNumbers(2,3))

// function prints out array from 1 to n.
// function countup(n) { 
//     if (n < 1) { 
//         return []; // this is the base case 
//     } else { 
//         const countArray = countup(n-1); // recursive call
//         countArray.push(n);
//         return countArray;
//     }
// }
// console.log(countup(5));

// function countdown(n) { 
//         if ( n < 1 ) { 
//         return [];
//         } else { 
//             const countArray = countdown(n-1); 
//             countArray.unshift(n);
//             return countArray;
//         }
// }

// console.log(countdown(5));

// Using Recursion to Create a Range of Numbers

// function rangeOfNumbers(startNum, endNum) {
//         if (startNum < endNum) {
//             return [];
//         } else { 
//             const numbers = rangeOfNumbers(startNum, endNum - 1);
//             numbers.push(endNum);
//             return numbers;
//         }
// }

// console.log(rangeOfNumbers(1,4));

// function rangeOfNumbers(startNum, endNum) {
//         let rangeArray = [];
//         for(i = startNum; i <= endNum; i++) { 
//            rangeArray.push(i); 
//         }
//         return rangeArray; 
// }

// console.log(rangeOfNumbers(5,10));

//function that generates a list of even numbers

// function rangeOfEven(startNum, endNum) { 
//         if (startNum < endNum) {
//             return [];
//         } else {
//             const numbers = rangeOfEven(startNum, endNum - 1) 
//             if (endNum % 2 == 0) {
//                 numbers.push(endNum);
//             }     
//             return numbers
            
//         }
// }

// console.log(rangeOfEven(2,9));




