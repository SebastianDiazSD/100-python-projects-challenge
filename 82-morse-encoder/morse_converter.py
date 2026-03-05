"""
Morse Code conversion logic.

This class is responsible for translating:
- Plain text → Morse code
- Morse code → Plain text
"""

import re
from morse_loader import MorseLoader


class MorseConverter:
    """
    Handles encoding and decoding between plain text and Morse code.
    """

    def __init__(self):
        # Load Morse code dictionary
        self.morse_table = MorseLoader().data

        # Regular expression to validate Morse symbols
        self.morse_pattern = re.compile(r"^[\-.]+$")

    def morse_encode(self, text: str) -> str:
        """
        Converts normal text into Morse code.

        Parameters
        ----------
        text : str
            Text written using letters, numbers or punctuation.

        Returns
        -------
        str
            Morse code representation of the text.
        """

        morse_result = ""

        # Convert input to uppercase so it matches dictionary keys
        for character in text.upper():

            # Handle spaces between words
            if character.isspace():
                morse_result += "/"

            else:
                try:
                    morse_result += self.morse_table[character]
                except KeyError:
                    return f"!!! Unsupported character detected: {character} !!!"

            # Separate each Morse symbol with a space
            morse_result += " "

        return morse_result.strip()

    def morse_decode(self, code: str) -> str:
        """
        Converts Morse code back into readable text.

        Parameters
        ----------
        code : str
            Morse code string using '.', '-' and '/'.

        Returns
        -------
        str
            Decoded plain text.
        """

        plain_text = ""

        # Split Morse symbols using spaces
        for symbol in code.split():

            # "/" represents a space between words
            if symbol == "/":
                plain_text += " "

            # Check if the symbol only contains valid Morse characters
            elif self.morse_pattern.match(symbol):

                # Find the corresponding letter
                for letter, morse in self.morse_table.items():
                    if morse == symbol:
                        plain_text += letter
                        break

            else:
                return f"!!! Invalid Morse symbol: {symbol} !!!"

        return plain_text