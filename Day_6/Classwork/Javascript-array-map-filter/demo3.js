const arr2 =[11,23,33,44,45]

console.log('sqaure without map')
for ( const i of arr2){
    const res = i * i
    console.log(res)
}

console.log('with map')

arr2.map((value,index,array)=>{
    return value * value }).forEach(value => console.log(value))

console.log('in one line')
arr2.map(value => value * value).forEach(value => console.log(value))