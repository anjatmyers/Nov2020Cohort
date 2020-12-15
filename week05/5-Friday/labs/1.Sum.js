// Create a function sum() that will sum all arguments passed to it.
// Quantity of the arguments is unknown.



// takes ...args as the parameter because this allows an unknown number of elements to be passed in
let sum = (...args) => {

   return args.reduce((acc, cV) => {
        return acc + cV 
    }, 0)
}


sum(1,3);
sum(10, 20, 5);

console.log(sum(10, 20, 5));



// swapping numbers
let arr = [4, 5, 6, 7];
[arr[0], arr[1]] = [arr[1], arr[0]];