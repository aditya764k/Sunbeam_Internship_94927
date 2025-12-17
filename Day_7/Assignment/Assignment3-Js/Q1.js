const student = {
    studentId: 127,
    fullName:"aditya dileep shintre",
    email: "aditya.shintre@example.com",
    course: "web development using Python",
    marks: [85, 90, 78]
}

// converting json object to String (stringify method)
const Json_string = JSON.stringify(student)

console.log(Json_string);

// converting string to json object (parse method)
const Json_object = JSON.parse(Json_string)
console.log(Json_object);

