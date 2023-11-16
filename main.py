from tkinter import *
from tkinter import messagebox
import pyperclip
import json

#--------------------ADD TO TXT--------------------#
def add_to_txt():
    if website_entry.get()=="" or username_entry.get()=="" or password_entry.get()=="":
        messagebox.showerror("Form", "Enter usrname and website!",icon ='error')
    else:
        new_pass={website_entry.get():{"password": password_entry.get(),"username":username_entry.get()}}
        try:
            with open("./Password_Manager/password.json",'r') as pw:
                data=json.load(pw)
        except FileNotFoundError:
            pw=open("./Password_Manager/password.json",'w') 
            json.dump(new_pass,pw,indent=5)
            pw.close()
        else:
            data.update(new_pass)    #updating json data
            with open("./Password_Manager/password.json",'w') as pw:
                json.dump(data,pw,indent=5)
        finally:
            website_entry.delete(0,END)
            username_entry.delete(0,END)
            password_entry.delete(0,END)
        
            messagebox.showinfo("Information","Password Saved")
        
#--------------------PASSOWRD DISPLAY--------------------#
import random
def create_password(LET=7,sym=2,num=1):
    letter=["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers=['1','2','3','4','5','6','7','8','9','0']
    symbols=['!',"@",'#','$',"%",'^','&',"*",'`','~']
    password=[]
    for i in range(LET):
        password.append(random.choice(letter))
    for i in range(sym):
        password.append(random.choice(symbols))
    for i in range(num):
        password.append(random.choice(numbers))
        
    random.shuffle(password)
    pyperclip.copy("".join(password))
    return "".join(password)

def generate():
    if website_entry.get()=="" or username_entry.get()=="":
        messagebox.showerror("ERROR!", "Enter usrname and website!",icon ='error')
    else:
        password_entry.delete(0,END)
        password_entry.insert(0,f"{create_password()}")
        
def search():
    if website_entry.get()=="":
        messagebox.showerror("Form", "Enter usrname and website!",icon ='error')
    else:
        website=website_entry.get()
        try:
            with open("./Password_Manager/password.json",'r') as pw:
                data=json.load(pw)
        except FileNotFoundError:
            with open("./Password_Manager/password.json",'w') as pw:
                json.dump({},pw)
                messagebox.showerror("Error","Data file not found, please save some data first")
        else:
            if(website in data):
                messagebox.showinfo("Password Found",f"Website: {website}\nUsername: {data[website]['username']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showerror("ERROR!","No such entry found")
            
        
#--------------------GUI--------------------#
window=Tk()
window.title("Password Generator")
window.config(bg="black",padx=50,pady=20)

canvas=Canvas(width=200,height=210,highlightthickness=0)
logo=PhotoImage(file="./Password_Manager/new_logo1.png")
canvas["bg"]="black"
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

# background=Canvas(highlightthickness=0)
# bg=PhotoImage(file="./Password_Manager/background.gif")
# background["bg"]="black"
# background.create_image(100,100,image=bg)
# background.grid(row=0,column=1)

website_entry=Entry(width=25)
website_entry.grid(row=1,column=1,columnspan=2)

username_entry=Entry(width=35)
username_entry.grid(row=2,column=1,columnspan=2)

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

generate=Button(text="Generate",command=generate)
generate.config(font=("courier",10,"bold"))
generate.grid(row=3,column=2)

add=Button(text="Add",width=36,command=add_to_txt)
add.config(font=("courier",10,"bold"))
add.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search",command=search)
search_button.grid(row=1,column=2,columnspan=2)

website_label=Label(text="Website: ",height=2,font=("courier",10,"bold"))
website_label.grid(row=1,column=0)
website_label.config(fg="white",bg="black")

username_label=Label(text="Username: ",height=2,font=("courier",10,"bold"))
username_label.grid(row=2,column=0)
username_label.config(fg="white",bg="black")

password_label=Label(text="Password: ",height=2,font=("courier",10,"bold"))
password_label.grid(row=3,column=0)
password_label.config(fg="white",bg="black")

window.mainloop()