# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

# Needed Output
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320"

total_points = 0

for topic, rank in my_ranks.items():
    if rank == 'A': points = 100
    
    elif rank == 'B': points = 80
    
    else: points = 40

    print(f"My Rank in {topic} Is {rank}. This Is Equal To {points} Points")

    total_points += points

else:
    print(f"- Total Points = {total_points}")
