

    
// find body and assign to a variable 
var body = document.querySelector('body');

// create div card container and append to body
var divContainer1 = document.createElement('div');
divContainer1.setAttribute('class', 'container-fluid');
body.appendChild(divContainer1);

// create row div 
var divRow2 = document.createElement('div');
divRow2.setAttribute('class', 'row');
divContainer1.appendChild(divRow2);

// append all cards to row above 

// create function to iterate through state data

function stateStats() {
    for(var i=0; i < data.length; i++){

// create div column
var divCol3 = document.createElement('div');
divCol3.setAttribute('class', 'col-3 mt-5');
divRow2.appendChild(divCol3);

// create card div
var divCard4 = document.createElement('div');
divCard4.setAttribute('class', 'card');
divCard4.setAttribute('style', 'width: 18rem;');
divCol3.appendChild(divCard4);

// create card body div
var divCardBody5 = document.createElement('div');
divCardBody5.setAttribute('class', 'card-body');
divCard4.appendChild(divCardBody5);

// create card title h5 heading appended to divCardBody 5
var cardTitle = document.createElement('h5');
cardTitle.setAttribute('class', 'card-title');
cardTitle.textContent = `${data[i].state}`
divCardBody5.appendChild(cardTitle);

// create card subtitle h6 heading appended to divCardBody 5
var cardSubTitle1 = document.createElement('h6');
cardSubTitle1.setAttribute('class', 'card-subtitle mb-2 text-muted');
cardSubTitle1.textContent = `Total Cases to date: ${data[i].cases}`
divCardBody5.appendChild(cardSubTitle1);

// create second card subtitle h6 heading appended to divCardBody 5
var cardSubTitle2 = document.createElement('h6');
cardSubTitle2.setAttribute('class', 'card-subtitle mb-2 text-muted');
cardSubTitle2.textContent = `Deaths to date: ${data[i].deaths}`
divCardBody5.appendChild(cardSubTitle2);


    }
}

stateStats ();



// Veronica's solution ...........................

// var html = "";
// data.forEach(function(obj){
//     html += `
//     <div class="col-3 mt-5 mr-3">
//         <div class="card" style="width: 18rem;">
//             <div class="card-body">
//                 <h5 class="card-title">${obj.state}</h5>
//                 <h6 class="card-subtitle mb-2 text-muted">Cases: ${obj.cases}</h6>
//                 <h6 class="card-subtitle mb-2 text-muted">Deaths: ${obj.deaths}</h6>
//             </div>
//             </div>
//     </div><!--end of col-->
//     `
// })
// // console.log(html)
// //find the div with row class 
// var row = document.querySelector('.row');
// row.innerHTML = html;
// // .innerHTML
