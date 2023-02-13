# Test 1
# get_the_scores("Osama", **scores_list)

# Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"

# Test 2
# get_the_scores("Osama")

# Output
# "Hello Osama You Have No Scores To Show"

# Test 3
# get_the_scores(**scores_list)

# Output
# "Math => 90"
# "Science => 80"
# "Language => 70"

# --------------------------------

scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}


def get_the_scores(name="default", **topics):
    if topics == {}:
        print(f"Hello {name} You Have No Score To Show")

    else:
        if name != "default":
            print(f"Hello {name} This Is Your Score Table:")

        for topic, score in topics.items():
            print(f"{topic} => {score}")

# Test 1
get_the_scores("Osama", **scores_list)

print('=' * 30)

# Test 2
get_the_scores("Osama")

print('=' * 30)

# Test 3
get_the_scores(**scores_list)
