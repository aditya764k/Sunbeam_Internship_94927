// using Constructor

function s3(name , age){
    this.name = name
    this.age = age
}

const s4 = new s3()
console.log(s4)

const s5 = new s3("rohan" , 30)
console.log(s5)