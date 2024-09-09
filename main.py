import json
import random
import string

class PasswordManager:
    #constructor called
    def __init__(self):
        self.password_file = "passwords.json"       #sets the file 
        self.passwords = self.inputPasswords()      #inputs all the passwords from the file to passwords variable

    def inputPasswords(self):
       #checks if the file is present else returns error 
        try:
            with open(self.password_file, 'r') as file:        #opens file in read mode and copies its content to psswords variable
                return json.load(file)
        except FileNotFoundError:
            return {}
            #if file not found returns empty list

    def savePasswords(self):
        # open the json file in write mode and updates the file with the changes
        with open(self.password_file, 'w') as file:
            json.dump(self.passwords, file, indent=4)

    def checkPassword(self, password):
        # checks if the password is secure i.e strength of the password . if not strong enought then returns false and troubles the user until a strong password is not set
        if len(password) < 8:                            
            return False, "Password must be at least 8 characters long."
        elif not any(char.isdigit() for char in password):
            return False, "Password must contain at least one digit."
        elif not any(char.islower() for char in password):
            return False, "Password must contain at least one lowercase letter."
        elif not any(char.isupper() for char in password):
            return False, "Password must contain at least one uppercase letter."
        elif not any(char in string.punctuation for char in password):
            return False, "Password must contain at least one special character."
        else:
            return True, "Valid password."

    def addPassword(self):
        # Add  a new password to the josn file . first input the password from the user , check the password if it is secure then save it in the file
        account_name = input("Enter the Account Name: ")
        username = input("Enter Username: ")
        while True:
            password = input("Enter the Password: ")
            valid, msg = self.checkPassword(password)
            if valid:
                break
            else:
                print(msg)
        self.passwords[account_name] = {"username": username, "password": password}
        self.savePasswords()
        print("Password added to the directory file")

    def displayAll(self):
        # view all saved passwords from the file
        if not self.passwords:
            print("You do not have any password saved")
        else:
            for account in sorted(self.passwords):  # Sort accounts alphabetically
                print(f"Account: {account}, Username: {self.passwords[account]['username']}, Password: {self.passwords[account]['password']}")

    def displayOne(self, account_name):
        # Reveal the password for a specific account do linear search in file and display the password
        if account_name in self.passwords:
            print(f"Password: {self.passwords[account_name]['password']}")
        else:
            print("Account not found.")

    def update_password(self, account_name):
        # Update the password for an existing account 
        if account_name in self.passwords:
            while True:
                new_password = input("Enter new Password: ")
                valid, msg = self.checkPassword(new_password)     #validate the password and addd it to directory
                if valid:
                    break
                else:
                    print(msg)
            self.passwords[account_name]['password'] = new_password
            self.savePasswords()
            print(f"Password updated for {account_name}.")
        else:
            print("Account not focund. Try again with another name")

    def delete_password(self, account_name):
        # delete a password entry from the directory
        if account_name in self.passwords:
            del self.passwords[account_name]
            self.savePasswords()
            print(f"{account_name} deleted.")
        else:
            print("Account not found.")

    def generate_password(self, length=12):
        # Generate a random password with the specified length inputed form the user
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        print(f"new generated Password: {password}")
        return password

def main():
    manager = PasswordManager()
    while True:
        print("\n1. Add new PAssword to the directory\n2. View all the passwords\n3. view password for a single username\n4. Update a password\n5. Delete a password form the directory\n6. Generate new password\n7. Exit the program")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            manager.addPassword()
        elif choice == 2:
            manager.displayAll()
        elif choice == 3:
            account_name = input("Enter account name: ")
            manager.displayOne(account_name)
        elif choice == 4:
            account_name = input("Enter account name: ")
            manager.update_password(account_name)
        elif choice == 5:
            account_name = input("Enter account name: ")
            manager.delete_password(account_name)
        elif choice == 6:
            length = int(input("Enter password length: "))
            manager.generate_password(length)
        elif choice == 7:
            print("Exiting the code")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
