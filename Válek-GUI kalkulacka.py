from tkinter import *

win = Tk() # vytvorenie okna
win.geometry("312x324")  # velkost okna 
win.resizable(0, 0)  # zákaz zmenenia velkosti okna
win.title("Kalkulačka")

# definicia co sa stane pri kliknuti na tlacitko 
def btn_click(item):
    global vyraz
    vyraz = vyraz + str(item)
    input_text.set(vyraz)


# definicia vycistenia vysledkoveho pola 
def bt_clear(): 
    global vyraz 
    vyraz = "" 
    input_text.set("")
 

# definicia rovna sa
def bt_equal():
    global vyraz
    result = str(eval(vyraz)) 
    input_text.set(result)
    vyraz = ""
 
vyraz = ""
 

 
input_text = StringVar()
 
# obrazovka kde su cisla
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 

 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#00f7ff", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) 
 
# vzhlad tlacitok
 
btns_frame = Frame(win, width=312, height=272.5, bg="#b3b3b3")
 
btns_frame.pack() 
 
# prvá rada
 
clear = Button(btns_frame, text = "C", fg = "white", width = 32, height = 3, bd = 0, bg = "#424242", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
deleno = Button(btns_frame, text = "/", fg = "white", width = 10, height = 3, bd = 0, bg = "#424242", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# druhá rada

sedem = Button(btns_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
osem = Button(btns_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
devet = Button(btns_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
nasobenie = Button(btns_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "#424242", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# tretia rada
 
styri = Button(btns_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
pät = Button(btns_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
sest = Button(btns_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "#424242", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# štvrtá rada
 
jedna = Button(btns_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
dva = Button(btns_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
tri = Button(btns_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "#424242", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

# ostatné operácie
 
znula = Button(btns_frame, text = "0", fg = "white", width = 21, height = 3, bd = 0, bg = "#696969", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
bodka = Button(btns_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "#424242", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
rovna = Button(btns_frame, text = "=", fg = "white", width = 10, height = 3, bd = 0, bg = "#424242", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()