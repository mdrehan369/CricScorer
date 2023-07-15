"""

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
"""


import customtkinter as t
from PIL import Image


def getImage(file):

    img = Image.open(file)
    image = t.CTkImage(img)

    return image


class App(t.CTk):

    def __init__(self, width, height, title):

        super().__init__()

        self.title(title)
        self.geometry(f"{width}x{height}")

        # t.set_default_color_theme('green')
        #Creating variables
        curr_frame = 'Home'
        dark_green = '#00e600'
        light_green = '#66ff66'
        lbs = []
        self.indicator = None
        # lbs[0].configure(fg_color=dark_green)

        def menu_change(id):

            global indicator
            if(self.indicator is not None):
                self.indicator.configure(fg_color=light_green)
                self.indicator = lbs[id]
                self.indicator.configure(fg_color=dark_green)
            else:
                self.indicator = lbs[0]
            

        def openSidebar():
            side_frame.configure(width = 200)

        def hideSidebar():
            side_frame.configure(width=0)
        #Creating frames and basic layout
        top_frame = t.CTkFrame(self, width=800, height=40, fg_color=light_green, border_width=1, corner_radius=0)
        top_frame.pack(side='top', fill='x')
        

        side_frame = t.CTkFrame(self, width=0, height=600, fg_color=light_green, border_width=1,bg_color=dark_green, border_color='black', corner_radius=0)
        side_frame.pack(side='left', fill = 'y')

        heading_label = t.CTkLabel(top_frame, text=curr_frame, font=t.CTkFont(size=18, family='lucida'))
        heading_label.place(relx = 0.5, rely = 0.2)

        menu_btn = t.CTkButton(top_frame, image=getImage('icons/menu.png'), text='', width=10, command=openSidebar, fg_color=dark_green, hover_color=dark_green, border_width=1, border_color='black',bg_color=dark_green)
        menu_btn.place(relx= 0.01, rely= 0.1)
    
        x_btn = t.CTkButton(side_frame, image=getImage('icons/x_mark.png'), text='', command=hideSidebar, width=10, fg_color=dark_green, hover_color=dark_green, border_width=1, border_color='black',bg_color=dark_green)
        x_btn.place(relx=0.8, rely=0.01)

        #Designing side bar
        items = ['Home', 'New Match', 'New Player', 'New Team', 'View Player', 'View Team', 'Edit Player', 'Edit Team', 'Themes']
        i = 1.9
        cnt = 0
        for item in items:
            btn = t.CTkButton(side_frame, text=item, font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/home.png'), command=lambda:menu_change(cnt))
            btn.place(relx=0.2, rely=i*0.1)
            lb = t.CTkLabel(side_frame, text= ' ', width=2, font=('lucida', 16),bg_color=light_green)
            lb.place(relx= 0.1, rely=i*0.1)
            lbs.append(lb)
            i = i + 0.65
            cnt += 1

        menu_change(0)

        btn = t.CTkButton(side_frame, text='Exit', font=t.CTkFont('lucida', 16), command=self.destroy, fg_color=light_green, hover_color=dark_green, text_color='black', width=50)
        btn.place(relx=0.2, rely=0.8)




if __name__ == '__main__':

    app = App(800, 600, 'CricScorer')
    app.mainloop()


