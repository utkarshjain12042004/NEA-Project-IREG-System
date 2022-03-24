# Importing all the required library modules to create the UI
from tkinter import *
from tkinter import ttk

class Attendance_Method:
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
        Attendace_Method_lbl= Label(mainFrame, text="Attendance Method", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Attendace_Method_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=438, y=283, width=400, height=190) # Specifying the coordinates along with the dimensions of the frame

        #======================================== Adding in the buttons ========================================#
        # Teacher Account Management Button
        automated_attendance_Button = Button(Button_Frame, text="Automated Method", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        automated_attendance_Button.place(x=5,y=5, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

        # Student Account Management Button
        manual_attendance_Button =  Button(Button_Frame, text="Manual Method", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        manual_attendance_Button.place(x=5,y=69, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

        # Delete Student Profile Button
        back_to_view_attendance_Button = Button(Button_Frame, text="Back to View Attendance", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        back_to_view_attendance_Button.place(x=5,y=133, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Attendance_Method(root)
    root.mainloop()
