import os
import re

# Helper function to make file names safe
def safe_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

# Read the letter template
with open('Mail Merge Project Start\\Input\\Letters\\starting_letter.txt', 'r', encoding='utf-8') as file:
    letter_template = file.read()

# Read the list of names
with open('Mail Merge Project Start\\Input\\Names\\invited_names.txt', 'r', encoding='utf-8') as file:
    names = [line.strip() for line in file.readlines()]

# Make sure output folder exists
output_dir = 'Mail Merge Project Start\\Output\\ReadyToSend'
os.makedirs(output_dir, exist_ok=True)

# Create a personalized letter for each name
for name in names:
    personalized_letter = letter_template.replace('[name]', name)
    filename = f"message_{safe_filename(name)}.txt"
    output_path = os.path.join(output_dir, filename)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(personalized_letter)
