# Importing all the required library modules to create the UI
from tkinter import *
from tkinter import ttk
import mysql.connector

class Timetable:
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
        Timetable_lbl= Label(mainFrame, text="Timetable", font=("Segoe UI Variable", 45, "bold"), bg="White", fg="Black")
        Timetable_lbl.place(x=1, y=5, width=1270, height=75) # Specifying the coordinates along with the dimensions of the frame

        # Period Frame
        Period_Frame =  LabelFrame(mainFrame, bd = 2, bg = "White", relief = RIDGE, text = "Timetable", font = ("Segoe UI Variable", 12, "bold"))
        Period_Frame.place(x = 5, y = 81, width = 1260, height = 663)

        # Adding the headings to the rows and columns
        # Adding the headings to the columns
        # Monday Label
        Monday_label = Label(Period_Frame, text = "Monday", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID, height=4)
        Monday_label.grid(row = 0, column = 1,sticky = NSEW)

        # Tuesday Label
        Tuesday_label = Label(Period_Frame, text = "Tuesday", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID, height=4)
        Tuesday_label.grid(row = 0, column = 2,sticky = NSEW)

        # Wednesday Label
        Wednesday_label = Label(Period_Frame, text = "Wednesday", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID, height=4)
        Wednesday_label.grid(row = 0, column = 3,sticky = NSEW)

        # Thurday Label
        Thursday_label = Label(Period_Frame, text = "Thursday", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID, height=4)
        Thursday_label.grid(row = 0, column = 4,sticky = NSEW)

        # Friday Label
        Friday_label = Label(Period_Frame, text = "Friday", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID, height=4)
        Friday_label.grid(row = 0, column = 5,sticky = NSEW)

        # Adding the headings to the rows
        # Label for period 1
        Period_Number_One_label = Label(Period_Frame, text = "1", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID, width=3)
        Period_Number_One_label.grid(row = 1, column = 0, padx=(8,0), sticky = NSEW)

        # Label for period 2
        Period_Number_Two_label = Label(Period_Frame, text = "2", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID, width=3)
        Period_Number_Two_label.grid(row = 2, column = 0, padx=(8,0),sticky = NSEW)

        # Label for period 3
        Period_Number_Three_label = Label(Period_Frame, text = "3", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID, width=3)
        Period_Number_Three_label.grid(row = 3, column = 0, padx=(8,0), sticky = NSEW)

        # Label for period 4
        Period_Number_Four_label = Label(Period_Frame, text = "4", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID, width=3)
        Period_Number_Four_label.grid(row = 4, column = 0, padx=(8,0), sticky = NSEW)

        # Label for period 5
        Period_Number_Five_label = Label(Period_Frame, text = "5", font = ("Segoe UI Variable", 12, "bold"), bg = "White", bd=2, relief=SOLID)
        Period_Number_Five_label.grid(row = 5, column = 0, padx=(8,0), sticky = NSEW)

        # Establishing the connection between the code file and the database
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "utkarshjain120", database = "mydb")
        my_cursor = conn.cursor()

        # Getting the information from the timetable table. 
        my_cursor.execute("SELECT * FROM tbl_timetable ORDER BY Day, From_Time")
        timetable_data = my_cursor.fetchall() # Storing the details in the array timetable
        
        period_counter = 0
        while period_counter < 25:
            day = str(timetable_data[period_counter][1])
            from_time = str(timetable_data[period_counter][2])

            subject_ID = timetable_data[period_counter][4]
            teacher_ID = timetable_data[period_counter][5]

            subject_name_query = "SELECT Subject_Name FROM tbl_subject WHERE Subject_ID = %s"
            my_cursor.execute(subject_name_query, (subject_ID,))
            subject_name = my_cursor.fetchall()[0][0]

            teacher_last_name_query = "SELECT Last_Name FROM tbl_teacher WHERE Teacher_ID = %s"
            my_cursor.execute(teacher_last_name_query, (teacher_ID,))
            teacher_last_name = my_cursor.fetchall()[0][0]

            # Getting the correct coordinates of where the data should be added
            # Setting the variables rows and columns to 0
            row = 0
            column = 0
            # Using if statements to determine the correct location
            if day == "Monday" and from_time == "8:40:00":
                row = 1
                column = 1
            elif day == "Monday" and from_time == "9:40:00":
                row = 2
                column = 1
            elif day == "Monday" and from_time == "11:00:00":
                row = 3
                column = 1
            elif day == "Monday" and from_time == "12:00:00":
                row = 4
                column = 1
            elif day == "Monday" and from_time == "13:45:00":
                row = 5
                column = 1
            elif day == "Tuesday" and from_time == "8:40:00":
                row = 1
                column = 2
            elif day == "Tuesday" and from_time == "9:40:00":
                row = 2
                column = 2
            elif day == "Tuesday" and from_time == "11:00:00":
                row = 3
                column = 2
            elif day == "Tuesday" and from_time == "12:00:00":
                row = 4
                column = 2
            elif day == "Tuesday" and from_time == "13:45:00":
                row = 5
                column = 2
            elif day == "Wednesday" and from_time == "8:40:00":
                row = 1
                column = 3
            elif day == "Wednesday" and from_time == "9:40:00":
                row = 2
                column = 3
            elif day == "Wednesday" and from_time == "11:00:00":
                row = 3
                column = 3
            elif day == "Wednesday" and from_time == "12:00:00":
                row = 4
                column = 3
            elif day == "Wednesday" and from_time == "13:45:00":
                row = 5
                column = 3
            elif day == "Thursday" and from_time == "8:40:00":
                row = 1
                column = 4
            elif day == "Thursday" and from_time == "9:40:00":
                row = 2
                column = 4
            elif day == "Thursday" and from_time == "11:00:00":
                row = 3
                column = 4
            elif day == "Thursday" and from_time == "12:00:00":
                row = 4
                column = 4
            elif day == "Thursday" and from_time == "13:45:00":
                row = 5
                column = 4
            elif day == "Friday" and from_time == "8:40:00":
                row = 1
                column = 5
            elif day == "Friday" and from_time == "9:40:00":
                row = 2
                column = 5
            elif day == "Friday" and from_time == "11:00:00":
                row = 3
                column = 5
            elif day == "Friday" and from_time == "12:00:00":
                row = 4
                column = 5
            elif day == "Friday" and from_time == "13:45:00":
                row = 5
                column = 5

            period_Button = Button(Period_Frame, text = f"""{subject_name}\n{teacher_last_name}""", cursor = "hand2", font = ("Segoe UI Variable", 12, "bold"), bg = "White", fg = "Black", width = 23, height = 5, bd=2, relief = SOLID)
            period_Button.grid(row = row, column = column)

            period_counter += 1

        conn.commit()
        conn.close()

        #=======================================================================================================#
# This piece of code helps in calling class Face_Recognition_System
if __name__=="__main__":
    root = Tk()
    obj = Timetable(root)
    root.mainloop()
