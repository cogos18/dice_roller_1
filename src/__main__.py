# File name: __main__.py | Date: 26/07/2025
# Made by cogos18
from random import randint
from visuals import dice_art


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


def main() -> None:
    # Get the amount of dice from the user
    dice_amount: int = get_dice_amount()

    if dice_amount < 1 or dice_amount > 6:
        print("Please choose an amount between 1 and 6.")
        raise SystemExit(1)

    dice_result: list[int] = roll_dice(dice_amount)
    print(dice_result)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass