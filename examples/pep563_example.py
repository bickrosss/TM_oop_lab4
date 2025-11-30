class Rectangle:
    def __init__(self, width: int, height: int, color: Color):
        self.width = width
        self.height = height
        self.color = color

class Rectangle:
    def __init__(self, width: int, height: int, color: "Color") -> None:
        self.width = width
        self.height = height
        self.color = color

from __future__ import annotations

class Rectangle:
    def __init__(self, width: int, height: int, color: Color):
        self.width = width
        self.height = height
        self.color = color

class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b
