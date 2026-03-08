##################### Birthday Wisher Project ######################

import random
import pandas as pd
import smtplib
import datetime as dt

# ---------------------------- STEP 1: READ BIRTHDAY DATA ---------------------------- #
# Load the birthdays.csv file into a pandas DataFrame.
# Each record should include: name, email, year, month, and day.
data_birthdays = pd.read_csv("birthdays.csv")
birthdays_list = data_birthdays.to_dict(orient="records")

# ---------------------------- STEP 2: CHECK TODAY'S DATE ---------------------------- #
# Get the current month and day to compare with each birthday.
today = dt.datetime.now()
today_month = today.month
today_day = today.day

# Initialize a flag to check if today matches anyone's birthday.
is_birthday = False

# Iterate through the list of birthdays.
for person in birthdays_list:
    if person["month"] == today_month and person["day"] == today_day:
        birthday_person = person
        is_birthday = True
        break  # Stop the loop once a match is found

# ---------------------------- STEP 3: GENERATE LETTER ---------------------------- #
# If today is someone’s birthday, randomly pick one of the letter templates.
if is_birthday:
    letter_number = random.randint(1, 3)
    with open(f"./letter_templates/letter_{letter_number}.txt") as letter_file:
        letter_contents = letter_file.read()
        # Replace placeholder [NAME] with the actual name.
        personalized_letter = letter_contents.replace("[NAME]", birthday_person["name"])
        # Optionally, replace the sender name with yours.
        personalized_letter = personalized_letter.replace("Angela", "Sebas")

        # Save the generated letter to a new file (optional).
        with open(f"./birthday_letters/letter_for_{birthday_person['name']}.txt", mode="w") as output_file:
            output_file.write(personalized_letter)

# ---------------------------- STEP 4: SEND EMAIL ---------------------------- #
# If today is a birthday, send the email using SMTP.

    # Replace with your actual email and use an environment variable or app password for safety.
    my_email = "youremail@example.com"
    my_password = "your_app_password"  # Never hardcode passwords in code!

    # Connect securely to the email server.
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday! 🎉\n\n{personalized_letter}"
        )

        print(f"Birthday email sent successfully to {birthday_person['name']}!")
else:
    print("No birthdays today.")
