import json
import os
import getpass
import random
import string
class PasswordManager:
    def __init__(self):
        self.password_file = "passwords.json"
        self.passwords = self.load_passwords()

    def load_passwords(self):
        """Load passwords from a JSON file if it exists, otherwise return an empty dictionary."""
        if not os.path.exists(self.password_file):
            return {}
        with open(self.password_file, 'r') as file:
            return json.load(file)

    def save_passwords(self):
        """Save the passwords to a JSON file."""
        with open(self.password_file, 'w') as file:
            json.dump(self.passwords, file, indent=4)

    def add_password(self):
        """Add a new password entry."""
        account_name = input("Account Name: ")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        self.passwords[account_name] = {"username": username, "password": password}
        self.save_passwords()
        print("Password added successfully!")

    def view_passwords(self):
        """View all saved account names and usernames."""
        if not self.passwords:
            print("No passwords saved.")
        else:
            for account, details in self.passwords.items():
                print(f"Account: {account}, Username: {details['username']}")

    def reveal_password(self, account_name):
        """Reveal the password for a specific account."""
        if account_name not in self.passwords:
            print(f"Account '{account_name}' not found.")
        else:
            print(f"Password for {account_name}: {self.passwords[account_name]['password']}")

    def delete_password(self, account_name):
        """Delete a password entry."""
        if account_name in self.passwords:
            confirm = input(f"Are you sure you want to delete {account_name}? (y/n): ")
            if confirm.lower() == 'y':
                del self.passwords[account_name]
                self.save_passwords()
                print(f"{account_name} deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Account '{account_name}' not found.")

    def update_password(self, account_name):
        """Update the password for an existing account."""
        if account_name in self.passwords:
            new_password = getpass.getpass("Enter new password: ")
            self.passwords[account_name]['password'] = new_password
            self.save_passwords()
            print(f"{account_name} updated successfully.")
        else:
            print(f"Account '{account_name}' not found.")

    def generate_password(self, length=12):
        """Generate a strong random password using a generalized for loop."""
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''  # Start with an empty password string

        # Use a for loop to generate the password character by character
        for i in range(length):
            random_char = random.choice(characters)  # Choose a random character
            password += random_char  # Append the character to the password

        print(f"Generated Password: {password}")
        return password


def main():
    manager = PasswordManager()

    while True:
        print("\n1.add\n2.view\n3.print\n4.update\n5.delete\n6.generateRandom\n7.exit")
        command = int(input("Enter your choice: "))

        if command == 1:
            manager.add_password()
        elif command == 2:
            manager.view_passwords()
        elif command == 3:
            account_name = input("Enter account name to reveal: ")
            manager.reveal_password(account_name)
        elif command == 4:
            account_name = input("Enter account name to update: ")
            manager.update_password(account_name)
        elif command == 5:
            account_name = input("Enter account name to delete: ")
            manager.delete_password(account_name)
        elif command == 6:
            length = int(input("Enter password length: "))
            manager.generate_password(length)
        elif command == 7:
            print("Exiting the program")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == '__main__':
    main()
