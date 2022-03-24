# Importing all the required library modules to create the UI
from tkinter import *
from tkinter import ttk

class Add_New_Teacher_Profile:
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
        Add_New_Teacher_Profile_lbl= Label(mainFrame, text="Add New Teacher Profile", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Add_New_Teacher_Profile_lbl.place(x=2, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Button Frame
        Button_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=5, y=612, width=1257, height=133) # Specifying the coordinates along with the dimensions of the frame

        # ======================================================================================================================================== #
        # Student Information frame: This frame will contain all the fields asking for information related to the student
        Teacher_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Teacher Details", font=("Segoe UI Variable", 12, "bold"))
        Teacher_Information_Frame.place(x=225, y=206, width=826, height=200) # Specifying the coordinates along with the dimensions of the frame
        # =================================================================== #
        # Adding in the teacher related text boxes and labels
        # Adding a teacher Id label and textbox
        teacherID_label = Label(Teacher_Information_Frame, text = "Teacher ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        teacherID_label.grid(row=0, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label

        teacherID_textbox = ttk.Entry(Teacher_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"))
        teacherID_textbox.grid(row=0, column=1, padx=(25,5), pady=17, sticky=W)# Specifying the location of the text box

        # Adding a subject taught label and combobox
        subject_taught_label = Label(Teacher_Information_Frame, text = "Subject Taught: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        subject_taught_label.grid(row=0, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label

        subject_taught_combobox=ttk.Combobox(Teacher_Information_Frame, width=23, font=("Segoe UI Variable", 12, "bold"), state="readonly")
        # The above line creates the combo box and makes it read only. The user will not be able to type in this box
        subject_taught_combobox["values"] = ("Select", "001", "002", "003", "004") # Adding in the values to be shown in the drop down list
        subject_taught_combobox.current(0) # Specifying the default item to be shown
        subject_taught_combobox.grid(row=0, column=3, padx=(25,5), pady=17, sticky=W) # Specifying the location of the combo box

        # Adding a teacher Email label and textbox
        teacher_email_label = Label(Teacher_Information_Frame, text = "Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        teacher_email_label.grid(row=1, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label
      
        teacher_email_textbox = ttk.Entry(Teacher_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"))
        teacher_email_textbox.grid(row=1, column=1, padx=(25,5), pady=17, sticky=W)# Specifying the location of the text box
      
        # Adding a first name label and textbox
        first_name_label = Label(Teacher_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        first_name_label.grid(row=1, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label

        first_name_textbox = ttk.Entry(Teacher_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"))
        first_name_textbox.grid(row=1, column=3, padx=(25,5), pady=17, sticky=W)# Specifying the location of the text box

        # Adding a last label and textbox
        last_name_label = Label(Teacher_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        last_name_label.grid(row=2, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label
      
        last_name_textbox = ttk.Entry(Teacher_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"))
        last_name_textbox.grid(row=2, column=1, padx=(25,5), pady=17, sticky=W)# Specifying the location of the text box

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Teacher_Information_Frame, text = "Date of Birth: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        date_of_birth_label.grid(row=2, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the location of the label

        date_of_birth_textbox = ttk.Entry(Teacher_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"))
        date_of_birth_textbox.grid(row=2, column=3, padx=(25,5), pady=17, sticky=W)# Specifying the location of the text box

        #======================================== Adding in the buttons ========================================#
        # Add New Student Profile Button
        add_new_student_Button = Button(Button_Frame, text="Add New Teacher Profile", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=31, height=3)
        add_new_student_Button.grid(row=0, column=0, padx=(21, 10), pady=(20, 10)) # Specifying the coordinates along with the dimensions of the frame

        # Clear All Fields Button
        clear_all_fields_Button = Button(Button_Frame, text="Clear All Fields", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=31, height=3)
        clear_all_fields_Button.grid(row=0, column=1, padx=(21, 10), pady=(20, 10)) # Specifying the coordinates along with the dimensions of the frame
       
        # Back to Student Account Management Button
        back_to_account_management_Button = Button(Button_Frame, text="Back to Teacher Account Management", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White", width=31, height=3)
        back_to_account_management_Button.grid(row=0, column=2, padx=(21, 10), pady=(20, 10)) # Specifying the coordinates along with the dimensions of the frame

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Add_New_Teacher_Profile(root)
    root.mainloop()
