import re

def check_password_strength(password: str) -> tuple:
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("🔸 Use at least 8 characters.")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("🔸 Add numbers (0-9).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("🔸 Include uppercase letters (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("🔸 Include lowercase letters (a-z).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        tips.append("🔸 Add special characters (!@#...).")

    strength_level = {
        5: ("Strong 💪", "green"),
        3: ("Medium 🤔", "orange"),
        0: ("Weak 😢", "red")
    }

    for key in sorted(strength_level.keys(), reverse=True):
        if score >= key:
            return strength_level[key][0], strength_level[key][1], score * 20, tips

    return "Weak 😢", "red", score * 20, tips
