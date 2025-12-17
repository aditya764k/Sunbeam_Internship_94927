const array = ['aditya','utkarsh','rohan','rushi']

console.log(array)
array.push('yogesh')
console.log(`after adding new student: ${array}`)

array.splice(0,1)
console.log(`After removing first element : ${array}`)

console.log(`total no. of students : ${array.length}`)

console.log(`Last student in list : ${array.at(-1)}`)