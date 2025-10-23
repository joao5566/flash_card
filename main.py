import tkinter as tk 
import sys,os
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


canvas = tk.Canvas(window,width=900,height=600,bg=BACKGROUND_COLOR, highlightthickness=0)


card_front_img = tk.PhotoImage(file=resource_path("images/card_front.png"))


canvas.create_image(440,300,image=card_front_img)
canvas.grid(row=0,column=0,columnspan=2)

idioma_label = tk.Label()
idioma_label.config(text="Frensh",font=("Arial", 40,"italic"), bg="white", fg="black")
canvas.create_window(450,200, window=idioma_label)

card_front_label = tk.Label()
card_front_label.config(text="teste", font=("Arial", 60,"bold"),  bg="white", fg="black")
canvas.create_window(450,350,window=card_front_label)


wrong_btn_img = tk.PhotoImage(file=resource_path("images/wrong.png"))

wrong_btn = tk.Button(image=wrong_btn_img,highlightthickness=0,borderwidth=0)
wrong_btn.grid(column=0,row=1)

right_btn_img = tk.PhotoImage(file=resource_path("images/right.png"))
right_btn = tk.Button(image=right_btn_img,highlightthickness=0,borderwidth=0)
right_btn.grid(column=1,row=1)

#button = Button(image=my_image, highlightthickness=0)



window.mainloop()



