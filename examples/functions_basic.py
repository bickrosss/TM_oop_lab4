from typing import Tuple

def min_max(values: list[int]) -> Tuple[int, int]:
    return min(values), max(values)

def min_max(values: list[int]) -> tuple[int, int]:
    return min(values), max(values)

def log_message(msg: str) -> None:
    print(f"LOG {msg}")

def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)
