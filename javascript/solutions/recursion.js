const myArray = [1,2,3,4,5];

//   function multiply(arr, n) {
//     if (n <= 0) {
//       return 1;
//     } else {
//       return multiply(arr, n - 1) * arr[n - 1];
//     }
//   }

// console.log(multiply(myArray, 5));

function sum(arr,n) { 
    if (n <= 0 ) { 
        return 0;
    } else { 
        return sum(arr, n - 1 ) + arr[n-1]; 
    }
}

console.log(sum([1], 0));
console.log(sum([2,3,4], 2 ));
console.log(sum([2,3,4,5], 3));
