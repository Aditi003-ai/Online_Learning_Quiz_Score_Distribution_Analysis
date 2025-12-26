aditi verma, [26-12-2025 23:55]
import gradio as gr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Plot helper functions
# -----------------------------

def plot_exam_score_distribution(data):
    plt.figure(figsize=(8,5))
    sns.histplot(data['exam_score'], bins=20, color="red", kde=True)
    plt.xlabel("Exam Score")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Exam Scores")
    return plt.gcf()

def plot_exam_score_mean_std(data):
    mean_score = data["exam_score"].mean()
    std_score = data["exam_score"].std()

    plt.figure(figsize=(8,5))
    sns.histplot(data["exam_score"], bins=20, color="#EDFFF0")
    plt.axvline(mean_score, color="red", linestyle="--", label="Mean")
    plt.axvline(mean_score + std_score, color="green", linestyle="--", label="+1 Std Dev")
    plt.axvline(mean_score - std_score, color="green", linestyle="--", label="-1 Std Dev")
    plt.legend()
    plt.title("Exam Score Distribution with Mean and Std Dev")
    return plt.gcf()

def plot_exam_score_boxplot(data):
    plt.figure(figsize=(6,4))
    sns.boxplot(x=data["exam_score"], color="red")
    plt.xlabel("Exam Score")
    plt.title("Boxplot of Exam Scores")
    return plt.gcf()

def plot_gender_distribution(data):
    gender_counts = data["gender"].value_counts()

    plt.figure(figsize=(5,5))
    plt.pie(
        gender_counts,
        labels=["Male", "Female", "Other"],
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Gender Distribution of Students")
    return plt.gcf()

def plot_exam_score_by_gender(data):
    gender_mean_scores = data.groupby("gender")["exam_score"].mean()

    plt.figure(figsize=(6,4))
    gender_mean_scores.plot(kind="bar", color="red")
    plt.xticks([0,1,2], ["Male", "Female", "Other"], rotation=0)
    plt.ylabel("Average Exam Score")
    plt.title("Average Exam Score by Gender")
    return plt.gcf()

def plot_exam_score_by_study_method(data):
    plt.figure(figsize=(8,5))
    sns.boxplot(x=data['study_method'], y=data["exam_score"], color="red")
    plt.xticks(
        ticks=[0,1,2,3,4],
        labels=['coaching','online videos','mixed','self-study','group study'],
        rotation=20
    )
    plt.xlabel("Study Method")
    plt.ylabel("Exam Score")
    plt.title("Exam Score Distribution by Study Method")
    return plt.gcf()

# -----------------------------
# Main processing function
# -----------------------------

def analyze_dataset(file):
    data = pd.read_csv(file.name)

    # Drop student_id
    data = data.drop(columns=["student_id"])

    # Encode categorical columns
    data["gender"] = data["gender"].map({"male":0, "female":1, "other":2})
    data["course"] = data["course"].map({
        'diploma':0, 'bca':1, 'b.sc':2,
        'b.tech':3, 'bba':4, 'ba':5, 'b.com':6
    })
    data["study_method"] = data["study_method"].map({
        'coaching':0, 'online videos':1,
        'mixed':2, 'self-study':3, 'group study':4
    })

    summary = data.describe()

    return (
        data.head(),
        summary,
        plot_exam_score_distribution(data),
        plot_exam_score_mean_std(data),
        plot_exam_score_boxplot(data),
        plot_gender_distribution(data),
        plot_exam_score_by_gender(data),
        plot_exam_score_by_study_method(data)
    )

# -----------------------------
# Gradio UI
# -----------------------------

with gr.Blocks(title="Online Learning – Exam Score Distribution Analysis") as demo:
    gr.Markdown(
        """
        # Online Learning Quiz / Exam Score Distribution Analysis
        Upload the Exam_Score_Prediction.csv file to explore student performance patterns.
        """
    )

    file_input = gr.File(label="Upload CSV Dataset")

    run_btn = gr.Button("Analyze Dataset")

    gr.Markdown("## Dataset Preview")
    data_preview = gr.Dataframe()

    gr.Markdown("## Statistical Summary")
    data_summary = gr.Dataframe()

    gr.Markdown("## Exam Score Analysis")
    plot1 = gr.Plot()
    plot2 = gr.Plot()
    plot3 = gr.Plot()

aditi verma, [26-12-2025 23:55]
gr.Markdown("## Demographic & Study Method Analysis")
    plot4 = gr.Plot()
    plot5 = gr.Plot()
    plot6 = gr.Plot()

    run_btn.click(
        analyze_dataset,
        inputs=file_input,
        outputs=[
            data_preview,
            data_summary,
            plot1,
            plot2,
            plot3,
            plot4,
            plot5,
            plot6
        ]
    )

demo.launch()
