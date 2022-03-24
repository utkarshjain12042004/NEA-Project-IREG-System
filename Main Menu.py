# Importing all the required library modules to create the UI
from tkinter import *
from tkinter import ttk

class IREG_Main_Menu:
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
        Image_Registration_lbl= Label(mainFrame, text="IREG: Image Registration", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Image_Registration_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=438, y=202, width=400, height=325) # Specifying the coordinates along with the dimensions of the frame

        #======================================== Adding in the buttons ========================================#
        # Start Attendance Button
        start_Attendance_Button = Button(Button_Frame, text="Start Attendance", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        start_Attendance_Button.place(x=5,y=5, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

        # View Attendance
        view_Attendance_Button =  Button(Button_Frame, text="View Attendance", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        view_Attendance_Button.place(x=5,y=69, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

        # Account Management Button
        account_Management_Button = Button(Button_Frame, text="Account Management", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        account_Management_Button.place(x=5,y=133, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame
        
        # Settings Button
        settings_Button = Button(Button_Frame, text="Settings", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        settings_Button.place(x=5,y=197, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

        # Exit Button
        exit_Button = Button(Button_Frame, text="Exit", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        exit_Button.place(x=5,y=261, width=387, height=50) # Specifying the coordinates along with the dimensions of the frame

    # ===================================================================================== #
    # Adding in the functions which call other pages
    #def Start_Attendance_Button_Implementation(self):
    #    self.new_window = Toplevel(self.root) # Creating an instance of a toplevel
    #    self.app = Start_Attendance(self.new_window)
    #    self.root.withdraw() # Deleting the current window

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = IREG_Main_Menu(root)
    root.mainloop()