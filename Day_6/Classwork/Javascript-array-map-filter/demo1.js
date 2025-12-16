const arr = [1, 2, 3, 4, 5];
console.log(arr)

for (const i of arr){
    console.log(i)
}
arr.forEach((value,index,array) =>{ console.log(`value -${value} , index - ${index} , array - ${array}`)})

console.log('using the foreach meathod')
arr.forEach(value => console.log(value))