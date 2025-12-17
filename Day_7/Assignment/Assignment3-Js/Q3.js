let marks = [35,67,82,49,90,58];

let Passed = marks.filter(value => value >= 50)
console.log(Passed)

let toPercent = marks.map(value => value + "%")
console.log(toPercent)

console.log(marks.some(value => value > 85))
