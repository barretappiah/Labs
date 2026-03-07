import random
from stack import Stack

FILES = ["config1.txt", "config2.txt", "config3.txt"]

# Create starting stacks based on the configuration file
def initialize_stacks(file):
    stacks = []
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().strip().splitlines()

        # Separate settings from data
        capacity = data[0][-1]
        quantity = data[1][-1]

        stack_data = data[2:]

        # Add empty stacks if there aren't enough
        if len(stack_data) < int(quantity):
            for _ in range(int(quantity) - len(stack_data)):
                stack_data.append([""] * int(capacity))

        # Create stack objects and store in list
        stacks = []
        for stack in stack_data:
            new_stack = Stack(int(capacity))
            for item in stack:
                if item != "":
                    new_stack.push(item)
            stacks.append(new_stack)

        return stacks

# Display the current state of the stacks
def display_stacks(stacks):
    print("\nCurrent Stacks:")
    for i, stack in enumerate(stacks):
        print(f"Stack {i + 1}: {stack}")

# Get the choice for move-from/move-to stack from the user
def get_stack_choice(prompt: str, n: int) -> int:
    #Returns a valid stack index in 1..n (as an int). Keeps retrying until valid.# 
    for i in range(2):
        try:
            choice = int(input(prompt))
            if 1 <= choice <= n:
                return choice
            else:
                print("Invalid stack number or stack is empty. Please try again.")

        except ValueError:
            if i == 0:
                print("Invalid stack number or stack is empty. Please try again.")

    raise ValueError


# Move an item between stacks
def move_item(stacks, from_stack, to_stack):
    item = None
    
    try:
        item = stacks[from_stack].pop()
        stacks[to_stack].push(item)
    except Exception as e:
        if item is not None: # If the pop failed to return an item (stack complete or empty), we shouldn't try to push it back (error in push will be raised instead)
            stacks[from_stack].push(item)  # Return the item back to the original
        print(e)
        
# check if all stacks are completed
def check_completion(stacks):
    # If its not completed and not empty, then its not good (mixed fruits, or not enough)

    completed = 0
    for stack in stacks:
        if stack.is_completed():
            completed += 1
        elif not stack.is_empty():
            return False
    
    return True

def main():
    print('Welcome to the Fruit Sorter!')
    chosen_file = random.choice(FILES) 
    stacks = initialize_stacks(chosen_file)

    all_complete = False

    # Game Loop
    while not all_complete:
        valid = True
        display_stacks(stacks)

        # Select stacks to move from and to
        range_of_stacks = f"(1-{len(stacks)})"

        try:
            move_from = get_stack_choice(f"Select a stack to move from {range_of_stacks}: ", len(stacks))
            move_to = get_stack_choice(f"Select a stack to move to {range_of_stacks}: ", len(stacks))
        except ValueError as e:
            print('Please enter valid integers for stack numbers.')
            valid = False



        # Execute the move
        if valid:
            try:
                move_item(stacks, move_from - 1, move_to - 1)
            
            except Exception as e:
                pass


        all_complete = check_completion(stacks)

    display_stacks(stacks)
    print("Congratulations! You've won the game!")
main()