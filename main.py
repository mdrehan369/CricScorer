
import customtkinter as t
from PIL import Image
from tkinter.filedialog import askopenfilename
# import tkinter as tk

dark_green = '#00e600'
light_green = '#66ff66'

def getImage(file, resize=None, decode=False):

    img = Image.open(file)
    if(resize is not None):
        image = t.CTkImage(img, size=resize)
    else:
        image = t.CTkImage(img)
    
    return image


def newPlayer(master):

    def changepic():

        file = askopenfilename(filetypes=(['JPG','*.jpg'], ['JPEG','*.jpeg'], ['PNG','*.png']))
        profile_pic.configure(image = getImage(file, resize=(170,170)))
        remove_profile.place_configure(relx=0.5, rely=0.8, relwidth=0.4, relheight=0.1, anchor='center')

    def removepic():

        profile_pic.configure(image = getImage('icons/user.png', (170,170)))
        remove_profile.place_forget()

    for widget in master.winfo_children():
        widget.destroy()

    main_frame = t.CTkFrame(master, corner_radius=50, border_width=3)
    main_frame.pack(side='left', fill='both', expand=True, padx=20, pady=20)

    #Creating sideframe
    side_frame = t.CTkFrame(main_frame, border_width=2, border_color='gray', corner_radius=30)
    side_frame.place(relx=0.2, rely=0.5, relwidth=0.3, relheight=0.85, anchor='center')

    profile_pic = t.CTkLabel(side_frame, image=getImage('icons/user.png', (170,170)), text=None)
    profile_pic.place(relx=0.5, rely=0.3, anchor='center', relwidth=0.9, relheight=0.45)

    remove_profile = t.CTkButton(side_frame, text='Remove Profile', fg_color='#ff004f', hover_color='red', text_color='black', command=removepic, font=t.CTkFont(family='lucida', size=18), border_width=2)

    add_profile = t.CTkButton(side_frame, text='Add Profile', font = t.CTkFont(family='lucida', size=18), fg_color=light_green, hover_color=dark_green, text_color='black', command=changepic, border_width=2, border_color='gray')
    add_profile.place(relx=0.5, rely=0.65, anchor='center', relwidth=0.4, relheight=0.1)

    #Creating infoframe
    infoframe = t.CTkFrame(main_frame, border_width=2, border_color='gray', corner_radius=30)
    infoframe.place(relx=0.65, rely=0.5, relwidth=0.55, relheight=0.85, anchor='center')

    #Creating names area
    firstName = t.StringVar()
    middleName = t.StringVar()
    lastName = t.StringVar()
    gender = t.StringVar()

    t.CTkLabel(infoframe, text='First Name* : ', font=t.CTkFont(family='roboto', size=18), text_color='black').place(relx=0.1, rely=0.1)
    t.CTkLabel(infoframe, text='Middle Name : ', font=t.CTkFont(family='roboto', size=18), text_color='black').place(relx=0.1, rely=0.17)
    t.CTkLabel(infoframe, text='last Name : ', font=t.CTkFont(family='roboto', size=18), text_color='black').place(relx=0.1, rely=0.24)

    t.CTkEntry(infoframe, border_width=2, border_color='gray', corner_radius=5, textvariable=firstName, font=t.CTkFont(family='roboto', size=17)).place(relx=0.4, rely=0.1,relwidth=0.55, relheight=0.06)
    t.CTkEntry(infoframe, border_width=2, border_color='gray', corner_radius=5, textvariable=middleName, font=t.CTkFont(family='roboto', size=17)).place(relx=0.4, rely=0.17,relwidth=0.55, relheight=0.06)
    t.CTkEntry(infoframe, border_width=2, border_color='gray', corner_radius=5, textvariable=lastName, font=t.CTkFont(family='roboto', size=17)).place(relx=0.4, rely=0.24,relwidth=0.55, relheight=0.06)

    t.CTkLabel(infoframe, text='Gender : ', font=t.CTkFont(family='roboto', size=18), text_color='black', width=30, height=10).place(relx=0.5, rely=6)
    # t.CTkRadioButton(infoframe, text='Male', font=t.CTkFont(family='roboto', size=18), variable=gender, value='male').pack(side='left',anchor='center', padx=20)
    # t.CTkRadioButton(infoframe, text='Female', font=t.CTkFont(family='roboto', size=18), variable=gender, value='female').pack(side='left',anchor='center')


    # tk.Radiobutton(infoframe, variable=gender, value=1, text= 'Male').pack()


class App(t.CTk):

    def __init__(self, width, height, title):

        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")

        #Creating variables
        self.curr_frame = t.StringVar(value='Home')
            

        def openSidebar():
            side_frame.configure(width = 200)

        def hideSidebar():
            side_frame.configure(width=0)

        def focus(i):
            self.indicator.place_configure(rely=i*0.1)

        def changeheading(heading):
            self.curr_frame.set(heading)



        #Creating frames and basic layout
        top_frame = t.CTkFrame(self, width=800, height=40, fg_color=light_green, border_width=1, corner_radius=0)
        top_frame.pack(side='top', fill='x')
        

        side_frame = t.CTkFrame(self, width=0, height=600, fg_color=light_green, border_width=1,bg_color=dark_green, border_color='black', corner_radius=0)
        side_frame.pack(side='left', fill = 'y')

        heading_label = t.CTkLabel(top_frame, textvariable=self.curr_frame, font=t.CTkFont(size=18, family='lucida'))
        heading_label.place(relx = 0.5, rely = 0.2)

        menu_btn = t.CTkButton(top_frame, image=getImage('icons/menu.png'), text='', width=10, command=openSidebar, fg_color=dark_green, hover_color=dark_green, border_width=1, border_color='black',bg_color=dark_green)
        menu_btn.place(relx= 0.01, rely= 0.1)
    
        x_btn = t.CTkButton(side_frame, image=getImage('icons/close.png'), text='', command=hideSidebar, width=10, fg_color=dark_green, hover_color=dark_green, border_width=1, border_color='black',bg_color=dark_green)
        x_btn.place(relx=0.8, rely=0.01)




        #Designing side bar
        i = 1.9

        self.indicator = t.CTkLabel(side_frame, text= ' ', width=3, font=('lucida', 16),bg_color=dark_green)
        self.indicator.place(relx= 0.1, rely=1.9*0.1)

        home_btn = t.CTkButton(side_frame, text='Home', font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/home.png'), command=lambda:focus(1.9))
        home_btn.place(relx=0.2, rely=i*0.1)
        i += 0.65


        new_match = t.CTkButton(side_frame, text='New Match', font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/newmatch.png'),command=lambda:focus(2.55))
        new_match.place(relx=0.2, rely=i*0.1)
        i += 0.65

        new_player = t.CTkButton(side_frame, text='New Player', font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/newplayer.png'),command=lambda:[focus(3.3), newPlayer(main_frame), changeheading('New Player')])
        new_player.place(relx=0.2, rely=i*0.1)
        i += 0.65

        new_team = t.CTkButton(side_frame, text='New Team', font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/newteam.png'),command=lambda:focus(3.95))
        new_team.place(relx=0.2, rely=i*0.1)
        i += 0.65

        view_player = t.CTkButton(side_frame, text='View Player', font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/viewplayer.png'),command=lambda:focus(4.6))
        view_player.place(relx=0.2, rely=i*0.1)
        i += 0.65


        view_team = t.CTkButton(side_frame, text='View Team', font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/viewteam.png'),command=lambda:focus(5.25))
        view_team.place(relx=0.2, rely=i*0.1)
        i += 0.65

        edit_player = t.CTkButton(side_frame, text='Edit Player', font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/editplayer.png'),command=lambda:focus(5.9))
        edit_player.place(relx=0.2, rely=i*0.1)
        i += 0.65

        edit_team = t.CTkButton(side_frame, text='Edit Team', font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/editteam.png'),command=lambda:focus(6.55))
        edit_team.place(relx=0.2, rely=i*0.1)
        i += 0.65

        themes = t.CTkButton(side_frame, text='Themes', font=t.CTkFont(family='lucida',size= 16), fg_color=light_green, text_color='black', hover_color=dark_green, compound='left', border_color=light_green, width=50, image=getImage('icons/themes.png'),command=lambda:focus(7.2))
        themes.place(relx=0.2, rely=i*0.1)
        i += 0.65

        btn = t.CTkButton(side_frame, text='Exit', font=t.CTkFont('lucida', 16), command=self.destroy, fg_color=light_green, hover_color=dark_green, text_color='black', width=50, image=getImage('icons/exit.png'))
        btn.place(relx=0.2, rely=0.8)


        #designing the main frame

        main_frame = t.CTkFrame(self, corner_radius=0, border_width=0)
        main_frame.pack(side='left', fill='both', expand=True)

        # new_player.bind('<Button-1>', new_player)




if __name__ == '__main__':

    app = App(800, 600, 'CricScorer')
    app.mainloop()


