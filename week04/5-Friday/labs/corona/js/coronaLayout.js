
function stateStats() {
    for(var i=0; i < data.length; i++){

    
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
var cardSubTitle = document.createElement('h5');
cardSubTitle.setAttribute('class', 'card-subtitle mb-2 text-muted');
cardSubTitle.textContent = `Total Cases to date: ${data[i].cases}`
divCardBody5.appendChild(cardSubTitle);

// create paragraph appended to divCardBody 5
var cardText = document.createElement('h6');
cardText.setAttribute('class', 'card-text');
cardText.textContent = `Deaths per million: ${data[i].deathsPerOneMillion}`
divCardBody5.appendChild(cardText);

    }

}

stateStats ();
