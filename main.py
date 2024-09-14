from paint import logo, created_by
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text

# ANSI escape codes for colors
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(f"{RED}{logo}{RESET}")
print(f"\n{YELLOW}{created_by}{RESET}\n")  # Print the created by text in yellow

should_end = False
while not should_end:
    print("Choose an option:")
    print("1. Encode a message")
    print("2. Decode a message")
    
    # Input validation for direction
    while True:
        direction = input("\nEnter 1 or 2:\n")
        if direction in ['1', '2']:
            break
        else:
            print("Invalid option. Please enter 1 for encode or 2 for decode.")

    text = input("Type your message:\n").lower()
    
    # Input validation for shift
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Please enter a valid number for the shift.")

    shift = shift % 26  # Normalize the shift value
    cipher_direction = "encode" if direction == '1' else "decode"
    
    result = caesar(start_text=text, shift_amount=shift, cipher_direction=cipher_direction)
    print(f"\nHere's the {cipher_direction}d result: {result}\n")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_end = True
        print("Thank You Very Much!")
