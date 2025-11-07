# LOGIN SYSTEM (Nov. 7 practice)

USER_NAME = "vanbawilian"
EMAIL = "vanbawi@gmail.com"
PASSWORD = "Vanbawi25"

print("======USERNAME VALIDATION======")
attempts = 5
user_name = input("Enter your username: ").strip().lower()
while user_name != USER_NAME and attempts > 1:
    attempts -= 1
    print("Invalid username")
    if any(x.isupper() for x in user_name) or any(x.isdigit() for x in user_name):
        print("Username must contain only lowercase alphabets")
    user_name = input("Try again: ").strip().lower()
if user_name != USER_NAME:
    print("Too many incorrect username. Come back after 24 hours")

else:
    print("\n=====EMAIL VALIDATION=====")

    email = input("Enter your email: ").strip().lower()
    while email != EMAIL:
        print("Invalid email address")
        if not email.endswith("@gmail.com"):
            print("Email must end with @gmail.com")
        email = input("Enter your email again: ").strip().lower()

    print("\n=====PASSWORD VALIDATION=====")
    attempts = 5
    password = input("Enter your password: ").strip()
    while password != PASSWORD and attempts > 1:
        attempts -= 1
        print("Invalid password")
        password = input(f"You've {attempts} attempt(s) left. Try again: ").strip()
    if password == PASSWORD:
        print("Login Successful!")
    else:
        print("Too many failed attempts. Access Denied")
        exit("Come back after 3 days")

