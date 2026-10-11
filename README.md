
# Student Performance Data Analysis

## Project Overview
This mini project analyzes student performance using Python. It studies students' marks, attendance, and daily study hours to understand academic performance through statistical analysis and graphs.

The project uses **Pandas, NumPy, and Matplotlib**.

## Objectives
- Analyze student marks in Maths, Science, and English.
- Clean the dataset by handling missing values and duplicate records.
- Calculate mean, median, and standard deviation.
- Compare average marks by gender.
- Study the relationship between attendance, study hours, and marks.
- Visualize student performance using graphs.
- Identify important findings from the dataset.

## Technologies Used
- **Python** — Programming language
- **Pandas** — Data handling and cleaning
- **NumPy** — Numerical operations
- **Matplotlib** — Data visualization

## Dataset Description
The project generates a simulated dataset of 120 students. It includes the following columns:

| Column | Description |
|---|---|
| Student_ID | Unique student identifier |
| Gender | Student gender |
| Attendance_Percent | Attendance percentage |
| Study_Hours_Per_Day | Daily study hours |
| Maths_Marks | Marks in Maths |
| Science_Marks | Marks in Science |
| English_Marks | Marks in English |
| Average_Marks | Average marks across three subjects |
| Performance | Performance category |

**Note:** The dataset is generated for educational purposes and does not represent real students.

## Data Cleaning
The code performs the following cleaning operations:
1. Checks missing values.
2. Identifies duplicate records.
3. Removes duplicate rows.
4. Fills missing numerical values using column medians.
5. Recalculates average marks and performance categories.
6. Saves the cleaned dataset as `cleaned_student_performance.csv`.

## Data Analysis
The project calculates:
- Mean, median, and standard deviation of subject marks.
- Overall average marks.
- Gender-wise average marks.
- Number of students in each performance category.
- Top 10 students based on average marks.
- Number of students with attendance of 75% or more.
- Correlation between attendance, study hours, and marks.

## Data Visualization
The project creates three graphs using Matplotlib:

1. **Average Marks by Subject** — compares average marks in the three subjects.
2. **Attendance vs Average Marks** — displays the relationship between attendance and average marks.
3. **Distribution of Student Average Marks** — shows the distribution of average marks.

## How to Run the Project

### 1. Install Required Libraries
Run the following command:

```bash
pip install pandas numpy matplotlib
```

### 2. Run the Python File
Save the source code as `Student_Performance_Analysis.py` and run:

```bash
python Student_Performance_Analysis.py
```

You can also run the code in Google Colab after ensuring the required libraries are available.

### 3. View the Results
The program prints the analysis and findings, displays three graphs, and saves the cleaned dataset as a CSV file.

## Key Findings
The program automatically prints eight findings, including:
- Total number of students analyzed.
- Best-performing subject.
- Subject with the lowest average marks.
- Overall average marks.
- Average attendance.
- Average daily study hours.
- Attendance-mark correlation.
- Study-hour-mark correlation.

The actual findings depend on the generated dataset.

## Conclusion
This project demonstrates how Python can be used to clean, analyze, and visualize student performance data. Pandas and NumPy support data processing and statistical calculations, while Matplotlib presents the results graphically.

The results can help summarize patterns in student marks, attendance, and study habits. Since the data is simulated, the findings should not be treated as conclusions about real students.

## Author
**Student Performance Data Analysis Mini Project**
