# Importing all the required modules to create the UI
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import os
import numpy as np
import cv2
import csv
import pandas as pd

FONT1 = ("Calibri", 45)
FONT2 = ("Calibri", 16)
FONT3 = ("Calibri", 14)

class IREG(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # We are giving the window a title. This remains the same for all frames which will be shown
        tk.Tk.wm_title(self, "IREG: Image Registration")
        tk.Tk.wm_frame(self)
        tk.Tk.wm_geometry(self, "1280x800+0+0")
        self.state("zoomed")
        tk.Tk.wm_resizable(self, width=False, height=False)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Creating a dictionary of frames where all the frames will be stored
        self.frames = {}

        # Adding the frames to the dictionary
        for F in (IREG_Main_Menu_Page, Account_Management_Menu_Page, Student_Account_Management_Page, Teacher_Account_Management_Page, Start_Attendance_Page, View_Attendance_Page, Settings_Page):
            frame = F(container, self)
            frame.configure(bg="Black")
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        # This calls the show page function where the IREG_Main_Menu_Page is a parameter
        self.show_frame(IREG_Main_Menu_Page)
    # This function takes the container parameter which is essentially the index of the dictionary location of the frame to be shown
    def show_frame(self, cont):
        # Assigns the created frame at the dictionary location container
        frame = self.frames[cont]
        # This raises the frame to the top of the screen. This essentially means that this frame is displayed on top of the previous frame
        frame.tkraise()
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class IREG_Main_Menu_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        IREG_Main_Menu_Label = tk.Label(self, text="IREG: Main Menu", font=FONT1) # Creating label with text and setting the font
        IREG_Main_Menu_Label.place(x=205, y=5, width=870, height=75) # Specifiying the coordnates of the label
        IREG_Main_Menu_Label.config(bg="Black", fg="White") # Confuguring the colour of the label

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 20))
        #======================================== Adding in the buttons ========================================#
        # Adding the Start Attendance Button
        start_Attendance_Button = ttk.Button(self, text="Start Attendance", command=lambda: controller.show_frame(Start_Attendance_Page), style="big.TButton")
        start_Attendance_Button.place(x=440, y=240, width=400, height=50)

        # Adding the View Attendance Button
        view_Attendance_Button = ttk.Button(self, text="View Attendance", command=lambda: controller.show_frame(View_Attendance_Page), style="big.TButton")
        view_Attendance_Button.place(x=440, y=300, width=400, height=50)

        # Adding the Account Management Button
        account_Management_Button = ttk.Button(self, text="Account Management", command=lambda: controller.show_frame(Account_Management_Menu_Page), style="big.TButton")
        account_Management_Button.place(x=440, y=360, width=400, height=50)

        # Adding the Settings Button
        settings_Button = ttk.Button(self, text="Settings", command=lambda: controller.show_frame(Settings_Page), style="big.TButton")
        settings_Button.place(x=440, y=420, width=400, height=50)

        # Adding the Exit Button
        exit_Button = ttk.Button(self, text="Exit", command=lambda: IREG.quit(self), style="big.TButton")
        exit_Button.place(x=440, y=480, width=400, height=50)
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Account_Management_Menu_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Account_Managenent_Label = tk.Label(self, text="Account Management", font=FONT1)
        Account_Managenent_Label.place(x=205, y=5, width=870, height=75)
        Account_Managenent_Label.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 20))
        #======================================== Adding in the buttons ========================================#
        # Adding the Student Account Management Button
        student_account_management_Button =  ttk.Button(self, text="Student Account Management", command=lambda: controller.show_frame(Student_Account_Management_Page), style="big.TButton")
        student_account_management_Button.place(x=440, y=300, width=400, height=50)

        # Adding the Teacher Account Management Button
        teacher_account_management_Button = ttk.Button(self, text="Teacher Account Management", command=lambda: controller.show_frame(Teacher_Account_Management_Page), style="big.TButton")
        teacher_account_management_Button.place(x=440, y=360, width=400, height=50)

        # Adding the Back Button
        back_to_main_menu = ttk.Button(self, text="Back To Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page), style="big.TButton")
        back_to_main_menu.place(x=440, y=420, width=400, height=50)
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Student_Account_Management_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Student_Account_management_Lbl = tk.Label(self, text="Student Account Management", font=FONT1)
        Student_Account_management_Lbl.place(x=205, y=5, width=870, height=75)
        Student_Account_management_Lbl.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 12), bg="Black", fg="White")

        # Variables related to the students
        self.var_student_ID = IntVar()
        self.var_student_email = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_date_of_admission = StringVar()
        self.var_date_of_birth = StringVar()
        
        # Variables related to the father
        self.var_father_name = StringVar()
        self.var_father_email = StringVar()

        # Variables related to the mother
        self.var_mother_name = StringVar()
        self.var_mother_email = StringVar()

        # Search Variables
        self.var_search_by_combobox = StringVar()
        self.var_search = StringVar()
    ############################################################################################################################################
    #==========================================================================================================================================#
    #                                                                UI DESIGN
    # =========================================================================================================================================#
    # Adding in the student related text boxes and labels
        # Creating a new Student ID
        # - Estabilishing the connectin between this project and the database
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
        my_cursor = conn.cursor()
        # - Getting all the student IDs from the IREG Database and storing them in the form of an array named student_IDs. 
        my_cursor.execute("SELECT Student_ID FROM tbl_student")
        student_IDs = my_cursor.fetchall()

        # This checks if the number of student profiles stored in the tbl_student table of the database is 0 or not. If it is 0, the 
        # system automatically assigns the student ID as 0.
        if len(student_IDs)==0:
            self.var_student_ID = str(1)
        else:
            last_student_ID = student_IDs[len(student_IDs)-1][0]
            self.var_student_ID = last_student_ID + 1
        conn.close()

        # Adding a student id label and textbox
        studentID_lbl = Label(self, text="*Student ID: ", font=FONT3)
        studentID_lbl.grid(row=0, column=0, padx=5, pady=(105,18), sticky=E)
        studentID_lbl.config(bg="Black", fg="White")

        self.new_studentID_lbl = Label(self, text=self.var_student_ID, font=FONT3)
        self.new_studentID_lbl.grid(row=0, column=1, padx=5, pady=(105,18), sticky=W)
        self.new_studentID_lbl.config(bg="Black", fg="White")

        # Adding a Student Email label and textbox
        student_email_lbl = Label(self, text="*Student Email: ", font=FONT3)
        student_email_lbl.grid(row=0, column=2, padx=5, pady=(105, 18), sticky=E)
        student_email_lbl.config(bg="Black", fg="White")

        student_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_student_email, font=FONT3)
        student_email_textbox.grid(row=0, column=3, padx=5, pady=(105,18), sticky=W)

        # Adding a first name label and textbox
        first_name_lbl = Label(self, text="*First Name: ", font=FONT3)
        first_name_lbl.grid(row=2, column=0, padx=5, pady=18, sticky=E)
        first_name_lbl.config(bg="Black", fg="White")

        first_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_first_name, font=FONT3)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=18, sticky=W)

        # Adding a last label and textbox
        last_name_lbl = Label(self, text="*Last Name: ", font=FONT3)
        last_name_lbl.grid(row=2, column=2, padx=5, pady=18, sticky=E)
        last_name_lbl.config(bg="Black", fg="White")

        last_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_last_name, font=FONT3)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=18, sticky=W)

        # Adding a Student Date Of Admission label and textbox
        date_of_admission_lbl = Label(self, text="*Date Of Admission: ", font=FONT3)
        date_of_admission_lbl.grid(row=3, column=0, padx=5, pady=18, sticky=E)
        date_of_admission_lbl.config(bg="Black", fg="White")


        format_of_date1_lbl = Label(self, text="(yyyy/mm/dd)")
        format_of_date1_lbl.place(x=175, y=260)
        format_of_date1_lbl.config(bg="Black", fg="White")

        date_of_admission_textbox = ttk.Entry(self,width=25, textvariable=self.var_date_of_admission, font=FONT3)
        date_of_admission_textbox.grid(row=3, column=1, padx=5, pady=18, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_lbl = Label(self, text="*Date of Birth: ", font=FONT3)
        date_of_birth_lbl.grid(row=3, column=2, padx=5, pady=18, sticky=E)
        date_of_birth_lbl.config(bg="Black", fg="White")

        format_of_date2_lbl = Label(self, text="(yyyy/mm/dd)")
        format_of_date2_lbl.place(x=590, y=260)
        format_of_date2_lbl.config(bg="Black", fg="White")

        date_of_birth_textbox = ttk.Entry(self,width=25, textvariable=self.var_date_of_birth, font=FONT3)
        date_of_birth_textbox.grid(row=3, column=3, padx=5, pady=18, sticky=W)

        # Father's Information
        # Adding a father first name label and textbox
        father_name_lbl = Label(self, text="*Father's Name: ", font=FONT3)
        father_name_lbl.grid(row=4, column=0, padx=4, pady=18, sticky=E)
        father_name_lbl.config(bg="Black", fg="White")

        father_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_father_name, font=FONT3)
        father_name_textbox.grid(row=4, column=1, padx=5, pady=18, sticky=W)

        # Adding father's email label and text box
        father_email_lbl = Label(self, text="*Father's Email: ", font=FONT3)
        father_email_lbl.grid(row=4, column=2, padx=4, pady=18, sticky=E)
        father_email_lbl.config(bg="Black", fg="White")

        father_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_father_email, font=FONT3)
        father_email_textbox.grid(row=4, column=3, padx=5, pady=18, sticky=W)

        # Mother's Information
        # Adding a father first name label and textbox
        mother_name_lbl = Label(self, text="*Mother's Name: ", font=FONT3)
        mother_name_lbl.grid(row=5, column=0, padx=4, pady=18, sticky=E)
        mother_name_lbl.config(bg="Black", fg="White")

        mother_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_mother_name, font=FONT3)
        mother_name_textbox.grid(row=5, column=1, padx=5, pady=18, sticky=W)

        # Adding father's email label and text box
        mother_email_lbl = Label(self, text="*Mother's Email: ", font=FONT3)
        mother_email_lbl.grid(row=5, column=2, padx=4, pady=18, sticky=E)
        mother_email_lbl.config(bg="Black", fg="White")

        mother_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_mother_email, font=FONT3)
        mother_email_textbox.grid(row=5, column=3, padx=5, pady=18, sticky=W)
        # UI Design for getting the student's and their parents information completed
        # --------------------------------------------------------------------------- #
        # Adding the buttons and textboxes for creating a search system
        # Adding a search bar
        search_lbl = tk.Label(self, text="Search By:", font=FONT3)
        search_lbl.place(x=60, y=437, height=30)
        search_lbl.config(bg="Black", fg="White")

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(self, textvariable=self.var_search_by_combobox, font=FONT3, width=16, state="readonly")
        search_combobox["values"] = ("Select", "Student_ID", "First_Name", "Last_Name","Date_of_Birth", "Date_Of_Admission")
        search_combobox.current(0)
        search_combobox.place(x=165, y=437, height=30)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(self, textvariable=self.var_search, width=22, font=FONT3)
        search_entry_textbox.place(x=363, y=437, height=30)
        # Adding a Search button
        search_button = ttk.Button(self, text="Search",cursor="hand2")
        search_button.place(x=610, y=420, width=130, height=60)
        
        # Adding a Show All button
        show_all_button = ttk.Button(self, text="Show All", cursor="hand2")
        show_all_button.place(x=760, y=420, width=130, height=60)
        #============================================================================================================================================================================================================
        # Creating a Table Frame which will contain the table showing all the student profiles
        Table_Frame= ttk.Frame(self, relief=RIDGE)
        Table_Frame.place(x=5, y=500, width=1270, height=270)

        # Creating a scroll bar for both the x axxis and the y axis
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        # Creating a table structure with the heading variables being passed in the column brackets
        self.student_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "date_of_birth", "email", "date_of_admission", "father_name","father_email", "mother_name","mother_email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        # Placing the scroll bar on the x axis and the y axis
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Confuguring the scroll bars so that they work whenever the user uses the scroll bars
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Assigning the table headings to the heading variables created in the previous lines
        self.student_table.heading("std_ID", text="Student ID")
        self.student_table.heading("first_name", text="First Name")
        self.student_table.heading("last_name", text="Last Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("date_of_admission", text="Date Of Admission")
        self.student_table.heading("date_of_birth", text="Date Of Birth")
        self.student_table.heading("father_name", text="Father's Name")
        self.student_table.heading("father_email", text="Father Email")
        self.student_table.heading("mother_name", text="Mother's Name")
        self.student_table.heading("mother_email", text="Mother Email")
        self.student_table["show"] = "headings"

        # Setting the width of the columns
        self.student_table.column("std_ID", width=68)
        self.student_table.column("first_name", width=130)
        self.student_table.column("last_name", width=130)
        self.student_table.column("email", width=130)
        self.student_table.column("date_of_admission", width=120)
        self.student_table.column("date_of_birth", width=120)
        self.student_table.column("father_name", width=130)
        self.student_table.column("father_email", width=150)
        self.student_table.column("mother_name", width=130)
        self.student_table.column("mother_email", width=100)

        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        # UI Design for the search system completed
        # --------------------------------------------------------------------------- #
        # Buttons which will aid in adding, updating and deleting the student
        # Add Student Profile button
        add_student_profile_button = ttk.Button(self, text="Add New Student Profile", command=self.add_student_button, style="big.TButton")
        add_student_profile_button.place(x=910, y=95, width=350, height=60)

        # Update Student Profile
        update_student_profile_button = ttk.Button(self, text="Update Student Profile", command=self.update_student_button, style="big.TButton")
        update_student_profile_button.place(x=910, y=160, width=350, height=60)

        # Delete Student Profile
        delete_student_profile_button = ttk.Button(self, text="Delete Student Profile", command=self.delete_student_button, style="big.TButton")
        delete_student_profile_button.place(x=910, y=225, width=350, height=60)

        # Adding a capture face button below the label
        capture_face_button = ttk.Button(self, text="Capture Student Face", command=self.capture_face_button, style="big.TButton")
        capture_face_button.place(x=910, y=290, width=350, height=60)

        # Clear All Data button
        clear_all_button = ttk.Button(self, text="Clear All Fields", command=self.clear_all_button, style="big.TButton")
        clear_all_button.place(x=910, y=355, width=350, height=60)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Account Management", command=lambda: controller.show_frame(IREG_Main_Menu_Page), style="big.TButton")
        back_button.place(x=910, y=420, width=350, height=60)
    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for adding in the data when the user clicks on the add student button
    def add_student_button(self):
        if self.var_student_ID=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO tbl_student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                         self.var_student_ID,
                                                                                                         self.var_first_name.get(),
                                                                                                         self.var_last_name.get(),
                                                                                                         self.var_date_of_birth.get(),
                                                                                                         self.var_student_email.get(),
                                                                                                         self.var_date_of_admission.get(),
                                                                                                         self.var_father_name.get(),
                                                                                                         self.var_father_email.get(),
                                                                                                         self.var_mother_name.get(),
                                                                                                         self.var_mother_email.get()
                                                                                                        ))
                conn.commit()
                conn.close()  

                # Adding Student to the class table
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                my_cursor = conn.cursor()
                my_cursor.execute("""INSERT INTO tbl_student_class VALUES (%s, 001, 2021), 
                                                                          (%s, 002, 2021), 
                                                                          (%s, 003, 2021), 
                                                                          (%s, 004, 2021),
                                                                          (%s, 005, 2021)""",
                                                                          (int(self.var_student_ID), 
                                                                          int(self.var_student_ID), 
                                                                          int(self.var_student_ID), 
                                                                          int(self.var_student_ID), 
                                                                          int(self.var_student_ID)))

                conn.commit()
                conn.close()
                self.var_student_ID = f"{int(self.var_student_ID) + 1}"
                self.new_studentID_lbl.config(text=self.var_student_ID)
                self.fetch_data()
                messagebox.showinfo("Success", "Student details have been added succesfully", parent=self)

            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Update button implementation
    def update_student_button(self):
    # Validating if the user has entered in all the details asked for on the Update Student Profile page
        if self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self)
            # Send an error message to the user if details are not completely filled
        else:
            # Adding a try except block inorder to prevent the system from stop functioning completely incase of an error
            try:
                # Asks the user if they want to update the selected profile
                update = messagebox.askyesno("Update Student Account", "Do you want to update student details?", parent=self)
                if update > 0:
                # If the user click yes, the change will be made in the database
                    conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                    my_cursor = conn.cursor()
                    # Update student information SQL Query
                    my_cursor.execute("UPDATE tbl_student SET First_Name=%s, Last_Name=%s, Email=%s, date_of_admission=%s, Date_Of_Birth=%s, Father_Name=%s, Father_Email=%s, Mother_Name=%s, Mother_Email=%s WHERE Student_ID=%s",(
                                                                            self.var_first_name.get(), 
                                                                            self.var_last_name.get(), 
                                                                            self.var_student_email.get(),
                                                                            self.var_date_of_admission.get(), 
                                                                            self.var_date_of_birth.get(),
                                                                            self.var_father_name.get(), 
                                                                            self.var_father_email.get(), 
                                                                            self.var_mother_name.get(),
                                                                            self.var_mother_email.get(), 
                                                                            self.var_student_ID[0]))
                else:
                    # If not, the changes are not made
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details have been successfully updated.", parent=self) # Printing a success message
                conn.commit() # Making the changes in the database
                self.fetch_data() # Reflecting the change in the table on this page
                conn.close() # Closing the database connection 
                self.clear_all_button() # Clearing all the data peasant in the textboxes
            except Exception as es:
                # Incase of any errors, an error box will be shown to the user which will contain the error code along with the error message
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Delete Button Implementation
    def delete_student_button(self):
        if self.var_student_ID==None:
            messagebox.showerror("Error", "Student ID required.", parent=self)
        else:
            try:
                delete = messagebox.askyesno("Delete Student Account", "Do you want to delete student account?", parent=self)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                    my_cursor = conn.cursor()
                    # my_cursor.execute("DELETE FROM tbl_student WHERE Student_ID=%s", (self.var_student_ID.get()))
                    sql_query = "DELETE FROM tbl_student WHERE Student_ID=%s"
                    values = (self.var_student_ID,)

                    my_cursor.execute(sql_query, self.var_student_ID)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_all_button()
                messagebox.showinfo("Delete Student Account", "Student account has been succesfully deleted.", parent=self)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
        # Creating a new Student ID
        # - Estabilishing the connectin between this project and the database
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
        my_cursor = conn.cursor()
        # - Getting all the student IDs from the IREG Database and storing them in the form of an array named student_IDs. 
        my_cursor.execute("SELECT Student_ID FROM tbl_student")
        student_IDs = my_cursor.fetchall()

        # This checks if the number of student profiles stored in the tbl_student table of the database is 0 or not. If it is 0, the 
        # system automatically assigns the student ID as 0.
        if len(student_IDs)==0:
            self.var_student_ID = str(1)
        else:
            last_student_ID = student_IDs[len(student_IDs)-1][0]
            self.var_student_ID = last_student_ID + 1

        self.new_studentID_lbl.config(text=self.var_student_ID)
        self.var_student_email.set(""),
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_date_of_admission.set(""),
        self.var_date_of_birth.set(""),
        self.var_father_name.set(""),
        self.var_father_email.set(""),
        self.var_mother_name.set(""),
        self.var_mother_email.set("")
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function to fetch the date in the table frame created
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM tbl_student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Get Cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)         #
        print(content)
        data = content["values"]
        self.var_student_ID=(data[0]),
        self.new_studentID_lbl.config(text=self.var_student_ID)
        self.var_first_name.set(data[1]),
        self.var_last_name.set(data[2]),
        self.var_date_of_admission.set(data[5]),
        self.var_student_email.set(data[4]),
        self.var_date_of_birth.set(data[3]),
        self.var_father_name.set(data[6]),
        self.var_father_email.set(data[7]),
        self.var_mother_name.set(data[8]),
        self.var_mother_email.set(data[9])
# -------------------------------------------------------------------------------------------------------------------------------------------#
    def capture_face_button(self):
        # Validation that all fields are filled up
        if self.var_student_ID=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self)
        else:
            # Added a try box to get rid pf any exceptions which might arise
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                my_cursor = conn.cursor()
                # Selected all the data from the database and stored it in the variable myresult
                my_cursor.execute("SELECT * FROM tbl_student")
                myresult = my_cursor.fetchall()
                # We match the images to an id
                id=0
                # Therfore, we create a loop to manage the IDs
                for x in myresult:
                    id += 1
                my_cursor.execute("UPDATE tbl_student SET First_Name=%s, Last_Name=%s, Email=%s, date_of_admission=%s, Date_Of_Birth=%s, Father_Name=%s, Father_Email=%s, Mother_Name=%s, Mother_Email=%s WHERE Student_ID=%s",(
                                                                                                         self.var_first_name.get(),
                                                                                                         self.var_last_name.get(),
                                                                                                         self.var_student_email.get(),
                                                                                                         self.var_date_of_admission.get(),
                                                                                                         self.var_date_of_birth.get(),
                                                                                                         self.var_father_name.get(),
                                                                                                         self.var_father_email.get(),
                                                                                                         self.var_mother_name.get(),
                                                                                                         self.var_mother_email.get(),
                                                                                                         self.var_student_ID==id+1
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.clear_all_button()
                conn.close()
                # =========== Load predifined data on face frontals from Open CV. Loading Haarcascade frontal image default =========== #
                # ideally, we need to give the path of the location of teh haarcascasde file. But in this case, the haarcascade has been 
                # copied to the code folder and therefore we do not necessaily need to provide a path for it.
                face_classifier = cv2.CascadeClassifier("C:/Users/utkarshjain120/Desktop/IREG-Image-Registration-Based-Attendance-Mangement-System/haarcascade_frontalface_default.xml") 
                # ----------------------------------------------------------------------------------------------------------------------- #
                # Supplementary functions
                # Cropping the video footage and focussing specifially on the face
                def face_cropped(img):
                    # Converting a Blue Green Red BGR image to grayscale form
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces =  face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling Factor = 1.3
                    # Minimum Neighbour = 6
                
                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
            # ---------------------------------------------------------------------------------------------------------------------------- #
                # The 0 here is an extension for the camera footage. If I want it to read a video file, I need to add in the video 
                # location. By this line, we are accessing the camera footage
                cap = cv2.VideoCapture(0)

                img_id = 0
                while True:
                    ret, face_Frame = cap.read()
                    if face_cropped(face_Frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(face_Frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "C:/Users/utkarshjain120/Desktop/IREG-Image-Registration-Based-Attendance-Mangement-System/Student_Faces/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Face", face)

                    if cv2.waitKey(1)==13 or int(img_id==100):
                        break
                cap.release()
                cv2.destroyWindow("Capture Face")
                messagebox.showinfo("Capture Face", "Succesfully captured student face.")
                Settings_Page.train_data_button(self)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Teacher_Account_Management_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Teacher_Account_Management_Label = tk.Label(self, text="Teacher Account Management", font=FONT1)
        Teacher_Account_Management_Label.place(x=205, y=5, width=870, height=75)
        Teacher_Account_Management_Label.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 20))

        # Variables related to the teachers
        self.var_teacher_ID = IntVar()
        self.var_subject_taught = StringVar()
        self.var_teacher_email = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_date_of_birth = StringVar()

        # Search Variables
        self.var_search_by_combobox = StringVar()
        self.var_search = StringVar()

        # Adding in the teacher related text boxes and labels
        # Creating a new Teacher ID
        # - Estabilishing the connectin between this project and the database
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
        my_cursor = conn.cursor()
        # - Getting all the teacher IDs from the IREG Database and storing them in the form of an array named teacher_IDs. 
        my_cursor.execute("SELECT Teacher_ID FROM tbl_teacher")
        teacher_IDs = my_cursor.fetchall()

        # This checks if the number of teacher profiles stored in the tbl_teacher table of the database is 0 or not. If it is 0, the 
        # system automatically assigns the teacher ID as 0.
        if len(teacher_IDs)==0:
            self.var_teacher_ID = str(1)
        else:
            last_teacher_ID = teacher_IDs[len(teacher_IDs)-1][0]
            self.var_teacher_ID = last_teacher_ID + 1
        conn.close()

        teacherID_lbl = Label(self, text="Teacher ID: ", font=FONT3)
        teacherID_lbl.grid(row=0, column=0, padx=(15,5), pady=(105,18), sticky=E)
        teacherID_lbl.config(bg="Black", fg="White")

        self.new_teacherID_lbl = Label(self, text=self.var_teacher_ID, font=FONT3)
        self.new_teacherID_lbl.grid(row=0, column=1, padx=5, pady=(105,18), sticky=W)
        self.new_teacherID_lbl.config(bg="Black", fg="White")

        # Adding a Student Email label and textbox
        teacher_email_lbl = Label(self, text="Teacher Email: ", font=FONT3)
        teacher_email_lbl.grid(row=0, column=2, padx=(15,5), pady=(105, 18), sticky=E)
        teacher_email_lbl.config(bg="Black", fg="White")

        teacher_email_textbox = ttk.Entry(self, width=25, textvariable=self.var_teacher_email, font=FONT3)
        teacher_email_textbox.grid(row=0, column=3, padx=5, pady=(105,18), sticky=W)

        # Adding a first name label and textbox
        first_name_lbl = Label(self, text="First Name: ", font=FONT3)
        first_name_lbl.grid(row=2, column=0, padx=(15,5), pady=18, sticky=E)
        first_name_lbl.config(bg="Black", fg="White")

        first_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_first_name, font=FONT3)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=18, sticky=W)

        # Adding a last label and textbox
        last_name_lbl = Label(self, text="Last Name: ", font=FONT3)
        last_name_lbl.grid(row=2, column=2, padx=(15,5), pady=18, sticky=E)
        last_name_lbl.config(bg="Black", fg="White")

        last_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_last_name, font=FONT3)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=18, sticky=W)

        # Adding a date of birth label and textbox
        date_of_birth_lbl = Label(self, text="Date of Birth: ", font=FONT3)
        date_of_birth_lbl.grid(row=3, column=0, padx=(15,5), pady=18, sticky=E)
        date_of_birth_lbl.config(bg="Black", fg="White")

        date_of_birth_textbox = ttk.Entry(self,width=25, textvariable=self.var_date_of_birth, font=FONT3)
        date_of_birth_textbox.grid(row=3, column=1, padx=5, pady=18, sticky=W)

        # Adding a subject taught label and combobox
        subject_taught_lbl = tk.Label(self, text="Subject Taught:", font=FONT3)
        subject_taught_lbl.grid(row=3, column=2, padx=(15,5), pady=18, sticky=W)
        subject_taught_lbl.config(bg="Black", fg="White")

        # Adding a Search by combo box
        subject_taught_combobox=ttk.Combobox(self, textvariable=self.var_subject_taught, font=FONT3, width=24, state="readonly")
        subject_taught_combobox["values"] = ("Select", "Maths", "Physics", "Computer_Science","Biology", "Private_Study")
        subject_taught_combobox.current(0)
        subject_taught_combobox.grid(row=3, column=3, padx=5, pady=18, sticky=W)
#--------------------------------------------------------------------- #
        # Adding the buttons and textboxes for creating a search system
        # Adding a search bar
        search_lbl = tk.Label(self, text="Search By:", font=FONT3)
        search_lbl.place(x=60, y=317, height=30)
        search_lbl.config(bg="Black", fg="White")

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(self, textvariable=self.var_search_by_combobox, font=FONT3, width=16, state="readonly")
        search_combobox["values"] = ("Select", "Student_ID", "First_Name", "Last_Name","Date_of_Birth", "Date_Of_Admission")
        search_combobox.current(0)
        search_combobox.place(x=165, y=317, height=30)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(self, textvariable=self.var_search, width=22, font=FONT3)
        search_entry_textbox.place(x=363, y=317, height=30)
        # Adding a Search button
        search_button = ttk.Button(self, text="Search",cursor="hand2")
        search_button.place(x=610, y=300, width=130, height=60)
        
        # Adding a Show All button
        show_all_button = ttk.Button(self, text="Show All", cursor="hand2")
        show_all_button.place(x=760, y=300, width=130, height=60)
        #============================================================================================================================================================================================================
        # Creating a Table Frame which will contain the table showing all the student profiles
        Table_Frame= ttk.Frame(self, relief=RIDGE)
        Table_Frame.place(x=5, y=430, width=1270, height=340)

        # Creating a scroll bar for both the x axxis and the y axis
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        # Creating a table structure with the heading variables being passed in the column brackets
        self.teacher_table = ttk.Treeview(Table_Frame, column=("teacher_ID", "first_name", "last_name", "email", "subject_taught", "date_of_birth"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        # Placing the scroll bar on the x axis and the y axis
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Confuguring the scroll bars so that they work whenever the user uses the scroll bars
        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)

        # Assigning the table headings to the heading variables created in the previous lines
        self.teacher_table.heading("teacher_ID", text="Teacher ID")
        self.teacher_table.heading("first_name", text="First Name")
        self.teacher_table.heading("last_name", text="Last Name")
        self.teacher_table.heading("email", text="Email")
        self.teacher_table.heading("subject_taught", text="Subject Taught")
        self.teacher_table.heading("date_of_birth", text="Date Of Birth")
        self.teacher_table["show"] = "headings"
        
        self.teacher_table.column("teacher_ID", width=68)
        self.teacher_table.column("first_name", width=130)
        self.teacher_table.column("last_name", width=130)
        self.teacher_table.column("email", width=130)
        self.teacher_table.column("subject_taught", width=120)
        self.teacher_table.column("date_of_birth", width=120)

        self.teacher_table.bind("<ButtonRelease>", self.get_cursor)
        self.teacher_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        # UI Design for the search system completed
        # --------------------------------------------------------------------------- #
        # Buttons which will aid in adding, updating and deleting the student
        # Add Student Profile button
        add_teacher_profile_button = ttk.Button(self, text="Add New Teacher Profile", command=self.add_teacher_button, style="big.TButton")
        add_teacher_profile_button.place(x=910, y=95, width=350, height=60)

        # Update Student Profile
        update_teacher_profile_button = ttk.Button(self, text="Update Teacher Profile", command=self.update_teacher_button, style="big.TButton")
        update_teacher_profile_button.place(x=910, y=160, width=350, height=60)

        # Delete Student Profile
        delete_teacher_profile_button = ttk.Button(self, text="Delete Teacher Profile", command=self.delete_teacher_button, style="big.TButton")
        delete_teacher_profile_button.place(x=910, y=225, width=350, height=60)

        # Clear All Data button
        clear_all_button = ttk.Button(self, text="Clear All Fields", command=self.clear_all_button, style="big.TButton")
        clear_all_button.place(x=910, y=290, width=350, height=60)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Account Management", command=lambda: controller.show_frame(Account_Management_Menu_Page), style="big.TButton")
        back_button.place(x=910, y=355, width=350, height=60)
    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for adding in the data when the user clicks on the add teacher button
    def add_teacher_button(self):
        if self.var_subject_taught.get()=="Select" or self.var_teacher_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_birth.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                my_cursor = conn.cursor()

                # Adding the teacher profile to the teacher table in the database
                my_cursor.execute("INSERT INTO tbl_teacher VALUES(%s, %s, %s, %s, %s)",(
                                                                                            self.var_teacher_ID,
                                                                                            self.var_first_name.get(),
                                                                                            self.var_last_name.get(),
                                                                                            self.var_date_of_birth.get(),
                                                                                            self.var_teacher_email.get()
                                                                                           ))

                # Getting the subject Id of the subject tught by the teacher
                subject_id_query = f"SELECT Subject_ID FROM tbl_subject WHERE Subject_Name=%s"
                my_cursor.execute(subject_id_query, (self.var_subject_taught.get(),))
                subject_id = my_cursor.fetchall()[0][0]

                # Adding the teacher in the subject teacher table
                my_cursor.execute("INSERT INTO tbl_subject_teacher VALUES(%s, %s)", (subject_id, self.var_teacher_ID))

                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Teacher details have been added succesfully", parent=self)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self)
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Update button implementation
    def update_teacher_button(self):
    # Validating if the user has entered in all the details asked for on the Update teacher Profile page
        if self.var_teacher_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()==""or self.var_date_of_birth.get()=="" :
            messagebox.showerror("Error", "All fields are required", parent=self)
            # Send an error message to the user if details are not completely filled
        else:
            # Adding a try except block inorder to prevent the system from stop functioning completely incase of an error
            try:
                # Asks the user if they want to update the selected profile
                update = messagebox.askyesno("Update teacher Account", "Do you want to update teacher details?", parent=self)
                if update > 0:
                # If the user click yes, the change will be made in the database
                    conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                    my_cursor = conn.cursor()
                    # Update teacher information SQL Query
                    my_cursor.execute("UPDATE tbl_teacher SET First_Name=%s, Last_Name=%s, Date_Of_Birth=%s, Email=%s WHERE teacher_ID=%s",(
                                                                                self.var_first_name.get(), 
                                                                                self.var_last_name.get(), 
                                                                                self.var_date_of_birth.get(),
                                                                                self.var_teacher_email.get(), 
                                                                                self.var_teacher_ID[0]))
                    # Getting the subject Id of the subject taught by the teacher
                    subject_id_query = f"SELECT Subject_ID FROM tbl_subject WHERE Subject_Name=%s"
                    my_cursor.execute(subject_id_query, (self.var_subject_taught.get(),))
                    subject_id = my_cursor.fetchall()[0][0]
                
                    # Updating the teacher profile in the subject teacher table
                    my_cursor.execute("UPDATE tbl_subject_teacher SET Subject_ID=%s WHERE teacher_ID=%s",(
                                                                                subject_id,
                                                                                self.var_teacher_ID[0]))
                
                else:
                    # If not, the changes are not made
                    if not update:
                        return
                messagebox.showinfo("Success", "Teacher details have been successfully updated.", parent=self) # Printing a success message
                conn.commit() # Making the changes in the database
                self.fetch_data() # Reflecting the change in the table on this page
                conn.close() # Closing the database connection 
                self.clear_all_button() # Clearing all the data peasant in the textboxes
            except Exception as es:
                # Incase of any errors, an error box will be shown to the user which will contain the error code along with the error message
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Delete Button Implementation
    def delete_teacher_button(self):
        if self.var_teacher_ID==None:
            messagebox.showerror("Error", "Teacher ID required.", parent=self)
        else:
            try:
                delete = messagebox.askyesno("Delete teacher Account", "Do you want to delete teacher account?", parent=self)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                    my_cursor = conn.cursor()
                    # my_cursor.execute("DELETE FROM tbl_teacher WHERE teacher_ID=%s", (self.var_teacher_ID.get()))
                    sql_query = "DELETE FROM tbl_teacher WHERE teacher_ID=%s"
                    values = (self.var_teacher_ID,)

                    my_cursor.execute(sql_query, self.var_teacher_ID)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_all_button()
                messagebox.showinfo("Delete teacher Account", "Teacher profile has been succesfully deleted.", parent=self)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function to fetch the date in the table frame created
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM tbl_teacher")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for i in data:
                self.teacher_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Get Cursor
    def get_cursor(self, event=""):
        cursor_focus = self.teacher_table.focus()
        content = self.teacher_table.item(cursor_focus)
        data = content["values"]
        self.var_teacher_ID=(data[0]),
        self.new_teacherID_lbl.config(text=self.var_teacher_ID)

        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Subject_ID FROM tbl_subject_teacher WHERE Teacher_ID=%s", (self.var_teacher_ID))
        subject_id = my_cursor.fetchall()[0][0]

        my_cursor.execute("SELECT Subject_Name FROM tbl_subject WHERE Subject_ID=%s", (subject_id,))
        subject_name = my_cursor.fetchall()[0][0]
        conn.close()
        self.var_subject_taught.set(f"{subject_name}")
        self.var_first_name.set(data[1]),
        self.var_last_name.set(data[2]),
        self.var_date_of_birth.set(data[3]),
        self.var_teacher_email.set(data[4])
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
        # Creating a new Teacher ID
        # - Estabilishing the connectin between this project and the database
        conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
        my_cursor = conn.cursor()
        # - Getting all the teacher IDs from the IREG Database and storing them in the form of an array named teacher_IDs. 
        my_cursor.execute("SELECT Teacher_ID FROM tbl_teacher")
        teacher_IDs = my_cursor.fetchall()

        # This checks if the number of teacher profiles stored in the tbl_teacher table of the database is 0 or not. If it is 0, the 
        # system automatically assigns the teacher ID as 0.
        if len(teacher_IDs)==0:
            self.var_teacher_ID = str(1)
        else:
            last_teacher_ID = teacher_IDs[len(teacher_IDs)-1][0]
            self.var_teacher_ID = last_teacher_ID + 1
        conn.close()
        self.new_teacherID_lbl.config(text=self.var_teacher_ID)
        self.var_subject_taught.set("Select")
        self.var_teacher_email.set(""),
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_date_of_birth.set("")
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class View_Attendance_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        View_Attendance_Label = tk.Label(self, text="View Attendance", font=FONT1) # Creating label with text and setting the font
        View_Attendance_Label.place(x=205, y=5, width=870, height=75) # Specifiying the coordnates of the label
        View_Attendance_Label.config(bg="Black", fg="White") # Confuguring the colour of the label

        self.csv_file = "C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Physics_Register.csv"

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 20))
        #======================================== Adding in the buttons ========================================#
        # Adding the Start Attendance Button
        physics_attendance_Button = ttk.Button(self, text="Physics Attendance", command=self.physics_attendance, style="big.TButton")
        physics_attendance_Button.place(x=15, y=95, width=400, height=60)

        # Adding the Account Management Button
        maths_attendance_Button = ttk.Button(self, text="Maths Attendance", command=self.maths_attendance, style="big.TButton")
        maths_attendance_Button.place(x=15, y=170, width=400, height=60)

        # Adding the Settings Button
        computer_science_attendance_Button = ttk.Button(self, text="Computer Science Attendance", command=self.computer_science_attendance, style="big.TButton")
        computer_science_attendance_Button.place(x=15, y=245, width=400, height=60)

        # Adding the Exit Button
        biology_attendance_Button = ttk.Button(self, text="Biology Attendance", command=self.biology_attendance, style="big.TButton")
        biology_attendance_Button.place(x=15, y=320, width=400, height=60)

        # Adding the Exit Button
        private_study_attendance_Button = ttk.Button(self, text="Private Study Attendance", command=self.private_study_attendance, style="big.TButton")
        private_study_attendance_Button.place(x=15, y=395, width=400, height=60)

        # Adding the Exit Button
        back_to_main_menu_Button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page), style="big.TButton")
        back_to_main_menu_Button.place(x=15, y=470, width=400, height=60)

        # Creating a Table Frame which will contain the table showing all the student profiles
        Table_Frame= ttk.Frame(self, relief=RIDGE)
        Table_Frame.place(x=430, y=95, width=830, height=665)

        # Creating a scroll bar for both the y axis
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        # Creating a table structure with the heading variables being passed in the column brackets
        self.attendance_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "date_of_attendance", "time_of_attendance", "attendance_status"), yscrollcommand=scroll_y.set)
        
        # Placing the scroll bar on the y axis
        scroll_y.pack(side=RIGHT, fill=Y)

        # Confuguring the scroll bars so that they work whenever the user uses the scroll bars
        scroll_y.config(command=self.attendance_table.yview)

        # Assigning the table headings to the heading variables created in the previous lines
        self.attendance_table.heading("std_ID", text="Student ID")
        self.attendance_table.heading("first_name", text="First Name")
        self.attendance_table.heading("last_name", text="Last Name")
        self.attendance_table.heading("date_of_attendance", text="Date of Attendance")
        self.attendance_table.heading("time_of_attendance", text="Time of Attendance")
        self.attendance_table.heading("attendance_status", text="Attendance Status")
        self.attendance_table["show"] = "headings"

        # Setting the width of the columns
        self.attendance_table.column("std_ID", width=68)
        self.attendance_table.column("first_name", width=130)
        self.attendance_table.column("last_name", width=130)
        self.attendance_table.column("date_of_attendance", width=130)
        self.attendance_table.column("time_of_attendance", width=120)
        self.attendance_table.column("attendance_status", width=120)

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def physics_attendance(self):
        self.csv_file = "C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Physics_Register.csv"
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def maths_attendance(self):
        self.csv_file = "C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Maths_Register.csv"
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def computer_science_attendance(self):
        self.csv_file = "C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Computer_Science_Register.csv"
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def biology_attendance(self):
        self.csv_file = "C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Biology_Register.csv"
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def private_study_attendance(self):
        self.csv_file = "C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Private_Study_Register.csv"
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def fetchData(self):
        attendance_file = pd.read_csv(self.csv_file)
        attendance_file.to_csv(self.csv_file, header=['Student_ID', 'First_Name', 'Last_Name', 'Time_Of_Attendance', 'Date_Of_Attendance', 'Attendance_Status'], index=False)
        if len(attendance_file['Student_ID']) != 0:
            self.attendance_table.delete(*self.attendance_table.get_children())
            index=0
            for student_id in attendance_file['Student_ID']:
                attendance_data = [attendance_file['Student_ID'][index], 
                                   attendance_file['First_Name'][index], 
                                   attendance_file['Last_Name'][index],
                                   attendance_file['Time_Of_Attendance'][index],
                                   attendance_file['Date_Of_Attendance'][index], 
                                   attendance_file['Attendance_Status'][index]]
                self.attendance_table.insert("", END, values=attendance_data)
                index += 1
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Start_Attendance_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.var_student_ID = IntVar()
        self.var_attendance_status = StringVar()
        self.var_date_of_attendance = StringVar()
        self.var_time_of_attendance = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_search_by_combobox = StringVar()
        self.var_search = StringVar()
        self.csv_path = ""
        self.subject_name = ""

        # Adding the Page tk.Label
        Start_Attendance_Label = tk.Label(self, text="Start Attendance", font=FONT1)
        Start_Attendance_Label.place(x=205, y=5, width=870, height=75)
        Start_Attendance_Label.config(bg="Black", fg="White")

        style = ttk.Style()
        style.configure("big.TButton", font=('Calibri', 20))

        # Adding the Student ID label
        studentID_lbl = Label(self, text="Student ID: ", font=FONT3)
        studentID_lbl.grid(row=0, column=0, padx=15, pady=(100, 15), sticky=E)
        studentID_lbl.config(bg="Black", fg="White")

        self.var_student_ID = None
        # Adding the student ID label which will b edisplayed whe a user clicks on the records
        self.new_studentID_lbl = Label(self, text=self.var_student_ID, font=FONT3)
        self.new_studentID_lbl.grid(row=0, column=1, padx=10, pady=(100, 15), sticky=W)
        self.new_studentID_lbl.config(bg="Black", fg="White")

        # Adding a first name label and textbox
        first_name_lbl = Label(self, text="First Name: ", font=FONT3)
        first_name_lbl.grid(row=2, column=0, padx=15, pady=15, sticky=E)
        first_name_lbl.config(bg="Black", fg="White")

        first_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_first_name, font=FONT3)
        first_name_textbox.grid(row=2, column=1, padx=10, pady=15, sticky=W)

        # Adding a last name label and textbox
        last_name_lbl = Label(self, text="Last Name: ", font=FONT3)
        last_name_lbl.grid(row=3, column=0, padx=15, pady=15, sticky=E)
        last_name_lbl.config(bg="Black", fg="White")

        last_name_textbox = ttk.Entry(self, width=25, textvariable=self.var_last_name, font=FONT3)
        last_name_textbox.grid(row=3, column=1, padx=10, pady=15, sticky=W)

        # Adding a date of attendance label and textbox
        date_of_attendance_lbl = Label(self, text="Date of Attendance: ", font=FONT3)
        date_of_attendance_lbl.grid(row=4, column=0, padx=15, pady=15, sticky=E)
        date_of_attendance_lbl.config(bg="Black", fg="White")

        date_of_attendance_textbox = ttk.Entry(self, width=25, textvariable=self.var_date_of_attendance, font=FONT3)
        date_of_attendance_textbox.grid(row=4, column=1, padx=10, pady=15, sticky=W)

        # Adding a time of attendance label and textbox
        time_of_attendance_lbl = Label(self, text="Time of Attendance: ", font=FONT3)
        time_of_attendance_lbl.grid(row=5, column=0, padx=15, pady=15, sticky=E)
        time_of_attendance_lbl.config(bg="Black", fg="White")

        time_of_attendance_textbox = ttk.Entry(self, width=25, textvariable=self.var_time_of_attendance, font=FONT3)
        time_of_attendance_textbox.grid(row=5, column=1, padx=10, pady=15, sticky=W)

        # Adding a date of attendance label and combo box
        attendance_status_lbl = Label(self, text="Attendance Status: ", font=FONT3)
        attendance_status_lbl.grid(row=6, column=0, padx=15, pady=15, sticky=E)
        attendance_status_lbl.config(bg="Black", fg="White")

        # Adding a Search by combo box
        attendance_status_combobox=ttk.Combobox(self, textvariable=self.var_attendance_status, font=FONT3, width=16, state="readonly")
        attendance_status_combobox["values"] = ("Attendance_Status", "Present", "Absent")
        attendance_status_combobox.current(0)
        attendance_status_combobox.grid(row=6, column=1, padx=10, pady=15, sticky=W)

        # Adding in the buttons
        # Start Attendance button
        start_attendance_button = ttk.Button(self, text="Start Attendance", style="big.TButton", command=self.face_recognition)
        start_attendance_button.place(x=50, y=455, width=370, height=60)

        # Update Attendance Profile
        update_attendance_button = ttk.Button(self, text="Update Attendance", style="big.TButton", command=self.update_attendance_button)
        update_attendance_button.place(x=50, y=530, width=370, height=60)

        # Clear All Data button
        clear_all_button = ttk.Button(self, text="Clear All Fields", style="big.TButton", command=self.clear_all_button)
        clear_all_button.place(x=50, y=605, width=370, height=60)

        # Adding the back button
        back_to_start_attendance_button = ttk.Button(self, text="Back to Start Attendance", command=lambda: controller.show_frame(IREG_Main_Menu_Page), style="big.TButton")
        back_to_start_attendance_button.place(x=50, y=680, width=370, height=60)

        # Adding the search system labels and textboxes
        # Adding a search bar
        search_lbl = tk.Label(self, text="Search By:", font=FONT3)
        search_lbl.grid(row=0, column=2, padx=5, pady=(100,10))
        search_lbl.config(bg="Black", fg="White")

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(self, textvariable=self.var_search_by_combobox, font=FONT3, width=10, state="readonly")
        search_combobox["values"] = ("Select", "Student_ID", "First_Name", "Last_Name", "Present", "Absent")
        search_combobox.current(0)
        search_combobox.grid(row=0, column=3, padx=5, pady=(100,10))

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(self, textvariable=self.var_search, width=15, font=FONT3)
        search_entry_textbox.grid(row=0, column=4, padx=5, pady=(100,10))

        # Adding a Search button
        search_button = ttk.Button(self, text="Search",cursor="hand2")
        search_button.grid(row=0, column=5, padx=5, pady=(100,10), ipadx=18, ipady=8)
        
        # Adding a Mark All Present button
        mark_all_present_button = ttk.Button(self, text="Mark All Present", cursor="hand2", command=self.mark_all_present_button)
        mark_all_present_button.grid(row=0, column=6, padx=5, pady=(100,10), ipadx=18, ipady=8)

        # Adding a Mark All Absent button
        mark_all_absent_button = ttk.Button(self, text="Mark All Absent", cursor="hand2", command=self.mark_all_absent_button)
        mark_all_absent_button.grid(row=0, column=7, padx=5, pady=(100,10), ipadx=18, ipady=8)
        #============================================================================================================================================================================================================
        # Creating a Table Frame which will contain the table showing all the student profiles
        Table_Frame= ttk.Frame(self, relief=RIDGE)
        Table_Frame.place(x=477, y=150, width=785, height=620)

        # Creating a scroll bar for both the y axis
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        # Creating a table structure with the heading variables being passed in the column brackets
        self.attendance_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "date_of_attendance", "time_of_attendance", "attendance_status"), yscrollcommand=scroll_y.set)
        
        # Placing the scroll bar on the y axis
        scroll_y.pack(side=RIGHT, fill=Y)

        # Confuguring the scroll bars so that they work whenever the user uses the scroll bars
        scroll_y.config(command=self.attendance_table.yview)

        # Assigning the table headings to the heading variables created in the previous lines
        self.attendance_table.heading("std_ID", text="Student ID")
        self.attendance_table.heading("first_name", text="First Name")
        self.attendance_table.heading("last_name", text="Last Name")
        self.attendance_table.heading("date_of_attendance", text="Date of Attendance")
        self.attendance_table.heading("time_of_attendance", text="Time of Attendance")
        self.attendance_table.heading("attendance_status", text="Attendance Status")
        self.attendance_table["show"] = "headings"

        # Setting the width of the columns
        self.attendance_table.column("std_ID", width=68)
        self.attendance_table.column("first_name", width=130)
        self.attendance_table.column("last_name", width=130)
        self.attendance_table.column("date_of_attendance", width=130)
        self.attendance_table.column("time_of_attendance", width=120)
        self.attendance_table.column("attendance_status", width=120)

        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)
        self.attendance_table.pack(fill=BOTH, expand=1)
        self.fetchData()
    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf,):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0 ,255, 0), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                my_cursor = conn.cursor()


                my_cursor.execute("SELECT * FROM tbl_Student WHERE Student_ID=" + str(id))
                data = my_cursor.fetchall()
                fetch_student_id = data[0][0]
                fetch_first_name = data[0][1]
                fetch_last_name = data[0][2]

                # Confidence is the percentage of difference from the original image. Lower the confidence, the result is more 
                # accurate and vice versa
                if confidence > 77:
                    cv2.putText(img, f"Student ID: {fetch_student_id}", (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
                    cv2.putText(img, f"First Name: {fetch_first_name}", (x, y-35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
                    cv2.putText(img, f"Last Name: {fetch_last_name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
                    self.mark_attendance(fetch_student_id, fetch_first_name, fetch_last_name)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0 , 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (000, 000, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognise(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img


        faceCascade = cv2.CascadeClassifier("C:/Users/utkarshjain120/Desktop/IREG-Image-Registration-Based-Attendance-Mangement-System/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:/Users/utkarshjain120/Desktop/IREG-Image-Registration-Based-Attendance-Mangement-System/Trained_Faces.xml")

        video_Capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_Capture.read()
            img = recognise(img, clf, faceCascade)
            cv2.imshow("Welcome to IREG", img)

            if cv2.waitKey(1)==13:
                self.marking_student_absent()
                break
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def mark_attendance(self, student_id, first_name, last_name):
        with open(self.csv_path,"r+", newline="\n") as Attendance_File:
            next(Attendance_File) # Skips over the first item of the csv file which contains the headers for the items
            stored_attendance  = Attendance_File.readlines() # Reading the lines from the csv file to the variable store_attendance
            student_ID_list = [] # Creating empty list which will store the data


            for line in stored_attendance:
                entry = line.split((",")) # Splitting each line in the csv file at the comma
                student_ID_list.append(int(entry[0])) # Adding the line from the csv file which was split at commas

            if ((student_id not in student_ID_list)):
                now = datetime.now() # Getting the current date and time
                attendance_time = now.strftime("%d/%m/%Y") # Setting the current time in the set format
                attendance_date = now.strftime("%H:%M:%S") # Setting the current date in the set format
                student_ID_list.append(student_id) # Adding the student ID to the student id list

                Attendance_File.writelines(f"\n{student_id},{first_name},{last_name},{attendance_date},{attendance_time},Present")
                # Adding the attendance in the csv file
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def fetchData(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        if now.strftime("%A") == "Sunday" or now.strftime("%A") == "Saturday":
            day="Monday"
        else:
            day = now.strftime("%A")
        day = "Monday"

        # Determining the from time to get the class id of the current period
        if current_time > "08:40:00" and current_time < "09:40:00":
            from_time = "08:40:00"
        elif current_time > "09:40:00" and current_time < "10:40:00":
           from_time = "09:40:00"
        elif current_time > "11:00:00" and current_time < "12:00:00":
            from_time = "11:00:00"
        elif current_time > "12:00:00" and current_time < "13:00:00":
            from_time = "12:00:00"
        elif current_time > "13:40:00" and current_time < "14:45:00":
            from_time = "13:45:00"
        else:                              
            from_time = "12:00:00"
        from_time = "08:40:00"
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "utkarshjain120", database = "mydb")
        my_cursor = conn.cursor()


        # Please add in a fake day of it is Saturday or a Sunday
        # Getting the class ID from the tbl_timetable in the database
        my_cursor.execute("SELECT * FROM tbl_timetable WHERE Day=%s AND From_Time=%s", (day, from_time))
        record = my_cursor.fetchall()
        subject_ID = record[0][5]
        class_ID = record[0][0]

        my_cursor.execute("SELECT * FROM tbl_subject WHERE Subject_ID=%s", (subject_ID,))
        self.subject_name= my_cursor.fetchall()[0][1]

        # Setting the csv file of the attendance register
        self.csv_path = f"C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/{self.subject_name}_Register.csv"

        attendance_file = pd.read_csv(self.csv_path)
        attendance_file.to_csv(self.csv_path, header=['Student_ID', 'First_Name', 'Last_Name', 'Time_Of_Attendance', 'Date_Of_Attendance', 'Attendance_Status'], index=False)
        if len(attendance_file['Student_ID']) != 0:
            self.attendance_table.delete(*self.attendance_table.get_children())
            index=0
            for student_id in attendance_file['Student_ID']:
                attendance_data = [attendance_file['Student_ID'][index], 
                                   attendance_file['First_Name'][index], 
                                   attendance_file['Last_Name'][index],
                                   attendance_file['Time_Of_Attendance'][index],
                                   attendance_file['Date_Of_Attendance'][index], 
                                   attendance_file['Attendance_Status'][index]]
                self.attendance_table.insert("", END, values=attendance_data)
                index += 1
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Get Cursor
    def get_cursor(self, event=""):
        cursor_focus = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_focus)
        data = content["values"]
        self.var_student_ID=(data[0]),
        self.new_studentID_lbl.config(text=self.var_student_ID)
        self.var_first_name.set(data[1]),
        self.var_last_name.set(data[2]),
        self.var_time_of_attendance.set(data[3]),
        self.var_date_of_attendance.set(data[4]),
        self.var_attendance_status.set(data[5])
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def mark_all_present_button(self):
        # reading the csv file
        attendance_file = pd.read_csv(self.csv_path)
        attendance_file.to_csv(self.csv_path, header=['Student_ID', 'First_Name', 'Last_Name', 'Time_Of_Attendance', 'Date_Of_Attendance', 'Attendance_Status'], index=False)
        # updating the column value data
        for student_ids in attendance_file['Student_ID']:
            attendance_file.loc[student_ids-1, 'Attendance_Status'] = 'Present'

        # writing into the file
        attendance_file.to_csv(self.csv_path, index=False)
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def mark_all_absent_button(self):
        # reading the csv file
        attendance_file = pd.read_csv(self.csv_path)
        attendance_file.to_csv(self.csv_path, header=['Student_ID', 'First_Name', 'Last_Name', 'Time_Of_Attendance', 'Date_Of_Attendance', 'Attendance_Status'], index=False)
        # updating the column value data
        for student_ids in attendance_file['Student_ID']:
            attendance_file.loc[student_ids-1, 'Attendance_Status'] = 'Absent'

        # writing into the file
        attendance_file.to_csv(self.csv_path, index=False)
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def update_attendance_button(self):
        if self.var_student_ID=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_time_of_attendance.get()=="" or self.var_date_of_attendance.get()=="" or self.var_attendance_status.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self)
        else:
            try:
                attendance_file = pd.read_csv(self.csv_path)
                attendance_file.to_csv(self.csv_path, header=['Student_ID', 'First_Name', 'Last_Name', 'Time_Of_Attendance', 'Date_Of_Attendance', 'Attendance_Status'], index=False)

                attendance_file.loc[self.var_student_ID[0]-1, 'Last_Name'] = self.var_last_name.get()
                attendance_file.loc[self.var_student_ID[0]-1, 'First_Name'] = self.var_first_name.get()
                attendance_file.loc[self.var_student_ID[0]-1, 'Time_Of_Attendance'] = self.var_time_of_attendance.get()
                attendance_file.loc[self.var_student_ID[0]-1, 'Date_Of_Attendance'] = self.var_date_of_attendance.get()
                attendance_file.loc[self.var_student_ID[0]-1, 'Attendance_Status'] = self.var_attendance_status.get()

                attendance_file.to_csv(self.csv_path, index=False)
                self.fetchData()
                self.clear_all_button()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self)
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
        self.var_student_ID = None
        self.new_studentID_lbl.config(text=self.var_student_ID)
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_time_of_attendance.set(""),
        self.var_date_of_attendance.set(""),
        self.var_attendance_status.set("")
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def marking_student_absent(self):
        # Establishing the connection between the code file and the database
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "utkarshjain120", database = "mydb")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT Subject_ID FROM tbl_subject WHERE Subject_Name=%s", (self.subject_name,))
        Subject_ID = my_cursor.fetchall()[0][0]

        my_cursor.execute("SELECT Class_ID FROM tbl_class WHERE Subject_ID=%s", (Subject_ID,))
        Class_ID = my_cursor.fetchall()[0][0]

        my_cursor.execute("SELECT Student_ID FROM tbl_student_class WHERE Class_ID=%s", (Class_ID,))
        profiles = my_cursor.fetchall()

        for profile in profiles:
            student_id = profile[0]

            my_cursor.execute("SELECT First_Name FROM tbl_student WHERE Student_ID=%s", (student_id,))
            first_name = my_cursor.fetchall()[0][0]

            my_cursor.execute("SELECT Last_Name FROM tbl_student WHERE Student_ID=%s", (student_id,))
            last_name = my_cursor.fetchall()[0][0]


            with open(self.csv_path,"r+") as Attendance_File:
                next(Attendance_File) # Skips over the first item of the csv file which contains the headers for the items
                stored_attendance  = Attendance_File.readlines() # Reading the lines from the csv file to the variable store_attendance
                student_ID_list = [] # Creating empty list which will store the data

                for line in stored_attendance:
                    entry = line.split((",")) # Splitting each line in the csv file at the comma
                    if entry[0] != f"\n":
                        student_ID_list.append(int(entry[0])) # Adding the line from the csv file which was split at commas
                    
                if ((student_id not in student_ID_list)):
                    now = datetime.now() # Getting the current date and time
                    attendance_time = now.strftime("%d/%m/%Y") # Setting the current time in the set format
                    attendance_date = now.strftime("%H:%M:%S") # Setting the current date in the set format
                    student_ID_list.append(student_id) # Adding the student ID to the student id list

                    Attendance_File.writelines(f"\n{student_id},{first_name},{last_name},{attendance_date},{attendance_time},Absent")
                # Adding the attendance in the csv file
        self.fetchData()
##############################################################################################################################################
##############################################################################################################################################
# ========================================================================================================================================== #
# ========================================================================================================================================== #
class Settings_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding the Page tk.Label
        Settings_Lbl = tk.Label(self, text="Settings", font=FONT1)
        Settings_Lbl.place(x=205, y=5, width=870, height=75)
        Settings_Lbl.config(bg="Black", fg="White")

        # Adding the View Attendance
        train_data_Button =  ttk.Button(self, text="Train Data", command= self.train_data_button, style="big.TButton")
        train_data_Button.place(x=440, y=360, width=400, height=50)

        # Adding the Account Management Button
        student_faces_Button = ttk.Button(self, text="Student Faces", command= self.student_faces_button, style="big.TButton")
        student_faces_Button.place(x=440, y=420, width=400, height=50)

        # Adding the back button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(IREG_Main_Menu_Page), style="big.TButton")
        back_button.place(x=440,y=480, width=400, height=50)
    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for viewing teh studnet faces stored on the device
    def student_faces_button(self):
        os.startfile("C:/Users/utkarshjain120/Desktop/IREG-Image-Registration-Based-Attendance-Mangement-System/Student_Faces")
    # ----------------------------------------------------------------------------------------------------------------------- #
    def train_data_button(self):
        data_dir = ("C:/Users/utkarshjain120/Desktop/IREG-Image-Registration-Based-Attendance-Mangement-System/Student_Faces")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for face in path:
            img = Image.open(face).convert("L") # Grey Scale Image
            imageNP = np.array(img, 'uint8') # Converting gray scale image to an array of data type uint
            face_ID = int(os.path.split(face)[1].split(".")[1])

            faces.append(imageNP)
            ids.append(face_ID)
            cv2.imshow("Training", imageNP)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # Train Classifier and Save
        train_classifier = cv2.face.LBPHFaceRecognizer_create()
        train_classifier.train(faces, ids)
        train_classifier.write("C:/Users/utkarshjain120/Desktop/IREG-Image-Registration-Based-Attendance-Mangement-System/Trained_Faces.xml")
        cv2.destroyWindow("Training")
        messagebox.showinfo("Training Success", "Datasets have been trained successfully.")

app = IREG()
app.mainloop()