# Oscilloscope Simulator (Python / Tkinter)

A simple oscilloscope simulator I built at school (Elektrotechnische
wetenschappen) to better understand sine waves.

## Features
- Live sine wave on a canvas with a measurement grid
- Adjustable frequency (Hz) and amplitude (V)
- Vpp (peak-to-peak) readout: Vpp = 2 · amplitude

## Run
    python oscilloscope.py

Python 3 with Tkinter (included in the standard Windows installer).

## Known issues (found while preparing this repo)
- The STOP/START button toggles a flag, but the drawing loop never checks it
- The grid lines are re-created every frame (30 ms) and never removed, so the
  canvas slows down over time
- Bare `except:` hides real errors

I'm fixing these in follow-up commits.

## What I learned
Event-driven GUI code with `after()`, drawing on a canvas, and connecting
electrical theory (Vpp = 2·Vp) to code.
