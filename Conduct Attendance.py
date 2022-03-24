    # Importing all the required modules to create the UI
from tkinter import *
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
from tkinter import filedialog
import pandas as pd
from tempfile import NamedTemporaryFile
import shutil

class Show_Attendance:
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
        Automated_Attendace_Method_lbl= Label(mainFrame, text="Conduct Attendance", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Automated_Attendace_Method_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        self.var_student_ID = IntVar()
        self.var_attendance_status = StringVar()
        self.var_date_of_attendance = StringVar()
        self.var_time_of_attendance = StringVar()
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()

        # Button Frame
        Button_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=885, y=75, width=380, height=230) # Specifying the coordinates along with the dimensions of the frame

        # ======================================================================================================================================== #
        # student Information frame: This frame will contain all the fields asking for information related to the student
        Attendance_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Attendance", font=("Segoe UI Variable", 12, "bold"))
        Attendance_Frame.place(x=5, y=75, width=875, height=220)
        # =================================================================== #
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        studentID_label = Label(Attendance_Frame, text = "Student ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        studentID_label.grid(row=0, column=0, padx=(25,20), pady=18, sticky=W) # Specifying the coordinates of the label

        self.var_student_ID = None
        self.new_studentID_lbl = Label(Attendance_Frame, text=self.var_student_ID, font=("Segoe UI Variable", 12, "bold"), bg = "White")
        self.new_studentID_lbl.grid(row=0, column=1, padx=(15,5), pady=15, sticky=W)

        # Adding a student Email label and textbox
        attendance_date_label = Label(Attendance_Frame, text = "Attendance Date: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        attendance_date_label.grid(row=0, column=2, padx=(35,20), pady=18, sticky=W) # Specifying the coordinates of the label

        attendance_date_textbox = ttk.Entry(Attendance_Frame, width=22, textvariable=self.var_date_of_attendance, font=("Segoe UI Variable", 12, "bold"),)
        attendance_date_textbox.grid(row=0, column=3, padx=5, pady=18, sticky=W) # Specifying the coordinates of the textbox

        # Adding a first name label and textbox
        first_name_label = Label(Attendance_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        first_name_label.grid(row=2, column=0, padx=(25,20), pady=18, sticky=W) # Specifying the coordinates of the label

        first_name_textbox = ttk.Entry(Attendance_Frame, width=22, textvariable=self.var_first_name, font=("Segoe UI Variable", 12, "bold"),)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=18, sticky=W) # Specifying the coordinates of the textbox

        # Adding a last label and textbox
        last_name_label = Label(Attendance_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        last_name_label.grid(row=2, column=2, padx=(35,20), pady=18, sticky=W) # Specifying the coordinates of the label
       
        last_name_textbox = ttk.Entry(Attendance_Frame, width=22, textvariable=self.var_last_name, font=("Segoe UI Variable", 12, "bold"),)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=18, sticky=W) # Specifying the coordinates of the textbox

        # Adding a student Date Of hiring label and textbox
        attendance_status_label = Label(Attendance_Frame, text = "Attendance Status: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        attendance_status_label.grid(row=3, column=0, padx=(25,6), pady=18, sticky=W) # Specifying the coordinates of the label
       
        attendance_status_combobox=ttk.Combobox(Attendance_Frame, width=20, textvariable=self.var_attendance_status, font=("Segoe UI Variable", 12, "bold"), state="readonly")
        # The above line creates the combo box and makes it read only. The user will not be able to type in this box
        attendance_status_combobox["values"] = ("--Attendance Status--", "Present", "Absent", "Late") # Adding in the values to be shown in the drop down list
        attendance_status_combobox.current(0) # Specifying the default item to be shown
        attendance_status_combobox.grid(row=3, column=1, padx=(6,5), pady=17, sticky=W) # Specifying the location of the combo box

        # Adding a date of birth label and textbox
        time_of_attendance_label = Label(Attendance_Frame, text = "Time of Attendance: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        time_of_attendance_label.grid(row=3, column=2, padx=(35,20), pady=18, sticky=W) # Specifying the coordinates of the label

        time_of_attendance_textbox = ttk.Entry(Attendance_Frame,width=22, textvariable=self.var_time_of_attendance, font=("Segoe UI Variable", 12, "bold"),)
        time_of_attendance_textbox.grid(row=3, column=3, padx=5, pady=18, sticky=W) # Specifying the coordinates of the textbox

        # ====================================================================================================================================== #
        # Adding in the buttons to the button frame
        # Update Student Attendance Button
        start_capture_Button = Button(Button_Frame, text="Start Capture", cursor="hand2", command=self.face_recognition, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        start_capture_Button.place(x=5, y=5, height=50, width=365) # Specifying the coordinates along with the dimensions of the button

        # Back to student Account Management Button
        update_attendance_Button = Button(Button_Frame, text="Update Attendance", cursor="hand2", command=self.update_attendance_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        update_attendance_Button.place(x=5, y=60, height=50, width=365) # Specifying the coordinates along with the dimensions of the button

        # Clear All Fields Button
        clear_all_Button = Button(Button_Frame, text="Clear All Fields", cursor="hand2", command=self.clear_all_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        clear_all_Button.place(x=5, y=115, height=50, width=365) # Specifying the coordinates along with the dimensions of the button
        
        # Back to Start Attendance Button
        back_to_start_attendance_Button = Button(Button_Frame, text="Back to Start Attendance Button", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        back_to_start_attendance_Button.place(x=5, y=170, height=50, width=365) # Specifying the coordinates along with the dimensions of the button

        # ======================================================================================================================================== #
        # Search Frame: This frame will contain the search system which will be show the user all the student profiles created
        Search_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Search_Frame.place(x=5, y=325, width=1260, height=420)

        # Adding a search bar
        search_label = Label(Search_Frame, text="Search By:", font=("Segoe UI Variable", 12, "bold"), bg="White", fg="Black")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(Search_Frame, font=("Segoe UI Variable", 12, "bold"), width=20, state="readonly")
        search_combobox["values"] = ("Select", "Student ID", "First Name", "LastName","Time of Attendance")
        search_combobox.current(0)
        search_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Adding an entry field textbox
        search_entry_textbox = ttk.Entry(Search_Frame, width=22, font=("Segoe UI Variable", 12, "bold"))
        search_entry_textbox.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # Adding a Search button
        search_button = Button(Search_Frame, width=10, text="Search", cursor="hand2", font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="White")
        search_button.grid(row=0, column=3,padx=5, pady=5, sticky=W)
        
        # Adding a Mark All Present button
        mark_all_present_button = Button(Search_Frame, width=12, text="Mark All Present", cursor="hand2", command=self.mark_all_present_button, font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="White")
        mark_all_present_button.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        # Adding a Mark All Absent button
        mark_all_present_button = Button(Search_Frame, width=12, text="Mark All Absent", cursor="hand2", command=self.mark_all_absent_button, font=("Segoe UI Variable", 12, "bold"), bg="Black", fg="White")
        mark_all_present_button.grid(row=0, column=5, padx=5, pady=5, sticky=W)
#============================================================================================================================================================================================================
        # Table Frame
        Table_Frame= Frame(Search_Frame, bd=2, bg="White", relief=RIDGE)
        Table_Frame.place(x=0, y=45, width=1255, height=370)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.attendance_table = ttk.Treeview(Table_Frame, column=("student_ID", "first_name", "last_name", "attendance_status", "date_of_attendance", "time_of_attendance"), 
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("student_ID", text="Student ID")
        self.attendance_table.heading("first_name", text="First Name")
        self.attendance_table.heading("last_name", text="Last Name")
        self.attendance_table.heading("attendance_status", text="Attendance Status")
        self.attendance_table.heading("date_of_attendance", text="Attendance Data")
        self.attendance_table.heading("time_of_attendance", text="Attendance Time")
        self.attendance_table["show"] = "headings"
        
        self.attendance_table.column("student_ID", width=68)
        self.attendance_table.column("first_name", width=130)
        self.attendance_table.column("last_name", width=130)
        self.attendance_table.column("attendance_status", width=130)
        self.attendance_table.column("date_of_attendance", width=120)
        self.attendance_table.column("time_of_attendance", width=120)

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
    # Button Implementation
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
                break
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def mark_attendance(self, student_id, first_name, last_name):
        with open("C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv","r+", newline="\n") as Attendance_File:
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
        attendance_file = pd.read_csv('C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv')
        attendance_file.to_csv('C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv', header=['Student_ID', 'First_Name', 'Last_Name', 'Time_Of_Attendance', 'Date_Of_Attendance', 'Attendance_Status'], index=False)
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
        attendance_file = pd.read_csv("C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv")
        attendance_file.to_csv('C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv', header=['Student_ID', 'First_Name', 'Last_Name', 'Time_Of_Attendance', 'Date_Of_Attendance', 'Attendance_Status'], index=False)
        # updating the column value data
        for student_ids in attendance_file['Student_ID']:
            attendance_file.loc[student_ids-1, 'Attendance_Status'] = 'Present'

        # writing into the file
        attendance_file.to_csv("C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv", index=False)
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def mark_all_absent_button(self):
        # reading the csv file
        attendance_file = pd.read_csv("C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv")
        attendance_file.to_csv('C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv', header=['Student_ID', 'First_Name', 'Last_Name', 'Time_Of_Attendance', 'Date_Of_Attendance', 'Attendance_Status'], index=False)
        # updating the column value data
        for student_ids in attendance_file['Student_ID']:
            attendance_file.loc[student_ids-1, 'Attendance_Status'] = 'Absent'

        # writing into the file
        attendance_file.to_csv("C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv", index=False)
        self.fetchData()
# ------------------------------------------------------------------------------------------------------------------------------------------#
    def update_attendance_button(self):
        if self.var_student_ID=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_time_of_attendance.get()=="" or self.var_date_of_attendance.get()=="" or self.var_attendance_status.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                attendance_file = pd.read_csv("C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv")
                attendance_file.to_csv('C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv', header=['Student_ID', 'First_Name', 'Last_Name', 'Time_Of_Attendance', 'Date_Of_Attendance', 'Attendance_Status'], index=False)

                attendance_file.loc[self.var_student_ID[0]-1, 'First_Name'] = self.var_first_name.get()
                attendance_file.loc[self.var_student_ID[0]-1, 'Last_Name'] = self.var_last_name.get()
                attendance_file.loc[self.var_student_ID[0]-1, 'Time_Of_Attendance'] = self.var_time_of_attendance.get()
                attendance_file.loc[self.var_student_ID[0]-1, 'Date_Of_Attendance'] = self.var_date_of_attendance.get()
                attendance_file.loc[self.var_student_ID[0]-1, 'Attendance_Status'] = self.var_attendance_status.get()

                attendance_file.to_csv("C:/Users/utkarshjain120/Source/Repos/IREG-Image-Registartion-Based-Attendance-Mangement-System/IREG_Main_Menu/Attendance_Registers/Attendance.csv", index=False)
                self.fetchData()
                self.clear_all_button()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_time_of_attendance.set(""),
        self.var_date_of_attendance.set(""),
        self.var_attendance_status.set("")



# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Show_Attendance(root)
    root.mainloop()
