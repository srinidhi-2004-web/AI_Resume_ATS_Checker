skills = [
    "python", "java", "sql", "machine learning",
    "opencv", "flask", "html", "css", "javascript",
    "kmeans", "dbscan", "gmm",
    "pandas", "numpy", "scikit-learn",
    "tensorflow", "deep learning",
    "data analysis", "git", "github"
]

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in skills:

        if skill in text:
            found_skills.append(skill)

    return found_skills