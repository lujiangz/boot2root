#!/usr/bin/python3
from turtle import *
import time

t = Turtle()
t.pensize(3)
t.left(90)

with open('turtle', 'r') as file:
    for line in file:
        if not line.strip():
            continue
            
        value = int(''.join(filter(str.isdigit, line)))
        
        if "Tourne gauche" in line:
            t.left(value)
        elif "Tourne droite" in line:
            t.right(value)
        elif "Avance" in line:
            t.forward(value)
        elif "Recule" in line:
            t.backward(value)

time.sleep(1)
done()