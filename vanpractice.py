# REGISTRATION SYSTEM (November 8 Practice)

print("===Register your account===")

# USERNAME
name = input("Create your username: ").strip()
while not name.islower() or not name.isalpha:
    print("Username must contain only lowercase letters.")
    name = input("Create your username: ").strip()

# EMAIL ADDRESS
email = input("Enter your email address: ").strip()
while not (email.endswith("@gmail.com") and not email.islower()):
    print("Email must end with @gmail.com and in lowercase.")
    email = input("Enter your email again: ").strip()

# PHONE NUMBER
phone = input("Enter your phone number: ").strip()
while not (phone.startswith("01") and len(phone) != 11):
    print("Phone number must start with 01 and consist of 11 digits.")
    phone = input("Enter your phone number again: ").strip()

# PASSWORD
password = input("Create your password: ").strip()
while not (
    any(x.isdigit() for x in password) and
    any(x.isupper() for x in password) and
    any(x.islower() for x in password) and
    len(password) >= 8
):
    print("\nPassword must contain:")
    print("- At least one uppercase")
    print("- At least one lowercase")
    print("- At lease one digit")
    print("- A minimum of 8 characters")
    password = input("Create your password again: ").strip()
print(f"\nWelcome {name.upper()}! Thank you for joining our community.")

# LOGIN SYSTEM
print("\n===Login to your dashboard===")
attempts = 5
username = input("Enter your username: ").strip()
while username != name and attempts > 1:
    attempts -= 1
    print("Invalid username")
    username = input("Enter your username again: ").strip()
if username != name:
    print("Too many incorrect username. Try again after 3 hours.")
else:
    print("\n===Password===")
    attempts = 5
    your_password = input("Enter your password: ")
    while your_password != password and attempts > 1:
        attempts -= 1
        print(f"Incorrect password! You've {attempts} attempt(s) left.")
        your_password = input("Enter your password again: ")
    if your_password == password:
        print("Login successful! \nWelcome to your Dashboard")
    else:
        print("Too many failed attempts. Try again after 24 hours")



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


