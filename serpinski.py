from tkinter import *
from tkinter import ttk
import random
from datetime import datetime

class SierpinskiTriangle:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.point_dict = {1:[250,100], 2:[50, 400], 3:[450,400]}
        self.colours = {1:'green', 2:'red', 3:'blue', 4:'yellow'}
        self.pointNum = 0
        self.canvas.create_line(self.x, self.y , self.x+1, self.y , fill='black')
        self.canvas.create_text((400, 20), text='Created points: '+str(self.pointNum), fill='white', tags=('points',))
        self.startTime = datetime.now()
        self.canvas.create_text((400, 50), text='Elapsed time: '+str(0), fill='white', tags=('time',))


    def drawPoint(self):
        S = self.point_dict[random.randint(1,3)]
        self.x = 0.5*(self.x +S[0])
        self.y = 0.5*(self.y +S[1])
        colour = self.colours[random.randint(1,4)] if self.pointNum < 2000 else 'black'
        self.canvas.create_line(self.x, self.y, self.x+1, self.y, fill=colour)
        
        self.pointNum+=1
        self.canvas.delete('points')
        self.canvas.create_text((400, 20), text='Created points: '+str(self.pointNum), fill='white', tags=('points',))

        elapsedTime = datetime.now() - self.startTime
        self.canvas.delete('time')
        self.canvas.create_text((400, 50), text='Elapsed time: '+str(elapsedTime), fill='white', tags=('time',))
        self.canvas.after(1, self.drawPoint)


# initialize root Window and canvas
root = Tk()
root.title(" sierpinski triangle")
root.resizable(False,False)
canvas = Canvas(root, width = 500, height = 500, background='black')
canvas.pack()

t1 = SierpinskiTriangle(canvas, 150, 250)
t1.drawPoint()

root.mainloop()