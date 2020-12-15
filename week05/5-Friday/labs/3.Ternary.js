// ***Ternary Operator 

//Change the contents of the isNumber function using ternary operator

// function isNumber(a) {
//     if (typeof a === "number") {
//         return "that's a number";
//     }
//     else {
//         return "That's not a number";

//     }
// }


// let isNumber = a => typeof(a) == "number" ? "that's a number" : "that's not a number";


// console.log(isNumber(10));
// console.log(isNumber('hey there'));
// console.log(isNumber(true));


// let add = (x=0, y=0) => {
    // x = x || 0;
    // y = y || 0;
    // x=0 and y=0 are the eqivilant to setting details above 

//     return x + y 
// }

// add();


//  you can access the rest paramenters using ... arguments 

let logArguments = (...args) => {

    // ...args is an array so you can loop through 

    args.forEach(el => {
        console.log(el);
    })

}

logArguments(5, 6, 7, 8, 9);