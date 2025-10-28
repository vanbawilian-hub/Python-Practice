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
