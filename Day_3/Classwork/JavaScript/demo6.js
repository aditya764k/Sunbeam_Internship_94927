// Default argument function
function f1(n1 = 3 , n2 = 4 , n3 = 8){
    console.log('Inside f1()')
    console.log(`n1 - ${n1} , n2 - ${n2} , n3 - ${n3}`)
}

f1(4,5,6)
f1(2)
f1(76,30,30,30)
