# Input
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

# Needed Output
# "------------------------------"
# "-- Student Name => Ahmed"
# "------------------------------"
# "- Math => 100 Points"
# "- Science => 20 Points"
# "- Draw => 80 Points"
# "- Sports => 40 Points"
# "- Thinking => 100 Points"
# "Total Points For Ahmed Is 340"
# "------------------------------"
# "-- Student Name => Sayed"
# "------------------------------"
# "- Math => 80 Points"
# "- Science => 80 Points"
# "- Draw => 80 Points"
# "- Sports => 20 Points"
# "- Thinking => 100 Points"
# "Total Points For Sayed Is 360"
# "------------------------------"
# "-- Student Name => Mahmoud"
# "------------------------------"
# "- Math => 20 Points"
# "- Science => 100 Points"
# "- Draw => 100 Points"
# "- Sports => 80 Points"
# "- Thinking => 80 Points"
# "Total Points For Mahmoud Is 380"
# ---------------------------------------

points = {
    'A': 100,
    'B': 80,
    'C': 40,
    'D': 20
}

# Method One
for main_key, main_value in students.items():
    print("------------------------------")
    print(f"-- Student Name => {main_key}")
    print("------------------------------")

    total_points = 0

    for child_key, child_vlue in main_value.items():
        print(f"- {child_key} => {points[child_vlue]} Points")

        total_points += points[child_vlue]

    else:
        print(f"Total Point For {main_key} Is {total_points}")

print("------------------------------")

# Method Two
for name in students:
    print("------------------------------")
    print(f"-- Sudent Name => {name}")
    print("------------------------------")

    total_points = 0

    for topic in students[name]:
        print(f"- {topic} => {points[students[name][topic]]} Points")

        total_points += points[students[name][topic]]

    else:
        print(f"Total Points For {name} Is {total_points}")

print("------------------------------")
