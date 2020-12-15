// ***Object Destructuring
/* 
Declare mult() function that will multiply values of the x,y,z 
fields of the passed object
*/
// var obj = {
//     x: 5,
//     y: 20,
//     z: 3
// }

// let mult = obj => {
//     let {x, y, z} = obj;
//     return x * y * z;
// }


// console.log(mult(obj));
//300


/*
Create shortPerson() function that will destructure each person object.
Sample result:
{n: "Mike", c: "Spain", a: 23, p:100}

If input object doesn't have postsQuantitiy field it should get default value 0.
*/


var person1 = {
    name: "Mike",
    info: {
        country: "Spain",
        age: 23
    },
    postsQuantitiy: 100
}

var person2 = {
    name: "Alice",
    info: {
        country: "Italy",
        age: 25
    }
}

let person = (obj) => {

    let {name:n, info:{country:c, age:a}, postsQuantitiy:p=0} = obj;
// postQuantity:p=0 is setting a default value of zero if that key doesn't exist for an object youre passing through
    console.log(`name ${n} country ${c} age ${a} posts ${p}`);
}

person(person1);
person(person2);
// person2 needs a default value for postQuantity b/c it doesnt have that obj key


// turnary functions

// (condition) quesion mark block one : block two
//  if condition is true block 1 executes, if false block two executes 

// b > a ? console.log("b is bigger") : console.log('a is bigger');

// let str = `this is my result ${a > b ? 4 : 10}`
// if a > b is true str = 4, if false str = 10