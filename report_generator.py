def generate_report(conflicts, analyses):
    suggestions = []
    for c in conflicts:
        if "Deadline" in c["type"]:
            suggestions.append("Clarify if the submission deadline is 10 PM or midnight.")
        if "Attendance" in c["type"]:
            suggestions.append("Decide if minimum attendance is 65% or 75%.")

    return {
        "conflicts": conflicts,
        "suggestions": suggestions,
        "analysis": analyses
    }
