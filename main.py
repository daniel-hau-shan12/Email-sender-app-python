from tkinter import *

root = Tk()
root.title('Email Sender App')
root.geometry('680x520+100+50')
root.resizable(0, 0)
root.config(bg='dodgerblue2')

titleFrame = Frame(root, bg='white')
titleFrame.grid(row=0, column=0)
logoImage = PhotoImage(
    file='inbox_envelope_receive_letter_mail_icon_219523.png')
titleLabel = Label(titleFrame,
                   text='Email Sender',
                   image=logoImage,
                   compound=LEFT,
                   font=('Goudy old style', 10, 'bold'),
                   bg='white',
                   fg='dodgerblue2')
titleLabel.grid(row=0, column=0)

settingImage = PhotoImage(file='folder_settings_tools_22597.png')
Button(titleFrame,
       image=settingImage,
       cursor='hand2',
       activebackground='white').grid(row=0, column=1)

root.mainloop()
