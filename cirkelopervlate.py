import tkinter as tk
from math import pi

def bereken_oppervlakte(straal1, straal2):
    oppervlakte1 = pi * straal1**2
    oppervlakte2 = pi * straal2**2
    
    afstand_tussen_centra = straal1 + straal2
    
    overlappend_gedeelte = 0
    
    # Bereken de oppervlakte van het overlappende gedeelte
    if afstand_tussen_centra < straal1 + straal2:
        d = (straal1**2 - straal2**2 + afstand_tussen_centra**2) / (2 * afstand_tussen_centra)
        overlappend_gedeelte = oppervlakte1 - (pi * (straal1 - d)**2) + oppervlakte2 - (pi * (straal2 - d)**2)
    
    return overlappend_gedeelte

def teken_cirkels(canvas, straal1, straal2):
    x1, y1 = 100, 150
    x2, y2 = x1 + straal1 * 2, y1 + straal1 * 2
    canvas.create_oval(x1, y1, x2, y2, outline="blue", width=2, tags="cirkel1")

    # Calculate the midpoint of circle 1
    x_midpoint = x1 + straal1
    y_midpoint = y1 + straal1

    # Calculate the coordinates of circle 2
    x3 = x_midpoint - straal2
    y3 = y_midpoint - straal2
    x4 = x_midpoint + straal2
    y4 = y_midpoint + straal2

    canvas.create_oval(x3, y3, x4, y4, outline="red", width=2, tags="cirkel2")

# Rest of the code...
