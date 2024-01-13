from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Canvas Application")
root.geometry("800x600")

label = Label(root, text = "endx")
label.place(relx = 0.5 , rely = 0.9, anchor = CENTER)

label4 = Label(root, text = "endy")
label4.place(relx = 0.7 , rely = 0.9, anchor = CENTER)

label5 = Label(root, text = "Type Color")
label5.place(relx = 0.65 , rely = 0.965, anchor = CENTER)

label2 = Label(root, text = "starty")
label2.place(relx = 0.3 , rely = 0.9, anchor = CENTER)

dededede = Label(root, text = "startx")
dededede.place(relx = 0.1 , rely = 0.9, anchor = CENTER)


endx = Entry(root)
endx.place(relx =0.6 , rely = 0.9, anchor = CENTER)

colors = ["red", "blue", "black", "yellow", "green", "orange"]
color = ttk.Combobox(root, values = colors,)
color['state'] = 'readonly'
color.place(relx = 0.8 , rely = 0.965, anchor = CENTER)

endy = Entry(root)
endy.place(relx =0.8 , rely = 0.9, anchor = CENTER)

starty = Entry(root)
starty.place(relx =0.4 , rely = 0.9, anchor = CENTER)

startx = Entry(root)
startx.place(relx =0.2 , rely = 0.9, anchor = CENTER)


canvas= Canvas(root, width = 800, height = 510, bg = "white", highlightbackground="lightgray")
canvas.pack()

def create_circle(event):
    draw_oval=canvas.create_oval(startx.get(), starty.get(), endx.get(),endy.get(),fill = color.get())
    canvas.draw_oval()
def create_lines(event):
    draw_line=canvas.create_line(startx.get(), starty.get(), endx.get(),endy.get(),width = 10,fill = color.get())
    canvas.draw_line()
def create_square(event):
    draw_square=canvas.create_rectangle(startx.get(), starty.get(), endx.get(),endy.get(),fill = color.get())
    canvas.draw_square()
root.bind("<c>", create_circle)
root.bind("<l>", create_lines)
root.bind("<s>", create_square)



root.mainloop()