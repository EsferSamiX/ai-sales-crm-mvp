def calculate_priority(row):
    persona = str(row["persona"]).lower()
    industry = str(row["industry"]).lower()
    size = int(row["company_size"])

    score = 0

    if any(p in persona for p in ["founder", "cto", "co-founder", "product"]):
        score += 4
    elif any(p in persona for p in ["vp", "head", "director"]):
        score += 3
    elif "manager" in persona:
        score += 2
    else:
        score += 1

    if size >= 200:
        score += 3
    elif size >= 50:
        score += 2
    elif size >= 20:
        score += 1

    high_interest = [
        "saas", "fintech", "health", "edtech", "ai",
        "cyber", "hrtech", "ecommerce", "travel"
    ]
    medium_interest = ["retail", "media", "martech"]

    if any(ind in industry for ind in high_interest):
        score += 3
    elif any(ind in industry for ind in medium_interest):
        score += 1

    if score >= 8:
        return score, "High"
    elif score >= 5:
        return score, "Medium"
    else:
        return score, "Low"
