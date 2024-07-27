import string
import random

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    total = letters + digits
    final_result = ""
    for _ in range(length):
        final_result += random.choice(total)
    return final_result

def main():
    while True:
        print("Enter the password length:")
        length = input()
        
        try:
            length = int(length)
            if length <= 0:
                raise ValueError("Password length must be positive.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
        
        password = generate_password(length)
        print("The password is: " + password)

if __name__ == "__main__":
    main()
