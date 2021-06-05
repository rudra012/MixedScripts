from tkinter import Frame, YES, BOTH, Button


# # Creating frame for calculator
# def iCalc(source, side):
#     storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
#     storeObj.pack(side=side, expand=YES, fill=BOTH)
#     return storeObj
#
#
# # Creating Button
# def button(source, side, text, command=None):
#     storeObj = Button(source, text=text, command=command)
#     storeObj.pack(side=side, expand=YES, fill=BOTH)
#     return storeObj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')


# Start the GUI
if __name__ == '__main__':
    app().mainloop()
