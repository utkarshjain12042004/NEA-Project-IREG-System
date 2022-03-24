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

class Settings:
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
        Settings_lbl= Label(mainFrame, text="Settings", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Settings_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=438, y=277, width=400, height=200) # Specifying the coordinates along with the dimensions of the frame

        #======================================== Adding in the buttons ========================================#
        # Train Data Button
        train_data_button = Button(Button_Frame, text="Train Data", cursor="hand2", command=self.train_data_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        train_data_button.place(x=5,y=5, width=387, height=90)

        # Student Faces
        student_faces_Button =  Button(Button_Frame, text="Student Faces", cursor="hand2", command=self.student_faces_button, font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        student_faces_Button.place(x=5,y=100, width=387, height=90)
        #=======================================================================================================#
#                                                            END OF UI DESIGN
#===========================================================================================================================================#
#############################################################################################################################################
#===========================================================================================================================================#
#                                                      BUTTON IMPLEMENTATION FUNCTIONS
# ------------------------------------------------------------------------------------------------------------------------------------------#
    # Function for adding in the student faces to a file on the computer
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
# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Settings(root)
    root.mainloop()