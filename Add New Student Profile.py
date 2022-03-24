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

class Add_New_Student_Profile:
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
        Add_New_Student_Profile_lbl= Label(mainFrame, text="Add New Student Profile", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Add_New_Student_Profile_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

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

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=115, y=489, width=1045, height=245) # Specifying the coordinates along with the dimensions of the frame

        # ======================================================================================================================================== #
        # Student Information frame: This frame will contain all the fields asking for information related to the student
        Student_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Student Details", font=("Segoe UI Variable", 12, "bold"))
        Student_Information_Frame.place(x=5, y=85, width=826, height=200)
        # =================================================================== #
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
        studentID_label = Label(Student_Information_Frame, text = "Student ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        studentID_label.grid(row=0, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        #studentID_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        #studentID_textbox.grid(row=0, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        self.new_studentID_lbl = Label(Student_Information_Frame, text=self.var_student_ID, font=("Segoe UI Variable", 12, "bold"), bg = "White")
        self.new_studentID_lbl.grid(row=0, column=1, padx=(15,5), pady=15, sticky=W)

        # Adding a Student Email label and textbox
        student_email_label = Label(Student_Information_Frame, text = "Student Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        student_email_label.grid(row=0, column=2, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label
       
        student_email_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_student_email)
        student_email_textbox.grid(row=0, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a first name label and textbox
        first_name_label = Label(Student_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        first_name_label.grid(row=2, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        first_name_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_first_name)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a last label and textbox
        last_name_label = Label(Student_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        last_name_label.grid(row=2, column=2, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label
       
        last_name_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_last_name)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a Student Date Of Admission label and textbox
        date_of_admission_label = Label(Student_Information_Frame, text = "Date Of Admission: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        date_of_admission_label.grid(row=3, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label
       
        date_of_admission_textbox = ttk.Entry(Student_Information_Frame,width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_date_of_admission)        
        date_of_admission_textbox.grid(row=3, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Student_Information_Frame, text = "Date of Birth: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        date_of_birth_label.grid(row=3, column=2, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        date_of_birth_textbox = ttk.Entry(Student_Information_Frame,width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_date_of_birth)
        date_of_birth_textbox.grid(row=3, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # ======================================================================================================================================== #
        # Parent Inforamtion Frame: This frame will contain all the fields asking for information related to the parents
        Parent_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Parent Details", font=("Segoe UI Variable", 12, "bold"))
        Parent_Information_Frame.place(x=5, y=300, width=826, height=150)
        # =================================================================== #
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        father_name_label = Label(Parent_Information_Frame, text = "Father's Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        father_name_label.grid(row=0, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label

        father_name_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_father_name)
        father_name_textbox.grid(row=0, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a Student Email label and textbox
        father_email_label = Label(Parent_Information_Frame, text = "Father's Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        father_email_label.grid(row=0, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label
       
        father_email_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_father_email)
        father_email_textbox.grid(row=0, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a first name label and textbox
        mother_name_label = Label(Parent_Information_Frame, text = "Mother's Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        mother_name_label.grid(row=2, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label

        mother_name_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_mother_name)
        mother_name_textbox.grid(row=2, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a last label and textbox
        mother_email_label = Label(Parent_Information_Frame, text = "Mother's Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        mother_email_label.grid(row=2, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label
       
        mother_email_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"), textvariable=self.var_mother_email)
        mother_email_textbox.grid(row=2, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # ======================================================================================================================================== #
        # Capture Student Face Frame: This frame will be blank in the beginning but after the user clicks on the capture 
        # student face button, the live video footage will be embedded in the frame
        Capture_Student_Face_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Capture Student Face", font=("Segoe UI Variable", 12, "bold"))
        Capture_Student_Face_Frame.place(x=835, y=85, width=430, height=365)

        #======================================== Adding in the buttons ========================================#
        # Add New Student Profile Button
        add_new_student_Button = Button(Button_Frame, text="Add New Student Profile", cursor="hand2", command = self.add_student_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=40, height=3)
        add_new_student_Button.grid(row=0, column=0, padx=(20, 10), pady=(20, 10)) # Specifying the coordinates along with the dimensions of the frame

        # Capture Student Face
        capture_student_face_Button =  Button(Button_Frame, text="Capture Student Face", cursor="hand2", command = self.capture_face_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=40, height=3)
        capture_student_face_Button.grid(row=0, column=1, padx=(10, 20), pady=(20, 10)) # Specifying the coordinates along with the dimensions of the frame

        # Clear All Fields Button
        clear_all_fields_Button = Button(Button_Frame, text="Clear All Fields", cursor="hand2", command = self.clear_all_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=40, height=3)
        clear_all_fields_Button.grid(row=1, column=0, padx=(20, 10), pady=(10, 20)) # Specifying the coordinates along with the dimensions of the frame
       
        # Back to Student Account Management Button
        back_to_student_account_management_Button = Button(Button_Frame, text="Back to Student Account Management", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=40, height=3)
        back_to_student_account_management_Button.grid(row=1, column=1, padx=(10, 20), pady=(10, 20)) # Specifying the coordinates along with the dimensions of the frame
    #                                                            END OF UI DESIGN
    #===========================================================================================================================================#
    #############################################################################################################################################
    #===========================================================================================================================================#
    #                                                      BUTTON IMPLEMENTATION FUNCTIONS
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for adding in the data when the user clicks on the add student button
    def add_student_button(self):
        if self.var_student_ID=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
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
                
                print("After Add classes")
                conn.commit()
                conn.close()
                self.var_student_ID = f"{int(self.var_student_ID) + 1}"
                self.new_studentID_lbl.config(text=self.var_student_ID)
                messagebox.showinfo("Success", "Student details have been added succesfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=root)
    # ------------------------------------------------------------------------------------------------------------------------------------------#
    # Clear All Fields button Implementation
    def clear_all_button(self):
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
    # Capture Student Face button implementation
    def capture_face_button(self):
        # Validation that all fields are filled up
        if self.var_student_ID=="" or self.var_student_email.get()=="" or self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_date_of_admission.get()=="" or self.var_date_of_birth.get()=="" or self.var_father_name.get()=="" or self.var_father_email.get()=="" or self.var_mother_name.get()=="" or self.var_mother_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            # Added a try box to get rid of any exceptions which might arise
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="utkarshjain120", database="mydb")
                my_cursor = conn.cursor()
                # Selected all the data from the database and stored it in the variable student_profiles
                my_cursor.execute("SELECT * FROM tbl_student")
                student_profiles = my_cursor.fetchall()
                # We match the images to an id
                id=0
                # Therfore, we create a loop to manage the IDs
                for profile in student_profiles:
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
                    # Scalinng Factor = 1.3
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
                self.train_data_button()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    # ------------------------------------------------------------------------------------------------------------------------ #
    # Train the classifier using these face captures
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
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write("C:/Users/utkarshjain120/Desktop/IREG-Image-Registration-Based-Attendance-Mangement-System/Trained_Faces.xml")
        cv2.destroyWindow("Training")
        messagebox.showinfo("Train Face Data", "Datasets have been trained using the student faces")

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Add_New_Student_Profile(root)
    root.mainloop()