from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser(description="Password Strength Checker")
    parser.add_argument("--name", help="Enter your name")
    parser.add_argument("--age", type=int, help="Enter your age")
    parser.add_argument("--pet", help="Enter the name of your pet")

    args = parser.parse_args()
    name = args.name
    age = args.age
    pet = args.pet

    password = input("Enter your password: ")

    strength = check_password_strength(password, name, age, pet)

    if strength >= 3:
        print("Password is strong!")
    else:
        print("Password is weak!")

def check_password_strength(password, name, age, pet):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if name.lower() not in password.lower():
        strength += 1

    if str(age) not in password:
        strength += 1

    if pet.lower() not in password.lower():
        strength += 1

    return strength

if __name__ == "__main__":
    main()