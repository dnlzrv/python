# Erstelle eine GUI mit der Anzeige einer Liste an
# Programmiersprachen (die Einträge in verschiedenen (!) Labels)
#   Die bg Farbe soll zufällig gewählt werden
#   Die fg Farbe soll entweder schwarz sein oder weiß - 
# abhängig von der Helligkeit der gewählten bg-Farbe
#       wenn der Wert der Helligkeit kleiner als 120 ist, dann weiß
#
#lang = ['Python', 'C#', 'Perl', 'C++', 'Java', 'Tcl/Tk']
#
#rgb = (red, green, blue)
#rgb_hex = '%02x%02x%02x' % rgb
#helligkeit = math.sqrt(0.299 * rgb[0] ** 2 + 0.587 * rgb[1] ** 2 + 0.114 * rgb[2] ** 2)

import tkinter as tk
import random
import math
from math import sqrt

class LanguagePro(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Programmiersprachen")
        self.geometry('350x500')
        
        def rgbToHex(rgb):
            return "#%02x%02x%02x" % rgb

        def makeColor():
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            return (red, green, blue)
        
        def makeLabel(title, rgb):
            rgb_hex =rgbToHex(rgb)
            helligkeit = sqrt(0.299 * rgb[0] ** 2 + 0.587 * rgb[1] ** 2 + 0.114 * rgb[2] ** 2)
            font = "Helvetica 16 bold italic"
            fg = ""
            if helligkeit >= 255 / 2:
                fg = "black"
            else:
                fg = "white"
            return tk.Label(self, text = title, font = font, fg = fg, bg = rgb_hex, height = 2)
        
        languages = ['Python', 'C#', 'Perl', 'C++', 'Java', 'Tcl/Tk']
        
        for lang in languages:
            rgb = makeColor()
            label = makeLabel(lang, rgb)
            label.pack(expand=True, fill='both')

lang = LanguagePro() 
lang.mainloop()       
        