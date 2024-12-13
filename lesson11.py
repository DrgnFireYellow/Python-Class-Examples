import tkinter

window = tkinter.Tk()
window.geometry("400x300")

label_frame = tkinter.Frame(window)
label_frame.pack()

hello_label = tkinter.Label(label_frame, text="Hello World!")
hello_label.pack()

goodbye_label = tkinter.Label(label_frame, text="Goodbye!")
goodbye_label.pack()

why_label = tkinter.Label(label_frame, text="Why so many labels?")
why_label.pack()


grid_frame = tkinter.Frame(window)

grid_label_1 = tkinter.Button(grid_frame, text="Hello this is my friend -> ")
grid_label_1.grid(row=1, column=1)

grid_label_2 = tkinter.Button(grid_frame, text=":)")
grid_label_2.grid(row=1, column=2)

grid_frame.pack()

window.mainloop()