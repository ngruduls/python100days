import random
from pathlib import Path
from tkinter import *
import pandas

# ---------------------------randomness----------------------------------#
to_learn = {}
# try:
#     data = pandas.read_csv("data/words_to_learn.csv")
# except FileNotFoundError:
#     original_data = pandas.read_csv("data/french_words.csv")
#     to_learn = original_data.to_dict('records')
# else:
#     to_learn = data.to_dict('records')
path = Path("data/words_to_learn.csv")
if path.is_file():
    data = pandas.read_csv("data/words_to_learn.csv")
else:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict('records')
idx = 0
flip_action = None
first_run = None
def next_card():
    global idx
    global flip_action
    if flip_action != None:
        window.after_cancel(flip_action)
    total_words = len(to_learn)
    idx = random.randint(0,total_words - 1)
    fra_word = to_learn[idx]["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{fra_word}", fill="black")
    canvas.itemconfig(background_image, image=card_front)
    flip_action = window.after(3000, flip_card)
def flip_card():
    eng_word = to_learn[idx]["English"]
    # to change the image
    canvas.itemconfig(background_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{eng_word}", fill="white")
    # cancel flipping
    #window.after_cancel(flip_action)
def is_known():
    to_learn.remove(to_learn[idx])
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
background_image = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

#Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
