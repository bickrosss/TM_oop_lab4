from typing import Any

def show(value: Any) -> None:
    print(f"Получено значение: {value}")

from typing import NoReturn
import sys

def fatal_error(msg: str) -> NoReturn:
    print(f"Фатальная ошибка: {msg}")
    sys.exit(1)

fatal_error("Ошибка конфигурации!")
