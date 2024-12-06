from tkinter import *

root = Tk()
root.title("Calculator")  

# Input field
ketik = Entry(root, width=35, borderwidth=5)
ketik.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Fungsi untuk tombol
def button_click(number):
    CURRENT = ketik.get()
    ketik.delete(0, END)
    ketik.insert(0, str(CURRENT) + str(number))

def button_clear():
    ketik.delete(0, END)
    
def button_equal():
    try:
        result = eval(ketik.get())
        ketik.delete(0, END)
        ketik.insert(0, str(result))
    except Exception as e:
        ketik.delete(0, END)
        ketik.insert(0, "Error")

def button_square():
    try:
        CURRENT = ketik.get()
        result = eval(CURRENT)**2
        ketik.delete(0, END)
        ketik.insert(0, str(result))
    except Exception as e:
        ketik.delete(0, END)
        ketik.insert(0, "Error") 
        
#fungsi untuk tombol angka       
def Mybutton():
    
    position = [
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2),
        (3, 0), (3, 1), (3, 2),
        (4, 1)
    ]
    
    for i, (row, col) in enumerate(position): 
        button = Button(root, text=str(i), padx=40, pady=20, command=lambda i=i: button_click(i))
        button.grid(row=row, column=col)
Mybutton()

#Tombol untuk operator
button_add = Button(root, text="+", padx=40, pady=20,  command=lambda: button_click("+"))
button_sub = Button(root, text="-", padx=41, pady=20, command=lambda: button_click("-"))
button_mul = Button(root, text="X", padx=40, pady=20, command=lambda: button_click("*"))
button_div = Button(root, text=":", padx=41, pady=20, command=lambda: button_click("/"))
button_pow = Button(root, text="*", padx=41, pady=20, command=button_square)
button_dot = Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."))
button_equal = Button(root, text="=", padx=90, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)


#Posisi Tombol operator
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_pow.grid(row=4, column=0)
button_dot.grid(row=4, column=2)

#Posisi Tombol = dan CLEAR
button_equal.grid(row=5, column=0, columnspan = 2)
button_clear.grid(row=5, column=2, columnspan = 2)

root.mainloop()
