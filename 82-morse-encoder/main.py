"""
Main entry point for the Morse Code Converter program.

This file handles the command line interface where the user can choose
different actions like encoding text to Morse code or decoding Morse
code back into readable text.
"""

from morse_converter import MorseConverter

# Create converter instance
converter = MorseConverter()


def display_help():
    """
    Displays instructions about how to use the program.
    Includes examples of valid inputs.
    """
    print("\n" + "*" * 120)
    print("\nWelcome! Here you can convert Plain Text to Morse Code and vice versa.\n")

    print("Plain Text")
    print("Allowed characters: letters, numbers, punctuation and spaces.")
    print('Example: "This is a simple message 4 the converter!"\n')

    print("Morse Code")
    print("Letters must be separated by spaces.")
    print("Symbols used:")
    print("  .  = dot (dih)")
    print("  -  = dash (dah)")
    print("  /  = space between words")

    print('Example: "... .- -- / .---- ..--- ...-- / .-.-.- -.-.-- ..--.."\n')
    print("*" * 120 + "\n")


# Show instructions when program starts
display_help()

# Main interaction loop
while True:

    choice = input(
        "Choose an option:\n"
        "0 → Show help\n"
        "1 → Convert Plain Text to Morse Code\n"
        "2 → Convert Morse Code to Plain Text\n"
        "9 → Exit program\n"
        "Your choice: "
    )

    if choice == "0":
        display_help()
        continue

    elif choice == "1":
        text = input("Enter plain text: ")
        result = converter.morse_encode(text)

    elif choice == "2":
        text = input("Enter Morse code: ")
        result = converter.morse_decode(text)

    elif choice == "9":
        print("\nAlright! See you later. Keep coding! 🚀\n")
        break

    else:
        print("\nOops! That option is not valid. Try again.\n")
        continue

    print(f"\nConverted Result:\n{result}\n")