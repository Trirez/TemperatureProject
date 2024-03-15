from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Trirez\Downloads\New folder\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x768")
window.configure(bg = "#0D17FA")


canvas = Canvas(
    window,
    bg = "#0D17FA",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    20.0,
    64.0,
    anchor="nw",
    text="Temperature",
    fill="#FFFFFF",
    font=("Inter", 40 * -1)
)

canvas.create_text(
    20.0,
    176.0,
    anchor="nw",
    text="Pressure",
    fill="#FFFFFF",
    font=("Inter", 40 * -1)
)

canvas.create_rectangle(
    412.0,
    0.0,
    1024.0,
    768.0,
    fill="#D9D9D9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    717.0,
    586.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#AFA9A9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=471.0,
    y=552.0,
    width=492.0,
    height=67.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    717.0,
    467.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#AFA9A9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=471.0,
    y=433.0,
    width=492.0,
    height=67.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    717.0,
    211.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#AFA9A9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=471.0,
    y=177.0,
    width=492.0,
    height=67.0
)

canvas.create_text(
    20.0,
    307.0,
    anchor="nw",
    text="Relative Humidity",
    fill="#FFFFFF",
    font=("Inter", 40 * -1)
)

canvas.create_text(
    20.0,
    440.0,
    anchor="nw",
    text="Air Quality",
    fill="#FFFFFF",
    font=("Inter", 40 * -1)
)

canvas.create_text(
    20.0,
    564.0,
    anchor="nw",
    text="Altitude",
    fill="#FFFFFF",
    font=("Inter", 40 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    717.0,
    87.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#AFA9A9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=471.0,
    y=53.0,
    width=492.0,
    height=67.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    717.0,
    337.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#AFA9A9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=471.0,
    y=303.0,
    width=492.0,
    height=67.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=607.0,
    y=671.0,
    width=220.0,
    height=62.0
)
window.resizable(False, False)
window.mainloop()
