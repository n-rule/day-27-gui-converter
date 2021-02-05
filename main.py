import tkinter

window = tkinter.Tk()

window.title('GUI SHIT')
window.minsize(500, 300)
window.config(padx='200', pady='200')

# Label

label = tkinter.Label(text="I am Label", font=("Arial", 18, "bold"))
label.grid(row='0', column='0')

label['text'] = 'New Text'


# Button

def button_click():
    label['text'] = input.get()


button = tkinter.Button(text='Click ME!', command=button_click)
button.grid(row='1', column='1')

button2 = tkinter.Button(text='Click ME!', command=button_click)
button2.grid(row='0', column='2')

# Entry


input = tkinter.Entry(width=20)
input.grid(row='2', column='3')

window.mainloop()
