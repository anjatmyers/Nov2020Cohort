// // console.log("Hello Hello! I'm in an external js file.")

// console.log("Andrea")
// console.log("Jacob")
// console.log("Claude")

// console.log(`
// Backticks 
//     allow 
//     you to
//     have long
//     quotes 
// `) 

// var a = 3
// // have to declare your varables with var 

// // weUseCamelCaseInJavascript
// // we_dont_use_snake_case_like_python

// // len is a property in Javascript 
// // digitalCrafts.length

// var name = "Andrea";
// console.log(name)

// console.log(name.length) 
// will give you 6 

// console.log(name.indexOf('n'))
// will tell you the index of whats in the '', even spaces

// if statement in Javascript

// if (condition){
//     // block of code;
    // separated by semicolons;
// }

// var age = 20;

// if (age >= 21){
//     console.log("you can drink");
// }
// else if (age < 21){
//     console.log("You can't drink");
// }
// else {
//     console.log("Well how old are you?");
// }


// another way to do an if statement - switch statement
// this gives you another way to test against the input repeatedly with less code

// var fruit = 'Papayas';
// switch (fruit) {
//   case 'Oranges':
//     console.log('Oranges are $0.59 a pound.');
//     break;
//   case 'Mangoes':
//   case 'Papayas':
//     console.log('Mangoes and papayas are $2.79 a pound.');
//     // expected output: "Mangoes and papayas are $2.79 a pound."
//     break;
//   default:
//     console.log('Sorry, we are out of ' + fruit + '.');
// }

// var age = 23;

// switch (true) {
//   case age >= 21:
//     console.log("You are over 21 and can drink.")
//     break;
//   case age < 21:
//     console.log("You are under 21 and can't drink.")
//     break;
// }


// while statement

// var count= 0;

// while (count < 10) {
  
//     count++;
//     console.log(count);
// // counts one to ten
// }


// for loops take the while loop and counter and simplifies it

// for (start; test; increment){
  
// }

// for (var count = 1; count <= 10; count++){
//   console.log(count);
// }



// Arrays are called lists in python
// use PUSH instead of append

// var myArray = [4, 4, 4, 4, 4, 4]

// console.log(myArray);
// // also zero indexed
// myArray.push(55);
// console.log(myArray);

// to reassign a number in an array
// myArray[0] = 5
// now is [5, 4, 4, 4, 4, 4]

// POP takes the last element from the array 
// SHIFT and UNSHIFT
// shift 
// unshift adds an element to the start of the array 

// splicing removes a number from an array and mutates it permanently 
// removes an element from the beginning from the array and returns them i a new array

// var lottoNums = [23, 11, 43, 19, 37, 16];
// var arrayOfSplicedValues = lottoNums.splice(2, 1);
// console.log(arrayOfSplicedValues);

// starts at index of two and removes 1 element 


// Slicing does not mutate the original array 

// var lottoNums = [23, 11, 43, 19, 37, 16];
// var arrayOfSplicedValues = lottoNums.splice(2, 5);
// console.log(arrayOfSplicedValues);
// this takes items from index 2-5 (not including 5) and returns them
// Without altering the original array 


// split
// doesnt original string
// alph = "abcdefghijklmnopqrstuvwxyz"
// let chars = alph.split('');

// console.log(chars);
// prints all letters in an array separately


// JOIN puts array back into a string

// let alph2 = chars.join('');
// console.log(alph2);
// returns array into a string



// var a = "6"

// var intA = parseInt(a);
// // turns an int into a number
// console.log(a +3)
// // returns 9


// toString turns a number into a string


// parseInt or Number()
// toString
// split('')
// reverse
// join('')

// USE above methods to reverse a number 
// var num = -17345;

// // numString = num.toString();
// // // turned number into a string "17345"
// // stringArray = numString.split('');
// // // split the string into an array of individual numbers 
// // reversedArray = stringArray.reverse();
// // // reversed the array's items
// // joinedString = reversedArray.join('');
// // // turned the array back into a string
// // reversedNum = parseInt(joinedString);
// // // changed the string back into a number 
// // console.log(reversedNum);

// // you can combine the methods as well and check for negatives

// var sign = Math.sign(num);
// var reverse = num.toString().split('').reverse().join('');
// var rnum = parseInt(reverse) * sign;
// console.log(rnum);





// to LOOP through an array 

// var arr = [6, 7, 9, 3]

// for (var index = 0; index < arr.length; index++){

//     arr[index]
// }


// var amount= 50
// var coins = [25, 10, 5]
// var coinTotal = 0
// var index = 0

// while(amount > 0 ){
//   if(coins[index] <= amount){
//     amount = amount - coins[index];
//     coinTotal++;
//   }
//   else{
//     index++;
//   }
// }

// console.log(coinTotal);




// dictionaries

// var phonebook = {
//   firstName: 'Andrea',
//   lastName: 'myers'
//   }

// phonebook['middleName'] = 'Therese'
// // you can add keys into the dictionary
// phonebook['lastName'] = 'Myers'
// // you can update to correct mistakes or change values
// delete phonebook['lastName']
// // you can delete entire keys

// console.log(phonebook);

// look up: for in - allows you to go through dictionaries 




// Functions 

// function fname(){
//     console.log('a function was executed');
// }

// fname()

// function add(num1, num2){
//   return num1 + num2;
// }

// var result = add(4, 6)

// console.log('The sum of num1 and num2 is', result)

// console.log(`Twice the sum of the numbers is ${2* result}`);
// this is interperlating strings with backticks
// similar to fstrings in python 



// how to cycle through an objects key names
// var characterSheet = {
//   name: 'tim berners-lee',
//   title: 'sir',
//   powers: 'invernt the word'
// };

// var keyNameList = Object.keys(characterSheet);
// for (var i= 0; i<keyNameList.length; 
//     i++){
//     console.log(characterSheet[keyNameList[i]]);
// }


// loop over an array
// Loop over an Array

// fruits.forEach(function(item, index, array) {
//   console.log(item, index)
// })
// Apple 0
// Banana 1


// for (var count = 1; count <= 10; count++){
//     console.log(count);
// }

// count = 0 

// while (count <10){
//   count++;
//   console.log(count);
// }

// var input = 5

// for (var i=0; i< input; i++){
//   console.log('*****');
// }

// inputText = "Welcome to Digital Crafts"

// bannerLength = inputText.length 

// function banner() {
//   console.log("*".repeat(bannerLength +4));
//   console.log("* " + inputText + " *");
//   console.log("*".repeat(bannerLength +4));
// }
// banner()


// print hallow box
// function printBox(x,y) {
//   console.log(` ${"-".repeat(x)} `);
//   var i = 1;
//   while (i <= (y-2)) {
//       console.log(`|${" ".repeat(x)}|`);
//       i++;
//   }
//   console.log(` ${"-".repeat(x)} `);
// }
// printBox(20,10);



// var str = "Write a function leetspeak which is given a string, and returns the leetspeak equivalent of the string."
// function leetspeak(text) {
//     let leet = {
//         a: 4,
//         e: 3,
//         g: 6,
//         i: 1,
//         o: 0,
//         s: 5,
//         t: 7};
//         let newText = "";
//     for (let char of text) {
//         if (Object.keys(leet).includes(char.toLowerCase())) {
//             char = leet[char].toString();
//         }
//         newText = newText.concat(char);
//     }
//     return newText
// }
// console.log(leetspeak(str));




// long vowel function
// function longLong(word){
//   let vowels = ['a','e','i','o','u']
//   let newWord = ''
//   let prevChar = ''
//   for (let char of word){
//       if (char.toLowerCase() === prevChar && vowels.includes(char)){
//           newWord = newWord + char.repeat(4)
//       } else {
//           newWord = newWord + char
//       }
//       prevChar = char.toLowerCase()
//   }
//   return newWord
// }
// console.log(longLong('Cheese'))


// making a list of only positive numbers
// function posNums(numArray)
// {
//     var tempList = [];
//     for(var x = 0; x<numArray.length;x++)
//     {
//         if(numArray[x] > 0)
//         {
//             tempList.push(numArray[x]);
//         }
//     }
//     return tempList;
// }
// var example = [-5,-3,-2,0,1,2,3,5];
// console.log(posNums(example));


// Ceasar's cypher

// function decipher(string, offset)
// {
//     let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
//     'h', 'i', 'j', 'k', 'l', 'm', 'n',
//     'o', 'p', 'q', 'r', 's', 't', 'u',
//     'v', 'w', 'x', 'y', 'z' ];
//     let lengthString = string.length;
//     let alphabetLength = alphabet.length;
//     let cipher = "";
//     for(let x = 0; x < lengthString; x++)
//     {
//         let temp = myString[x];
//         if(temp == ' ')
//         {
//             cipher = cipher + ' ';
//         }
//         for(let y = 0; y < alphabetLength; y++)
//         {
//             if(temp == alphabet[y])
//             {
//                 // handles index overflow
//                 if(y + offset > 25)
//                 {
//                     newIndex = ((y + offset) % 25) - 1
//                 }
//                 else
//                 {
//                     newIndex = y + offset;
//                 }
//                 cipher = cipher + alphabet[newIndex];
//                 // saves run-time
//                 break;
//             }
//         }
//     }
//     return cipher;
// }
// let offset = 13;
// let myString = "lbh zhfg hayrnea jung lbh unir yrnearq";
// console.log(decipher(myString, offset))






