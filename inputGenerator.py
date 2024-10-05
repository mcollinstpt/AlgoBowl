import random

# Define the weights
weights = [
    ('.', 0.65),
    ('0', 0.05),
    ('1', 0.05),
    ('2', 0.05),
    ('3', 0.05),
    ('4', 0.05),
    ('X', 0.10)
]

# Create a list of characters based on weights
choices = [char for char, weight in weights for _ in range(int(weight * 100))]

# Generate the grid
grid = []
for _ in range(250):
    row = ''.join(random.choices(choices, k=400))
    grid.append(row)

file = open("input_backup.txt", "w")

# Print the grid
for row in grid:
    file.write(row)
    file.write("\n")