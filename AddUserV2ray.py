import base64
import json
from datetime import datetime, timedelta

class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, username, password, months):
        expiry_date = (datetime.now() + timedelta(days=30 * months)).strftime('%Y-%m-%d')
        self.users.append({"username": username, "password": password, "expiry_date": expiry_date})
        return f"User '{username}' added with expiry date {expiry_date}."
    
    def remove_user(self, username):
        self.users = [user for user in self.users if user["username"] != username]
        return f"User '{username}' removed."
    
    def update_user_date(self, username, months):
        for user in self.users:
            if user["username"] == username:
                user["expiry_date"] = (datetime.now() + timedelta(days=30 * months)).strftime('%Y-%m-%d')
                return f"User '{username}' updated with new expiry date {user['expiry_date']}."
        return f"User '{username}' not found."
    
    def get_users(self, format_type):
        if format_type == "json":
            return json.dumps(self.users, indent=4)
        elif format_type == "base64":
            users_str = json.dumps(self.users)
            return base64.b64encode(users_str.encode()).decode()
        elif format_type == "json_base64":
            users_json = json.dumps(self.users)
            return json.dumps({"base64": base64.b64encode(users_json.encode()).decode()}, indent=4)
        elif format_type == "text":
            return "\n".join([f"Username: {u['username']}, Expiry Date: {u['expiry_date']}" for u in self.users])
        else:
            return "Invalid format. Choose json, base64, json_base64, or text."

# Example usage
if __name__ == "__main__":
    manager = UserManager()
    while True:
        print("1. Add User")
        print("2. Remove User")
        print("3. Update User Date")
        print("4. Get Users")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            months = int(input("Enter number of months: "))
            print(manager.add_user(username, password, months))
        elif choice == "2":
            username = input("Enter username to remove: ")
            print(manager.remove_user(username))
        elif choice == "3":
            username = input("Enter username to update: ")
            months = int(input("Enter number of months: "))
            print(manager.update_user_date(username, months))
        elif choice == "4":
            format_type = input("Choose format (json, base64, json_base64, text): ")
            print(manager.get_users(format_type))
        elif choice == "5":
            break
        else:
            print("Invalid option, try again.")
