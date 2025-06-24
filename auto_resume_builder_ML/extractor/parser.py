def format_data(entities):
    return {
        "name": entities.get("name") or "Your Name",
        "email": entities.get("email") or "you@example.com",
        "skills": entities.get("skills") or [],
        "experience": entities.get("experience") or [],
        "education": entities.get("education") or []
    }
