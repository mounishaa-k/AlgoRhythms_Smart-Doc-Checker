def detect_conflicts(analyses):
    """Naive conflict detection (stub for MVP)."""
    conflicts = []
    texts = [a["rules"] for a in analyses]

    # Example: simple string-based contradiction check
    if "10 PM" in str(texts) and "midnight" in str(texts):
        conflicts.append({
            "type": "Deadline conflict",
            "description": "One document says 10 PM, another says midnight."
        })

    if "75%" in str(texts) and "65%" in str(texts):
        conflicts.append({
            "type": "Attendance conflict",
            "description": "One rule says 75%, another says 65%."
        })

    return conflicts
