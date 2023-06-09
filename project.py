from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
from tkinter import messagebox

def Database():
    global conn, cursor
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()
    

def mainwindow():
    root = Tk()
    w = 900
    h = 400
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#FFD1D1')
    root.title("Project by Jirat")
    root.option_add('*font',"Garamond 12 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginlayout() :
    global userentry,pwdentry
    global loginframe

    loginframe = Frame(root,bg='#FFD1D1')
    #loginframe.place(width=900,height=400)
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    loginframe.grid(sticky="news",row=3,column=1)
    
    Label(loginframe,image=img,bg="#FFD1D1").grid(row=0,column=1,sticky=W,padx=10)
    Label(loginframe,text="Username : ",bg='#FFD1D1',fg='black',padx=20).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e4fbff',width=20,font=('Garamond 15'),textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e4fbff',width=20,font=('Garamond 15'),show='*',textvariable=pwdinfo)
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='#FFD1D1',fg='black',padx=20).grid(row=2,column=0,sticky='e')
    Button(loginframe,text="Login",width=10,bg='#FF9494',command=lambda:loginclick(userinfo.get(),pwdinfo.get())).grid(row=3,column=1,pady=20,ipady=15,sticky='e',padx=20)
    Button(loginframe,text="Register",width=10,bg='#FF9494',command=regislayout).grid(row=3,column=1,pady=20,ipady=15,sticky='w')
    Button(loginframe,text='Exit',width=10,height=1,command=root.quit).grid(row=3,column=0,pady=20,ipady=15,sticky='w',padx=20)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def loginclick(user,pwd) :
    #global result
    if user == "" :
        messagebox.showwarning("Admin:","Pleas enter username")
        userentry.focus_force()
    else :
        sql = "select * from login where username=?"
        cursor.execute(sql,[user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Admin:","Please enter password")
                pwdentry.focus_force()
            else :
                sql = "select * from login where username=? and password=? "
                cursor.execute(sql,[user,pwd])   #case1
                #cursor.execute(sql,(user,pwd))   #case2
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Admin:","Login Successfully")
                    print(result)
                    Displaymain(root)
                else :
                    messagebox.showwarning("Admin:","Incorrect Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found\n Please register before Login")
            userentry.select_range(0,END)
            userentry.focus_force()

def regislayout() :
    global regis1,regis2,regis3,regis6,regis7,regis8
    root.title("Welcome to User Registration : ")
    root.config(bg='#FFD1D1')
    regisframe = Frame(root,bg='#FFD1D1')
    regisframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    regisframe.columnconfigure((0,1),weight=1)

    Label(regisframe,image=img,bg='#FFD1D1').grid(row=0,column=1,sticky=NW,padx=5)

    # Label(regisframe,text="Registration Form",font="Garamond 26 bold",fg='black',compound=LEFT,bg='#FFD1D1').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    Label(regisframe,text='Student ID : ',bg='#FFD1D1',fg='black').grid(row=1,column=0,sticky='e',padx=10)
    regis1 = Entry(regisframe,width=20,bg='#d3e0ea')
    regis1.grid(row=1,column=1,sticky='w',padx=5)

    Label(regisframe,text='First name : ',bg='#FFD1D1',fg='black').grid(row=2,column=0,sticky='e',padx=10)
    regis2 = Entry(regisframe,width=20,bg='#d3e0ea')
    regis2.grid(row=2,column=1,sticky='w',padx=5)

    Label(regisframe,text='Last name : ',bg='#FFD1D1',fg='black').grid(row=3,column=0,sticky='e',padx=10)
    regis3 = Entry(regisframe,width=20,bg='#d3e0ea')
    regis3.grid(row=3,column=1,sticky='w',padx=5)

    Label(regisframe,text="Username : ",bg='#FFD1D1',fg='black').grid(row=4,column=0,sticky='e',padx=10)
    regis6 = Entry(regisframe,width=20,bg='#d3e0ea')
    regis6.grid(row=4,column=1,sticky='w',padx=5)

    Label(regisframe,text="Password : ",bg='#FFD1D1',fg='black').grid(row=5,column=0,sticky='e',padx=10)
    regis7 = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    regis7.grid(row=5,column=1,sticky='w',padx=5)

    Label(regisframe,text="Confirm Password : ",bg='#FFD1D1',fg='black').grid(row=6,column=0,sticky='e',padx=10)
    regis8 = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    regis8.grid(row=6,column=1,sticky='w',padx=5)

    regisaction = Button(regisframe,text="Register now",bg='#FF9494',command=registration)
    regisaction.grid(row=11,column=1,ipady=5,ipadx=5,pady=5,sticky='e')
    regis2.focus_force()
    loginbtn = Button(regisframe,text="Cancel",command=loginlayout)
    loginbtn.grid(row=11,column=0,ipady=5,ipadx=5,pady=5,sticky='w',padx=10)
    regisframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def check():
    global regis1,regis2,regis3,regis6,regis7,regis8
    stid = regis1.get()
    fname = regis2.get()
    lname = regis3.get()
    newuser = regis6.get()
    newpwd = regis7.get()
    cfpwd = regis8.get()
    print(regis1,regis2,regis3,regis6,regis7,regis8)
    print(stid,fname ,lname ,newuser,newpwd,cfpwd)
    

def registration() :
    global regis1,regis2,regis3,regis6,regis7,regis8

    stid = regis1.get()
    fname = regis2.get()
    lname = regis3.get()
    newuser = regis6.get()
    newpwd = regis7.get()
    cfpwd = regis8.get()
    
    if stid == "" :
        messagebox.showwarning("Student ID","Please enter Student ID")
        regis1.focus_force()
    elif fname == "" :
        messagebox.showwarning("Admin: ","Please enter firstname")
        regis2.focus_force()
    elif lname == "" :
        messagebox.showwarning("Admin: ","Please enter lastname")
        regis3.focus_force()
    elif newuser == "" :
        messagebox.showwarning("Admin: ","Please enter user")
        regis6.focus_force()
    elif newpwd == "" :
        messagebox.showwarning("Admin: ","Please enter pwd")
        newpwd.focus_force()
    elif cfpwd == "" :
        messagebox.showwarning("Admin: ","Please enter cfpwd")
        regis7.focus_force()
    elif newpwd != cfpwd  :
        messagebox.showwarning("Admin:","Passwords do not match")
        regis8.select_range(0,END)
        regis8.focus_force()
    else : 
        sql = "select * from login where sid=?"
        cursor.execute(sql,[regis1.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showwarning("Student ID","Student ID already Exist")
            regis1.select_range(0,END)
            regis1.focus_force()
        else :
            sql = "select * from login where username=?"
            cursor.execute(sql,[regis6.get()])
            result = cursor.fetchall()

            if result :
                messagebox.showwarning("Username","Username already Exist")
                regis6.select_range(0,END)
                regis6.focus_force()

            else:                
                sql = "insert into login (sid,fname,lname,username,password) values (?,?,?,?,?)"
                cursor.execute(sql,[stid,fname,lname,newuser,newpwd])
                conn.commit()
                messagebox.showinfo("Admin:","Registration Successful")
                conn.rollback()

def retrivedata() :
    sql = "select * from login"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)
    

def Displaymain(root):
    display_screen = Frame(root)
    display_screen.place(width=900,height=400)
    display_screen.rowconfigure((0,1,2,3),weight=1)
    display_screen.columnconfigure((0,1),weight=1)

    global tree
    global SEARCH
    global p_id,pname,brand,price,amount

    SEARCH = StringVar()
    p_id = StringVar()
    pname = StringVar()
    brand = StringVar()
    price = StringVar()
    amount = StringVar()

    TopViewForm = Frame(display_screen, width=600, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    
    LFrom = Frame(display_screen, width="350",bg="#97DEFF")
    LFrom.pack(side=LEFT, fill=Y)
    
    LeftViewForm = Frame(display_screen, width=500,bg="#95BDFF")
    LeftViewForm.pack(side=LEFT, fill=Y)
    
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)

    
    lbl_text = Label(TopViewForm, text="Stock List", font=('verdana', 18), width=600,bg="#62CDFF")
    lbl_text.pack(fill=X)
    
    
    Label(LFrom, text="Product ID  ", font=("Arial", 10),bg="#97DEFF",fg="black").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=p_id).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Product Title ", font=("Arial", 10),bg="#97DEFF",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=pname).pack(side=TOP, padx=10, fill=X)


    Label(LFrom, text="Brand ", font=("Arial", 10),bg="#97DEFF",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=brand).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Product Price ", font=("Arial", 10),bg="#97DEFF",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=price).pack(side=TOP, padx=10, fill=X)

    Label(LFrom,text='Amount ',font=("Arial", 10),bg="#97DEFF",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=amount).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Submit",font=("Arial", 10, "bold"),command=register,bg="#97DEFF",fg="black").pack(side=TOP, padx=10,pady=5, fill=X)

    
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('verdana', 10),bg="#95BDFF")
    lbl_txtsearch.pack()
    
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord,bg="white")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_view = Button(LeftViewForm, text="View All", command=DisplayData,bg="white")
    btn_view.pack(side=BOTTOM, padx=10, pady=10, fill=X)
    
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset,bg="white")
    btn_reset.pack(side=BOTTOM, padx=10, pady=10, fill=X)
    
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete,bg="white")
    btn_delete.pack(side=BOTTOM, padx=10, pady=10, fill=X)
    
    btn_delete = Button(LeftViewForm, text="Update", command=Update,bg="white")
    btn_delete.pack(side=BOTTOM, padx=10, pady=10, fill=X)
    
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Id", "Name", "Brand", "Price","Amount"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    
    tree.heading('Id', text="Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Brand', text="Brand", anchor=W)
    tree.heading('Price', text="Price", anchor=W)
    tree.heading('Amount', text="Amount", anchor=W)
    
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=130)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    
    tree.pack()
    DisplayData()

def Update():
    Database()
    p_id1=p_id.get()
    pname1=pname.get()
    brand1=brand.get()
    price1=price.get()
    amount1=amount.get()
    if p_id1=='' or pname1==''or brand1=='' or price1==''or amount1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!! wow")
    else:
        
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        conn.execute('UPDATE stocklist SET pid=?,pname=?,brand=?,price=?,amount=? WHERE pid=?',(p_id1,pname1,brand1,price1,amount1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully")
        Reset()
        DisplayData()
        conn.close()

def register():
    Database()
    p_id1=p_id.get()
    pname1=pname.get()
    brand1=brand.get()
    price1=price.get()
    amount1=amount.get()
    if p_id1=='' or pname1==''or brand1=='' or price1==''or amount1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        conn.execute('INSERT INTO stocklist (pid,pname,brand,price,amount) \
              VALUES (?,?,?,?,?)',(p_id1,pname1,brand1,price1,amount1));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        DisplayData()
        conn.close()
def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    
    SEARCH.set("")
    p_id.set("")
    pname.set("")
    brand.set("")
    price.set("")
    amount.set("")
def Delete():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM stocklist WHERE pid = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def SearchRecord():
    Database()
    
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor=conn.execute("select * from stocklist WHERE pid LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def DisplayData():
    Database()
    tree.delete(*tree.get_children())
    cursor=conn.execute("select * from stocklist")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()
def OnDoubleClick(self):
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    
    p_id.set(selecteditem[0])
    pname.set(selecteditem[1])
    brand.set(selecteditem[2])
    price.set(selecteditem[3])
    amount.set(selecteditem[4])


Database()
# Displaymain()
root = mainwindow()
img = PhotoImage(file='profile.png').subsample(3,3)
userinfo = StringVar()
pwdinfo = StringVar()
stid = IntVar()
fname = StringVar()
lname = StringVar()
newuser = StringVar()
newpwd = StringVar()
cfpwd = StringVar()
loginlayout()
mainloop()
# cursor.close()
# conn.close()



