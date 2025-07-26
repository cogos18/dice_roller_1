# File name: __main__.py | Date: 26/07/2025
# Made by cogos18


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


def main() -> None:
    # Get the amount of dice from the user
    dice_amount: int = get_dice_amount()

    if dice_amount < 1 or dice_amount > 6:
        print("Please choose an amount between 1 and 6.")
        raise SystemExit(1)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass