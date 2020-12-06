// Creating elements - two step process
// 1. create and element 2. append it to the dom

var div = document.createElement('div');
// step 1 created the element
div.textContent = "Hey, cool! You're making dom elements."

// append another element to existing div
var anchor = document.createElement('a');

anchor.textContent = "Google";
anchor.setAttribute('href', 'https://google.com')

div.appendChild(anchor);
// this is now nested inside of the div tag

var body = document.querySelector('body');
// now need to append it to an existing element

body.appendChild(div);
// you passed the body element your new div


// Removing an element 1. find it 2. remove it 

var p = document.querySelector('p')

document.body.remove(p) 