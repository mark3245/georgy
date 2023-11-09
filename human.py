from tkinter import Tk, Canvas, ARC, SE, W


class Human():
    
    def __init__(self, canvas, name,x ,y):
        self.canvas=canvas
        self.__name=name
        self.x=x
        self.y=y
        self.gender=gender
        
    def display(self):
        self.__drawname()
        self.__drawhead()
        self.__drawbody()
        self.__drawleggs()
        self.__drawhands()
        if self.gender=="Женщина":
            self.__drawpigtails()
        elif self.gender=="Мужчина":
            self.__drawhair()
        
        
    def __drawname(self):
        self.canvas.create_text(self.x+20,self.y-200,text=self.__name,font="Times 18",anchor=W,fill="black")
        
    def __drawhead(self):
        self.canvas.create_oval(self.x+20,self.y-180,self.x+80,self.y-120,width=2)
        self.canvas.create_arc(self.x+40,self.y-150,self.x+60,self.y-135,start=0, extent=-180,
            style=ARC, outline="red", width=3)
        self.canvas.create_oval(self.x+30,self.y-150,self.x+40,self.y-160,width=0,fill="blue")
        self.canvas.create_oval(self.x+60,self.y-150,self.x+70,self.y-160,width=0,fill="blue")
        
    def __drawbody(self):
        self.canvas.create_line(self.x+50,self.y-120,self.x+50,self.y-50,width=2)
        
    def __drawleggs(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100,self.y,width=2)
        
    def __drawhands(self):
        self.canvas.create_line(self.x+10,self.y-70,self.x+50,self.y-110,self.x+90,self.y-70,width=2)
        
    def __drawhair(self):
        self.canvas.create_line(self.x+35,self.y-185,self.x+35,self.y-175,width=2)
        self.canvas.create_line(self.x+50,self.y-190,self.x+50,self.y-180,width=2)
        self.canvas.create_line(self.x+65,self.y-185,self.x+65,self.y-175,width=2)
        
    def __drawpigtails(self):
        self.canvas.create_line(self.x+35,self.y-225,self.x+35,self.y-175,width=2)
        self.canvas.create_line(self.x+65,self.y-225,self.x+65,self.y-175,width=2)