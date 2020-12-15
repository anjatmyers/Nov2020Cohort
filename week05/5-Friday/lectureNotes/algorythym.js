// friday algorythym notes
// cashing is a way to help run times

// const isUnique = (arr) => {

//     let cashe = {}
//     let result = true;
//     for (let i = 0; i < arr.length; i++) {
      
//         if(cache[arr[i]]){
//             return false;
//         }
//         else{
//             cache[arr[i]] = true;
//         }



//     }
//     return result;
//   };

//   let arr = [1, 2, 2, 3];


//   sorting function 
//   const uniqSort = function(arr) {
    
//     let cache = {};

//     let result = [];

    // for (let i = 0; i < arr.length; i++){

    //     if(!cache[arr[i]]){
    //         // means this value is not yet in cache
    //         // if already in cache, num gets skipped over 
    //         result.push(arr[i]);
    //         cache[arr[i]] = true;
    //     }

    // }

//     result.sort((a, b) => a-b)

//     return result;
// };

// let arr = [1, 1, 1, 1, 5, 2, 10];
// console.log(clearuniqSort(arr));



// let str = 'hello world'

// str.replace(/[^\w]/g, "")
// /[^\w]/g will let you repace all the white space with no space

// forof and forin 

str1 = 'A gentleman'

str2 = 'Elegant man'


function strReady(str){

strlower = str.toLowerCase()
strNoSpace = strlower.replace(/[^\w]/g, "");

return strNoSpace;

}

function anagram(str1, str2){

    let strA = str1.sort()
}


anagram(strReady(str1), strReady(str2));


// for (let i = 0; i < arr.length; i++){

//     if(!cache[arr[i]]){
//         // means this value is not yet in cache
//         // if already in cache, num gets skipped over 
//         result.push(arr[i]);
//         cache[arr[i]] = true;
//     }

// }

// let iterable = [10, 20, 30];
// for (let value of iterable) {
//   value += 1;
//   console.log(value);
// }


// use nested loops to make a sorted function 

// loop up bubble sort, selection sort and insertion sort on Visualgo
// look at merge sort as well 




