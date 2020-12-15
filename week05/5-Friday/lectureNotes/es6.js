// Ternary Statements (works like an if/else)

// let a = 5;
// let b = 7;

// if (a > b) {
//     // block
// }
// else{
//     // block
// }

// ternary statement
// these statements are important with print statement 
// 1. condition  then question mark   first block executes if true: second block if false



// you can execute blocks of code in `${}` interpellating brackets
// but NOT if statements or for loops in interpellating brackets
// let str = `${a + b}`

// // so you could say ....

// let str = `sum of a + b = ${a < b ? console.log('a < b') : console.log('false block of code')}`


// function isNumber(a) {
//     if (typeof(a) === 'number'){
//         return 'this is a number';
//         // true block
//     }
//     else{
//         // false block
//         return 'this is not a number';
//     }
// }

// // function above turned into ternary statement 
// let isNumber = a => typeof(a) === "number" ? "that is a number" : "that is not a number";


// destructuring: you can do this to an object or an array


// unpacks them and assigns individual values to variables 
// you do this to help refer to data nested very deep more easily by having a variable for it 

// let arr = [1, 2, 3, 4, 5];

// let [a, b, c, d, e] = arr;
// console.log(a); 
// console.log(b); 


// object destructuring

// let luke = { occupation: 'jedi', father: 'anakin' };
// let {occupation, father} = luke;
// // this assigns value of the keys in obj luke to variables occupation and father 
// // here, has to be the same key names as used in the object 
// console.log(occupation); // 'jedi'
// console.log(father); // 'anakin'

// let {occupation:o, father:f} = luke;
// // here, the variable can be whatever you want after the colon
// console.log(o); 
// // 'jedi'


// // if obj is nested deeper:

// let luke = { occupation: 'jedi', father: {fName:'anakin', lName:'skywalker'}};

// let {occupation: o, father:{fName:f, lName:l}} = luke;




// es5 way of setting default values
// function addTwoNumbers(x, y) {
//     x = x || 0;
//     y = y || 0;
//     return x + y;
//   }

//   es6 way to do it 

// let add = (a=0, b=0) => {
//     return a + b
// }

// add(); 
// this would normally produce an error bc no arguments were passed 
// but we can put defaults to avoid this 



// restt parameters ... used when you dont know how many arguments are going to be passed in 

// let sum = (...args) => {
//     // will represent all arguments sent in 

//     if(args.length === 0) return 0;
//     if(args.length === 1) return args[0];
//     // for edge cases so you dont have to loop through anything


//     let sum = 0;

//     sum = args.reduce((acc, el) => acc + el, 0)

//     return sum

// }

// let nums = sum(5, 8, 9, 10);
// let nums2 = sum(3);

// console.log(nums2);





// let arr = [1, 3, 5]

// let arrB = arr;

// console.log(arr);

// arrb[0] = 99;

// console.log(arr, arrB);
// changes original arra bc it is passed by reference 

// SPRED OPERATOR will make a brand new copy to avoid pass by reference
// also lets you merge two arrays without affecting the first 

// let arr = [1, 3, 5, 7, 8, 3, 11]

// let arrB = [...arr]

// let arr2 = [10, 20, 40, ...arr, 95, 96];

// console.log(arr);

// arrB[0] = 99;

// console.log(arr, arrB);
// // now will only change arrB because its not referring to original array by reference 

// console.log(arr2);
// // merged two arrays 

// let result = Math.max(...arr);
// console.log(result);
// returns max value of the array


// swapping values

// let arr1 = [1, 2, 3, 4];

// let arr2 = [4, 5, 9, 0];


// how you have to traditionally swap values, using a temp variable 
// let temp = arr1[0];
// arr1[0] = arr2[0];
// arr2[0] = temp;

// new ES6 way to swap array values 

// [arr1[0], arr2[0]] = [arr2[0], arr1[0]]

// console.log(arr1, arr2);




// FOR OF  for arrays (instead of a for loop)


// let arr = [1, 2, 3, 4];

// for(let  val of arr) {
//     console.log(val);
// }

// For IN for objects 
let obj = {
    a: 1, 
    b: 2,
    c: 3,
}
for(let key in obj) {
    let value = obj[key]
    console.log(key, value);
}

// another way to do it using objects method

let objKeys = Object.keys(obj);
// returns an array of keys in an object 
let objValues = Object.values(obj);
// returns an array of values 




