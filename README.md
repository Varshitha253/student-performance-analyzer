# Student Performance Analyzer

A student analytics dashboard built using Python, Pandas, SQLite, and Streamlit to monitor academic performance, analyze subject-wise marks, track attendance, and identify students who may need additional academic support.

## Features

- **Performance Dashboard** — View total student count, average marks, and average attendance.
- **Subject-Wise Analytics** — Visualize average marks across subjects.
- **Student Performance Analysis** — Explore individual student records and academic results.
- **Academic Support Indicators** — Identify students who may need additional support.
- **Interactive Filtering** — Filter students based on their average marks.
- **Student Comparison** — Compare the Maths and Science performance of selected students.
- **Student Registration** — Add new student records through an interactive form.
- **SQLite Database** — Store student information persistently.
- **CSV Report Export** — Download student performance data for further analysis.

## Technology Stack

- Python
- Pandas
- Streamlit
- SQLite
- SQL

## Project Structure

```text
student-performance-analyzer/
├── app.py
├── requirements.txt
├── README.md
└── students.db
```

*Note: `students.db` is the local database file. If it is generated automatically by the application, it may not exist until the app runs.*

## Prerequisites

- Python installed on your computer
- pip, Python's package installer

## Run Locally

### 1. Open the project folder

Open a terminal in the project directory.

### 2. Create a virtual environment

```bash
py -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 5. Launch the application

```bash
py -m streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`, where you can access the dashboard.

## Database

The application uses SQLite to store student records locally. Student information can persist between application restarts.

## Purpose

This project demonstrates practical use of Python, data analysis with Pandas, SQL database integration, and interactive dashboard development using Streamlit.

## Future Enhancements

- Additional subjects and academic metrics
- More advanced performance visualizations
- Automated report generation
- Deployment as a web application

## Author

Developed as a Python data analytics portfolio project.