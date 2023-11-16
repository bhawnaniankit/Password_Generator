from tkinter import *
window=Tk()
window.title("Password Generator")
window.config(bg="black")
canvas=Canvas(width=540,height=360)
logo=PhotoImage(file="./Password_Manager/logo.png")
canvas.create_image(0,0,image=logo)
window.mainloop()