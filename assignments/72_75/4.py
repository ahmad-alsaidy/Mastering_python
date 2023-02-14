skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"


for counter, skill in enumerate(reversed(skills), 50):
    if str(skill).isalpha():
        print(f"{counter} - {skill}")
