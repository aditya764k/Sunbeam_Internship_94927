function isEven(num){
    if(num % 2 == 0){
        return true
    }
    else{
        return false
    }
}
let a = 5
console.log(`${a} is Even ? ${isEven(a)}`)