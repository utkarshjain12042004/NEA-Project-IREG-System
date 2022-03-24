# Importing all the required library modules to create the UI
from tkinter import *
from tkinter import ttk

class Start_Attendance:
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
        Start_Attendance_lbl= Label(mainFrame, text="Start Attendance", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Start_Attendance_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        #=======================================================================================================#
        # Year Group Frame
        Year_Group_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Year_Group_Frame.place(x=501, y=358, width=268, height=39) # Specifying the coordinates along with the dimensions of the frame

        # ===================== Adding the label and combo box ==================== #
        # Adding a subject taught label and combobox
        year_group_label = Label(Year_Group_Frame, text = "Year Group: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        year_group_label.grid(row=0, column=0, padx=5, pady=5, sticky=W) # Specifying the location of the label

        year_group_combobox=ttk.Combobox(Year_Group_Frame, width=13, font=("Segoe UI Variable", 12, "bold"), state="readonly")
        # The above line creates the combo box and makes it read only. The user will not be able to type in this box
        year_group_combobox["values"] = ("-- Year Group --", "Yr 11", "L6", "U6") # Adding in the values to be shown in the drop down list
        year_group_combobox.current(0) # Specifying the default item to be shown
        year_group_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=W) # Specifying the location of the combo box
        #=======================================================================================================#
        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=501, y=397, width=268, height=39) # Specifying the coordinates along with the dimensions of the frame
        # ===================== Adding the button ==================== #
        ok_button = Button(Button_Frame, text="Ok", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        ok_button.place(x=2,y=2, width=261, height=32)

    def Start_Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Start_Attendance(self.new_window)
        self.root.withdraw()


# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Start_Attendance(root)
    root.mainloop()