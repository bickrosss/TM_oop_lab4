from typing import TypeVar, List

T = TypeVar("T")
def first(items: List[T]) -> T:
    return items[0]

from typing import Generic

T = TypeVar("T")
class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value
    def get(self) -> T:
        return self.value

b1 = Box[int](10)
b2 = Box[str]("Hello")
print(b1.get())
print(b2.get())
