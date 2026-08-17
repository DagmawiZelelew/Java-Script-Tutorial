class contact{
    constructor(name,phone_no){
        this.name =name;
        this.phone_no =phone_no;

    }
    static displaycontact(){
        console.log("Contact successfully saved");
    }
}
const contact1 = new contact("Yoseph",947899506);
const contact2 = new contact("Dagmawi",923231226);
console.log(contact1.name);
contact.displaycontact();