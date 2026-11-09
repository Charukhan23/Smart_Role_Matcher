# 1. Interface - Only rules, no code inside
class RoleChecker:
    def check_eligible(self, student):
        pass

# 2. Main Class
class Role(RoleChecker):
    def __init__(self, role_name, required_skills, min_cgpa):
        self.role_name = role_name
        self.required_skills = required_skills
        self.min_cgpa = min_cgpa

    def check_eligible(self, student):
        matched = []
        for skill in self.required_skills:
            if skill in student['skills']:
                matched.append(skill)

        if student['cgpa'] >= self.min_cgpa and len(matched) >= 2:
            return True, matched
        else:
            return False, matched

# 3. 4 Roles
roles = {
    "Gen AI Engineer": Role("Gen AI Engineer", ["llm", "rag", "langchain", "prompt"], 7.0),
    "AI/ML Engineer": Role("AI/ML Engineer", ["python", "machine learning", "tensorflow", "pytorch"], 7.0),
    "Data Scientist": Role("Data Scientist", ["pandas", "sql", "statistics", "power bi"], 6.5),
    "AI Research Scientist": Role("AI Research Scientist", ["research", "paper", "transformer", "mathematics"], 8.0)
}

# 4. 10 Students Data
students = [
    {"name": "charukh", "cgpa": 8.5, "skills": ["llm", "rag", "langchain"]},
    {"name": "viswa", "cgpa": 7.8, "skills": ["python", "machine learning", "tensorflow"]},
    {"name": "Anto", "cgpa": 6.0, "skills": ["pandas", "sql"]},
    {"name": "Jayashree", "cgpa": 9.0, "skills": ["research", "paper", "transformer"]},
    {"name": "Divya", "cgpa": 7.2, "skills": ["llm", "prompt"]},
    {"name": "Vinoth", "cgpa": 8.0, "skills": ["python", "pandas", "sql", "statistics"]},
    {"name": "Anirudh", "cgpa": 6.8, "skills": ["python"]},
    {"name": "Karthi", "cgpa": 8.2, "skills": ["rag", "llm", "prompt"]},
    {"name": "Shreya", "cgpa": 7.5, "skills": ["machine learning", "pytorch"]},
    {"name": "Rakesh", "cgpa": 9.2, "skills": ["research", "mathematics", "paper"]},
]

# 5. Input
print("Available Roles: Gen AI Engineer, AI/ML Engineer, Data Scientist, AI Research Scientist")
selected_role_name = input("Enter role name: ")
selected_role = roles.get(selected_role_name)

# 6. Output - Simple and neat box
if selected_role:
    print("\n==========================================")
    print("ROLE:", selected_role.role_name)
    print("==========================================")

    for student in students:
        is_selected, matched = selected_role.check_eligible(student)

        if is_selected:
            status = "✅SELECTED"
        else:
            status = "❌NOT SELECTED"

        if len(matched) == 0:
            skills_text = "None"
        else:
            skills_text = ", ".join(matched)

        print("------------------------------------------")
        print("👤Name   :", student['name'])
        print("🎓CGPA   :", student['cgpa'])
        print("🛠️Skills :", skills_text)
        print("📌Status :", status)
        print("------------------------------------------")
else:
    print("Wrong role name. Please type correctly.")