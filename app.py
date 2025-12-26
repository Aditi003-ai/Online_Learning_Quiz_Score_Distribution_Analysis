
import pandas as pd
import gradio as gr

# Load data
data = pd.read_csv("Exam_Score_Prediction.csv")

data = data.drop(["student_id"], axis=1)

data["gender"] = data["gender"].map({"male": 0, "female": 1, "other": 2})
data["course"] = data["course"].map({'diploma':0, 'bca':1, 'b.sc':2, 'b.tech':3, 'bba':4, 'ba':5, 'b.com':6})
data["study_method"] = data["study_method"].map({'coaching':0, 'online videos':1, 'mixed':2, 'self-study':3, 'group study':4})

mean_score = data["exam_score"].mean()
std_score = data["exam_score"].std()

def exam_score_insight(age, gender, study_hours, attendance, study_method):
    return f'''
Exam Score Analysis

Mean Score: {mean_score:.2f}
Standard Deviation: {std_score:.2f}

Expected Score Range:
{mean_score - std_score:.1f} to {mean_score + std_score:.1f}

Note:
Higher study hours and attendance generally lead to better exam scores.
'''

interface = gr.Interface(
    fn=exam_score_insight,
    inputs=[
        gr.Number(label="Age"),
        gr.Radio(["Male", "Female", "Other"], label="Gender"),
        gr.Slider(0, 10, step=1, label="Study Hours per Day"),
        gr.Slider(0, 100, step=5, label="Class Attendance (%)"),
        gr.Dropdown(["Coaching", "Online Videos", "Mixed", "Self-Study", "Group Study"], label="Study Method")
    ],
    outputs=gr.Textbox(label="Exam Score Insight"),
    title="Exam Score Analysis UI",
    description="Gradio-based UI for Exam Score Distribution Analysis"
)

if __name__ == "__main__":
    interface.launch()
