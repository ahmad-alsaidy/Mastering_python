# Create Dictionary Here
skills = {
    "HTML": 90,
    "CSS": 80,
    "Python": 30
}

# Needed Output

# "HTML Progress Is 90%"
print("HTML Progress Is {:d}%".format(skills.get("HTML")))

# "CSS Progress Is 80%"
print("CSS Progress Is {:d}%".format(skills.get("CSS")))
# "Python Progress Is 30%"
print("Python Progress Is {:d}%".format(skills.get("Python")))

# "AI Progress Is 20%"
skills.setdefault("AI", 30)
print("AI Progress Is {:d}%".format(skills.get("AI")))
