class Contact:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
class ContactManager:
    def __init__(self):
        self.contacts=[]
    def addContact(self,name,phone):
        contact=Contact(name,phone)
        self.contacts.append(contact)
    def viewContact(self):
        if not self.contacts:
            print("no contact found")
            return
        for contact in self.contacts:
            print(contact.name,contact.phone)
    def insertionSort(self):
        for i in range(1,len(self.contacts)):
            key=self.contacts[i]
            j=i-1
            while j>=0 and self.contacts[j].name>key.name:
                self.contacts[j+1]=self.contacts[j]
                j-=1
            self.contacts[j+1]=key
        self.viewContact()
def main():
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Sort Contacts")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            manager.addContact(name, phone)
            print("Contact added.")
        elif choice == '2':
            manager.viewContact()
        elif choice == '3':
            manager.insertionSort()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()