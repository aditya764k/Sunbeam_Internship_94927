function add(n1,n2){
    console.log(`addition - ${n1 + n2}`)
}
// function alias
const myadd = add

add(10,20)
myadd(11,22)
console.log(`myadd = ${myadd} , typeof(myadd) - ${typeof(myadd)}`)

// storing function in a variable is called function alias
// type of variable is function