# Function to calculate the minimum number of players who need to get shot
def min_players_to_shot(N, K, heights):
    max_height = K  # Initialize the maximum height encountered so far
    shot_count = 0  # Initialize the count of players who need to get shot

    # Iterate through the heights of the players
    for height in heights:
        # If the height is greater than the maximum height encountered so far
        if height > max_height:
            shot_count += 1  # Increment the shot count
        # Update the maximum height encountered so far
        max_height = max(max_height, height)

    return shot_count

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read N and K for the current test case
    N, K = map(int, input().split())
    # Read the heights of the players for the current test case
    heights = list(map(int, input().split()))
    # Calculate and print the minimum number of players who need to get shot
    print(min_players_to_shot(N, K, heights))