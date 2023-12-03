from tkinter import *# type:ignore
import tkinter as tk
from PIL import Image,ImageTk 
from Employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time

class IOS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Invetory Organizer System")
        self.root.config(bg="White")
        # ------title-------
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Organizer System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        
        #--------button------
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="#FBEEAC", cursor="hand2", command=self.logout)
        btn_logout.place(x=1350, y=10, height=50, width=150)
        
        #-------clock------
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Organizer System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #------left menu-----
        self.Menulogo=Image.open("Images/menu_im.png")# type:ignore
        self.Menulogo=self.Menulogo.resize((200,200),Image.ANTIALIAS)# type:ignore
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menulogo=Label(LeftMenu,image=self.Menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)
        
        #------ menu buttons-------
        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="category",command= self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #--------content------
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5 ,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total supplier\n[ 0 ]",bd=5 ,relief=RIDGE,bg="#322653",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_category=Label(self.root,text="Total category\n[ 0 ]",bd=5 ,relief=RIDGE,bg="#8062D6",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="Total product\n[ 0 ]",bd=5 ,relief=RIDGE,bg="#9288F8",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="Total sales\n[ 0 ]",bd=5 ,relief=RIDGE,bg="#FFD2D7",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        

        #------footer-----
        lbl_footer=Label(self.root,text="IOS-Inventory Organizer System || Developed by team\nFor any technical issue contact 95XXXXX8",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_content()
#-----------------------------------------------------------------------------------------------------------------------
         
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)   
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)        
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)       
    
    def update_content(self):
        con=sqlite3.connect(database='IOS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[ {str(len(product))} ]')
            
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total suppliers\n[ {str(len(supplier))} ]')
       
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total category\n[ {str(len(category))} ]')
       
       
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total employee\n[ {str(len(employee))} ]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')
       
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Organizer System\t\t Date:{str(date_)}\t\t Time:{str(time_)}")   
            self.lbl_clock.after(200,self.update_content)
    
          
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)        


    def logout(self):
        self.root.destroy()
        os.system("python login.py")


if __name__ =="__main__":
    root=Tk()
    obj=IOS(root) 
    root.mainloop()       