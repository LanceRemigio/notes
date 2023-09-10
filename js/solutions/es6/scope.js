// Compare Scopes of the var and let Keywords

// var numArray = [];
// var i;
// for(i =0; i < 3; i++) {
//     numArray.push(i);
// }
// console.log(numArray);
// console.log(i);

function checkScope() { 
    let i = 'function scope';
    if (true) {
      let  i = 'block scope';
        console.log('Block scope i is: ', i);
    }
    console.log('Function scope i is: ', i);
    return i;
}
console.log(checkScope());
