import random


def simulate_response(priority: str) -> str:
    if priority == "High":
        return random.choice(["Interested", "Interested", "No Response"])
    elif priority == "Medium":
        return random.choice(["No Response", "Interested"])
    else:
        return "Not Interested"
