import tkinter as tk
import random
from PIL import Image, ImageTk

palabras = ['python', 'ahorcado', 'juego', 'ventana', 'computadora', 'programa']
palabra_secreta = random.choice(palabras).lower()
letras_adivinadas = []
errores = 0

imagenes = [ImageTk.PhotoImage(Image.open(f"imagen{i}.jpg")) for i in range(7)] 

ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("600x500")

imagen_label = tk.Label(ventana)
imagen_label.pack()

palabra_label = tk.Label(ventana, font=("Arial", 20))
palabra_label.pack(pady=10)

estado_label = tk.Label(ventana, text="", font=("Arial", 14))
estado_label.pack(pady=5)

teclado_frame = tk.Frame(ventana)
teclado_frame.pack()

def mostrar_palabra():
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    palabra_label.config(text=palabra_mostrada.strip())

def presionar_letra(letra, boton):  #error
    global errores
    boton.config(state="disabled")
    if letra in palabra_secreta:
        letras_adivinadas.append(letra)
    else:
        errores += 1
        if errores >= len(imagenes):  #error
            errores = len(imagenes) - 1
    actualizar_juego()

def actualizar_juego():
    imagen_label.config(image=imagenes[errores])
    mostrar_palabra()
    
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        estado_label.config(text="¡Ganaste!")
        deshabilitar_botones()
    elif errores == len(imagenes) - 1:
        estado_label.config(text=f"¡Perdiste! La palabra era: {palabra_secreta}")
        deshabilitar_botones()

def deshabilitar_botones():
    for boton in botones:
        boton.config(state="disabled")

def reiniciar_juego():
    global palabra_secreta, letras_adivinadas, errores
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = []
    errores = 0
    for boton in botones:
        boton.config(state="normal")
    estado_label.config(text="")
    mostrar_palabra()
    imagen_label.config(image=imagenes[errores])

botones = []
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
for i, letra in enumerate(alfabeto):
    boton = tk.Button(teclado_frame, text=letra, width=3, font=("Arial", 12))
    boton.grid(row=i//9, column=i%9, padx=2, pady=2)
    boton.config(command=lambda l=letra.lower(), b=boton: presionar_letra(l, b))  #error
    botones.append(boton)

reiniciar_btn = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
reiniciar_btn.pack(pady=10)

mostrar_palabra()
imagen_label.config(image=imagenes[errores])
ventana.mainloop()