# Test 1
# get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"

# Test 2
# get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
# "Hello Mahmoud This Is Your Score Table:"
# "Logic => 70"
# "Problems => 60"

# Test 3
# get_people_scores(Logic=70, Problems=60)

# Output
# "Logic => 70"
# "Problems => 60"

# Test 4
# get_people_scores("Ahmed")

# Output
# "Hello Ahmed You Have No Scores To Show"

# -----------------------------------------

# Method 1 => only one name is available
# def get_people_scores(name="default", **topic):
#     if name == None:
#         pass

#     if topic == {}:
#         print(f"Hello, {name}. You Have No Score To Show")

#     else:
#         if name != "default":
#             print(f"Hello, {name}. This is your score table:")

#         for topic_key, topic_value in topic.items():
#             print(f"{topic_key} => {topic_value}")

# -----------------------------------------

# Method 2 => any number of names is available
# def get_people_scores(*names, **topic):
#     for name in names:
#         if name != ():
#             if topic == {}:
#                 print(f"Hello, {name}. You Have No Score To Show")

#             else:
#                 print(f"Hello, {name}. This is your score table:")

#     for topic_key, topic_value in topic.items():
#         print(f"{topic_key} => {topic_value}")

# -----------------------------------------

# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

print('=' * 30)

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

print('=' * 30)

# Test 3
get_people_scores(Logic=70, Problems=60)

print('=' * 30)

# Test 4
get_people_scores("Ahmed")
