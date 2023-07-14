import tkinter as t
# from PIL import Image, ImageTk

#Creating the instance of tkinter class
root = t.Tk()

#Setting title and dimensions
root.title('CricScorer')
root.geometry('900x700')

#Creating menu
mymenu = t.Menu(root)

#Creating new menu and adding it to my menu
newMenu = t.Menu(mymenu, tearoff=False)

newMenu.add_command(label='New Match')
newMenu.add_command(label='New Player')
newMenu.add_command(label='New Team')

mymenu.add_cascade(menu=newMenu, label='New')


#Creating view menu and adding it to my menu
viewMenu = t.Menu(mymenu, tearoff=False)

viewMenu.add_command(label='Edit Player')
viewMenu.add_command(label='Edit Team')

mymenu.add_cascade(menu=viewMenu, label='View')

#Creating edit menu and adding it to my menu
editMenu = t.Menu(mymenu, tearoff=False)

editMenu.add_command(label='Edit Player')
editMenu.add_command(label='Edit Team')

mymenu.add_cascade(menu=editMenu, label='Edit')

#Creating help command and adding it to my menu
mymenu.add_command(label='Help')

root.config(menu=mymenu)


header = t.Frame(root, bg='#ff004f')
header.pack(side='top', anchor='n', fill='x')

header_label = t.Label(header, text='Home', bg='#ff004f', font="lucida 13")
header_label.pack(side='top')


root.mainloop()
