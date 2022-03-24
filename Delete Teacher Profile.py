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

class Delete_Teacher_Profile:
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
        Update_Teacher_Profile_lbl= Label(mainFrame, text="Delete Teacher Profile", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Update_Teacher_Profile_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

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
        Button_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=885, y=85, width=380, height=220) # Specifying the coordinates along with the dimensions of the frame

        # ======================================================================================================================================== #
        # Teacher Information frame: This frame will contain all the fields asking for information related to the teacher
        Teacher_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Teacher Details", font=("Segoe UI Variable", 12, "bold"))
        Teacher_Information_Frame.place(x=5, y=85, width=875, height=220)
        # ======================================================================================================== #
        # Adding a teacher Id label and textbox
        teacherID_label = Label(Teacher_Information_Frame, text = "Teacher ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        teacherID_label.grid(row=0, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        #teacherID_textbox = ttk.Entry(Teacher_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        #teacherID_textbox.grid(row=0, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        self.var_teacher_ID = None
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


        # ====================================================================================================================================== #
        # Adding in the buttons to the button frame
        # Add New teacher Profile Button
        delete_teacher_Button = Button(Button_Frame, text="Delete Teacher Profile", cursor="hand2", command=self.delete_teacher_button,font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        delete_teacher_Button.place(x=5, y=5, height=65, width=365) # Specifying the coordinates along with the dimensions of the button

        # Clear All Fields Button
        clear_all_fields_Button = Button(Button_Frame, text="Clear All Fields", cursor="hand2", command=self.clear_all_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        clear_all_fields_Button.place(x=5, y=75, height=65, width=365) # Specifying the coordinates along with the dimensions of the button
       
        # Back to teacher Account Management Button
        back_to_teacher_account_management_Button = Button(Button_Frame, text="Back to Previous Page", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        back_to_teacher_account_management_Button.place(x=5, y=145, height=65, width=365) # Specifying the coordinates along with the dimensions of the button

        # ======================================================================================================================================== #
        # Search Frame: This frame will contain the search system which will be show the user all the teacher profiles created
        Search_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Search_Frame.place(x=5, y=325, width=1260, height=420)

        # Adding a search bar
        search_label = Label(Search_Frame, text="Search By:", font=("Segoe UI Variable", 12, "bold"), bg="White", fg="Black")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(Search_Frame, font=("Segoe UI Variable", 12, "bold"), width=15, state="readonly")
        search_combobox["values"] = ("Select", "Teacher ID", "First Name", "LastName","Date of Birth", "Date Of Hiring")
        search_combobox.current(0)
        search_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(Search_Frame, width=20, font=("Segoe UI Variable", 12, "bold"))
        search_entry_textbox.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # Adding a Search button
        search_button = Button(Search_Frame, width=10, text="Search", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="White")
        search_button.grid(row=0, column=3,padx=5, pady=5, sticky=W)
        
        # Adding a Show All button
        show_all_button = Button(Search_Frame, width=10, text="Show All", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="White")
        show_all_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)
#============================================================================================================================================================================================================
        # Table Frame
        Table_Frame= Frame(Search_Frame, bd=2, bg="White", relief=RIDGE)
        Table_Frame.place(x=0, y=45, width=1255, height=370)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.teacher_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "email", "subject_taught", "date_of_birth"), 
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)

        self.teacher_table.heading("std_ID", text="Teacher ID")
        self.teacher_table.heading("first_name", text="First Name")
        self.teacher_table.heading("last_name", text="Last Name")
        self.teacher_table.heading("email", text="Email")
        self.teacher_table.heading("subject_taught", text="Subejct Taught")
        self.teacher_table.heading("date_of_birth", text="Date Of Birth")
        self.teacher_table["show"] = "headings"
        
        self.teacher_table.column("std_ID", width=68)
        self.teacher_table.column("first_name", width=130)
        self.teacher_table.column("last_name", width=130)
        self.teacher_table.column("email", width=130)
        self.teacher_table.column("subject_taught", width=120)
        self.teacher_table.column("date_of_birth", width=120)

        self.teacher_table.bind("<ButtonRelease>", self.get_cursor)
        self.teacher_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
#                                                            END OF UI DESIGN
#===========================================================================================================================================#
#############################################################################################################################################
#===========================================================================================================================================#
#                                                      BUTTON IMPLEMENTATION FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Delete Button Implementation
    def delete_teacher_button(self):
        if self.var_teacher_ID==None:
            messagebox.showerror("Error", "Teacher ID required.", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete teacher Account", "Do you want to delete teacher account?", parent=self.root)
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
                messagebox.showinfo("Delete teacher Account", "Teacher profile has been succesfully deleted.", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
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
        self.var_subject_taught.set("Select")
        self.var_teacher_email.set(""),
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_date_of_birth.set("")


# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Delete_Teacher_Profile(root)
    root.mainloop()
