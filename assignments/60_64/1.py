# Tests
# get_score(Math=90, Science=80, Language=70)

# Output
# "Math => 90"
# "Science => 80"
# "Language => 70"

# Tests
# get_score(Logic=70, Problems=60)

# Output
# "Logic => 70"
# "Problems => 60"

def get_score(**topic):
    for topic_key, topic_value in topic.items():
        print(f"{topic_key} => {topic_value}")

get_score(Math=90, Science=80, Language=70)

print('=' * 30)

get_score(Logic=70, Problems=60)
