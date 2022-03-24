# Importing all the required library modules to create the UI
from tkinter import *
from tkinter import ttk

class Add_New_Student_Profile:
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
        Add_New_Student_Profile_lbl= Label(mainFrame, text="Update Student Profile", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Add_New_Student_Profile_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Button Frame
        Button_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Button_Frame.place(x=885, y=460, width=380, height=290) # Specifying the coordinates along with the dimensions of the frame

        # ======================================================================================================================================== #
        # Student Information frame: This frame will contain all the fields asking for information related to the student
        Student_Information_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Student Details", font=("Segoe UI Variable", 12, "bold"))
        Student_Information_Frame.place(x=5, y=85, width=826, height=200)
        # =================================================================== #
        # Adding in the student related text boxes and labels
        # Adding a student id label and textbox
        studentID_label = Label(Student_Information_Frame, text = "Student ID: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        studentID_label.grid(row=0, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        studentID_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        studentID_textbox.grid(row=0, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a Student Email label and textbox
        student_email_label = Label(Student_Information_Frame, text = "Student Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        student_email_label.grid(row=0, column=2, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label
       
        student_email_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        student_email_textbox.grid(row=0, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a first name label and textbox
        first_name_label = Label(Student_Information_Frame, text = "First Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        first_name_label.grid(row=2, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        first_name_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        first_name_textbox.grid(row=2, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a last label and textbox
        last_name_label = Label(Student_Information_Frame, text = "Last Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        last_name_label.grid(row=2, column=2, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label
       
        last_name_textbox = ttk.Entry(Student_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        last_name_textbox.grid(row=2, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a Student Date Of Admission label and textbox
        date_of_admission_label = Label(Student_Information_Frame, text = "Date Of Admission: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        date_of_admission_label.grid(row=3, column=0, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label
       
        date_of_admission_textbox = ttk.Entry(Student_Information_Frame,width=25, font=("Segoe UI Variable", 12, "bold"),)
        date_of_admission_textbox.grid(row=3, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a date of birth label and textbox
        date_of_birth_label = Label(Student_Information_Frame, text = "Date of Birth: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        date_of_birth_label.grid(row=3, column=2, padx=(15,5), pady=15, sticky=W) # Specifying the coordinates of the label

        date_of_birth_textbox = ttk.Entry(Student_Information_Frame,width=25, font=("Segoe UI Variable", 12, "bold"),)
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

        father_name_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        father_name_textbox.grid(row=0, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a Student Email label and textbox
        father_email_label = Label(Parent_Information_Frame, text = "Father's Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        father_email_label.grid(row=0, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label
       
        father_email_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        father_email_textbox.grid(row=0, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a first name label and textbox
        mother_name_label = Label(Parent_Information_Frame, text = "Mother's Name: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        mother_name_label.grid(row=2, column=0, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label

        mother_name_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        mother_name_textbox.grid(row=2, column=1, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # Adding a last label and textbox
        mother_email_label = Label(Parent_Information_Frame, text = "Mother's Email: ", font=("Segoe UI Variable", 12, "bold"), bg = "White")
        mother_email_label.grid(row=2, column=2, padx=(25,5), pady=17, sticky=W) # Specifying the coordinates of the label
       
        mother_email_textbox = ttk.Entry(Parent_Information_Frame, width=25, font=("Segoe UI Variable", 12, "bold"),)
        mother_email_textbox.grid(row=2, column=3, padx=5, pady=15, sticky=W) # Specifying the coordinates of the textbox

        # ======================================================================================================================================== #
        # Capture Student Face Frame: This frame will be blank in the beginning but after the user clicks on the capture 
        # student face button, the live video footage will be embedded in the frame
        Capture_Student_Face_Frame= LabelFrame(mainFrame, bd=2, bg="White", relief=RIDGE, text="Capture Student Face", font=("Segoe UI Variable", 12, "bold"))
        Capture_Student_Face_Frame.place(x=835, y=85, width=430, height=365)

        #======================================== Adding in the buttons ========================================#
        # Add New Student Profile Button
        add_new_student_Button = Button(Button_Frame, text="Add New Student Profile", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        add_new_student_Button.place(x=5, y=5, height=65, width=365) # Specifying the coordinates along with the dimensions of the frame

        # Capture Student Face
        capture_student_face_Button =  Button(Button_Frame, text="Capture Student Face", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        capture_student_face_Button.place(x=5, y=75, height=65, width=365) # Specifying the coordinates along with the dimensions of the frame

        # Clear All Fields Button
        clear_all_fields_Button = Button(Button_Frame, text="Clear All Fields", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        clear_all_fields_Button.place(x=5, y=145, height=65, width=365) # Specifying the coordinates along with the dimensions of the frame
       
        # Back to Student Account Management Button
        back_to_student_account_management_Button = Button(Button_Frame, text="Back to Previous Page", cursor="hand2", font=("Segoe UI Variable", 15, "bold"), bg="Black", fg="White")
        back_to_student_account_management_Button.place(x=5, y=216, height=65, width=365) # Specifying the coordinates along with the dimensions of the frame

        # ======================================================================================================================================== #
        # Search Frame: This frame will contain the search system which will be show the user all the student profiles created
        Search_Frame= Frame(mainFrame, bd=2, bg="White", relief=RIDGE)
        Search_Frame.place(x=5, y=460, width=875, height=285)

        # Adding a search bar
        search_label = Label(Search_Frame, text="Search By:", font=("Segoe UI Variable", 12, "bold"), bg="White", fg="Black")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Adding a Search by combo box
        search_combobox=ttk.Combobox(Search_Frame, font=("Segoe UI Variable", 12, "bold"), width=15, state="readonly")
        search_combobox["values"] = ("Select", "Student ID", "First Name", "LastName","Date of Birth", "Date Of Admission")
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
        Table_Frame.place(x=0, y=45, width=870, height=235)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(Table_Frame, column=("std_ID", "first_name", "last_name", "email", "date_of_admission", "date_of_birth", "father_name", "father_email", "mother_name", "mother_email"), 
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("std_ID", text="Student ID")
        self.student_table.heading("first_name", text="First Name")
        self.student_table.heading("last_name", text="Last Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("date_of_admission", text="Date Of Admission")
        self.student_table.heading("date_of_birth", text="Date Of Birth")
        self.student_table.heading("father_name", text="Father's Name")
        self.student_table.heading("father_email", text="Father Email")
        self.student_table.heading("mother_name", text="Mother's Name")
        self.student_table.heading("mother_email", text="Mother Email")
        self.student_table["show"] = "headings"
        
        self.student_table.column("std_ID", width=68)
        self.student_table.column("first_name", width=130)
        self.student_table.column("last_name", width=130)
        self.student_table.column("email", width=130)
        self.student_table.column("date_of_admission", width=120)
        self.student_table.column("date_of_birth", width=120)
        self.student_table.column("father_name", width=130) 
        self.student_table.column("father_email", width=150)
        self.student_table.column("mother_name", width=130)
        self.student_table.column("mother_email", width=100)

        self.student_table.pack(fill=BOTH, expand=1)

# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Add_New_Student_Profile(root)
    root.mainloop()
