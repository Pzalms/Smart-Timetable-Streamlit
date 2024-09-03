# Timetable and Course Management App

## Overview

The Timetable and Course Management App is a web application designed to manage academic courses and generate timetables. This app allows users to:

- **Add, Edit, and Delete Courses:** Manage course information including course codes, credits, types, semesters, and durations.
- **Generate Timetables:** Create weekly timetables based on the courses and their details.
- **Allocate Teachers:** Assign teachers to courses based on availability and workload.

The application is built using Streamlit for the web interface and SQLite for the database.

## Features

- **Course Management:**
  - Add new courses with details such as program name, course code, credits, type, semester, and duration.
  - Edit existing courses to update their details.
  - Delete courses from the database.
  
- **Timetable Generation:**
  - Generate a weekly timetable based on the sorted list of courses.
  - View the generated timetable in a tabular format.

- **Teacher Allocation:**
  - Allocate teachers to courses based on their availability and course requirements.
  - View the allocation results and update teacher hours in the database.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- SQLite (included with Python)
- Streamlit (for the web interface)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone *repo-link*
   cd your-repository
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create the Database and Tables:**
   Run the provided `create_tables.py` script to initialize the database:
   ```bash
   python create_tables.py
   ```

### Running the Application

1. **Start the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

2. **Open Your Web Browser:**
   - Navigate to `http://localhost:8501` to access the application.

## Usage

### Adding a Course

1. Go to the "Add Course" tab.
2. Enter the course details including program name, course code, credits, type, semester, and duration.
3. Click "Add Course" to save the new course.

### Editing a Course

1. Go to the "Edit Course" tab.
2. Select a program and semester to filter the available courses.
3. Choose the course code you wish to edit.
4. Update the course details and click "Edit Course" to save changes.

### Deleting a Course

1. Go to the "Delete Course" tab.
2. Select a program and semester to filter the available courses.
3. Choose the course code you wish to delete.
4. Click "Delete Course" to remove the selected course.

### Generating a Timetable

1. Go to the "Generate Timetable" tab.
2. Select a course and semester to fetch the course data.
3. Click "Generate Timetable" to create and view the timetable.

### Saving Timetable

1. After generating a timetable, click "Save Timetable" to save the timetable and allocate teachers.
2. The timetable and teacher allocation details will be saved to a text file on your desktop.

## Troubleshooting

- **Database Errors:** Ensure that the database tables have been created correctly by running the `create_tables.py` script.
- **Index Errors:** Ensure that all dropdowns and selections have valid values before making changes.

## Contributing

Feel free to open issues or submit pull requests to contribute to this project. Please ensure that your contributions follow the coding standards and include appropriate documentation.


---
