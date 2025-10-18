class Library:
    def __init__(self, list_of_books, name):
        self.bookList = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We Have The Following Books In Our Library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.bookList:
            print("Sorry, We Do Not Have That Book In Our Library. Please Choose A Book We Have In Our Library.")
        else:
            self.lendDict[book] = user
            print("Book Display Updated. You May Take The Book Now.")

    def addBook(self, book):
        self.bookList.append(book)
        print(f"{book} Has Been Added To Our Library.")
        
    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book Display Updated. Book Has Been Returned Suucessfully.")
        else:
            print("The Book Was Not Borrowed From This Library.")

if __name__ == '__main__':
    books = Library(["Harry Potter", "Tin Tin", "Hobbit", "The Importance Of Being Earnest", "To Kill A Mocking Bird"], "Let's Upskil")

    user_name = input("Welcome To Our Library! What's Your Name? ")

    while True:
        print(f"Hello, {user_name}, Welcome To The {books.name} Library. Please Choose One Of The Foolowing Options: ")
        print("1. Display Books\n2. Lend A Book\n3. Add A Book\n4. Return A Book\n5. Exit")

        user_choice = input("Please Enter A Choice To Continue: ")

        if  user_choice not in ['1', '2', '3', '4', '5']:
            print("Please Enter A Valid Choice.")
            continue

        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            book = input("Enter The Name Of The Book You Want To Borrow: ")
            books.lendBook(user_name, book)
        elif user_choice == '3':
            book = input("Enter The Name Of The Book You Want To Add: ")
            books.addBook(book)
        elif user_choice == '4':
            book = input("Enter The Name Of The Book You Want To Return: ")
            books.returnBook(book)
        elif user_choice == '5':
            print(f"Thank You For Using Our Library, {user_name}. We Hope You Have Good Day!")
            break
