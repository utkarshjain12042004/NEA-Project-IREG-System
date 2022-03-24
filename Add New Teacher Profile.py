# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
import mysql.connector
from datetime import datetime

class Add_New_Teacher_Profile:
    # This is the constructor of the class IREG_Main_Menu
    def __init__(self, root):
        self.root = root
        # Setting the dimensions of the window and the point where the window is displayed from
        self.root.geometry("1280x760+0+0")
        # Setting the property of resizing the window to false
        self.root.resizable(width=False, height=False)
        self.root.title("IREG")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="White", relief = SOLID)
        mainFrame.place(x=2, y=2, width=1276, height=755) # Specifying the coordinates along with the dimensions of the frame

        # Label Frame
        Add_New_Teacher_Profile_lbl= Label(mainFrame, text="Add New Teacher Profile", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Add_New_Teacher_Profile_lbl.place(x=2, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

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

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=5, y=612, width=1257, height=133) # Specifying the coordinates along with the dimensions of the frame

        # ======================================================================================================================================== #
        # teacher Information frame: This frame will contain all the fields asking for information related to the teacher
        Teacher_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Teacher Details", font=("Segoe UI Variable", 12, "bold"))
        Teacher_Information_Frame.place(x=225, y=206, width=826, height=200) # Specifying the coordinates along with the dimensions of the frame
        # =================================================================== #
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

        # Adding a teacher Id label and textbox
        teacherID_label = Label(Teacher_Information_Frame, text = "Teacher ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        teacherID_label.grid(row=0, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        #teacherID_textbox = ttk.Entry(Teacher_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        #teacherID_textbox.grid(row=0, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        self.new_teacherID_lbl = Label(Teacher_Information_Frame, text = self.var_teacher_ID, font=("Segoe UI Variable", 12, "bold"), bg = "White")
        self.new_teacherID_lbl.grid(row=0, column=1, padx=(15,5), pady=15, sticky=W)
        
        # Adding a subject taught label and combobox
        subject_taught_label = Label(Teacher_Information_Frame, text = "Subject Taught: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        subject_taught_label.grid(row=0, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label

        subject_taught_combobox=ttk.Combobox(Teacher_Information_Frame , width=23, textvariable = self.var_subject_taught, font=("Segoe UI Variable", 12, "bold"), state="readonly")
        # The above line creates the combo box and makes it read only. The user will not be able to type in this box
        subject_taught_combobox["values"] = ("Select", "Maths", "Computer Science", "Physics", "Free", "Private Study") # Adding in the values to be shown in the drop down list
        subject_taught_combobox.current(0) # Specifying the default item to be shown
        subject_taught_combobox.grid(row=0, column=3, padx=(25,5), pady=17, sticky=W) # Specifying the location of the combo box

        # Adding a teacher Email label and textbox
        teacher_email_label = Label(Teacher_Information_Frame, text = "Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        teacher_email_label.grid(row=1, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label
      
        teacher_email_textbox = ttk.Entry(Teacher_Information_Frame, width=25, textvariable = self.var_teacher_email, font=("Segoe UI Variable", 12, "bold"))
        teacher_email_textbox.grid(row=1, column=1, padx=(25,5), pady=17, sticky=W)# Specifying the location of the text box
      
        # Adding a first name label and textbox
        first_name_label = Label(Teacher_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        first_name_label.grid(row=1, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label

        first_name_textbox = ttk.Entry(Teacher_Information_Frame, width=25, textvariable = self.var_first_name, font=("Segoe UI Variable", 12, "bold"))
        first_name_textbox.grid(row=1, column=3, padx=(25,5), pady=17, sticky=W)# Specifying the location of the text box

        # Adding a last label and textbox
        last_name_label = Label(Teacher_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        last_name_label.grid(row=2, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label
      
        last_name_textbox = ttk.Entry(Teacher_Information_Frame, width=25, textvariable = self.var_last_name, font=("Segoe UI Variable", 12, "bold"))
        last_name_textbox.grid(row=2, column=1, padx=(25,5), pady=17, sticky=W)# Specifying the location of the text box

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Teacher_Information_Frame, text = "Date of Birth: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        date_of_birth_label.grid(row=2, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label

        date_of_birth_textbox = ttk.Entry(Teacher_Information_Frame, width=25, textvariable = self.var_date_of_birth, font=("Segoe UI Variable", 12, "bold"))
        date_of_birth_textbox.grid(row=2, column=3, padx=(25,5), pady=17, sticky=W)# Specifying the location of the text box

        #======================================== Adding in the buttons ========================================#
        # Add New teacher Profile Button
        add_new_teacher_Button = Button(Button_Frame, text="Add New Teacher Profile", cursor="hand2", command=self.add_teacher_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=31, height=3)
        add_new_teacher_Button.grid(row=0, column=0, padx=(21, 10), pady=(20, 10)) # Specifying the coordinates along with the dimensions of the frame

        # Clear All Fields Button
        clear_all_fields_Button = Button(Button_Frame, text="Clear All Fields", cursor="hand2", command=self.clear_all_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=31, height=3)
        clear_all_fields_Button.grid(row=0, column=1, padx=(21, 10), pady=(20, 10)) # Specifying the coordinates along with the dimensions of the frame
       
        # Back to teacher Account Management Button
        back_to_account_management_Button = Button(Button_Frame, text="Back to Teacher Account Management", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=31, height=3)
        back_to_account_management_Button.grid(row=0, column=2, padx=(21, 10), pady=(20, 10)) # Specifying the coordinates along with the dimensions of the frame
#                                                            END OF UI DESIGN
#===========================================================================================================================================#
#############################################################################################################################################
#===========================================================================================================================================#
#                                                      BUTTON IMPLEMENTATION FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for adding in the data when the user clicks on the add teacher button
    def add_teacher_button(self):
        if self.var_subject_taught.get()=="Select" or self.var_teacher_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_birth.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
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
                messagebox.showinfo("Success", "Teacher details have been added succesfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
        self.var_teacher_email.set(""),
        self.var_subject_taught.set(""),
        self.var_teacher_email.set("")
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_date_of_birth.set("")

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Add_New_Teacher_Profile(root)
    root.mainloop()
