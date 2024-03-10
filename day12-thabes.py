#function manipulation
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just called a function in python.")

if __name__ == '__main__':
    first_name = str(input("Enter your first name: "))
    last_name = str(input("Enter your last name: "))
    print_full_name(first_name, last_name)