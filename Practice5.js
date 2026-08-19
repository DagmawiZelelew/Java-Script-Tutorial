const events = [
    {
        title: "Started Learning JavaScript",
        details: {
            category: "Education",
            importance: 10
        },
        people: ["Dagmawi"],
        date: new Date("2026-01-10")
    },
    {
        title: "Built My First Project",
        details: {
            category: "Programming",
            importance: 9
        },
        people: ["Dagmawi", "Friend"],
        date: new Date("2026-03-15")
    }
];
console.log(events[0]);
console.log("========================")
console.log(events[1]);
console.log(events[0].details.category)
events.sort((a,b) =>a.date -b.date );
console.log("================Sorted in impotance================")
events.sort((a,b)=> b.details.importance - a.details.importance)
console.log(events)
console.log("===========Title Alphabetical Ordered ===========")
events.sort((a,b) =>a.title.localeCompare(b.title));
console.log(events);
console.log("======Sorted by Date======") 
console.log(events)

// I know its not the best mehtod to shuffle but....🙄
const shuffled = events.sort(() => Math.random() - 0.5);
console.log(shuffled)
console.log("______________Date_____________")
const date = new Date()
const difference_of_event_1 = date - events[0].date;
console.log(`It has been ${Math.floor( difference_of_event_1/ 86400000)} since the event has passed`);