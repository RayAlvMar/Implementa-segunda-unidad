import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
#esto para que leyera las imagenes que no las leia :(
os.chdir(os.path.dirname(os.path.abspath(__file__)))

palabras = ["python", "ahorcado", "computadora", "programar", "teclado", "pantalla", "algoritmo", "variable", "código", "juego", "letras", "trevi", "estrella", "payan", "java", "dificultad", "octal"]
palabra = random.choice(palabras).upper()
letras_adivinadas = []
intentos = 0

def actualizar_imagen():
    global imagen_label, imagenes, intentos
    imagen = imagenes[intentos]
    imagen_label.config(image=imagen)
    imagen_label.image = imagen

def mostrar_palabra():
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def actualizar_palabra():
    palabra_label.config(text=mostrar_palabra())

def verificar_letra(letra):
    global intentos
    boton_letras[letra].config(state="disabled")
    if letra in palabra:
        letras_adivinadas.append(letra)
        actualizar_palabra()
        if all(l in letras_adivinadas for l in palabra):
            messagebox.showinfo("¡Ganaste!", "Has adivinado la palabra.")
            desactivar_teclado()
    else:
        intentos += 1
        actualizar_imagen()
        if intentos == 6:
            palabra_label.config(text=palabra)  #error
            messagebox.showinfo("Perdiste", f"La palabra era: {palabra}")
            desactivar_teclado()

def desactivar_teclado():
    for boton in boton_letras.values():
        boton.config(state="disabled")

def reiniciar_juego():
    global palabra, letras_adivinadas, intentos
    palabra = random.choice(palabras).upper()
    letras_adivinadas = []
    intentos = 0
    actualizar_imagen()
    actualizar_palabra()
    for boton in boton_letras.values():
        boton.config(state="normal")

ventana = tk.Tk()
ventana.title("Juego del Ahorcado")

#error
imagenes = []
for i in range(7):
    try:
        img = Image.open(f"imagen{i}.JPG")
        img = img.resize((200, 200))
        imagenes.append(ImageTk.PhotoImage(img))
    except:
        print(f"Error cargando imagen{i}.JPG")  #error
        imagenes.append(None)

imagen_label = tk.Label(ventana)
imagen_label.pack()
actualizar_imagen()

palabra_label = tk.Label(ventana, text=mostrar_palabra(), font=("Courier", 24))
palabra_label.pack(pady=10)

marco_teclado = tk.Frame(ventana)
marco_teclado.pack()

boton_letras = {}
letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fila = 0
col = 0

for letra in letras:
    boton = tk.Button(marco_teclado, text=letra, width=4, height=2,
                      command=lambda l=letra: verificar_letra(l))
    boton.grid(row=fila, column=col, padx=2, pady=2)
    boton_letras[letra] = boton
    col += 1
    if col == 9:
        fila += 1
        col = 0

#error
boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
boton_reiniciar.pack(pady=10)

ventana.mainloop()