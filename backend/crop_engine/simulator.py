def simulate_growth(state):
    updated = []

    for crop in state["inventory"]:
        crop["growth"] += 1

        if crop["growth"] >= crop["growth_time"]:
            crop["yield"] += 1

        updated.append(crop)

    return updated
