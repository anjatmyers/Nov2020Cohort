
/*
Create a function sumPlusMinus() that takes an array and sums 
separately positive and negative numbers

it should return an object like this:

{
    plus: 74, // sum of all positive numbers
    minus: -54 // sum of all negative numbers
}

*/


var nums = [10, -12, 30, -1, -8, 0, 14, -33, 20];

// Write code here
// veronica's solution 

let sumPlusMinus = arr => {

    arr.reduce((acc, elem) => {
        
        return (
            {
                plus: elem > 0 ? acc.plus + elem : acc.plus, 
                minus: elem < 0 ? acc.minus + elem : acc.minus
            }
        )

    }, {plus: 0, minus: 0})

}




// matthews solution


sumPlusMinus(nums);
// {plus: 74, minus: -54}

var nums = [10, -12, 30, -1, -8, 0, 14, -33, 20];
// Write code here
// console.log(sumPlusMinus(nums));
// {plus: 74, minus: -54}
let obj = {plus:0 , minus :0};
function sumPlusMinus(nums){
    for (let x of nums){
            if(x > 0 ){
                obj.plus += x;
            }
            else 
                obj.minus += x;
            }
}
    
sumPlusMinus(nums)
console.log(obj);

