def encode(password):
    num_list = [int(char) for char in password]
    for i in range(len(num_list)):
        num_list[i] += 3
    password_encoded = ''.join([str(num) for num in num_list])
    return password_encoded


def decode(password):
    decoded = ''.join(str(int(char) - 3) for char in password)
    return decoded


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    password = input("Please enter the password to encode: ")

    while True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {password}.")
        elif option == 3:
            break


if __name__ == "__main__":
    menu()

