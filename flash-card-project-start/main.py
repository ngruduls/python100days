import random
from tkinter import *
import pandas

# ---------------------------randomness----------------------------------#
data = pandas.read_csv("data/french_words.csv")
print(type(data))
eng_french_dict = data.to_dict('records')
print(eng_french_dict)
total_words = len(eng_french_dict)
def unknown_clicked():
    idx = random.randint(0,total_words - 1)
    fra_word = eng_french_dict[idx]["French"]
    canvas.itemconfig(word_text, text=f"{fra_word}")
    #canvas.itemconfig(your_text_id, text="New Text")
def known_clicked():
    pass
# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

#Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=unknown_clicked)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=known_clicked)
known_button.grid(row=1, column=1)

window.mainloop()
