import tkinter as tk 
import sys, os
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_FRENCH = ""  # Corrigido o nome da variável
CURRENT_ENGLISH = ""
flip_timer = None  # Para controlar o temporizador

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

window = tk.Tk()
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card App")



#---------------Salvando os dados -----------------------# 

words_to_learn_dic = {
        "French":[],
        "English":[]
        }











def random_word():
    global CURRENT_FRENCH, CURRENT_ENGLISH
    try:
        data = pd.read_csv(resource_path("data/french_words.csv"))
        df = pd.DataFrame(data)
        random_index = random.randint(0, len(df) - 1)
        CURRENT_FRENCH = df.loc[random_index, "French"]
        CURRENT_ENGLISH = df.loc[random_index, "English"]
        df_save = pd.DataFrame(words_to_learn_dic)
        df_save.to_csv("words_to_learn_dic.csv",index=False)
    except Exception as e:
        print(f"Erro ao carregar palavras: {e}")

def flip_card():
    # Vira o cartão para mostrar a tradução em inglês
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(TITLE, text="English", fill="white")
    canvas.itemconfig(WORD, text=CURRENT_ENGLISH, fill="white")

def new_card():
    global flip_timer
    # Cancela o temporizador anterior se existir
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    
    # Seleciona uma nova palavra
    random_word()
    
    # Mostra o lado francês do cartão
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(TITLE, text="French", fill="black")
    canvas.itemconfig(WORD, text=CURRENT_FRENCH, fill="black")
   
    words_to_learn_dic["French"].append(CURRENT_FRENCH)
    words_to_learn_dic["English"].append(CURRENT_ENGLISH)
    print(words_to_learn_dic)
    # Configura o temporizador para virar o cartão após 3 segundos
    flip_timer = window.after(3000, flip_card)

# Configuração do Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Carrega as imagens
card_front_img = tk.PhotoImage(file=resource_path("images/card_front.png"))
card_back_img = tk.PhotoImage(file=resource_path("images/card_back.png"))

# Cria a imagem do cartão
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Cria os textos
TITLE = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
WORD = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Botões
wrong_btn_img = tk.PhotoImage(file=resource_path("images/wrong.png"))
wrong_btn = tk.Button(image=wrong_btn_img, highlightthickness=0, borderwidth=0, command=new_card)
wrong_btn.grid(column=0, row=1)

right_btn_img = tk.PhotoImage(file=resource_path("images/right.png"))
right_btn = tk.Button(image=right_btn_img, highlightthickness=0, borderwidth=0, command=new_card)
right_btn.grid(column=1, row=1)

# Inicia com o primeiro cartão
new_card()




window.mainloop()
