
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    
    def __init__(self, root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Pannel")
        
        
        #====================Varaibles 
        self.var_attend_id=StringVar()
        self.var_attend_Roll=StringVar()
        self.var_attend_Name=StringVar()
        self.var_attend_Time=StringVar()
        self.var_attend_Date=StringVar()
        self.var_attend_Status=StringVar()
        
        
        
        
        img3=Image.open(r"D:\Facial Recognition smart attendence system\Images\main.jpg")       
        img3=img3.resize((1360,693),Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT",font=("times new roman",35,"bold"),background="white",foreground="red")
        title_lbl.place(x=0,y=0,width=1360,height=55)
        
        #Main Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=70,width=1340,height=620)
        
        #Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance",font=("times new roman",20,"bold"),foreground="red")
        Left_frame.place(x=10,y=10,width=650,height=600)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=10,width=635,height=550)
        
        #stuend ID Entry
        studentID_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",14,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        studentID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #roll number
        rollLable=Label(left_inside_frame,text="Roll NO:",font=("times new roman",14,"bold"),bg="white")
        rollLable.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        atten_roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_Roll,width=20,font=("times new roman",12,"bold"))
        atten_roll_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #name 
        nameLable=Label(left_inside_frame,text="Name:",font=("times new roman",14,"bold"),bg="white")
        nameLable.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_attend_Name,width=20,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        
        #time
        timeLable=Label(left_inside_frame,text="Time:",font=("times new roman",14,"bold"),bg="white")
        timeLable.grid(row=1,column=2,padx=5,pady=10,sticky=W)

        attenTime=ttk.Entry(left_inside_frame,textvariable=self.var_attend_Time,width=20,font=("times new roman",12,"bold"))
        attenTime.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        
        
        #Date
        dateLable=Label(left_inside_frame,text="Date:",font=("times new roman",14,"bold"),bg="white")
        dateLable.grid(row=3,column=0,padx=5,pady=10,sticky=W)

        attenDate=ttk.Entry(left_inside_frame,textvariable=self.var_attend_Date,width=20,font=("times new roman",12,"bold"))
        attenDate.grid(row=3,column=1,padx=5,pady=10,sticky=W)
        
        #States
        attenStatusLable=Label(left_inside_frame,text="Status:",font=("times new roman",14,"bold"),bg="white")
        attenStatusLable.grid(row=3,column=2,padx=5,pady=10,sticky=W)

        self.attenStatus=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_Status,font=("times new roman",12,"bold"),state="readonly",width=18)
        self.attenStatus["values"]=("Status","Present","Absent")
        self.attenStatus.current(0)
        self.attenStatus.grid(row=3,column=3,padx=5,pady=10,sticky=W)
        
        #button
        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=490,width=620,height=55)

        save_btn=Button(btn_frame,command=self.import_csv,text="Imoprt CSV",width=15,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        save_btn.grid(row=0,column=0,padx=3,pady=5,sticky=W)

        update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=15,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        update_btn.grid(row=0,column=1,padx=3,pady=5,sticky=W)

        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        delete_btn.grid(row=0,column=2,padx=3,pady=5,sticky=W)

        reset_btn=Button(btn_frame,text="Reset",width=15,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        reset_btn.grid(row=0,column=3,padx=3,pady=5,sticky=W)



        
        
        
        
        #left farame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details ",font=("times new roman",20,"bold"),foreground="red")
        Right_frame.place(x=670,y=10,width=660,height=600)
        
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=10,width=636,height=550)
        
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("ID","Roll","Name","Time","Date","Attendance Status",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        
        self.AttendenceReportTable.heading("ID",text="Attendance ID")
        self.AttendenceReportTable.heading("Roll",text="Roll")
        self.AttendenceReportTable.heading("Name",text="Name")
        self.AttendenceReportTable.heading("Time",text="Time")
        self.AttendenceReportTable.heading("Date",text="Date")
        self.AttendenceReportTable.heading("Attendance Status",text="Attendance Status")
        
        self.AttendenceReportTable["show"]="headings"
        
        self.AttendenceReportTable.column("ID",width=100)
        self.AttendenceReportTable.column("Roll",width=100)
        self.AttendenceReportTable.column("Name",width=100)
        self.AttendenceReportTable.column("Time",width=100)
        self.AttendenceReportTable.column("Date",width=100)
        self.AttendenceReportTable.heading("Attendance Status", text="Attendance Status")

        
        
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
    #===================================fatch====================
    def fatchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i) 
            
     #import  Csv       
    import logging
    logging.getLogger('PyQt5.QtCore').setLevel(logging.ERROR)
    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fatchData(mydata)

            
    #=Export  Csv
    
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        conetent=self.AttendenceReportTable.item(cursor_row)
        rows=conetent['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_Roll.set(rows[1])
        self.var_attend_Name.set(rows[2])        
        self.var_attend_Time.set(rows[3])
        self.var_attend_Date.set(rows[4])
        self.var_attend_Status.set(rows[5])
        
        
        

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()