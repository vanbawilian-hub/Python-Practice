# Registration Form

password = "123vanbawi"
attempts = 5
print("\nRegistration Form")
name = input("Enter your name: ").strip()

email = input("\nEnter your email: ").strip()
while not email.endswith("@gmail.com"):
    print("Enter a valid email address.")
    email = input("Enter your email: ").strip()

phone_number = input("\nEnter your phone number: ").strip()
while not (phone_number.startswith("09") and len(phone_number) == 10):
    print("Phone number must start with 09 and must be 10 digit numbers.")
    phone_number = input("Enter your phone number: ").strip()

your_password = input("\nEnter your password: ")
while your_password != password and attempts > 0:
    attempts -= 1
    print(f"Wrong password. You have {attempts} attempts left.")
    your_password = input("Enter your password: ")
if your_password == password:
    print("Thank you for providing your details.")
    print(f"Name: {name} \nEmail: {email} \nPhone number: {phone_number}")
else:
    print("Access denied. Too many attempts.")


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
    print("Too many wrong username. Come back after 24 hours")

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
        password = input(f"You've {attempts} left. Try again: ").strip()
    if password == PASSWORD:
        print("Login Successful!")
    else:
        print("Too many attempts. Access Denied")
        exit("Come back after 3 days")
