
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
        dep_combo["values"]=("Select Depertment","Computer","AIDS","IT","Electronics","Civil","Mechanical")
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
        semester_combo["values"]=("Select semester","semester-1","semester-2","semester-3","semester-4","semester-5","semester-6","Semester-7","Semester-8")
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


        #Redio Buttions
        self.var_radio1=StringVar()
        rediobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a photo sample",value="yes")
        rediobtn1.grid(row=6,column=0)


        self.var_radio2=StringVar()
        rediobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="no")
        rediobtn2.grid(row=6,column=1)


        #button frame 
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=270,width=625,height=95)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        save_btn.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=15,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        update_btn.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=15,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        delete_btn.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=15,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        reset_btn.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=15,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        take_photo_btn.grid(row=1,column=0,padx=5,pady=5,sticky=W)

       


        

        #Right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details ",font=("times new roman",20,"bold"),foreground="red")
        Right_frame.place(x=670,y=10,width=660,height=600)
 
        #============================= Searching data ============================ 

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search data ",font=("times new roman",18,"bold"),foreground="black")
        Search_frame.place(x=5,y=10,width=635,height=150)


        search_label=Label(Search_frame,text="Search By",font=("times new roman",14,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_search_by,font=("times new roman",10,"bold"),state="readonly")
        search_combo["values"]=("Select ","Student_id","Name","Roll","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=18,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)


        search_btn=Button(Search_frame,command=self.search_data,text="Search",width=16,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        search_btn.grid(row=1,column=1)

        showAll_btn=Button(Search_frame,text="Show All",width=16,font=("times new roman",12,"bold"),bg="blue",foreground="white")
        showAll_btn.grid(row=1,column=2)

        back=Button(Search_frame,command=self.Back,text="Back",width=12,font=("times new roman",13,"bold"),bg="red",foreground="white")
        back.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #============================ table Frame============================       

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=170,width=636,height=375)

        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photos"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("roll",text="ROll NO")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photos",text="Photo Sample Status")


        self.student_table["show"]="headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photos",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #===================== Fuction declerion===================
    def search_data(self):
        if self.var_search_by.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",user="root",password="IrannaDK@0504",database="student_database")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student_details WHERE " + str(self.var_search_by.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('', END, values=row)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showinfo("Error",f"Due to :{str(es)},",parent=self.root)
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="IrannaDK@0504",database="student_database")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(), 
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),                                                                                                                                                                                 
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),  
                                                                                                                self.var_address.get(),                                                                                           
                                                                                                                self.var_teacher.get(),  
                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                                                                                            
                 
                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showinfo("Error",f"Due to :{str(es)},",parent=self.root)

    #==============================featch data======================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="IrannaDK@0504",database="student_database")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_details")
        data=my_cursor.fetchall()


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #========================get cursor================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #======================Update function ===================
    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Upate","Do you want to upate this students details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="IrannaDK@0504",database="student_database")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_details set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(), 
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                   self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),                                                                                                                                                                                 
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),  
                                                                                                                                                                                    self.var_address.get(),                                                                                           
                                                                                                                                                                                    self.var_teacher.get(),  
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                )) 
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student Details data Update Complated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #===============delete functon============
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required ",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="IrannaDK@0504",database="student_database")
                    my_cursor=conn.cursor()
                    sql="delete from student_details where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Delete","Successfully Delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #======reset================================
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select year"),
        self.var_semester.set("Select semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    


    #============== Generate data set of take photo sample-===============================
    def generate_dataset(self):
        messagebox.showinfo("Note","Make some from Comera and should be in front of camera  one student")
        messagebox.showinfo("2 Note","Dont move when taking a samples and hand or other object should not come in front of the camera  ")        
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="IrannaDK@0504",database="student_database")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student_details")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student_details set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(), 
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                   self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),                                                                                                                                                                                 
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),  
                                                                                                                                                                                    self.var_address.get(),                                                                                           
                                                                                                                                                                                    self.var_teacher.get(),  
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()   




                 #==================Load predfinend data on face ======================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling Factor=1.3
                    #minimum neighbor=5


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Photo/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Reslt","Generating data sets completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            


                

        


    def Back(self):
	    self.root.destroy()




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()