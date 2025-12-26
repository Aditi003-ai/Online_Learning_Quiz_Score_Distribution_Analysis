Overview

This project focuses on analyzing student exam scores using Python.
The goal is to understand how different factors such as gender, course, study method, attendance, and study hours affect exam performance.

We use data cleaning, statistical analysis, and visualizations to gain meaningful insights from the dataset.

Dataset Information

File Name: Exam_Score_Prediction.csv

The dataset contains student-related attributes such as:
Age ,Gender, Course ,Study Hours, Class Attendance, Study Method , Exam Score

Tools & Libraries Used

Python

NumPy – numerical computations

Pandas – data manipulation and analysis

Matplotlib – data visualization

Seaborn – statistical visualizations


Data Preprocessing Steps
Loaded dataset using pandas.read_csv()


Checked:
Dataset shape,
Column names
Missing values
Duplicate records,
Removed unnecessary column:
student_id,
Converted categorical columns into numeric values using mapping:
Gender,
Course,
Study Method

Exploratory Data Analysis (EDA)
The following analyses and visualizations were performed:

Exam Score Analysis

Histogram of exam scores
Mean and standard deviation visualization
Boxplot to detect score spread and outliers


Gender-based Analysis

Gender distribution using pie chart
Average exam score by gender (bar chart)

Correlation Analysis
Correlation matrix to understand relationships between variables


Key Insights

Exam scores follow a near-normal distribution.

Study method has a noticeable impact on exam performance.

Some variation in average exam scores exists across genders.

Correlation analysis helps identify factors influencing exam scores.


 How to Run the Project

Clone the repository

Install required libraries:
pip install numpy pandas matplotlib seaborn
