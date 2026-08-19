const students = [
    { name: "Dagi", score: 87 },
    { name: "Abel", score: 95 },
    { name: "Mike", score: 72 },
    { name: "Sara", score: 91 },
    { name: "John", score: 64 }
];

for(const x of students){
    console.log(x.name);
}
console.log("--------Sorted Names(Highest to Lowest)--------------")

students.sort((a,b) => b.score - a.score);

for(const x of students){
    console.log(x.name);
}
// Bonus 
console.log(" ====================Sorting alphabetically===================");

students.sort((a,b) => a.name.localeCompare(b.name));
console.log(students)

