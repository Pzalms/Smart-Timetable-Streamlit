import sqlite3
import streamlit as st

class Course:
    def __init__(self, name, code, credit, course_type, semester, duration):
        self.name = name
        self.code = code
        self.credit = credit
        self.course_type = course_type
        self.semester = semester
        self.duration = duration

    def _establish_connection(self):
        return sqlite3.connect('timetable.db')

    def add_course(self):
        data = (self.name, self.code, self.credit, self.course_type, self.semester, self.duration)
        query = """INSERT INTO course
                   (PROGRAM_NAME, COURSE_CODE, COURSE_CREDIT, COURSE_TYPE, COURSE_SEM, COURSE_DURATION)
                   VALUES
                   (?, ?, ?, ?, ?, ?)"""

        connection = self._establish_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()

    def delete_course(self, course_code):
        query_delete_teacher_course = "DELETE FROM teacher_course_allocation WHERE COURSE_CODE = ?"
        query_delete_course = "DELETE FROM course WHERE COURSE_CODE = ?"

        connection = self._establish_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute(query_delete_teacher_course, (course_code,))
            cursor.execute(query_delete_course, (course_code,))
            connection.commit()

    def edit_course(self, course_code, new_program_name, new_credit, new_course_type, new_semester, new_duration):
        query = """UPDATE course
                   SET PROGRAM_NAME=?, COURSE_CREDIT=?, COURSE_TYPE=?, COURSE_SEM=?, COURSE_DURATION=?
                   WHERE COURSE_CODE=?"""

        data = (new_program_name, new_credit, new_course_type, new_semester, new_duration, course_code)

        connection = self._establish_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()

    @staticmethod
    def get_all_courses():
        query = "SELECT * FROM course"
        connection = sqlite3.connect('timetable.db')
        with connection:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()

def add_course_ui():
    st.header("ADD COURSE")
    name = st.text_input("Enter Program Name")
    code = st.text_input("Enter Course Code")
    credit = st.number_input("Enter Course Credit", min_value=1)
    duration = st.number_input("Enter Course Duration (Hours)", min_value=1, max_value=4)
    course_type = st.radio("Select Course Type", ["Theory", "Practical"])
    semester = st.number_input("Enter Course Semester", min_value=1)

    if st.button("Add Course"):
        course_instance = Course(name=name, code=code, credit=credit, course_type=course_type, semester=semester, duration=duration)
        course_instance.add_course()
        st.success("Course added successfully!")

def delete_course_ui():
    st.header("DELETE COURSE")
    all_courses = Course.get_all_courses()
    available_programs = list(set([course[0] for course in all_courses]))

    selected_program = st.selectbox("Select Program Name", available_programs)
    available_semesters = list(set([course[4] for course in all_courses if course[0] == selected_program]))

    selected_semester = st.selectbox("Select Semester", available_semesters)
    program_semester_courses = [course for course in all_courses if course[0] == selected_program and course[4] == selected_semester]
    available_course_codes = [course[1] for course in program_semester_courses]

    delete_code = st.selectbox("Select Course Code to Delete", available_course_codes)

    if st.button("Delete Course"):
        course_instance = Course(name="", code="", credit=0, course_type="", semester=0, duration=0)
        course_instance.delete_course(delete_code)
        st.success(f"Course with code {delete_code} deleted successfully!")

def edit_course_ui():
    st.header("EDIT COURSE")

    # Fetch all available program names from the database
    all_courses = Course.get_all_courses()
    available_programs = list(set([course[0] for course in all_courses]))  # Assuming program name is at index 0

    # Create a selectbox to choose the program name
    selected_program = st.selectbox("Select Program Name", available_programs)

    # Fetch all available semesters for the selected program
    available_semesters = list(set([course[4] for course in all_courses if course[0] == selected_program]))

    # Create a selectbox to choose the semester
    selected_semester = st.selectbox("Select Semester", available_semesters)

    # Filter courses based on the selected program and semester
    program_semester_courses = [course for course in all_courses if course[0] == selected_program and course[4] == selected_semester]
    available_course_codes = [course[1] for course in program_semester_courses]  # Assuming course code is at index 1

    # Create a selectbox to choose the course code
    edit_code = st.selectbox("Select Course Code to Edit", available_course_codes)

    if edit_code:
        # Get the current details of the selected course
        selected_courses = [course for course in program_semester_courses if course[1] == edit_code]
        
        if not selected_courses:
            st.warning(f"No course found with code {edit_code}")
            return

        selected_course = selected_courses[0]
        current_credit, current_course_type, current_semester, current_duration = selected_course[2:6]

        # Display current details
        st.write(f"Current Course Code: {edit_code}")
        st.write(f"Current Course Credit: {current_credit}")
        st.write(f"Current Course Type: {current_course_type}")
        st.write(f"Current Course Semester: {current_semester}")
        st.write(f"Current Course Duration: {current_duration} hours")

        # Allow user to input new details
        new_credit = st.number_input("Enter New Course Credit", min_value=0, value=current_credit)
        new_duration = st.number_input("Enter New Course Duration (Hours)", min_value=0, value=current_duration)
        # Use a radio button for course type
        new_course_type = st.radio("Select New Course Type", ["Theory", "Practical"], index=0 if current_course_type == "Theory" else 1)
        new_semester = st.number_input("Enter New Course Semester", min_value=0, value=current_semester)

        if st.button("Edit Course"):
            course_instance = Course(name="", code="", credit=0, course_type="", semester=0, duration=0)
            course_instance.edit_course(edit_code, selected_program, new_credit, new_course_type, new_semester, new_duration)
            st.success(f"Course with code {edit_code} edited successfully!")
    else:
        st.warning("Please select a course code to edit.")

def run_course():
    st.title("COURSES")
    tabs = ["Add Course", "Edit Course", "Delete Course"]
    current_tab = st.sidebar.selectbox("Select Action", tabs)

    if current_tab == "Add Course":
        add_course_ui()
    elif current_tab == "Edit Course":
        edit_course_ui()
    elif current_tab == "Delete Course":
        delete_course_ui()

if __name__ == "__main__":
    run_course()
