import tkinter
import os

window = tkinter.Tk()

window.geometry("300x600")

items = []


items_frame = tkinter.Frame(window)
items_frame.pack()

input_frame = tkinter.Frame(window)

item_input = tkinter.Entry(input_frame)
item_input.pack()

def add_item(item=None):
    if item == None:
        item_name = item_input.get()
    
    else:
        item_name = item
    
    checkbox = tkinter.Checkbutton(items_frame, text=item_name)
    checkbox.pack()
    
    items.append(item_name + "\n")
    
    # How to clear screen:
    # for child in window.winfo_children():
    #     child.destroy()

def save():
    file = open("todos.txt", "w")
    
    file.writelines(items)
    
    file.close()

if os.path.exists("todos.txt"):
    file = open("todos.txt")
    file_contents = file.readlines()
    
    for line in file_contents:
        add_item(line.strip())


add_item_button = tkinter.Button(input_frame, text="Add Item", command=add_item)
add_item_button.pack()

save_button = tkinter.Button(window, text="Save", command=save)
save_button.pack(side="bottom")

input_frame.pack(side="bottom")


window.mainloop()