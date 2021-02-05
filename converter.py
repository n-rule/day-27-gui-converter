from tkinter import *

window = Tk()

window.title('Shitty Mono Converter')
window.minsize()
window.config(padx='10', pady='10')


def button_click():
    label_result['text'] = round(int(input.get()) * 1.60934)


button = Button(text='Calculate', command=button_click)
button.grid(column='1', row='2')

input = Entry(width=10)
input.grid(column='1', row='0')

label_result = Label(text="0", font=("Arial", 10, "bold"))
label_result.grid(column='1', row='1')

label1 = Label(text="is equal to:", font=("Arial", 10, "bold"))
label1.grid(column='0', row='1')

label2 = Label(text="miles", font=("Arial", 10, "bold"))
label2.grid(column='2', row='0')

label3 = Label(text="km", font=("Arial", 10, "bold"))
label3.grid(column='2', row='1')

window.mainloop()
