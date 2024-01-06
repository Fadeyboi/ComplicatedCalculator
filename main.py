import tkinter as tk
from tkinter import ttk
fieldValue = ""


def field_place(number):
    global fieldValue
    fieldValue += number
    field.delete("1.0", "end")
    field.insert("1.0", fieldValue)


def field_calc():
    global fieldValue
    result = str(eval(fieldValue))
    if result == "69":
        field.delete("1.0", "end")
        field.insert("1.0", "Nice!")
    elif result == "6969":
        field.delete("1.0", "end")
        field.insert("1.0", "Double Nice!")
    else:
        field.delete("1.0", "end")
        field.insert("1.0", result)


def clear_button():
    global fieldValue
    field.delete("1.0", "end")
    fieldValue = ""


window = tk.Tk()  # main window
window.title("Unnecessarily Complicated Calculator")  # main window title
window.geometry('450x600')
window.resizable(False, False)
field = tk.Text(window, height=4, width=30, font=('Times New Roman',20,'bold'))


# NUMBERS
zeroIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/zero.png")
zero = ttk.Button(window, image=zeroIcon, command=lambda: field_place('0'))
oneIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/one.png")
one = ttk.Button(window, image=oneIcon, command=lambda: field_place('1'))
twoIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/two.png")
two = ttk.Button(window, image=twoIcon, command=lambda: field_place('2'))
threeIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/three.png")
three = ttk.Button(window, image=threeIcon, command=lambda: field_place('3'))
fourIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/four.png")
four = ttk.Button(window, image=fourIcon, command=lambda: field_place('4'))
fiveIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/five.png")
five = ttk.Button(window, image=fiveIcon, command=lambda: field_place('5'))
sixIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/six.png")
six = ttk.Button(window, image=sixIcon, command=lambda: field_place('6'))
sevenIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/seven.png")
seven = ttk.Button(window, image=sevenIcon, command=lambda: field_place('7'))
eightIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/eight.png")
eight = ttk.Button(window, image=eightIcon, command=lambda: field_place('8'))
nineIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/nine.png")
nine = ttk.Button(window, image=nineIcon, command=lambda: field_place('9'))


# OPERATORS
plusIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/plus.png")
plus = ttk.Button(window, image=plusIcon, command=lambda: field_place('+'))
minusIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/minus.png")
minus = ttk.Button(window, image=minusIcon, command=lambda: field_place('-'))
equalsIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/equals.png")
equals = ttk.Button(window, image=equalsIcon, command=lambda: field_calc())
clearIcon = tk.PhotoImage(file="C:/Users/GAMER/OneDrive/Pictures/Unnecessarily Complicated Calculator/clear.png")
clear = ttk.Button(window, image=clearIcon, command=lambda: clear_button())


'''
SIDE EDGE IS 335, OFFSET EDGES BY 15
CENTER IS 167.5
BOTTOM EDGE IS 530, OFFSET EDGES BY 15, OFFSET BUTTONS BY 100
'''
# 1st row
plus.place(x=15, y=515)
zero.place(x=167.5, y=515)
minus.place(x=320, y=515)
# 2nd row
one.place(x=15, y=415)
two.place(x=167.5, y=415)
three.place(x=320, y=415)
# 3rd row
four.place(x=15, y=315)
five.place(x=167.5, y=315)
six.place(x=320, y=315)
# 4th row
seven.place(x=15, y=215)
eight.place(x=167.5, y=215)
nine.place(x=320, y=215)
# random tbh
equals.place(x=15, y=145)
clear.place(x=15, y=495)
# field
field.place(x=15, y=15)


# mainloop
window.mainloop()