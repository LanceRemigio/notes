
const contacts = [
  {
    firstName: "Akira",
    lastName: "Laine",
    number: "0543236543",
    likes: ["Pizza", "Coding", "Brownie Points"],
  },
  {
    firstName: "Harry",
    lastName: "Potter",
    number: "0994372684",
    likes: ["Hogwarts", "Magic", "Hagrid"],
  },
  {
    firstName: "Sherlock",
    lastName: "Holmes",
    number: "0487345643",
    likes: ["Intriguing Cases", "Violin"],
  },
  {
    firstName: "Kristian",
    lastName: "Vos",
    number: "unknown",
    likes: ["JavaScript", "Gaming", "Foxes"],
  },
];

// function takes in name and property
// checks name is an actual contact's firstName (use OwnProperty(prop))
// if name != contact return "No such contact"
// if prop != to any valid properties of a contact name => return "No such property"
// console.log(contacts[0].firstName);

function lookUpProfile(name, prop) {
  // Only change code below this line
    for (let i = 0  ; i < contacts.length ; i++) { 
        if (contacts[i].firstName === name  ) { 
               if (contacts[i].hasOwnProperty(prop) === true)  { 
                    return contacts[i][prop];
               } else { 
                    return "No such property";
               }  
        }  
    }
    return "No such contact";
     
  // Only change code above this line
}

// console.log(lookUpProfile("Cristian", "color" ));
// console.log(lookUpProfile("Christian", "likes" ));
console.log(lookUpProfile("Akira", "table"));





