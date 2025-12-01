#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import get_type_hints
import pytest
from coords import get_coords


def test_type_hints_exist():
    hints = get_type_hints(get_coords)
    assert "point" in hints
    assert "return" in hints


def test_type_hints_correct():
    hints = get_type_hints(get_coords)
    assert str(hints["point"]) == "tuple[float, float]"
    assert hints["return"] == str


def test_get_coords_correctness():
    assert get_coords((3.5, 2.7)) == "x=3.5, y=2.7"
    assert get_coords((0.0, 0.0)) == "x=0.0, y=0.0"
    assert get_coords((-1.5, -3.2)) == "x=-1.5, y=-3.2"


def test_argument_types():
    hints = get_type_hints(get_coords)
    point_val = (3.5, 2.7)
    result = get_coords(point_val)
    assert isinstance(result, hints["return"])
    assert isinstance(point_val, tuple)


def test_get_coords_with_integers():
    # Целые числа должны работать, так как они совместимы с float
    assert get_coords((10, 20)) == "x=10, y=20"
