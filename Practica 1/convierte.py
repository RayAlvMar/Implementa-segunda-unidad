import tkinter as tk
from tkinter import messagebox

def convertir_a_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario

def convertir_a_octal(numero):
    if numero == 0:
        return "0"
    octal = ""
    while numero > 0:
        octal = str(numero % 8) + octal
        numero //= 8
    return octal

def convertir_a_hexadecimal(numero):
    if numero == 0:
        return "0"
    digitos = "0123456789ABCDEF"
    hexadecimal = ""
    while numero > 0:
        resto = numero % 16
        hexadecimal = digitos[resto] + hexadecimal
        numero //= 16
    return hexadecimal

def realizar_conversion(tipo):
    entrada = entrada_numero.get()
    if not entrada.isdigit():
        messagebox.showerror("Error", "Por favor, ingresa solo números enteros positivos.")
        return
    
    numero = int(entrada)
    
    if tipo == "bin":
        resultado = convertir_a_binario(numero)
    elif tipo == "oct":
        resultado = convertir_a_octal(numero)
    elif tipo == "hex":
        resultado = convertir_a_hexadecimal(numero)
    else:
        resultado = "Error en tipo"

    etiqueta_resultado.config(text="Resultado: " + resultado)
ventana = tk.Tk()
ventana.title("Conversor de Números")
ventana.geometry("300x250")
tk.Label(ventana, text="Ingresa un número entero:").pack(pady=10)
entrada_numero = tk.Entry(ventana, justify="center")
entrada_numero.pack()
tk.Button(ventana, text="Convertir a Binario", command=lambda: realizar_conversion("bin")).pack(pady=5)
tk.Button(ventana, text="Convertir a Octal", command=lambda: realizar_conversion("oct")).pack(pady=5)
tk.Button(ventana, text="Convertir a Hexadecimal", command=lambda: realizar_conversion("hex")).pack(pady=5)
etiqueta_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=15)
ventana.mainloop()