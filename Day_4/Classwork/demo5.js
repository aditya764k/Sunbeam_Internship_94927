//printing a array

const arr5 = [20,23,1,2,3]

for(let i = 0 ; i<arr5.length ; i++){
    console.log(arr5[i])
}

// for of loop - iterate over values - used in array

for (const i of arr5){
    console.log(i)
}

// for in loop -iterate over keys  - used for object

const a1 = {
    "first Name" : "aditya",
    "Age" : 20,
    "skils" : ["java","cpp","c"]
}

for ( const i in a1){
    console.log(i)
} 