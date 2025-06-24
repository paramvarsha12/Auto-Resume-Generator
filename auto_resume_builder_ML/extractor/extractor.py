import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    entities = {
        "name": None,
        "email": None,
        "skills": [],
        "experience": [],
        "education": []
    }

    
    lines = text.splitlines()
    for line in lines:
        if line.strip() and "@" not in line and ":" not in line:
            entities["name"] = line.strip()
            break

    
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    if email_match:
        entities["email"] = email_match.group(0)

    
    skill_keywords = ["Python", "Java", "Machine Learning", "C++", "SQL", "JavaScript", "HTML", "CSS"]
    for skill in skill_keywords:
        if skill.lower() in text.lower():
            entities["skills"].append(skill)

    
    for line in lines:
        if line.lower().startswith("education:"):
            value = line.split(":", 1)[1].strip()
            if value:
                entities["education"] = [x.strip() for x in value.split(",") if x.strip()]

    
    for line in lines:
        if line.lower().startswith("experience:"):
            value = line.split(":", 1)[1].strip()
            if value:
                entities["experience"] = [x.strip() for x in value.split(",") if x.strip()]

    return entities
