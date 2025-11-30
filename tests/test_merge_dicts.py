#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import get_type_hints
import pytest
from merge_dicts import merge_dicts


def test_type_hints_exist():
    hints = get_type_hints(merge_dicts)
    assert "dict1" in hints
    assert "dict2" in hints
    assert "return" in hints


def test_type_hints_correct():
    hints = get_type_hints(merge_dicts)
    assert "Dict" in str(hints["dict1"])
    assert "Dict" in str(hints["dict2"])
    assert "Dict" in str(hints["return"])


def test_merge_dicts_correctness():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    result = merge_dicts(dict1, dict2)
    expected = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert result == expected


def test_merge_dicts_overwrite():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 20, "c": 3}
    result = merge_dicts(dict1, dict2)
    expected = {"a": 1, "b": 20, "c": 3}
    assert result == expected


def test_argument_types():
    hints = get_type_hints(merge_dicts)
    dict1_val = {"a": 1}
    dict2_val = {"b": 2}
    result = merge_dicts(dict1_val, dict2_val)
    assert isinstance(result, dict)
    assert isinstance(dict1_val, dict)
    assert isinstance(dict2_val, dict)


def test_merge_dicts_different_value_types():
    dict1 = {"a": 1, "b": "hello"}
    dict2 = {"c": 3.14, "d": [1, 2, 3]}
    result = merge_dicts(dict1, dict2)
    expected = {"a": 1, "b": "hello", "c": 3.14, "d": [1, 2, 3]}
    assert result == expected
