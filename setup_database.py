import sqlite3

def create_tables():
    connection = sqlite3.connect('timetable.db')
    cursor = connection.cursor()

    # Create course table
    create_course_table = """
    CREATE TABLE IF NOT EXISTS course (
        PROGRAM_NAME TEXT NOT NULL,
        COURSE_CODE TEXT PRIMARY KEY,
        COURSE_CREDIT INTEGER NOT NULL,
        COURSE_TYPE TEXT NOT NULL,
        COURSE_SEM INTEGER NOT NULL,
        COURSE_DURATION INTEGER NOT NULL
    );
    """
    cursor.execute(create_course_table)

    # Create teacher table
    create_teacher_table = """
    CREATE TABLE IF NOT EXISTS teacher (
        TEACHER_NAME TEXT PRIMARY KEY,
        TEACHER_WORKING INTEGER NOT NULL
    );
    """
    cursor.execute(create_teacher_table)

    # Create teacher_course_allocation table
    create_teacher_course_allocation_table = """
    CREATE TABLE IF NOT EXISTS teacher_course_allocation (
        COURSE_CODE TEXT NOT NULL,
        TEACHER_NAME TEXT NOT NULL,
        FOREIGN KEY (COURSE_CODE) REFERENCES course(COURSE_CODE),
        FOREIGN KEY (TEACHER_NAME) REFERENCES teacher(TEACHER_NAME)
    );
    """
    cursor.execute(create_teacher_course_allocation_table)

    connection.commit()
    connection.close()
    print("Tables created successfully (if they didn't already exist).")

if __name__ == "__main__":
    create_tables()
