# File name: __main__.py | Date: 26/07/2025
# Made by cogos18
from random import randint
from visuals import dice_art, die_height, die_width, die_separator


# Get the amount of dice from the user
def get_dice_amount() -> int:
    dice_amount: int
    user_input: str = input("How many dice do you want to throw? [1-6]: ").strip()

    if len(user_input) <= 0:
        raise SystemExit(0)
    
    try:
        dice_amount = int(user_input)
    except ValueError:
        print("Please enter a valid amount.")
        raise SystemExit(1)

    return dice_amount


# Try and roll the amount of dice
def roll_dice(amount: int) -> list[int]:
    dice_numbers: list[int] = []

    for _ in range(amount):
        dice_numbers.append(randint(1, 6)) 
    
    return dice_numbers


# Create a visual representation of the rolled dice.
def generate_visual_for_rolled_dice(rolled_dice: list) -> str:
    dice_faces: list = []
    for die in rolled_dice:
        dice_faces.append(dice_art[die])   

    dice_face_rows: list = []
    for row_index in range(die_height):
        row_components: list = []

        for die in dice_faces:
            row_components.append(die[row_index])

        row_output: str = die_separator.join(row_components)
        dice_face_rows.append(row_output)

    
    width: int = len(dice_face_rows[0])
    output_header: str = " Results ".center(width, "─")

    output: str = "\n".join([output_header + "\n"] + dice_face_rows)
    return output

    


def main() -> None:
    # Get the amount of dice from the user
    dice_amount: int = get_dice_amount()

    if dice_amount < 1 or dice_amount > 6:
        print("Please choose an amount between 1 and 6.")
        raise SystemExit(1)

    dice_result: list[int] = roll_dice(dice_amount)
    print(generate_visual_for_rolled_dice(dice_result))


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass