from tkinter import *
window=Tk()
window.title("Password Generator")
window.config(bg="black",padx=20,pady=20)
canvas=Canvas(width=200,height=200,highlightthickness=0)
logo=PhotoImage(file="./Password_Manager/new_logo1.png")
canvas["bg"]="black"
canvas.create_image(100,100,image=logo)
canvas.pack()
window.mainloop()