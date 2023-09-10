function checkEqual (a,b) { 
    return a == b ? "Equal" : "Not Equal";
}
console.log(checkEqual(2,3));
console.log(checkEqual(5,5));

// Use Multiple Conditional (Ternary) Operators


function findGreaterOrEqual(a,b) { 
    return (a === b) ? "a and b are equal"
        : (a > b) ? "a is greater" 
        : "b is greater";
}

console.log(findGreaterOrEqual(2,3));
console.log(findGreaterOrEqual(5,5));

function checkSign (num) { 
    return (num > 0) ? "positive" 
            : (num == 0) ? "zero"
            : "negative";
}

console.log(checkSign(10));
