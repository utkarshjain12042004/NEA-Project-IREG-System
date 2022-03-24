# Importing all the required library modules to create the UI
from tkinter import *
from tkinter import ttk

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
        Show_Attendance_lbl= Label(mainFrame, text="Show Attendance", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Show_Attendance_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Button Frame
        Button_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=885, y=85, width=380, height=220) # Specifying the coordinates along with the dimensions of the frame

        # ======================================================================================================================================== #
        # student Information frame: This frame will contain all the fields asking for information related to the student
        Attendance_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Teacher Details", font=("Segoe UI Variable", 12, "bold"))
        Attendance_Frame.place(x=5, y=85, width=875, height=220)
        # =================================================================== #
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        studentID_label = Label(Attendance_Frame, text = "Student ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        studentID_label.grid(row=0, column=0, padx=(25,20), pady=18, sticky=W) # Specifying the coordinates of the label

        studentID_textbox = ttk.Entry(Attendance_Frame, width=22, font=("Segoe UI Variable", 12, "bold"),)
        studentID_textbox.grid(row=0, column=1, padx=5, pady=18, sticky=W) # Specifying the coordinates of the textbox

        # Adding a student Email label and textbox
        attendance_date_label = Label(Attendance_Frame, text = "Attendance Date: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        attendance_date_label.grid(row=0, column=2, padx=(35,20), pady=18, sticky=W) # Specifying the coordinates of the label

        attendance_date_textbox = ttk.Entry(Attendance_Frame, width=22, font=("Segoe UI Variable", 12, "bold"),)
        attendance_date_textbox.grid(row=0, column=3, padx=5, pady=18, sticky=W) # Specifying the coordinates of the textbox

        # Adding a first name label and textbox
        first_name_label = Label(Attendance_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        first_name_label.grid(row=2, column=0, padx=(25,20), pady=18, sticky=W) # Specifying the coordinates of the label

        first_name_textbox = ttk.Entry(Attendance_Frame, width=22, font=("Segoe UI Variable", 12, "bold"),)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=18, sticky=W) # Specifying the coordinates of the textbox

        # Adding a last label and textbox
        last_name_label = Label(Attendance_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        last_name_label.grid(row=2, column=2, padx=(35,20), pady=18, sticky=W) # Specifying the coordinates of the label
       
        last_name_textbox = ttk.Entry(Attendance_Frame, width=22, font=("Segoe UI Variable", 12, "bold"),)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=18, sticky=W) # Specifying the coordinates of the textbox

        # Adding a student Date Of hiring label and textbox
        attendance_status_label = Label(Attendance_Frame, text = "Attendance Status: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        attendance_status_label.grid(row=3, column=0, padx=(25,6), pady=18, sticky=W) # Specifying the coordinates of the label
       
        attendance_status_combobox=ttk.Combobox(Attendance_Frame, width=20, font=("Segoe UI Variable", 12, "bold"), state="readonly")
        # The above line creates the combo box and makes it read only. The user will not be able to type in this box
        attendance_status_combobox["values"] = ("--Attendance Status--", "Present", "Absent", "Late") # Adding in the values to be shown in the drop down list
        attendance_status_combobox.current(0) # Specifying the default item to be shown
        attendance_status_combobox.grid(row=3, column=1, padx=(6,5), pady=17, sticky=W) # Specifying the location of the combo box

        # Adding a date of birth label and textbox
        time_of_attendance_label = Label(Attendance_Frame, text = "Time of Attendance: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        time_of_attendance_label.grid(row=3, column=2, padx=(35,20), pady=18, sticky=W) # Specifying the coordinates of the label

        time_of_attendance_textbox = ttk.Entry(Attendance_Frame,width=22, font=("Segoe UI Variable", 12, "bold"),)
        time_of_attendance_textbox.grid(row=3, column=3, padx=5, pady=18, sticky=W) # Specifying the coordinates of the textbox

        # ====================================================================================================================================== #
        # Adding in the buttons to the button frame
        # Update Student Attendance Button
        update_attendance_Button = Button(Button_Frame, text="Update Student Attendance", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        update_attendance_Button.place(x=5, y=5, height=65, width=365) # Specifying the coordinates along with the dimensions of the button

        # Clear All Fields Button
        clear_all_fields_Button = Button(Button_Frame, text="Clear All Fields", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        clear_all_fields_Button.place(x=5, y=75, height=65, width=365) # Specifying the coordinates along with the dimensions of the button
       
        # Back to student Account Management Button
        back_to_view_attendance_Button = Button(Button_Frame, text="Back to Previous Page", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        back_to_view_attendance_Button.place(x=5, y=145, height=65, width=365) # Specifying the coordinates along with the dimensions of the button

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

        self.attendance_table.pack(fill=BOTH, expand=1)

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Show_Attendance(root)
    root.mainloop()
