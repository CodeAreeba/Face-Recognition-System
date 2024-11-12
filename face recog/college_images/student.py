from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("SUPERIOR ATTENDENCE SYSTEM")

        title_lbl=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",17,"bold"), fg="white",bg="#000066")
        title_lbl.place(x=-100,y=0,width=1530,height=45)

        title_lbl=Label(self.root,text="STUDENT ATTENDENCE",font=("times new roman",17,"bold"), fg="white",bg="#000066")
        title_lbl.place(x=-100,y=45,width=1530,height=45)

        main_frame=Frame(bd=2,bg="#000066")
        main_frame.place(x=0,y=100,width=1500,height=650)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=640,height=580)

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="#000066",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"),fg="white")
        current_course_frame.place(x=5,y=10,width=625,height=230)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","SE","AI")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","Computer","Robotics","ML","AI")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester","Sems-1","Sems-2","Sems-3","Sems-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="#000066",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"),fg="white")
        class_student_frame.place(x=5,y=130,width=625,height=500)

        #StudentID
        studentID_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #StudentName
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #ClassDivision
        class_division_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_division_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        class_division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #RollNo
        RollNo_label=Label(class_student_frame,text="Roll No :",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        RollNo_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        RollNo_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        RollNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Student Email:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        email_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        email_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #PhoneNUmber
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Adress
        adress_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        adress_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        adress_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        adress_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #TeacherName
        teacherName_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        teacherName_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        teacherName_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        teacherName_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #DOB
        DOB_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        DOB_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,font=("times new roman",12,"bold"),width=18)
        DOB_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        #Radio Buttons

        # Create style for ttk.Radiobutton
        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="#000066", foreground="white", font=("times new roman", 12, "bold"))

        # Applying the custom style to the ttk.Radiobuttons
        radiobtn1 = ttk.Radiobutton(class_student_frame, text="Photo Sample", value="Yes", style="Custom.TRadiobutton")
        radiobtn1.grid(row=6, column=0, pady=5, padx=10)

        radiobtn2 = ttk.Radiobutton(class_student_frame, text="No Photo Sample", value="No", style="Custom.TRadiobutton")
        radiobtn2.grid(row=6, column=1, pady=5, padx=10)

        #buttons Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=220,width=620,height=50)

        save_button=Button(btn_frame,text="Save",width=15,font=("times new roman", 12, "bold"),bg="#000066",fg="white")
        save_button.grid(row=0,column=0,padx=5,pady=5)

        update_button=Button(btn_frame,text="Update",width=15,font=("times new roman", 12, "bold"),bg="#000066",fg="white")
        update_button.grid(row=0,column=1,padx=5,pady=5)

        reset_button=Button(btn_frame,text="Reset",width=15,font=("times new roman", 12, "bold"),bg="#000066",fg="white")
        reset_button.grid(row=0,column=3,padx=5,pady=5)

        save_button=Button(btn_frame,text="Save",width=15,font=("times new roman", 12, "bold"),bg="#000066",fg="white")
        save_button.grid(row=0,column=4,padx=5,pady=5)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=270,width=620,height=50)

        take_photo_button=Button(btn_frame1,text="Take Photo Sample",width=32,font=("times new roman", 12, "bold"),bg="#000066",fg="white")
        take_photo_button.grid(row=0,column=0,padx=5,pady=5)

        upadte_photo_button=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman", 12, "bold"),bg="#000066",fg="white")
        upadte_photo_button.grid(row=0,column=1,padx=5,pady=5)

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=660,y=10,width=580,height=580)

        #Search System
        search_frame=LabelFrame(right_frame,bd=2,bg="#000066",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),fg="white")
        search_frame.place(x=5,y=10,width=565,height=73)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),fg="white",bg="#000066")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="read only",width=10)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,font=("times new roman",12,"bold"),width=14)
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_frame2=LabelFrame(search_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"),fg="white")
        search_frame2.place(x=350,y=3,width=200,height=45)

        search_button=Button(search_frame2,text="Search",width=9,font=("times new roman", 12, "bold"),bg="#000066",fg="white")
        search_button.grid(row=0,column=0,padx=4,pady=5)

        showall_button=Button(search_frame2,text="Show All",width=9,font=("times new roman", 12, "bold"),bg="#000066",fg="white")
        showall_button.grid(row=0,column=1,padx=2,pady=5)

        #Table Frame
        table_frame=Frame(right_frame,bd=2,bg="#000066",relief=RIDGE)
        table_frame.place(x=5,y=85,width=565,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sems","id","name","div","roll","gender",'email',"phone","address","teacher","dob","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)



 





if __name__== "__main__":
    root=Tk() #calling root with tool kit
    obj=Student(root)
    root.mainloop()
