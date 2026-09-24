# utils.py

def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Помилка! Введіть коректне ціле число.")

def get_bool(prompt: str) -> bool:
    while True:
        val = input(prompt).strip().lower()
        if val in ['так', 'y', 'yes', '1']:
            return True
        if val in ['ні', 'n', 'no', '0']:
            return False
        print("Помилка! Введіть 'так' або 'ні'.")