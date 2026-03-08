import pandas
from turtle import Screen, colormode
import CodedName as cdn

# --- Load data from CSV ---
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for _, row in nato_df.iterrows()}

# --- Setup screen ---
screen = Screen()
screen.bgcolor("white")
screen.title("🇨🇴 What's your Colombian-coded name?")
screen.setup(width=800, height=800)
colormode(255)
screen.tracer(0)

# --- Create coded name writer ---
coded = cdn.CodedName()
coded.draw_flag_banner()
coded.draw_title_text()
screen.update()

# --- Main loop for multiple names ---
keep_going = True
while keep_going:
    user_name = screen.textinput(
        title="Tu nombre, llave!",
        prompt="What's your name, panita?"
    )

    if not user_name:
        break

    # Generate code words
    code_list = [nato_dict[letter.upper()] for letter in user_name if letter.upper() in nato_dict]

    # Display codes
    for code in code_list:
        coded.write_name(code)
        screen.update()

    # Ask to try again
    answer = screen.textinput(
        title="¿Otra vuelta?",
        prompt="Want to try with another name, parcero? (yes/no)"
    )

    if answer is None or answer.strip().lower() not in ["yes", "y", "si", "sí"]:
        keep_going = False
    else:
        coded.reset_position()

# --- Say goodbye ---
coded.show_goodbye()
screen.update()
screen.exitonclick()
