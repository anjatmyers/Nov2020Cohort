const companies = [
    { name: "Company One", category: "Finance", start: 1981, end: 2003 },
    { name: "Company Two", category: "Retail", start: 1992, end: 2008 },
    { name: "Company Three", category: "Auto", start: 1999, end: 2007 },
    { name: "Company Four", category: "Retail", start: 1989, end: 2010 },
    { name: "Company Five", category: "Technology", start: 2009, end: 2014 },
    { name: "Company Six", category: "Finance", start: 1987, end: 2010 },
    { name: "Company Seven", category: "Auto", start: 1986, end: 1996 },
    { name: "Company Eight", category: "Technology", start: 2011, end: 2016 },
    { name: "Company Nine", category: "Retail", start: 1981, end: 1989 }
];

const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32];


// var arr = [6, 4, 3, 2, 1];

// var newArr = arr.map(function(num) {

//     return num * 3;
// })

// console.log(newArr);


// var students = ['Andrea', 'Kim', 'Kanny', 'Ally']

// var greetingArr = students.map(function(student){

//         return `Hello ${student}`
// })

// console.log(greetingArr);

// .............................................


// ages.forEach(function(age){
//     let birthYear = 2020 - age;
//     console.log(birthYear);

// })


// Filter out all ages greater than 35 
// var ageFilter = ages.filter((age)=> age<=35)

// var over35 = ages.filter(function(num){

//     return num > 35;
// })

// console.log(over35);


// Filter all even numbers

// var evenNum = ages.filter(function(num){

//     if (num % 2 === 0){
//         return num
//     }

// })

// console.log(evenNum);

/// map through ages array and return a new ages array where 5 is added to each element.


// var agesPlusFive = ages.map(function(num){
//      return num + 5;
    
// })
// console.log(ages);
// console.log(agesPlusFive);

// var newAges = ages.map(arrVAl => arrVAl +5)






//map through the companies array and change the end date to 2020


//using a for loop print each object of companies array 


//using forEach print each object of companies array


// check if there is a number greater than 60 in the ages array 

// var over60 = ages.some(function(num){
//     return num > 60
// })
// console.log(over60);




//map through the companies array and list the name, start and end data

// companies.forEach(function(object){
    
//     console.log(object.name, object.start, object.end);

// })

// return an array with just company names
// var comNames = companies.map(function(object){
//     return object.name;
// })

// console.log(comNames);

// 


// filter out companies started before 1990

// var start1Before1990 = companies.filter(function(object){

//     return object.start >= 1990;
//     // if (object.start > 1990) {
//     //     return object.name
//     // }
    
// })

// console.log(start1Before1990);