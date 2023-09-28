###########################@@@Imported Files@@@############################
from tkinter import*
from tkinter import ttk
from Main_Module import*
import datetime
from tkinter import messagebox as mb
###########################@@@Functions Used@@@############################
def copyrights():
    wel_frame.grid_forget()
    cor.grid(row=0,column=0,padx=130,pady=200)
def call_wel():
    U=use_var.get()
    P=pass_var.get()
    if U=='':
        user_entry1=Entry(sign_frame,textvariable=use_var,highlightcolor='red',highlightthickness=2)
        user_entry1.grid(row=2,column=1,padx=20)
        user_entry1.focus()
        mb.showinfo("Error","Please Fill All Information")
        return
    if P=='':
        passw_entry1=Entry(sign_frame,show='*',textvariable=pass_var,highlightcolor='red',highlightthickness=2)
        passw_entry1.grid(row=3,column=1,padx=20)
        passw_entry1.focus()
        mb.showinfo("Error","Please Fill All Information")
        return
    f=open('Pass.txt','r')
    l=f.readlines()
    for i in l:
        a=i.find('[u=')+3
        b=i.find(' p=')
        e=i.find(']')
        c=b
        b=b+3
        u=i[a:c]
        p=i[b:e]
        if u==U and p==P:
            user_entry.delete(0,END)
            passw_entry.delete(0,END)
            sign_frame.grid_forget()
            wel_frame.grid(column=0, row=0,padx=230,pady=150)
            return
        elif i==l[len(l)-1]:
            user_entry.delete(0,END)
            passw_entry.delete(0,END)
            mb.showinfo("Info","No!! Account with This Information")
def BkTF():
    sign2_frame.grid_forget()
    welcome_frame.grid(row=0,column=0,pady=155,padx=85)
def BkTF2():
    sign_frame.grid_forget()
    welcome_frame.grid(row=0,column=0,pady=155,padx=85)
def call_wel2():
    global name_e, age_e, dob_e, user_e, pass1_e, pass2_e
    l=[name_var.get(),dob_var.get(),gender_var.get(),state_var.get(),user_var.get(),pass1_var.get()]
    for i in age_var.get():
        if ord(i) not in [48,49,50,51,52,53,54,55,56,57]:
            mb.showinfo("Info","Please Fill Age in Integer type")
            return
    for i in dob_var.get():
        if ord(i) not in [48,49,50,51,52,53,54,55,56,57]:
            mb.showinfo("Info","Please Fill D.O.B in Integer type")
            return
    if len(dob_var.get())!=8:
        mb.showinfo("Info","Please Fill Full Date")
        return
    for i in range(len(l)):
        if l[i]=='':
            if i==0:
                name_e=Entry(sign2_frame,width=20,textvariable=name_var,highlightcolor='red',highlightthickness=2)
                name_e.focus()
                name_e.grid(row=2,column=1,padx=10)
                mb.showinfo("Error","Please Fill All Information")
                return
            if i==1:
                age_e=Entry(sign2_frame,width=20,textvariable=age_var,highlightcolor='red',highlightthickness=2)
                age_e.focus()
                age_e.grid(row=3,column=1,padx=10)
                mb.showinfo("Error","Please Fill All Information")
                return
            if i==1:
                dob_e=Entry(sign2_frame,width=20,textvariable=dob_var,highlightcolor='red',highlightthickness=2)
                dob_e.focus()
                dob_e.grid(row=4,column=1,padx=10)
                mb.showinfo("Error","Please Fill All Information")
                return
            if i==4:
                user_e=Entry(sign2_frame,width=20,textvariable=user_var,highlightcolor='red',highlightthickness=2)
                user_e.focus()
                user_e.grid(row=7,column=1,padx=10)
                mb.showinfo("Error","Please Fill All Information")
                return
            if i==5:
                pass1_e=Entry(sign2_frame,width=20,textvariable=pass1_var,highlightcolor='red',highlightthickness=2,show='*')
                pass1_e.focus()
                pass1_e.grid(row=8,column=1,padx=10)
                mb.showinfo("Error","Please Fill All Information")
                return
        else:
            if pass2_var.get()=='':
                pass2_e=Entry(sign2_frame,width=20,textvariable=pass2_var,highlightcolor='red',highlightthickness=2,show='*')
                pass2_e.focus()
                pass2_e.grid(row=9,column=1,padx=10) 
                mb.showinfo("Error","Please Fill All Information")
                return
            else:
                pass
    d=str(datetime.date.today())
    y1=int(d[0:4])
    m1=int(d[5:7])
    d1=int(d[8:10])
    y=int(dob_var.get()[4:])
    m=int(dob_var.get()[2:4])
    date=int(dob_var.get()[0:2])
    a=int(age_var.get())
    if y1-y!=a and y1-y-1!=a:
        mb.showinfo("Error","Age and D.O.B does\'nt match")
        return
    if y1-y==a :
        if m1==m:
            if d1<date:
              mb.showinfo("Error","Age and D.O.B does\'nt match")
              return
        elif m1<m:
            mb.showinfo("Error","Age and D.O.B does\'nt match")
            return
    if y1-y-1==a:
        if m1==m:
            if d1>=date:
                mb.showinfo("Error","Age and D.O.B does\'nt match")
                return
        elif m1>m:
            mb.showinfo("Error","Age and D.O.B does\'nt match")
            return 
    if pass1_var.get()!=pass2_var.get():
        mb.showinfo("Error","Two Different Password Given Rewrite Them!!")
        delete(pass1_e)
        delete(pass2_e)
        pass1_e=Entry(sign2_frame,width=20,textvariable=pass1_var,highlightcolor='red',highlightthickness=2,show='*')
        pass1_e.focus()
        pass1_e.grid(row=8,column=1,padx=10)
        return
    else:
        f=open('Pass.txt','a+')
        f.write(name_var.get() +' '+ dob_var.get() +' '+ gender_var.get() +' '+ state_var.get() +' [u='+ user_var.get() +' p='+ pass1_var.get() + ']\n')
        f.flush()
        f.close()
        name_e.delete(0,END)
        age_e.delete(0,END)
        dob_e.delete(0,END)
        user_e.delete(0,END)
        pass1_e.delete(0,END)
        pass2_e.delete(0,END)
        sign2_frame.grid_forget()
        wel_frame.grid(column=0, row=0,padx=230,pady=150)
def Bktwel_fr():
    wel_frame.grid(column=0, row=0,padx=230,pady=150)
    cor.grid_forget()
def BkTM():
    wel_frame.grid(column=0, row=0,padx=230,pady=150)
    chem_frame.grid_forget()
def call_sign():
    sign_frame.grid(column=0, row=0,padx=170,pady=180)
    welcome_frame.grid_forget()
def chem_menu():
    wel_frame.grid_forget()
    chem_frame.grid(row=0,column=0,padx=160,pady=30)
def history():
    wel_frame.grid_forget()
    his.grid(row=0,column=0,padx=180,pady=26)
def register():
    sign2_frame.grid(column=0, row=0,padx=420,pady=13)
    welcome_frame.grid_forget()
def Back1():
    his.grid_forget()
    wel_frame.grid(column=0, row=0,padx=230,pady=150)
def logout():
    a=mb.askyesno('Informative Software','Do You Want To LOG OUT ?')
    if a==True:
        wel_frame.grid_forget()
        welcome_frame.grid(row=0,column=0,pady=155,padx=85)
def Quit():
    a=mb.askyesno('Informative Software','Do You Want To Quit ?')
    if a== True:
        root.destroy()
###########################@@@Window & Frames@@@###########################
root=Tk()
root.title("ELEMENT'S WORLD")
root.geometry('1300x700')
root.config(bg='#68d9d3')
w = 1200
h = 600
#WELCOME Frame
welcome_frame=Frame(root,relief='ridge', borderwidth=10)
welcome_frame.config(background='#0960f0')
welcome_label=Label(welcome_frame,text="Welcome To Our ELEMENT'S WORLD",
                    font=('Cambria',35,'bold','underline'),fg='#11ff2f',bg='#0960f0')
welcome_label.grid(row=0,column=0,padx=100,pady=100,columnspan=3)
btn1=ttk.Button(welcome_frame,text='   Sign In   ',command=call_sign).grid(row=1,column=0,pady=10,padx=4)
btn2=ttk.Button(welcome_frame,text='   Sign Up   ',command=register).grid(row=1,column=1,pady=10,padx=4)
btn3=ttk.Button(welcome_frame,text='    Quit      ',command=Quit).grid(row=1,column=2,pady=10,padx=4)
welcome_frame.grid(row=0,column=0,pady=155,padx=85)
#SIGN-IN Frame
sign_frame=Frame(root,relief='ridge', borderwidth=10)
sign_frame.config(background='#c0c0c0')
top_label=Label(sign_frame,text="WELCOME  TO  INFORMATIVE  PROJECT",
                font=('Palatino Linotype',30,'bold','underline'),fg='#0f03f5',bg='#c0c0c0').grid(row=0,column=0,padx=10,columnspan=3)
sign_label=Label(sign_frame,text='---SIGN IN---',font=('HP Simplified',20,),fg='#0f03f5',bg='#c0c0c0')
sign_label.grid(row=1,column=0,padx=10,columnspan=4)
user_label=Label(sign_frame,text='Enter Username -',font=('Candara',25,'bold'),fg='#0f03f5',bg='#c0c0c0')
user_label.grid(row=2,column=0,padx=2)
use_var=StringVar()
user_entry=Entry(sign_frame,textvariable=use_var)
user_entry.grid(row=2,column=1,padx=20)
user_entry.focus()
passw_label=Label(sign_frame,text='Enter Password -',font=('Candara',25,'bold'),fg='#0f03f5',bg='#c0c0c0')
passw_label.grid(row=3,column=0,padx=20)
pass_var=StringVar()
passw_entry=Entry(sign_frame,show='*',textvariable=pass_var)
passw_entry.grid(row=3,column=1,padx=20)
bk=ttk.Button(sign_frame,text='  Back  ',command=BkTF2).grid(row=4,column=0,pady=15,padx=20)
ok_button=ttk.Button(sign_frame,text='SUBMIT',command=call_wel).grid(row=4,column=1,pady=15,padx=20)
sign_frame.grid(column=0, row=0)
#Create Account Frame
sign2_frame=Frame(root,width=w,height=h,relief='ridge', borderwidth=10)
sign2_frame.config(background='#00009f')
lab1=Label(sign2_frame,text='Create Account',font=('Mongolian Baiti',25,'bold','underline'),fg='#ffffff',bg='#00009f')
lab1.grid(row=0,column=0,padx=10,columnspan=3)
lab2=Label(sign2_frame,text="**Please Fill This Form To Proceed**",fg='#ffffff',bg='#00009f').grid(row=1,column=0)
name_l=Label(sign2_frame,text='Enter Full Name',font=('gabriola',20,'bold'),fg='#ffffff',bg='#00009f')
name_l.grid(row=2,column=0,padx=10)
name_var=StringVar()
name_e=Entry(sign2_frame,width=20,textvariable=name_var)
name_e.grid(row=2,column=1,padx=10)
name_e.focus()
age_l=Label(sign2_frame,text='Enter Age',font=('gabriola',20,'bold'),fg='#ffffff',bg='#00009f')
age_l.grid(row=3,column=0,padx=10)
age_var=StringVar()
age_e=Entry(sign2_frame,width=20,textvariable=age_var)
age_e.grid(row=3,column=1,padx=10)
dob_l=Label(sign2_frame,text='Enter Date of Birth(ddmmyyyy)',font=('gabriola',20,'bold'),fg='#ffffff',bg='#00009f')
dob_l.grid(row=4,column=0,padx=10)
dob_var=StringVar()
dob_e=Entry(sign2_frame,width=20,textvariable=dob_var)
dob_e.grid(row=4,column=1,padx=10)
gender_l=Label(sign2_frame,text='Select Your Gender',font=('gabriola',20,'bold'),fg='#ffffff',bg='#00009f')
gender_l.grid(row=5,column=0,padx=10)
gender_var=StringVar()
gender_combo=ttk.Combobox(sign2_frame,width=18,textvariable=gender_var,state='readonly')
gender_combo['values']=('Male','Female')
gender_combo.current(0)
gender_combo.grid(row=5,column=1,padx=10)
state_l=Label(sign2_frame,text='Select Your State',font=('gabriola',20,'bold'),fg='#ffffff',bg='#00009f')
state_l.grid(row=6,column=0,padx=10)
state_var=StringVar()
state_combo=ttk.Combobox(sign2_frame,width=18,textvariable=state_var,state='readonly')
state_combo['values']=("Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chattisgarh","Delhi","Goa",
                       "Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala",
                       "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
                       "Rajasthan","Sikkim","Tamil Nadu","Tripura","Uttar Pradesh","Uttrakhand","West Bengal")
state_combo.current(0)
state_combo.grid(row=6,column=1,padx=10)
user_l=Label(sign2_frame,text='Enter Your Username',font=('gabriola',20,'bold'),fg='#ffffff',bg='#00009f')
user_l.grid(row=7,column=0,padx=10)
user_var=StringVar()
user_e=Entry(sign2_frame,width=20,textvariable=user_var)
user_e.grid(row=7,column=1,padx=10)
pass1_l=Label(sign2_frame,text='Enter Your Password',font=('gabriola',20,'bold'),fg='#ffffff',bg='#00009f')
pass1_l.grid(row=8,column=0,padx=10)
pass1_var=StringVar()
pass1_e=Entry(sign2_frame,width=20,show='*',textvariable=pass1_var)
pass1_e.grid(row=8,column=1,padx=10)
pass2_l=Label(sign2_frame,text='Rewrite Your Password',font=('gabriola',20,'bold'),fg='#ffffff',bg='#00009f')
pass2_l.grid(row=9,column=0,padx=10)
pass2_var=StringVar()
pass2_e=Entry(sign2_frame,width=20,show='*',textvariable=pass2_var)
pass2_e.grid(row=9,column=1,padx=10)
sub=ttk.Button(sign2_frame,text=' Submit ',command=call_wel2).grid(row=10,column=1,pady=5)
bk=ttk.Button(sign2_frame,text='  Back  ',command=BkTF).grid(row=10,column=0,pady=5)
sign2_frame.grid(column=0, row=0)
#MENU Frame
wel_frame=Frame(root,width=w,height=h,relief='ridge', borderwidth=10)
wel_frame.config(background='#00b900')
wel_label=Label(wel_frame,text='You Successfully Logged In !!',bd=25,
              font=('Mongolian Baiti',40,'bold'),fg='#ffff0d',bg='#00b900')
wel_label.grid(row=0,column=0,padx=10,pady=20,columnspan=4)
wel_prdctbl=ttk.Button(wel_frame,text=' Periodic Table ',command=chem_menu)
wel_prdctbl.grid(row=1,column=0,padx=5,pady=10,ipadx=10,ipady=10)
wel_coprt=ttk.Button(wel_frame,text='Copyrights',command=copyrights)
wel_coprt.grid(row=2,column=1,pady=10,ipadx=10,ipady=10)
wel_his=ttk.Button(wel_frame,text='History',command=history)
wel_his.grid(row=1,column=2,pady=5,ipadx=10,ipady=10)
wel_lgot=ttk.Button(wel_frame,text='Log Out',command=logout)
wel_lgot.grid(row=2,column=3,ipadx=10,ipady=10)
wel_frame.grid(row=0,column=0)
wel_frame.grid_forget()
#COPYRIGHT Frame
cor=Frame(root,width=w,height=h,relief='ridge', borderwidth=10)
cor.config(background='#154360')
cr_lab1=Label(cor,text='Copyrights',font=('Times New Roman',30,'underline'),fg='#FFDF00',bg='#154360')
cr_lab1.grid(row=0,column=0,pady=20)
d=str(datetime.date.today())
a=d[0:4]
cr_lab2=Label(cor,text='Copyright (c) 2019-'+a+' Shivam Kumar, Shubham Prajapati, Vinit Aggarwal',
              font=('Goudy Old Style',20),fg='#FFDF00',bg='#154360').grid(row=1,column=0,padx=20,pady=10)
cr_lab3=Label(cor,text='All Rights Reserved.',font=('Goudy Old Style',20),fg='#FFDF00',bg='#154360')
cr_lab3.grid(row=2,column=0,padx=20,pady=10)
btn_bk=Button(cor,text='Back',command=Bktwel_fr).grid(row=2,column=1,padx=15)
cor.grid(row=0,column=0)
cor.grid_forget()
#HISTORY Frame
his=Frame(root,width=w,height=h,relief='ridge', borderwidth=10)
his.config(background='#5B2C6F')
his_lab1=Label(his,text='History',font=('Palatino Linotype',40,'bold','underline'),bg='#5B2C6F',fg='#ffffff')
his_lab1.grid(row=0,column=0,pady=10,columnspan=2)
his_lab2=Label(his,text='''Some elements were known since ancient times, such as gold, sulphur, and carbon. Alchemists
began to discover and identify new elements in the 17th century. By the beginning of the
19th century, about 47 elements had been discovered, providing enough data for chemists
to begin to see patterns. John Newlands had published his Law of Octaves in 1865. The
Law of Octaves had two elements in one box and did not allow space for undiscovered
elements, so it was criticized and did not gain recognition. A year earlier (1864)
Lothar Meyer published a periodic table that described the placement of 28 elements.
Meyer's periodic table ordered the elements into groups arranged in order of their
atomic weights. His periodic table arranged the elements into six families according to
their valence, which was the first attempt to classify the elements according to this property.
French geologist Alexandre-Emile Beguyer de Chancourtois noticed this trend earlier and
in 1862, he devised a three-dimensional chart, named the "telluric helix".With the elements
arranged in a spiral on a cylinder by order of increasing atomic weight, de Chancourtois saw
that elements with similar properties lined up vertically. Russian chemist Dmitri Mendeleev arranged
the elements by atomic mass, corresponding to relative molar mass.Mendeleev continued to
improve his ordering; in 1870, it gained a tabular shape, and in 1871, it was titled "periodic table".
Some changes also occurred with new revisions, with some elements changing positions.''',
               font=('Times New Roman',14),bg='#5B2C6F',fg='#ffffff').grid(row=1,column=0,padx=5)
his_lab3=Label(his,text=' '*(180)+'Source:-thoughtco.com,wikipedia.org',
               font=('Times New Roman',8),bg='#5B2C6F',fg='#ffffff').grid(row=2,column=0,padx=3)
bkntn=Button(his,text='Back',command=Back1).grid(row=2,column=1,padx=5,pady=5)
his.grid(row=0,column=0)
#CHEMISTRY Frame
chem_frame=Frame(root,width=w,height=h,relief='ridge', borderwidth=10)
chem_frame.config(background='#a8a8ff')
label1=Label(chem_frame,text='The Periodic Table',bd=25,
             font=('Times New Roman',72,'underline'),fg='blue',bg='#a8a8ff')
label1.grid(row=0,column=0,columnspan=2,padx=50,pady=30)
chem_frame2=Frame(chem_frame,width=w,height=h)
chem_frame2.config(background='#a8a8ff')
chem_frame3=Frame(chem_frame,width=w,height=h)
chem_frame3.config(background='#a8a8ff')
chem_frame4=Frame(chem_frame,width=w,height=h)
chem_frame4.config(background='#a8a8ff')
btn=ttk.Button(chem_frame,text='Back',command=BkTM).grid(row=3,column=1,pady=15,padx=10,sticky=S)
button1=Button(chem_frame2,text=' H  ', command=ANo1,activebackground='green', bg='teal',font=('Times New Roman',  11,'bold')).grid(row=5,column=0)
button2=Button(chem_frame2,text=' He ', command=ANo2,activebackground='crimson',bg='purple',font=('Times New Roman',  11,'bold')).grid(row=5,column=17)
button3=Button(chem_frame2,text=' Li ', command=ANo3, activebackground='plum',bg='crimson',font=('Times New Roman',  11,'bold')).grid(row=6,column=0)
button4=Button(chem_frame2,text=' Be ', command=ANo4, activebackground='gold',bg='orange',font=('Times New Roman',  11,'bold')).grid(row=6,column=1)
button5=Button(chem_frame2,text=' B ', command=ANo5, activebackground='teal',bg='green',font=('Times New Roman',  11,'bold')).grid(row=6,column=12)
button6=Button(chem_frame2,text=' C ', command=ANo6,activebackground='green',bg='teal', font=('Times New Roman',  11,'bold')).grid(row=6,column=13)
button7=Button(chem_frame2,text=' N ', command=ANo7, activebackground='green',bg='teal',font=('Times New Roman',  11,'bold')).grid(row=6,column=14)
button8=Button(chem_frame2,text='  O ', command=ANo8,activebackground='green', bg='teal',font=('Times New Roman',  11,'bold')).grid(row=6,column=15)
button9=Button(chem_frame2,text='  F  ', command=ANo9, activebackground='sky blue',bg='#1188ff',font=('Times New Roman',  11,'bold')).grid(row=6,column=16)
button10=Button(chem_frame2,text=' Ne ', command=ANo10, activebackground='crimson',bg='purple',font=('Times New Roman',  11,'bold')).grid(row=6,column=17)
button11=Button(chem_frame2,text='Na', command=ANo11, activebackground='plum',bg='crimson',font=('Times New Roman',  11,'bold')).grid(row=7,column=0)
button12=Button(chem_frame2,text='Mg', command=ANo12,activebackground='gold', bg='orange',font=('Times New Roman',  11,'bold')).grid(row=7,column=1)
button13=Button(chem_frame2,text=' Al', command=ANo13,activebackground='aqua', bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=7,column=12)
button14=Button(chem_frame2,text=' Si', command=ANo14, activebackground='teal',bg='green',font=('Times New Roman',  11,'bold')).grid(row=7,column=13)
button15=Button(chem_frame2,text=' P ', command=ANo15, activebackground='green',bg='teal',font=('Times New Roman',  11,'bold')).grid(row=7,column=14)
button16=Button(chem_frame2,text='  S ', command=ANo16, activebackground='green',bg='teal',font=('Times New Roman',  11,'bold')).grid(row=7,column=15)
button17=Button(chem_frame2,text=' Cl ', command=ANo17, activebackground='sky blue',bg='#1188ff',font=('Times New Roman',  11,'bold')).grid(row=7,column=16)
button18=Button(chem_frame2,text=' Ar ', command=ANo18,activebackground='crimson',bg='purple', font=('Times New Roman',  11,'bold')).grid(row=7,column=17)
button19=Button(chem_frame2,text=' K ', command=ANo19,activebackground='plum', bg='crimson',font=('Times New Roman',  11,'bold')).grid(row=8,column=0)
button20=Button(chem_frame2,text=' Ca', command=ANo20, activebackground='gold',bg='orange',font=('Times New Roman',  11,'bold')).grid(row=8,column=1)
button21=Button(chem_frame2,text=' Sc ', command=ANo21, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=2)
button22=Button(chem_frame2,text='Ti', command=ANo22, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=3)
button23=Button(chem_frame2,text=' V ', command=ANo23,activebackground='orchid', bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=4)
button24=Button(chem_frame2,text=' Cr', command=ANo24, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=5)
button25=Button(chem_frame2,text='Mn', command=ANo25, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=6)
button26=Button(chem_frame2,text=' Fe', command=ANo26,activebackground='orchid', bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=7)
button27=Button(chem_frame2,text='Co', command=ANo27, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=8)
button28=Button(chem_frame2,text='Ni', command=ANo28, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=9)
button29=Button(chem_frame2,text='Cu', command=ANo29, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=10)
button30=Button(chem_frame2,text='Zn', command=ANo30,activebackground='orchid', bg='gold',font=('Times New Roman',  11,'bold')).grid(row=8,column=11)
button31=Button(chem_frame2,text='Ga', command=ANo31,activebackground='aqua', bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=8,column=12)
button32=Button(chem_frame2,text='Ge', command=ANo32, activebackground='teal',bg='green',font=('Times New Roman',  11,'bold')).grid(row=8,column=13)
button33=Button(chem_frame2,text='As', command=ANo33, activebackground='teal',bg='green',font=('Times New Roman',  11,'bold')).grid(row=8,column=14)
button34=Button(chem_frame2,text=' Se', command=ANo34, activebackground='green',bg='teal',font=('Times New Roman',  11,'bold')).grid(row=8,column=15)
button35=Button(chem_frame2,text='  Br ', command=ANo35,activebackground='sky blue',bg='#1188ff', font=('Times New Roman',  11,'bold')).grid(row=8,column=16)
button36=Button(chem_frame2,text=' Kr ', command=ANo36, activebackground='crimson',bg='purple',font=('Times New Roman',  11,'bold')).grid(row=8,column=17)
button37=Button(chem_frame2,text='Rb', command=ANo37, activebackground='plum',bg='crimson',font=('Times New Roman',  11,'bold')).grid(row=9,column=0)
button38=Button(chem_frame2,text=' Sr', command=ANo38,activebackground='gold',bg='orange', font=('Times New Roman',  11,'bold')).grid(row=9,column=1)
button39=Button(chem_frame2,text='   Y  ', command=ANo39,activebackground='orchid',bg='gold', font=('Times New Roman',  11,'bold')).grid(row=9,column=2)
button40=Button(chem_frame2,text='Zr', command=ANo40, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=9,column=3)
button41=Button(chem_frame2,text='Nb', command=ANo41, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=9,column=4)
button42=Button(chem_frame2,text='Mo', command=ANo42, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=9,column=5)
button43=Button(chem_frame2,text=' Tc', command=ANo43,activebackground='orchid', bg='gold',font=('Times New Roman',  11,'bold')).grid(row=9,column=6)
button44=Button(chem_frame2,text='Ru', command=ANo44,activebackground='orchid', bg='gold',font=('Times New Roman',  11,'bold')).grid(row=9,column=7)
button45=Button(chem_frame2,text='Rh', command=ANo45,activebackground='orchid', bg='gold',font=('Times New Roman',  11,'bold')).grid(row=9,column=8)
button46=Button(chem_frame2,text='Pd', command=ANo46, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=9,column=9)
button47=Button(chem_frame2,text='Ag', command=ANo47, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=9,column=10)
button48=Button(chem_frame2,text='Cd', command=ANo48, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=9,column=11)
button49=Button(chem_frame2,text=' In', command=ANo49,activebackground='aqua', bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=9,column=12)
button50=Button(chem_frame2,text='Sn', command=ANo50,activebackground='aqua', bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=9,column=13)
button51=Button(chem_frame2,text=' Sb', command=ANo51, activebackground='teal',bg='green',font=('Times New Roman',  11,'bold')).grid(row=9,column=14)
button52=Button(chem_frame2,text=' Te', command=ANo52,activebackground='teal',bg='green', font=('Times New Roman',  11,'bold')).grid(row=9,column=15)
button53=Button(chem_frame2,text='   I  ', command=ANo53, activebackground='sky blue',bg='#1188ff',font=('Times New Roman',  11,'bold')).grid(row=9,column=16)
button54=Button(chem_frame2,text=' Xe ', command=ANo54, activebackground='crimson',bg='purple',font=('Times New Roman',  11,'bold')).grid(row=9,column=17)
button55=Button(chem_frame2,text=' Cs', command=ANo55, activebackground='plum',bg='crimson',font=('Times New Roman',  11,'bold')).grid(row=10,column=0)
button56=Button(chem_frame2,text=' Ba', command=ANo56, activebackground='gold',bg='orange',font=('Times New Roman',  11,'bold')).grid(row=10,column=1)
buttonL=Button(chem_frame2,text='  La* ', command=ANo57,activebackground='pink', bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=10,column=2)
button72=Button(chem_frame2,text='Hf', command=ANo72,activebackground='orchid',bg='gold', font=('Times New Roman',  11,'bold')).grid(row=10,column=3)
button73=Button(chem_frame2,text='Ta', command=ANo73, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=10,column=4)
button74=Button(chem_frame2,text=' W ', command=ANo74,activebackground='orchid',bg='gold', font=('Times New Roman',  11,'bold')).grid(row=10,column=5)
button75=Button(chem_frame2,text=' Re', command=ANo75,activebackground='orchid', bg='gold',font=('Times New Roman',  11,'bold')).grid(row=10,column=6)
button76=Button(chem_frame2,text='Os', command=ANo76,activebackground='orchid', bg='gold',font=('Times New Roman',  11,'bold')).grid(row=10,column=7)
button77=Button(chem_frame2,text='  Ir ', command=ANo77, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=10,column=8)
button78=Button(chem_frame2,text=' Pt ', command=ANo78, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=10,column=9)
button79=Button(chem_frame2,text='Au', command=ANo79,activebackground='orchid',bg='gold', font=('Times New Roman',  11,'bold')).grid(row=10,column=10)
button80=Button(chem_frame2,text='Hg', command=ANo80, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=10,column=11)
button81=Button(chem_frame2,text=' Tl', command=ANo81, activebackground='aqua',bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=10,column=12)
button82=Button(chem_frame2,text='Pb', command=ANo82,activebackground='aqua', bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=10,column=13)
button83=Button(chem_frame2,text=' Bi ', command=ANo83, activebackground='aqua',bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=10,column=14)
button84=Button(chem_frame2,text=' Po', command=ANo84,activebackground='teal', bg='green',font=('Times New Roman',  11,'bold')).grid(row=10,column=15)
button85=Button(chem_frame2,text=' At ', command=ANo85, activebackground='sky blue',bg='#1188ff',font=('Times New Roman',  11,'bold')).grid(row=10,column=16)
button86=Button(chem_frame2,text=' Rn ', command=ANo86, activebackground='crimson',bg='purple',font=('Times New Roman',  11,'bold')).grid(row=10,column=17)
button87=Button(chem_frame2,text=' Fr ', command=ANo87,activebackground='plum', bg='crimson',font=('Times New Roman',  11,'bold')).grid(row=11,column=0)
button88=Button(chem_frame2,text='Ra', command=ANo88, activebackground='gold',bg='orange',font=('Times New Roman',  11,'bold')).grid(row=11,column=1)
buttonA=Button(chem_frame2,text='A**', command=ANo89, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=11,column=2)
button104=Button(chem_frame2,text='Rf', command=ANo104, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=11,column=3)
button105=Button(chem_frame2,text='Db', command=ANo105, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=11,column=4)
button106=Button(chem_frame2,text='Sg', command=ANo106, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=11,column=5)
button107=Button(chem_frame2,text='Bh', command=ANo107, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=11,column=6)
button108=Button(chem_frame2,text='Hs', command=ANo108, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=11,column=7)
button109=Button(chem_frame2,text='Mt', command=ANo109, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=11,column=8)
button110=Button(chem_frame2,text='Ds', command=ANo110,activebackground='orchid', bg='gold',font=('Times New Roman',  11,'bold')).grid(row=11,column=9)
button111=Button(chem_frame2,text='Rg', command=ANo111, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=11,column=10)
button112=Button(chem_frame2,text='Cn', command=ANo112, activebackground='orchid',bg='gold',font=('Times New Roman',  11,'bold')).grid(row=11,column=11)
button113=Button(chem_frame2,text='Nh', command=ANo113, activebackground='aqua',bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=11,column=12)
button114=Button(chem_frame2,text=' Fl ', command=ANo114,activebackground='aqua', bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=11,column=13)
button115=Button(chem_frame2,text='Mc', command=ANo115, activebackground='aqua',bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=11,column=14)
button116=Button(chem_frame2,text=' Lv', command=ANo116, activebackground='aqua',bg='yellow',font=('Times New Roman',  11,'bold')).grid(row=11,column=15)
button117=Button(chem_frame2,text=' Ts ', command=ANo117, activebackground='sky blue',bg='#1188ff',font=('Times New Roman',  11,'bold')).grid(row=11,column=16)
button118=Button(chem_frame2,text=' Og ', command=ANo118, activebackground='crimson',bg='purple',font=('Times New Roman',  11,'bold')).grid(row=11,column=17)
button57=Button(chem_frame3,text=' La', command=ANo57, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=2)
button58=Button(chem_frame3,text='Ce', command=ANo58, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=3)
button59=Button(chem_frame3,text='Pr', command=ANo59,activebackground='pink', bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=4)
button60=Button(chem_frame3,text='Nd', command=ANo60, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=5)
button61=Button(chem_frame3,text='Pm', command=ANo61, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=6)
button62=Button(chem_frame3,text='Sm', command=ANo62, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=7)
button63=Button(chem_frame3,text=' Eu', command=ANo63,activebackground='pink', bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=8)
button64=Button(chem_frame3,text='Gd', command=ANo64, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=9)
button65=Button(chem_frame3,text='Tb', command=ANo65, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=10)
button66=Button(chem_frame3,text='Dy', command=ANo66,activebackground='pink', bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=11)
button67=Button(chem_frame3,text='Ho', command=ANo67, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=12)
button68=Button(chem_frame3,text=' Er ', command=ANo68, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=13)
button69=Button(chem_frame3,text='Tm', command=ANo69, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=14)
button70=Button(chem_frame3,text='Yb', command=ANo70, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=15)
button71=Button(chem_frame3,text='Lu', command=ANo71, activebackground='pink',bg='orchid',font=('Times New Roman',  11,'bold')).grid(row=12,column=16)
button89=Button(chem_frame3,text='Ac', command=ANo89, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=2)
button90=Button(chem_frame3,text='Th', command=ANo90,activebackground='salmon', bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=3)
button91=Button(chem_frame3,text='Pa', command=ANo91, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=4)
button92=Button(chem_frame3,text=' U ', command=ANo92, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=5)
button93=Button(chem_frame3,text='Np', command=ANo93,activebackground='salmon', bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=6)
button94=Button(chem_frame3,text='Pu', command=ANo94, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=7)
button95=Button(chem_frame3,text='Am', command=ANo95, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=8)
button96=Button(chem_frame3,text='Cm', command=ANo96,activebackground='salmon', bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=9)
button97=Button(chem_frame3,text='Bk', command=ANo97, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=10)
button98=Button(chem_frame3,text=' Cf', command=ANo98,activebackground='salmon',bg='maroon', font=('Times New Roman',  11,'bold')).grid(row=13,column=11)
button99=Button(chem_frame3,text=' Es', command=ANo99, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=12)
button100=Button(chem_frame3,text='Fm', command=ANo100, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=13)
button101=Button(chem_frame3,text='Md', command=ANo101, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=14)
button102=Button(chem_frame3,text='No', command=ANo102, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=15)
button103=Button(chem_frame3,text='Lr', command=ANo103, activebackground='salmon',bg='maroon',font=('Times New Roman',  11,'bold')).grid(row=13,column=16)
chem_frame2.grid(row=1,column=0,padx=50)
chem_frame3.grid(row=3,column=0,pady=20)
chem_frame.grid(row=0,column=0)
#Forget all frame axcept SIGN-IN Frame
sign_frame.grid_forget()
sign2_frame.grid_forget()
his.grid_forget()
chem_frame.grid_forget()
wel_frame.grid_forget()
root.mainloop()
############################@@@End Of File@@@#############################
