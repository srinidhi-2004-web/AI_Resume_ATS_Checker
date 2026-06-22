from skill_extractor import extract_skills
from resume_parser import extract_text
from flask import Flask, render_template, request
import os
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]
    if file:
     filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )
    file.save(filepath)
    extracted_text = extract_text(filepath)
    skills = extract_skills(extracted_text)
    all_skills = [
    "python", "java", "sql", "machine learning",
    "opencv", "flask", "html", "css", "javascript",
    "kmeans", "dbscan", "gmm",
    "pandas", "numpy", "scikit-learn",
    "tensorflow", "deep learning",
    "data analysis", "git", "github"
]
    missing_skills = [skill for skill in all_skills if skill not in skills]
    total_skills = len(all_skills)
    ats_score = 100
    recommendation = "Excellent Resume"
    return f"""
    <h1>AI Resume ATS Checker</h1>
    <h2>ATS Score: {ats_score}%</h2>
    <h3>Recommendation: {recommendation}</h3>
    <h2>Detected Skills</h2>
    {"<br>".join(skills)}
     <h2>Missing Skills</h2>
     {"<br>".join(missing_skills)}
     <hr>
     <pre>{extracted_text}</pre>
     """
if __name__ == "__main__":
    app.run(debug=True)