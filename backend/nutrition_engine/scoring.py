def compute_nutrition(crops):
    score = 0

    for c in crops:
        score += c.get("calories", 0)

    return {
        "nutrition_score": score
    }
