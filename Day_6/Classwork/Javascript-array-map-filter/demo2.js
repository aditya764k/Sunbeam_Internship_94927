const arr1 =[10,203,44,4,47,43]

console.log('even numbers')
for (const i of arr1){
    if (i % 2 == 0){
        console.log(i)
    }
}

console.log('using filter')
arr1.filter((value,index,array) =>{
    return value % 2 == 0 }).forEach(value => console.log(value))
    
 arr1.filter(value => value % 2 != 0).forEach(value => console.log(value))        