import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown("""
<style>
/* ===== Modern dashboard foundation ===== */
.stApp {
    background: #F7F9FC;
    color: #1F2937;
}

.block-container {
    max-width: 1440px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ===== Typography ===== */
h1 {
    color: #111827 !important;
    font-size: 2.15rem !important;
    font-weight: 750 !important;
    letter-spacing: -1px;
}

h2, h3 {
    color: #1F2937 !important;
    font-weight: 650 !important;
    letter-spacing: -0.3px;
}

p, label {
    color: #4B5563;
}

/* ===== KPI metric cards ===== */
[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #E5EAF0;
    border-radius: 16px;
    padding: 22px 20px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.035);
    transition: border-color 0.2s ease,
                box-shadow 0.2s ease;
}

[data-testid="stMetric"]:hover {
    border-color: #A7DCC1;
    box-shadow: 0 7px 20px rgba(15, 23, 42, 0.06);
}

[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
}

[data-testid="stMetricValue"] {
    color: #065F46 !important;
    font-size: 1.9rem !important;
    font-weight: 750 !important;
}

/* ===== Sidebar ===== */
[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 1px solid #E5EAF0;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #111827 !important;
}

/* ===== Buttons ===== */
.stButton > button,
.stFormSubmitButton > button {
    background: #047857;
    color: #FFFFFF;
    border: 1px solid #047857;
    border-radius: 9px;
    min-height: 42px;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #065F46;
    border-color: #065F46;
    color: #FFFFFF;
}

/* ===== Inputs and selectors ===== */
[data-baseweb="input"] > div,
[data-baseweb="select"] > div,
[data-baseweb="textarea"] {
    border-radius: 9px;
    border-color: #D8E0E9;
}

[data-baseweb="input"] > div:focus-within,
[data-baseweb="textarea"]:focus-within {
    border-color: #059669;
}

/* ===== Data tables ===== */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background: #FFFFFF;
    border: 1px solid #E5EAF0;
    border-radius: 12px;
    overflow: hidden;
}

/* ===== Sections and dividers ===== */
hr {
    border-color: #E5EAF0;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
}

/* ===== Success and warning messages ===== */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* ===== Download button ===== */
.stDownloadButton > button {
    border-radius: 9px;
    font-weight: 600;
}

/* ===== Form container ===== */
[data-testid="stForm"] {
    background: #FFFFFF;
    padding: 22px;
    border: 1px solid #E5EAF0;
    border-radius: 16px;
}

/* ===== Footer spacing ===== */
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)



st.title("🎓 Student Performance Analyzer")

st.markdown("""
<div style="
    background: linear-gradient(120deg, #064E3B 0%, #047857 65%, #10B981 100%);
    padding: 30px 32px;
    border-radius: 18px;
    margin-bottom: 26px;
">
    <div style="
        color: #A7F3D0;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
    ">
        ACADEMIC ANALYTICS PLATFORM
    </div>
    <h1 style="
        color: #FFFFFF !important;
        margin: 10px 0 8px 0;
        font-size: 32px !important;
        letter-spacing: -0.8px;
    ">
        Student Performance Analyzer
    </h1>
    <p style="
        color: #D1FAE5;
        margin: 0;
        font-size: 15px;
    ">
        Track achievement. Discover insights. Support every learner.
    </p>
</div>
""", unsafe_allow_html=True)



# Connect to the SQLite database file
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student TEXT PRIMARY KEY,
        maths INTEGER NOT NULL,
        science INTEGER NOT NULL,
        attendance INTEGER NOT NULL
    )
""")

# Insert sample data only when the table is empty
cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    sample_students = [
        ("Ananya", 85, 78, 95),
        ("Rahul", 42, 35, 68),
        ("Priya", 91, 88, 98),
        ("Arjun", 67, 72, 80),
        ("Sneha", 76, 82, 92)
    ]

    cursor.executemany("""
        INSERT INTO students
        (student, maths, science, attendance)
        VALUES (?, ?, ?, ?)
    """, sample_students)

conn.commit()

# Retrieve records from the database
df = pd.read_sql_query("""
    SELECT
        student AS Student,
        maths AS Maths,
        science AS Science,
        attendance AS Attendance
    FROM students
""", conn)

conn.close()


st.subheader("Student Records")
st.dataframe(df, use_container_width=True)

st.markdown("## 📈 Class Overview")
st.caption("A snapshot of student achievement and attendance.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", len(df))

with col2:
    average_marks = df[["Maths", "Science"]].to_numpy().mean()
    st.metric("Average Marks", f"{average_marks:.1f}%")

with col3:
    average_attendance = df["Attendance"].mean()
    st.metric("Average Attendance", f"{average_attendance:.1f}%")
    st.markdown("## 📊 Subject Performance")
st.caption("Compare average marks across academic subjects.")

subject_averages = df[["Maths", "Science"]].mean()

st.bar_chart(subject_averages)

st.subheader("🎯 Students Who May Need Support")

# Calculate each student's average across the two subjects
df["Average Marks"] = df[["Maths", "Science"]].mean(axis=1)
df["Performance Status"] = df["Average Marks"].apply(
    lambda average: (
        "Needs Support" if average < 40
        else "Satisfactory" if average < 60
        else "Good" if average < 80
        else "Excellent"
    )
)
# Flag students whose average is below 40
support_students = df[df["Average Marks"] < 40]

if support_students.empty:
    st.success("No students meet the current support threshold.")
else:
    st.warning(
        f"{len(support_students)} student(s) may need additional support."
    )
    st.dataframe(support_students, width="stretch")


st.subheader("🔍 Filter Student Records")

minimum_average = st.slider(
    "Minimum average marks",
    min_value=0,
    max_value=100,
    value=0
)

filtered_df = df[
    df["Average Marks"] >= minimum_average
]

st.write(f"Students matching filter: {len(filtered_df)}")

st.dataframe(filtered_df, width="stretch")


st.subheader("🔎 Explore Individual Students")

selected_student = st.selectbox(
    "Choose a student",
    df["Student"].tolist()
)

student_record = df[df["Student"] == selected_student].iloc[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Maths Marks", student_record["Maths"])

with col2:
    st.metric("Science Marks", student_record["Science"])

with col3:
    st.metric("Attendance", f'{student_record["Attendance"]}%')

st.write(f"### Performance details for {selected_student}")

st.dataframe(
    student_record.to_frame().T,
    width="stretch"
)


st.subheader("📈 Compare Student Marks")

selected_students = st.multiselect(
    "Select students to compare",
    df["Student"].tolist(),
    default=df["Student"].tolist()[:3]
)

if selected_students:
    comparison_df = df[
        df["Student"].isin(selected_students)
    ].set_index("Student")[["Maths", "Science"]]

    st.bar_chart(comparison_df)
else:
    st.info("Select at least one student to view the comparison.")



st.subheader("📥 Download Performance Report")

# Convert the student records into CSV format
csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Student Report (CSV)",
    data=csv_data,
    file_name="student_performance_report.csv",
    mime="text/csv"
)



st.subheader("➕ Add a New Student")

with st.form("add_student_form"):
    student_name = st.text_input("Student name").strip()

    maths_marks = st.number_input(
        "Maths marks", min_value=0, max_value=100, value=0
    )
    science_marks = st.number_input(
        "Science marks", min_value=0, max_value=100, value=0
    )
    attendance = st.number_input(
        "Attendance (%)", min_value=0, max_value=100, value=0
    )

    submitted = st.form_submit_button("Add Student")

if submitted:
    if not student_name:
        st.error("Please enter a student name.")
    else:
        try:
            with sqlite3.connect("students.db") as conn:
                conn.execute(
                    """
                    INSERT INTO students
                    (student, maths, science, attendance)
                    VALUES (?, ?, ?, ?)
                    """,
                    (student_name, maths_marks, science_marks, attendance)
                )

            st.success(f"Student {student_name} added successfully!")
            st.rerun()

        except sqlite3.IntegrityError:
            st.error(
                "This student name already exists. "
                "Please enter a unique name."
            )
