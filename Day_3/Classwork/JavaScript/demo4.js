function f1(){
    console.log("Inside function f1()")
}
// paramaterised function

function f2(n1,n2){
    console.log("Inside function f2(n1,n2)")
    console.log(`n1 - ${n1} , typeof(n1) - ${typeof (n1)}`)
    console.log(`n2 - ${n2} , typeof(n2) - ${typeof (n2)}`)   
}

f1()
f2(20,'adi')
f2(false)
f2(null,'sunbeam')