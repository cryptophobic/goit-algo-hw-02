import sys
from collections import deque

if __name__ == "__main__":
    string = input("Будь ласка, введіть рядок для аналізу на те, чи є він паліндромом")
    queue = deque(string.strip().lower())
    length = len(queue)
    for i in range(length // 2):
        if queue.popleft() != queue.pop():
            print(f"Слово {string} - це ніякий не паліндром\nбо починаючи із символа '{string[i]}' під номером {i} букви не збігаються")
            sys.exit(0)

    print(f"Слово {string} - це паліндром")
