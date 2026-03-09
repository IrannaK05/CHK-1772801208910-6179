
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
from tkcalendar import DateEntry
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x767+0+0")
        self.root.title("Student Attendence System")

        #===================varibles=====================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_search=StringVar()
        self.var_search_by=StringVar()




         # bg img
        img3=Image.open(r"D:\Facial Recognition smart attendence system\Images\img3.jpg")       
        img3=img3.resize((1360,693),Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1366,height=768)
        
        text=" Student Information And Details"
        title_lbl=Label(bg_img,text=text,font=("times new roman",35,"bold"),background="red",foreground="white")
        title_lbl.place(x=0,y=0,width=1360,height=55)
        def scroll_text():
            nonlocal_text=title_lbl.cget("text")
            new_text=nonlocal_text[1:]+nonlocal_text[0]
            title_lbl.config(text=new_text)
            self.root.after(200,scroll_text)
            
        scroll_text()
                    
        

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=70,width=1340,height=620)



        #left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details ",font=("times new roman",20,"bold"),foreground="red")
        Left_frame.place(x=10,y=10,width=650,height=600)

 
        #Current course Information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information ",font=("times new roman",18,"bold"),foreground="black")
        current_course_frame.place(x=5,y=10,width=615,height=150)

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Depertment","Computer","AIDS","","Electronics","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)



        # course 
        course_label=Label(current_course_frame,text="course",font=("times new roman",14,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select course","FY","SY","TY","BTech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)


        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",14,"bold"),bg="white")
        year_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2024-2025","2025-2026","2026-2027","2027-2028")
        year_combo.current(0)
        year_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)


        #semester 
        semester_label=Label(current_course_frame,text="semester",font=("times new roman",14,"bold"),bg="white")
        semester_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select semester","semester-1","semester-2","semester-3","semester-4","semester-5","semester-6")
        semester_combo.current(0)
        semester_combo.grid(row=2,column=3,padx=5,pady=10,sticky=W)



         #Student Class Information 
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student class information ",font=("times new roman",18,"bold"),foreground="black")
        class_student_frame.place(x=5,y=160,width=636,height=400)


        #Student id 
        studentID_label=Label(class_student_frame,text="Student ID",font=("times new roman",14,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)


        #Student name 
        studentName_label=Label(class_student_frame,text="Student Name",font=("times new roman",14,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)


        #Class division  
        class_div_label=studentName_label=Label(class_student_frame,text="Batch  ",font=("times new roman",14,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("Batch 1","Batch 2")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)


        #Roll No   
        roll_no_label=studentName_label=Label(class_student_frame,text="Roll no",font=("times new roman",14,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=5,pady=10,sticky=W)

        roll_no_label=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_label.grid(row=1,column=3,padx=5,pady=10,sticky=W)



        #Gender 
        gender_label=studentName_label=Label(class_student_frame,text="Gender",font=("times new roman",14,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)


        #Date of Birth 
        dob_label=studentName_label=Label(class_student_frame,text="DOB",font=("times new roman",14,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        dob_entry = DateEntry(class_student_frame, textvariable=self.var_dob, width=18, font=("times new roman", 12, "bold"), date_pattern='dd/mm/yyyy')
        dob_entry.grid(row=2, column=3, padx=5, pady=10, sticky='w')

        #Email 
        email_label=studentName_label=Label(class_student_frame,text="Email",font=("times new roman",14,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=10,sticky=W)

        email_label=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=1,padx=5,pady=10,sticky=W)


        #phone no 
        phone_label=studentName_label=Label(class_student_frame,text="Phone No",font=("times new roman",14,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=5,pady=10,sticky=W)

        phone_label=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_label.grid(row=3,column=3,padx=5,pady=10,sticky=W)


        #Address 
        address_label=studentName_label=Label(class_student_frame,text="Address",font=("times new roman",14,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=5,pady=10,sticky=W)

        address_label=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=1,padx=5,pady=10,sticky=W)


        #Teacher Name
        address_label=studentName_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",14,"bold"),bg="white")
        address_label.grid(row=4,column=2,padx=5,pady=10,sticky=W)

        address_label=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=3,padx=5,pady=10,sticky=W)


      



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()