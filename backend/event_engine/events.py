import random

def generate_event(state):
    events = [
        "drought",
        "pest outbreak",
        "market surge",
        "soil depletion"
    ]

    return {
        "type": random.choice(events),
        "impact": -0.2
    }
