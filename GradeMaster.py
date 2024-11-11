from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox, ttk

class GradeMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GradeMaster")

        # Set window size and center it
        self.root.geometry("700x900")
        self.root.eval('tk::PlaceWindow . center')

        # Initialize database
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["grademaster_db"]
        self.students = self.db.students
        self.courses = self.db.courses

        # Set color scheme
        self.bg_color = "#ffffff"  # White background
        self.fg_color = "#000000"  # Black text
        self.highlight_color = "#4682b4"  # Blue highlight

        self.root.configure(bg=self.bg_color)

        # Define styles
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Bahnschrift", 10), background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TButton", font=("Bahnschrift", 10), background=self.highlight_color, foreground=self.fg_color, borderwidth=0, focusthickness=0)
        self.style.configure("TEntry", font=("Bahnschrift", 10), foreground=self.fg_color, fieldbackground=self.bg_color, borderwidth=0, focusthickness=0)
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabelframe", font=("Bahnschrift", 12, 'bold'), background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TLabelframe.Label", font=("Bahnschrift", 12, 'bold'), background=self.bg_color, foreground=self.fg_color)
        self.style.map("TButton", background=[("active", self.highlight_color)], foreground=[("active", self.fg_color)])

        # Create a main frame to center the content
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True)

        # Title Label
        self.title_label = ttk.Label(self.main_frame, text="GradeMaster", font=("Bahnschrift", 18, 'bold'), background=self.bg_color, foreground=self.highlight_color)
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        # Student Section
        self.student_frame = ttk.LabelFrame(self.main_frame, text="Student", padding=10)
        self.student_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.student_id_label = ttk.Label(self.student_frame, text="Student ID:")
        self.student_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.student_id_entry = ttk.Entry(self.student_frame, width=30)
        self.student_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.student_name_label = ttk.Label(self.student_frame, text="Student Name:")
        self.student_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.student_name_entry = ttk.Entry(self.student_frame, width=30)
        self.student_name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_student_button = ttk.Button(self.student_frame, text="Add Student", command=self.add_student)
        self.add_student_button.grid(row=2, columnspan=2, padx=5, pady=5)

        # Course Section
        self.course_frame = ttk.LabelFrame(self.main_frame, text="Course", padding=10)
        self.course_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.course_id_label = ttk.Label(self.course_frame, text="Course ID:")
        self.course_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.course_id_entry = ttk.Entry(self.course_frame, width=30)
        self.course_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.course_name_label = ttk.Label(self.course_frame, text="Course Name:")
        self.course_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.course_name_entry = ttk.Entry(self.course_frame, width=30)
        self.course_name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_course_button = ttk.Button(self.course_frame, text="Add Course", command=self.add_course)
        self.add_course_button.grid(row=2, columnspan=2, padx=5, pady=5)

        # Grade Section
        self.grade_frame = ttk.LabelFrame(self.main_frame, text="Grade", padding=10)
        self.grade_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.grade_student_id_label = ttk.Label(self.grade_frame, text="Student ID:")
        self.grade_student_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.grade_student_id_entry = ttk.Entry(self.grade_frame, width=30)
        self.grade_student_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.grade_course_id_label = ttk.Label(self.grade_frame, text="Course ID:")
        self.grade_course_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.grade_course_id_entry = ttk.Entry(self.grade_frame, width=30)
        self.grade_course_id_entry.grid(row=1, column=1, padx=5, pady=5)

        self.grade_label = ttk.Label(self.grade_frame, text="Grade:")
        self.grade_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.grade_entry = ttk.Entry(self.grade_frame, width=30)
        self.grade_entry.grid(row=2, column=1, padx=5, pady=5)

        self.record_grade_button = ttk.Button(self.grade_frame, text="Record Grade", command=self.record_grade)
        self.record_grade_button.grid(row=3, columnspan=2, padx=5, pady=5)

        # GPA Section
        self.gpa_frame = ttk.LabelFrame(self.main_frame, text="GPA", padding=10)
        self.gpa_frame.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.gpa_student_id_label = ttk.Label(self.gpa_frame, text="Student ID:")
        self.gpa_student_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.gpa_student_id_entry = ttk.Entry(self.gpa_frame, width=30)
        self.gpa_student_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.print_gpa_button = ttk.Button(self.gpa_frame, text="Print Student GPA", command=self.print_student_gpa)
        self.print_gpa_button.grid(row=1, columnspan=2, padx=5, pady=5)

        # Class Analytics Section
        self.analytics_frame = ttk.LabelFrame(self.main_frame, text="Class Analytics", padding=10)
        self.analytics_frame.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        self.print_analytics_button = ttk.Button(self.analytics_frame, text="Print Class Analytics", command=self.print_class_analytics)
        self.print_analytics_button.grid(row=0, columnspan=2, padx=5, pady=5)

    def add_student(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        if self.students.find_one({"student_id": student_id}):
            messagebox.showinfo("Error", f"Student with ID {student_id} already exists.")
        else:
            self.students.insert_one({"student_id": student_id, "name": student_name, "grades": []})
            messagebox.showinfo("Success", "Student added successfully.")

    def add_course(self):
        course_id = self.course_id_entry.get()
        course_name = self.course_name_entry.get()
        if self.courses.find_one({"course_id": course_id}):
            messagebox.showinfo("Error", f"Course with ID {course_id} already exists.")
        else:
            self.courses.insert_one({"course_id": course_id, "name": course_name})
            messagebox.showinfo("Success", "Course added successfully.")

    def record_grade(self):
        student_id = self.grade_student_id_entry.get()
        course_id = self.grade_course_id_entry.get()
        grade = self.grade_entry.get().upper()
        if not self.students.find_one({"student_id": student_id}):
            messagebox.showinfo("Error", "Invalid student ID.")
            return
        if not self.courses.find_one({"course_id": course_id}):
            messagebox.showinfo("Error", "Invalid course ID.")
            return
        if grade not in {'A', 'B', 'C', 'D', 'F'}:
            messagebox.showinfo("Error", "Invalid grade.")
            return
        student = self.students.find_one({"student_id": student_id})
        if len(student["grades"]) >= 6:
            messagebox.showinfo("Error", "A student cannot enroll in more than 6 courses.")
            return
        self.students.update_one(
            {"student_id": student_id},
            {"$push": {"grades": {"course_id": course_id, "grade": grade}}}
        )
        messagebox.showinfo("Success", "Grade recorded successfully.")

    def print_student_gpa(self):
        student_id = self.gpa_student_id_entry.get()
        student = self.students.find_one({"student_id": student_id})
        if not student:
            messagebox.showinfo("Error", "Invalid student ID.")
            return
        gpa = self.calculate_gpa(student["grades"])
        messagebox.showinfo("Student GPA", f"Student {student_id} GPA: {gpa:.2f}")

    def print_class_analytics(self):
        total_students = self.students.count_documents({})
        total_courses = self.courses.count_documents({})
        total_grades = sum([len(student['grades']) for student in self.students.find()])
        messagebox.showinfo("Class Analytics", f"Total Students: {total_students}\nTotal Courses: {total_courses}\nTotal Grades Recorded: {total_grades}")

    def calculate_gpa(self, grades):
        grade_points = {'A': 10.0, 'B': 9.0, 'C': 8.0, 'D': 7.0, 'F': 0.0}
        total_points = sum(grade_points[grade['grade']] for grade in grades)
        return total_points / len(grades) if grades else 0.0

def main():
    root = tk.Tk()
    app = GradeMasterApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()

client = MongoClient("mongodb://localhost:27017/")
print(client)

