from Tkinter import *

window=Tk()

def convert():
    kg = float(entry1.get())
    entry2.insert(END, kg * 1000)
    entry3.insert(END, kg * 2.20462)
    entry4.insert(END, kg * 35.274 )

label1=Label(window, text="Kg")
label1.grid(row=0, column=0)

entry1_value=StringVar()
entry1=Entry(window, textvariable=entry1_value)
entry1.grid(row=0, column=1)

button1=Button(window,text="Convert", command=convert)
button1.grid(row=0, column=2)

entry2=Entry(window)
entry2.grid(row=1, column=0)

entry3=Entry(window)
entry3.grid(row=1, column=1)

entry4=Entry(window)
entry4.grid(row=1, column=2)

window.mainloop()
