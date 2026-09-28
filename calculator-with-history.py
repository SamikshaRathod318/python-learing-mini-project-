from pathlib import Path
import re


HISTORY_FILE = Path(__file__).resolve().parent / "history.txt"


def show_history():
    with HISTORY_FILE.open("r") as file:
        lines = file.readlines()
    if not lines:
        print("No history found.")
    else:
        for line in reversed(lines):
            print(line.strip())


def clear_history():
    with HISTORY_FILE.open("w"):
        pass
    print("History cleared.")


def save_to_history(equation, result):
    with HISTORY_FILE.open("a") as file:
        file.write(equation + " = " + str(result) + "\n")


def calculate(user_input):
    match = re.fullmatch(
        r"\s*=?\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*([+\-*/])\s*"
        r"([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*",
        user_input,
    )
    if match is None:
        print("Invalid input. Please enter in the format: number1 operator number2")
        return
    num1 = float(match.group(1))
    op = match.group(2)
    num2 = float(match.group(3))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    if result.is_integer():
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)


def main():
    HISTORY_FILE.touch(exist_ok=True)
    print('simple calculator (type history, clear, or exit to quit)')
    while True:
        user_input = input("Enter calculation(+ - * /)or command(history, clear, exit)= ")
        if user_input.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)


if __name__ == "__main__":
    main()