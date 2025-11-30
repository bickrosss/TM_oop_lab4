#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import get_type_hints
from merge_dicts import merge_dicts

def main():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    result = merge_dicts(dict1, dict2)
    func_hints = get_type_hints(merge_dicts)
    actual_dict1 = type(dict1)
    actual_dict2 = type(dict2)
    actual_return = type(result)
    
    print(f"Первый словарь: {dict1}")
    print(f"Второй словарь: {dict2}")
    print(f"Результат объединения: {result}")
    print(f"Тип аргумента 'dict1': ожидается {func_hints['dict1']}, получен {actual_dict1}")
    print(f"Тип аргумента 'dict2': ожидается {func_hints['dict2']}, получен {actual_dict2}")
    print(f"Тип возвращаемого значения: ожидается {func_hints['return']}, получен {actual_return}")

if __name__ == "__main__":
    main()
