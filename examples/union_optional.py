from typing import Union

def normalize(value: Union[int, float, str]) -> float:
    if isinstance(value, str):
        value = value.replace(",", "")
    return float(value)

def normalize(value: int | float | str) -> float:
    if isinstance(value, str):
        value = value.replace(",", "")
    return float(value)

from typing import Optional

def find_user_id(name: str) -> Optional[int]:
    users = {"Alice": 1, "Bob": 2}
    return users.get(name)

uid = find_user_id("Charlie")
print(uid + 1)
