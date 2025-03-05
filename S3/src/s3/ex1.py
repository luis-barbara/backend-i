class Product:
    def __init__(self, name):
        self.name = name
       
    def __str__(self):
        return f"Product: {self.name}"


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"


class OnlineStore:
    def __init__(self):
        self.users = []
        self.products = []
        self.stock = ["batatas", "laranjas", "bananas"]

    def register_user(self):
        username = input("Enter your username: ")
        if any(user.username == username for user in self.users):
            print("User already exists")
        email = input("Enter your email: ")
        if any(user.email == email for email in self.users):
            print("Email already registered")
            return
        user = User(username, email)
        self.users.append(user)
        print(f"User {username} registered successfully.")

    def add_product(self):
        product_name = input("Enter the product name: ")
        if product_name not in self.products:
            print("Product does not exist in stock")
            return
        product = Product(product_name)
        self.products.append(product)
        print(f"Product '{product_name}' added successfully.")
    


store = OnlineStore()


store.register_user()
store.add_product()