import tkinter as tk
from tkinter import *   


GUI = Tk()
GUI.title('วงจรแบ่งแรงดัน') 
#GUI.geometry('350x500')     
canvas = Canvas(GUI, width = 400, height = 500)      
canvas.pack()      

L1 = Label(GUI,text='วงจรแบ่งแรงดัน',font=('',30))
L1.place(x=20,y=0)

img = PhotoImage(file="r2.PNG")      
canvas.create_image(150,80, anchor=NW, image=img)   

Vin = Label(GUI,text='Vin',font=('',10))
R1 = Label(GUI,text='R1',font=('',10))
R2 = Label(GUI,text='R2',font=('',10))
inputVoltage   = Text(GUI,height = 2,width = 5)
inputR1        = Text(GUI,height = 2,width = 5)
inputR2        = Text(GUI,height = 2,width = 5)


Vin.place(x=15,y=80)
R1.place(x=15,y=110)
R2.place(x=15,y=140)
inputVoltage.pack()
inputVoltage.place(x=50,y=80)
inputR1.pack()
inputR1.place(x=50,y=110)
inputR2.pack()
inputR2.place(x=50,y=140)

def showvo(data):
    data= str(data)+"V"
    L2 = Label(GUI,text=data,font=('',20))
    L2.place(x=290,y=170)

def showvalue(var1,var2,var3):
    volt=var1+"v"
    iVin = Label(GUI,text=volt,font=('',10))
    iR1 = Label(GUI,text=var2,font=('',10))
    iR2 = Label(GUI,text=var3,font=('',10))
    iVin.place(x=150,y=80)
    iR1.place(x=200,y=110)
    iR2.place(x=200,y=200)

def retrieve_input():

    voltValue=inputVoltage.get("1.0","end-1c")
    r1Value=inputR1.get("1.0","end-1c")
    r2Value=inputR2.get("1.0","end-1c")
    showvalue(voltValue,r1Value,r2Value)
    vout=int(voltValue)
    r1Valueint=int(r1Value)
    r2Valueint=int(r2Value)
    vout=(vout*r2Valueint)/(r1Valueint+r2Valueint)
    vout=round(vout, 2)
    showvo(vout)
    print(vout)


buttonCommit=Button(GUI, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
                  
buttonCommit.pack()
buttonCommit.place(x=150,y=340)
mainloop() 


