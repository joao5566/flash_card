import tkinter as tk 
import sys,os
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

window = tk.Tk()
window.configure(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flash Card App")




def random_word():

    data = pd.read_csv(resource_path("data/french_words.csv"))
    df = pd.DataFrame(data)
    
    return df.loc[random.randint(0,101),"French"]
    

def update_word_txt():
    new_word = random_word()
    canvas.itemconfig(word,text=new_word)

canvas = tk.Canvas(width=800,height=526, background=BACKGROUND_COLOR, highlightthickness=0)


card_front_img = tk.PhotoImage(file=resource_path("images/card_front.png"))


canvas.create_image(400,263,image=card_front_img)
canvas.grid(row=0,column=0,columnspan=2)

canvas.create_text(400,150,text="title",font=("Arial", 40,"italic"))
word = canvas.create_text(400,263,text=random_word(),font=("Arial", 60,"bold"))


wrong_btn_img = tk.PhotoImage(file=resource_path("images/wrong.png"))

wrong_btn = tk.Button(image=wrong_btn_img,highlightthickness=0,borderwidth=0,command=update_word_txt)
wrong_btn.grid(column=0,row=1)

right_btn_img = tk.PhotoImage(file=resource_path("images/right.png"))
right_btn = tk.Button(image=right_btn_img,highlightthickness=0,borderwidth=0,command=update_word_txt)
right_btn.grid(column=1,row=1)

#button = Button(image=my_image, highlightthickness=0)



window.mainloop()



