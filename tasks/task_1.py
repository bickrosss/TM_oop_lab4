#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import get_type_hints
from coords import get_coords

def main():
    point_val = (3.5, 2.7)
    result = get_coords(point_val)
    func_hints = get_type_hints(get_coords)
    actual_point = type(point_val)
    actual_return = type(result)
    
    print(f"Результат вызова функции get_coords: {result}")
    print(f"Тип аргумента 'point': ожидается {func_hints['point']}, получен {actual_point}")
    print(f"Тип возвращаемого значения: ожидается {func_hints['return']}, получен {actual_return}")

if __name__ == "__main__":
    main()
