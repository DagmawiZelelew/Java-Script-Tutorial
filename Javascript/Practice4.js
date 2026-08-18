// ==========================================
// TASK 1: CREATE A BASE LIBRARY ITEM CLASS
// ==========================================

// This will act as the parent class
class LibraryItem {
    constructor(title, author, pub_year, avail_status = true) {
        this.title = title;
        this.author = author;
        this.pub_year = pub_year;
        this.avail_status = avail_status;
    }
}


// ==========================================
// TASK 2: CREATE THE BOOK CLASS
// ==========================================

// Book inherits properties from LibraryItem
class Book extends LibraryItem {

    constructor(title, author, pub_year, avail_status = true) {

        // Call the parent constructor
        super(title, author, pub_year, avail_status);
    }
}
// ==========================================
// TASK 3: CREATE THE EBOOK CLASS
// ==========================================

// EBook inherits from Book
class EBook extends Book {

    constructor(title, author, pub_year, avail_status, fileFormat) {

        // Call the Book constructor
        super(title, author, pub_year, avail_status);

        // Additional property for an EBook
        this.fileFormat = fileFormat;
    }
}


// ==========================================
// TASK 4: CREATE THE LIBRARY CLASS
// ==========================================

class Library {

    constructor() {

        // An array to store all books
        this.books = [];
    }



    
    // ==========================================
    // TASK 5: ADD A BOOK
    // ==========================================

    addBook(book) {

        // Add the book to the books array
        this.books.push(book);

        console.log(`${book.title} was added to the library.`);
    }


    // ==========================================
    // TASK 6: DISPLAY ALL BOOKS
    // ==========================================

    displayBooks() {

        console.log("\n--- LIBRARY BOOKS ---");

        // Loop through every book
        for (const book of this.books) {

            console.log(`
Title: ${book.title}
Author: ${book.author}
Year: ${book.pub_year}
Available: ${book.avail_status}
            `);
        }
    }

