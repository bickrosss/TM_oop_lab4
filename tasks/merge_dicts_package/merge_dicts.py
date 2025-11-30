
from typing import Dict, TypeVar

K = TypeVar('K')
V = TypeVar('V')

def merge_dicts(dict1: Dict[K, V], dict2: Dict[K, V]) -> Dict[K, V]:
    result = dict1.copy()
    result.update(dict2)
    return result
