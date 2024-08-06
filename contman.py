class ContMan:
    def __init__(self):
        self.contacts = {}
        
    def inscont(self):
        name1 = input("Enter name (less than 20 characters): ")
        if len(name1) < 20:
            if name1 not in self.contacts:
                no1 = input("Enter contact no. (10 digits): ")
                if len(no1) == 10 and no1.isdigit():
                    self.contacts[name1] = no1
                    print("/*Contact added successfully.*/")
                else:
                     print("/*Check the length of number*/")
            else:
                print("/*This contact name already exists.*/")
        else:
            print("/*Check the length of Name*/")
            
    def updcont(self):
        name1 = input("Enter name: ")
        if len(name1) < 20:
            if name1 in self.contacts:
                     no1 = input("Enter new contact no. (10 digits): ")
                     if len(no1) == 10 and no1.isdigit():
                         self.contacts[name1] = no1
                         print("/*Contact updated successfully.*/")
                     else:
                         print("/*Check the length of number*/")
            else:
                print("/*This contact doesn't exist.*/")
        else:
            print("/*Check the length of name*/")
            
    def searccont(self):
        name2 = input("Enter the name of contact: ")
        if name2 in self.contacts:
            print(f"Contact number: {self.contacts[name2]}")
        else:
            print("/*There is no contact with this name*/")
            y = int(input("Press 1 to save this contact: "))
            if y == 1:
                self.inscont()
                
    def delecont(self):
        name2 = input("Enter the name of contact: ")
        if name2 in self.contacts:
            del self.contacts[name2]
            print("Deleted successfully.")
        else:
            print("Contact not found.")
            
    def viewconts(self):
        if self.contacts:
            print("All contacts:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("/*No contacts available.*/")

def main():
    obj = ContMan()
    while True:
        print('1. Insert a contact \n2. Update a contact \n3. Search for a contact \n4. Delete a contact \n5. View all \n6. Exit')
        try:
            x = int(input("Enter your choice: "))
            if x == 1:
                obj.inscont()
            elif x == 2:
                obj.updcont()
            elif x == 3:
                obj.searccont()
            elif x == 4:
                obj.delecont()
            elif x == 5:
                obj.viewconts()
            elif x == 6:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
if __name__ == "__main__":
    main()

