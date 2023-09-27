from tkinter import *

root = Tk()
root.title('Email sender app')
root.geometry('780x620+100+50')
root.resizable(0,0)
root.config(bg= 'dodgerblue2') 

titleFrame= Frame(root, bg='white')
titleFrame.grid(row=0,column=0)
logoImage=PhotoImage(file='email.png')
titleLabel=Label(titleFrame,text='  Email sender',image=logoImage,compound=LEFT,font=('Goudy oldstyle',28,'bold'),bg='white',fg='dodgerblue2')
titleLabel.grid(row=0,column=0)

settingImage=PhotoImage(file='setting.png')
Button(titleFrame,image=settingImage,bd=0,bg='white',cursor='hand2',activebackground='white').grid(row=0,column=1,padx=20)

chooseFrame=Frame(root,bg='dodgerblue2')
chooseFrame.grid(row=1,column=0,pady=10)
singleVariable=StringVar()
multipleVariable=StringVar()

singleRadioButton=Radiobutton(chooseFrame,text='Single',font=('times new roman',25,'bold'),variable=singleVariable,value='single',bg='dodgerblue2',activebackground='dodgerblue2')
singleRadioButton.grid(row=0,column=0,padx=20)

multipleRadioButton=Radiobutton(chooseFrame,text='Multiple',font=('times new roman',25,'bold'),variable=multipleVariable,value='multiple',bg='dodgerblue2',activebackground='dodgerblue2')
multipleRadioButton.grid(row=0,column=1,padx=20)

toLabelFrame=LabelFrame(root,text='To (Email Address)',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodgerblue2')
toLabelFrame.grid(row=2,column=0)

toEntryField=Entry(toLabelFrame,font=('times new roman',18,'bold'),width=30)
toEntryField.grid(row=0,column=0)

browseImage=PhotoImage(file='browse.png')
Button(toLabelFrame,text='Browse',image=browseImage,compound=LEFT,font=('arial',12,'bold'),cursor='hand2',bd=0,bg='dodgerblue2',activebackground='dodgerblue2').grid(row=0,column=1)


subjectLabelFrame=LabelFrame(root,text='Subject',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodgerblue2')
subjectLabelFrame.grid(row=3,column=0,pady=10)

subjectEntryField=Entry(subjectLabelFrame,font=('times new roman',18,'bold'),width=30)
subjectEntryField.grid(row=0,column=0)



emailLabelFrame=LabelFrame(root,text='Compose Email',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodgerblue2')
emailLabelFrame.grid(row=4,column=0,padx=20)

micImage=PhotoImage(file='mic.png')
Button(emailLabelFrame,text='Speak',image=micImage,compound=LEFT,font=('arial',12,'bold'),cursor='hand2',bd=0,bg='dodgerblue2',activebackground='dodgerblue2').grid(row=0,column=0)


attachImage=PhotoImage(file='attachments.png')
Button(emailLabelFrame,text='Attachment',image=attachImage,compound=LEFT,font=('arial',12,'bold'),cursor='hand2',bd=0,bg='dodgerblue2',activebackground='dodgerblue2').grid(row=0,column=1)


textarea=Text(emailLabelFrame,font=('times new roman',14,),height=8)
textarea.grid(row=1,column=0,columnspan=2)


sendImage=PhotoImage(file='send.png')
Button(titleFrame,image=sendImage,bd=0,bg='dodgerblue2',cursor='hand2',activebackground='dodgerblue2').place(x=490,y=540)

clearImage=PhotoImage(file='clear.png')
Button(titleFrame,image=clearImage,bd=0,bg='dodgerblue2',cursor='hand2',activebackground='dodgerblue2').place(x=590,y=550)

exitImage=PhotoImage(file='exit.png')
Button(titleFrame,image=exitImage,bd=0,bg='dodgerblue2',cursor='hand2',activebackground='dodgerblue2').place(x=690,y=550)


totalLabel=Label(root,font=('times new roman',18,'bold'),bg='dodgerblue2',fg='black')
totalLabel.place(x=10,y=560)

sentLabel=Label(root,font=('times new roman',18,'bold'),bg='dodgerblue2',fg='black')
sentLabel.place(x=100,y=560)

leftLabel=Label(root,font=('times new roman',18,'bold'),bg='dodgerblue2',fg='black')
leftLabel.place(x=190,y=560)

failedLabel=Label(root,font=('times new roman',18,'bold'),bg='dodgerblue2',fg='black')
failedLabel.place(x=280,y=560)



root.mainloop()