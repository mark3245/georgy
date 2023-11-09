from tkinter import Tk, Canvas
from grid import Grid
from human import Human


root = Tk()
canvas = Canvas(root,width=800,height=600)
canvas.pack()
grid=Grid(canvas)
grid.display()
p1 = Human(canvas,'Вася',100,500,"Мужчина")
p2 = Human(canvas, 'Маша',200,500,"Женщина")
p1.display()
p2.display()
root.mainloop()