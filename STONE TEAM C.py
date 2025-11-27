# Tree Plantation Counter
# Run this in VS Code with Python installed (e.g., via terminal: python tree_counter.py)

# Initialize the counter
tree_count = 0

# Function to plant a tree (increment counter)
def plant_tree():
    global tree_count
    tree_count += 1
    print(f"🌳 Tree planted! Total trees: {tree_count}")

# Main loop for user interaction
print("Welcome to the Tree Plantation Counter!")
while True:
    action = input("Type 'plant' to plant a tree, 'view' to see the count, or 'quit' to exit: ").strip().lower()
    if action == 'plant':
        plant_tree()
    elif action == 'view':
        print(f"Current tree count: {tree_count}")
    elif action == 'quit':
        print(f"Final tree count: {tree_count}. Thanks for planting!")
        break
    else:
        print("Invalid input. Try 'plant', 'view', or 'quit'.")

