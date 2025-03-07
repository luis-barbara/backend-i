def required_authentication(func):
    def wrapper(*args, **kwargs):
        user_authentication = False
        if not user_authentication:
            print("Access denied")
            return
        return func(*args, **kwargs)
    return wrapper


@required_authentication
def backoffice_panel():
    print("Welcome to backoffice")


if __name__ == "__main__":
    backoffice_panel()

