// Mutate an Array Declared with const

const s = [5,7,2];
function editInPlace() {
    s[0] = 2;
    s[1] = 5;
    s[2] = 7;
    console.log(s);
}
console.log(editInPlace(s));

// Prevent Object Mutation

function freezeObj() {
    const MATH_CONSTANTS =  {
        PI: 3.14
    };
    Object.freeze(MATH_CONSTANTS);
    try {
        MATH_CONSTANTS.PI = 99; 
    } catch(ex) {
        console.log(ex);
    } 
    return MATH_CONSTANTS.PI;
}
const PI = freezeObj();
