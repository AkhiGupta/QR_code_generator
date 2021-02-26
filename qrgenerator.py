from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("950x600+200+50")
        self.root.title("QR generator")
        self.root.resizable(True,True)

        title=Label(self.root,text="   HEART Disease Prediction",font=("times new roman",43),bg='pink',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        #=================Employee details========#

        #=========variables====#
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()
        
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=110,width=500,height=450)
        
        emp_title=Label(emp_Frame,text="Patient Details",font=("times new roman",22),bg='red',fg='white').place(x=0,y=0,relwidth=1)
        
        lbl_emp_code=Label(emp_Frame,text="Employee ID",font=("times new roman",19,'bold'),bg='white',fg='black').place(x=30,y=50)
        lbl_name=Label(emp_Frame,text="Name",font=("times new roman",19,'bold'),bg='white',fg='black').place(x=30,y=100)
        lbl_department=Label(emp_Frame,text="department",font=("times new roman",19,'bold'),bg='white',fg='black').place(x=30,y=150)
        lbl_designation=Label(emp_Frame,text="Disignation",font=("times new roman",19,'bold'),bg='white',fg='black').place(x=30,y=200)

        txt_emp_code=Entry(emp_Frame,font=("times new roman",19,),textvariable=self.var_emp_code,bg='light yellow',fg='black').place(x=200,y=50)
        txt_name=Entry(emp_Frame,font=("times new roman",19,),textvariable=self.var_name,bg='light yellow',fg='black').place(x=200,y=100)
        txt_department=Entry(emp_Frame,font=("times new roman",19,),textvariable=self.var_department,bg='light yellow',fg='black').place(x=200,y=150)
        txt_designation =Entry(emp_Frame,font=("times new roman",19,),textvariable=self.var_designation,bg='light yellow',fg='black').place(x=200,y=200)

        btn_generate=Button(emp_Frame,text='QR Generate',command=self.generate,font=("times new roman",19,'bold'),bg='#2196f3',fg='white' ).place(x=90,y=260,width=200,height=40)
        btn_clear=Button(emp_Frame,text='clear',command=self.clear,font=("times new roman",19,'bold'),bg='#607d8b',fg='white' ).place(x=320,y=260,width=130,height=40)
 
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",19,'bold'),bg='white',fg='orange')
        self.lbl_msg.place(x=0,y=330,relwidth=1)

        #=================Employee QR code========#
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=590,y=110,width=300,height=450)
        
        emp_title=Label(qr_Frame,text="Patient QR code",font=("times new roman",22),bg='red',fg='white').place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text="NO Qr code\n Available",font=('times new roman',15),bg='#3f51b6',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=220,height=200)
        
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
         
        
    def generate(self):
         if self.var_emp_code.get()=='' or self.var_name.get()=='' or self.var_department.get()=='' or self.var_designation.get()=='':
              self.msg='All fields are required!'
              self.lbl_msg.config(text=self.msg,fg='red')
         else:
              qr_data=(f"Employee ID: {self.var_emp_code.get()}\n Employee Name: {self.var_name.get()}\n Department:{self.var_department.get()}\n Designation:{self.var_designation.get()}")
              qr_code=qrcode.make(qr_data)
              # print(qr_code)
              qr_code=resizeimage.resize_cover(qr_code,[200,180])
              qr_code.save("QR/EMP_"+str(self.var_emp_code.get())+'.png')
              # print(qr_code)
              
              self.im=ImageTk.PhotoImage(file="QR/EMP_"+str(self.var_emp_code.get())+'.png')
              self.qr_code.config(image=self.im)

                      
              self.msg='QR code Generated Successfully'
              self.lbl_msg.config(text=self.msg,fg='orange')
                                                                                            
root = Tk()
obj=Qr_generator(root)
root.mainloop()
