from data_loader import load_adventure

import time

TIME_BETWEEN_CHARACTERS = 0
TIME_BETWEEN_LINES = 0
# TIME_BETWEEN_CHARACTERS = 0.05
# TIME_BETWEEN_LINES = 0.8

def cool_print(text):
    for x in text:
        print(x, end='')
        time.sleep(TIME_BETWEEN_CHARACTERS)
    print()

# Load Adventure Data
first_scene_name, scene_data = load_adventure("adventure.json")
current_scene = scene_data[first_scene_name]

# Start Adventure
def list_actions(actions):
    number = 1
    for action in actions:
        cool_print(str(number)+") "+action.command)
        number += 1


def get_user_action(n):
    while True:
        choice = input("Enter choice (1-"+str(n)+"): ")
        try:
            chosen_number = int(choice)
            if 1 <= chosen_number <= n:
                return chosen_number

            print("Invalid choice.  Please enter a number between 1-"+str(n)+".")

        except ValueError:
            cool_print("Please enter a number")


while True:
    # Print Scene description
    print()
    cool_print(current_scene.description)

    # Check for end, i.e. no actions
    if not current_scene.actions:
        exit()

    # Show action
    list_actions(current_scene.actions)

    # Get user action from input
    choice = get_user_action(len(current_scene.actions))
    action = current_scene.actions[int(choice)-1]
    current_scene = scene_data[action.next_scene]
