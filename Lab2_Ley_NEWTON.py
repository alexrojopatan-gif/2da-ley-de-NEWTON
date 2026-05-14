import tkinter as tk
from tkinter import messagebox

# =========================================================
# CONFIGURACIÓN PRINCIPAL
# =========================================================

ventana = tk.Tk()
ventana.title("Sistema de Poleas - Segunda Ley de Newton (Sistemas-UMG)")
ventana.geometry("1100x620")
ventana.config(bg="#DCE8F5")
ventana.resizable(False, False)

# =========================================================
# VARIABLES
# =========================================================

resultado_texto = tk.StringVar()

# =========================================================
# FUNCIÓN PARA DIBUJAR EL SISTEMA
# =========================================================

def dibujar_sistema(y1, y2):

    canvas.delete("all")

# -----------------------------------------------------
# FONDO PARA RESULTADOS
# -----------------------------------------------------

    canvas.create_rectangle(
        35, 15,
        210, 270,
        fill="#89FD6C",
        outline="darkblue",
        width=2
    )

    # Título
    canvas.create_text(
        125,
        40,
        text="RESULTADOS",
        font=("Arial", 15, "bold"),
        fill="darkblue"
    )

    # Texto resultados
    canvas.create_text(
        125,
        75,
        text=resultado_texto.get(),
        font=("Arial", 11, "bold"),
        fill="blue",
        justify="center",
        anchor="n"
    )

    # -----------------------------------------------------
    # BASE SUPERIOR
    # -----------------------------------------------------

    canvas.create_rectangle(
        240, 30,
        420, 50,
        fill="gray30"
    )

    # -----------------------------------------------------
    # POLEA
    # -----------------------------------------------------

    centro_x = 330
    centro_y = 120
    radio = 55

    # Polea exterior
    canvas.create_oval(
        centro_x - radio,
        centro_y - radio,
        centro_x + radio,
        centro_y + radio,
        fill="gray60",
        width=4
    )

    # Centro polea
    canvas.create_oval(
        centro_x - 10,
        centro_y - 10,
        centro_x + 10,
        centro_y + 10,
        fill="black"
    )

    # -----------------------------------------------------
    # CUERDA
    # -----------------------------------------------------

    # Lado izquierdo
    canvas.create_line(
        275, y1,
        275, 120,
        width=5,
        fill="#D28B00"
    )

    # Curva superior
    canvas.create_arc(
        275, 65,
        385, 175,
        start=180,
        extent=180,
        style="arc",
        width=5,
        outline="#D28B00"
    )

    # Lado derecho
    canvas.create_line(
        385, 120,
        385, y2,
        width=5,
        fill="#D28B00"
    )

    # -----------------------------------------------------
    # BLOQUE 1
    # -----------------------------------------------------

    canvas.create_rectangle(
        220, y1,
        325, y1 + 90,
        fill="red",
        width=3
    )

    canvas.create_text(
        275,
        y1 + 45,
        text=f"{entry_m1.get()} kg",
        fill="white",
        font=("Arial", 16, "bold")
    )

    # -----------------------------------------------------
    # BLOQUE 2
    # -----------------------------------------------------

    canvas.create_rectangle(
        335, y2,
        440, y2 + 90,
        fill="blue",
        width=3
    )

    canvas.create_text(
        385,
        y2 + 45,
        text=f"{entry_m2.get()} kg",
        fill="white",
        font=("Arial", 16, "bold")
    )

# =========================================================
# FUNCIÓN DE ANIMACIÓN
# =========================================================

def animar(direccion):

    y1 = 250
    y2 = 250

    LIMITE_SUPERIOR = 190
    LIMITE_INFERIOR = 350

    for i in range(90):

        if direccion == "bloque1":

            # Bloque 1 baja
            if y1 < LIMITE_INFERIOR:
                y1 += 2

            # Bloque 2 sube
            if y2 > LIMITE_SUPERIOR:
                y2 -= 2

        else:

            # Bloque 1 sube
            if y1 > LIMITE_SUPERIOR:
                y1 -= 2

            # Bloque 2 baja
            if y2 < LIMITE_INFERIOR:
                y2 += 2

        dibujar_sistema(y1, y2)

        ventana.update()
        canvas.after(20)

# =========================================================
# FUNCIÓN DE CÁLCULO
# =========================================================

def calcular():

    try:

        m1 = float(entry_m1.get())
        m2 = float(entry_m2.get())

        if m1 <= 0 or m2 <= 0:

            messagebox.showerror(
                "Error",
                "Las masas deben ser mayores a cero"
            )

            return

        g = 9.8

        opcion = movimiento.get()

        # -------------------------------------------------
        # BLOQUE 1 BAJA
        # -------------------------------------------------

        if opcion == 1:

            a = ((m1 - m2) * g) / (m1 + m2)

            T = (2 * m1 * m2 * g) / (m1 + m2)

            resultado_texto.set(
    f"""
Bloque 1 ↓

Aceleración:
{a:.2f} m/s²

Tensión:
{T:.2f} N
"""
)

            animar("bloque1")

        # -------------------------------------------------
        # BLOQUE 2 BAJA
        # -------------------------------------------------

        else:

            a = ((m2 - m1) * g) / (m1 + m2)

            T = (2 * m1 * m2 * g) / (m1 + m2)

            resultado_texto.set(
    f"""
Bloque 2 ↓

Aceleración:
{a:.2f} m/s²

Tensión:
{T:.2f} N
"""
)

            animar("bloque2")

    except:

        messagebox.showerror(
            "Error",
            "Ingrese datos válidos"
        )

# =========================================================
# TÍTULO
# =========================================================

titulo = tk.Label(
    ventana,
    text="SISTEMA DE POLEAS - SEGUNDA LEY DE NEWTON",
    font=("Arial", 20, "bold"),
    bg="#DCE8F5",
    fg="darkblue"
)

titulo.pack(pady=10)

# =========================================================
# CONTENEDOR PRINCIPAL
# =========================================================

contenedor = tk.Frame(
    ventana,
    bg="#DCE8F5"
)

contenedor.pack(fill="both", expand=True)

# =========================================================
# PANEL IZQUIERDO
# =========================================================

panel_izquierdo = tk.Frame(
    contenedor,
    bg="#DCE8F5",
    width=350
)

panel_izquierdo.pack(side="left", fill="y", padx=20)

# ---------------------------------------------------------
# ENUNCIADO
# ---------------------------------------------------------

enunciado = """
ENUNCIADO:

Dos bloques cuelgan de una polea ideal.

Calcular:

• Aceleración del sistema
• Tensión en la cuerda

Ingrese las masas y seleccione
qué bloque desciende.
"""

tk.Label(
    panel_izquierdo,
    text=enunciado,
    justify="left",
    font=("Arial", 12),
    bg="#DCE8F5"
).pack(anchor="w", pady=10)

# ---------------------------------------------------------
# INPUTS
# ---------------------------------------------------------

frame_inputs = tk.Frame(
    panel_izquierdo,
    bg="#DCE8F5"
)

frame_inputs.pack(anchor="w", pady=10)

# Masa 1
tk.Label(
    frame_inputs,
    text="Masa Bloque 1:",
    font=("Arial", 12),
    bg="#DCE8F5"
).grid(row=0, column=0, pady=8, sticky="w")

entry_m1 = tk.Entry(
    frame_inputs,
    font=("Arial", 12),
    width=10
)

entry_m1.grid(row=0, column=1)

# Masa 2
tk.Label(
    frame_inputs,
    text="Masa Bloque 2:",
    font=("Arial", 12),
    bg="#DCE8F5"
).grid(row=1, column=0, pady=8, sticky="w")

entry_m2 = tk.Entry(
    frame_inputs,
    font=("Arial", 12),
    width=10
)

entry_m2.grid(row=1, column=1)

# ---------------------------------------------------------
# RADIO BUTTONS
# ---------------------------------------------------------

movimiento = tk.IntVar()
movimiento.set(1)

tk.Label(
    panel_izquierdo,
    text="Seleccione qué bloque baja:",
    font=("Arial", 12, "bold"),
    bg="#DCE8F5"
).pack(anchor="w", pady=10)

frame_radio = tk.Frame(
    panel_izquierdo,
    bg="#DCE8F5"
)

frame_radio.pack(anchor="w")

tk.Radiobutton(
    frame_radio,
    text="Bloque 1",
    variable=movimiento,
    value=1,
    bg="#DCE8F5",
    font=("Arial", 11)
).pack(side="left", padx=10)

tk.Radiobutton(
    frame_radio,
    text="Bloque 2",
    variable=movimiento,
    value=2,
    bg="#DCE8F5",
    font=("Arial", 11)
).pack(side="left", padx=10)

# ---------------------------------------------------------
# BOTÓN
# ---------------------------------------------------------

boton = tk.Button(
    panel_izquierdo,
    text="CALCULAR Y ANIMAR",
    font=("Arial", 12, "bold"),
    bg="#2EAF3D",
    fg="white",
    padx=15,
    pady=10,
    command=calcular
)

boton.pack(pady=20)

# =========================================================
# PANEL DERECHO - ANIMACIÓN
# =========================================================

panel_derecho = tk.Frame(
    contenedor,
    bg="#DCE8F5"
)

panel_derecho.pack(side="right", padx=10)

tk.Label(
    panel_derecho,
    text="ANIMACIÓN DEL SISTEMA",
    font=("Arial", 16, "bold"),
    bg="#DCE8F5",
    fg="darkblue"
).pack()

# ---------------------------------------------------------
# CANVAS
# ---------------------------------------------------------

canvas = tk.Canvas(
    panel_derecho,
    width=650,
    height=500,
    bg="white",
    bd=3,
    relief="solid"
)

canvas.pack(pady=10)

# Dibujar sistema inicial
dibujar_sistema(250, 250)

# =========================================================
# EJECUTAR
# =========================================================

ventana.mainloop()