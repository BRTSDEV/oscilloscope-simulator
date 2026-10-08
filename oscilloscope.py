import tkinter as tk
import math
import time

venster = tk.Tk()
venster.title("Mijn Oscilloscoop")
venster.geometry("900x600")

frequentie = 2.0
amplitude = 2.0
gestart = True

canvas_breedte = 850
canvas_hoogte = 400

canvas = tk.Canvas(
    venster,
    width=canvas_breedte,
    height=canvas_hoogte,
    bg="black"
)

canvas.pack(pady=15)

frame = tk.Frame(venster)
frame.pack()

tk.Label(frame, text="Frequentie (Hz):").grid(row=0, column=0)

frequentie_box = tk.Entry(frame, width=10)
frequentie_box.insert(0, "2")
frequentie_box.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Amplitude (V):").grid(row=0, column=2)

amplitude_box = tk.Entry(frame, width=10)
amplitude_box.insert(0, "2")
amplitude_box.grid(row=0, column=3, padx=5)


def instellingen_veranderen():

    global frequentie
    global amplitude

    try:
        frequentie = float(frequentie_box.get())
        amplitude = float(amplitude_box.get())

        if frequentie < 0:
            frequentie = 0

        if amplitude < 0:
            amplitude = 0

    except:
        print("Ongeldige waarde")


knop = tk.Button(
    frame,
    text="Toepassen",
    command=instellingen_veranderen
)

knop.grid(row=0, column=4, padx=10)


def start_stop():

    global gestart

    gestart = not gestart

    if gestart:
        stop_knop.config(text="STOP")
    else:
        stop_knop.config(text="START")


stop_knop = tk.Button(
    venster,
    text="STOP",
    command=start_stop
)

stop_knop.pack(pady=5)


def raster():

    for y in range(0, canvas_hoogte, 40):
        canvas.create_line(
            0, y,
            canvas_breedte, y,
            fill="#333333"
        )

    for x in range(0, canvas_breedte, 40):
        canvas.create_line(
            x, 0,
            x, canvas_hoogte,
            fill="#333333"
        )

    canvas.create_line(
        0,
        canvas_hoogte / 2,
        canvas_breedte,
        canvas_hoogte / 2,
        fill="white"
    )


start_tijd = time.time()


def tekenen():

    canvas.delete("golf")

    raster()

    tijd = time.time() - start_tijd

    punten = []

    midden = canvas_hoogte / 2

    volt_schaal = 60

    for x in range(canvas_breedte):

        t = x / canvas_breedte * 2

        spanning = amplitude * math.sin(
            2 * math.pi * frequentie * t
            + tijd * frequentie * 2 * math.pi
        )

        y = midden - spanning * volt_schaal

        punten.append((x, y))

    for i in range(len(punten) - 1):

        canvas.create_line(
            punten[i][0],
            punten[i][1],
            punten[i + 1][0],
            punten[i + 1][1],
            fill="lime",
            width=2,
            tags="golf"
        )

    Vpp = amplitude * 2

    info = "Frequentie: " + str(round(frequentie, 2)) + " Hz"
    info += "     Amplitude: " + str(round(amplitude, 2)) + " V"
    info += "     Vpp: " + str(round(Vpp, 2)) + " V"

    canvas.create_text(
        10,
        15,
        anchor="w",
        text=info,
        fill="white",
        font=("Arial", 12),
        tags="golf"
    )

    venster.after(30, tekenen)


tekenen()

venster.mainloop()
