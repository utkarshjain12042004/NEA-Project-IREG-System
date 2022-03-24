# Importing all the required library modules to create the UI
from tkinter import *
from tkinter import ttk

class Account_Management:
    # This is the constructor of the class IREG_Main_Menu
    def __init__(self, root):
        self.root = root
        # Setting the dimensions of the window and the point where the window is displayed from
        self.root.geometry("1280x760+0+0")
        # Setting the property of resizing the widow to false
        self.root.resizable(width=False, height=False)
        self.root.title("IREG")

        # Main Frame: This will contain all the buttons
        mainFrame = Frame(bd=2, bg="White", relief = SOLID)
        mainFrame.place(x=2, y=2, width=1276, height=755) # Specifying the coordinates along with the dimensions of the frame

        # Label Frame
        Account_Management_lbl= Label(mainFrame, text="Account Management", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Account_Management_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=438, y=283, width=400, height=190) # Specifying the coordinates along with the dimensions of the frame

        #======================================== Adding in the buttons ========================================#
        # Teacher Account Management Button
        teacher_account_management_Button = Button(Button_Frame, text="Teacher Account Management", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        teacher_account_management_Button.place(x=5,y=5, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

        # Student Account Management Button
        student_account_management_Button =  Button(Button_Frame, text="Student Account Management", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        student_account_management_Button.place(x=5,y=69, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

        # Delete Student Profile Button
        back_to_main_menu_Button = Button(Button_Frame, text="Back to Main Menu", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        back_to_main_menu_Button.place(x=5,y=133, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Account_Management(root)
    root.mainloop()
