import functools


users_db = [
    {"username": "admin", "password": "1234"},
    {"username": "user1", "password": "abcd"},
]

def authenticate():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in users_db:
        if user["username"] == username and user["password"] == password:
            print("Login successful!")
            return True  
    print("Incorrect username or password.")
    return False  

def required_authentication(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not authenticate():  
            print("Access denied!")
            return
        return func(*args, **kwargs)  
    return wrapper


@required_authentication
def backoffice_panel():
    print("Welcome to Backoffice!")


if __name__ == "__main__":
    backoffice_panel()
