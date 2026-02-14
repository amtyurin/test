import pytest
from sort import sort


def test_standard_small_package():
    assert sort(10, 10, 10, 5) == "STANDARD"
    assert sort(1, 1, 1, 0.1) == "STANDARD"


def test_standard_just_under_thresholds():
    assert sort(99, 99, 99, 19) == "STANDARD"
    assert sort(149, 10, 10, 19.9) == "STANDARD"


def test_bulky_by_volume():
    # 100^3 = 1,000,000 exactly
    assert sort(100, 100, 100, 5) == "SPECIAL"
    assert sort(200, 200, 200, 5) == "SPECIAL"


def test_bulky_by_dimension():
    assert sort(150, 1, 1, 5) == "SPECIAL"
    assert sort(10, 150, 10, 1) == "SPECIAL"
    assert sort(10, 10, 150, 1) == "SPECIAL"
    assert sort(200, 1, 1, 1) == "SPECIAL"


def test_heavy():
    assert sort(10, 10, 10, 20) == "SPECIAL"
    assert sort(10, 10, 10, 50) == "SPECIAL"


def test_rejected_bulky_and_heavy():
    assert sort(100, 100, 100, 20) == "REJECTED"
    assert sort(150, 1, 1, 20) == "REJECTED"
    assert sort(200, 200, 200, 100) == "REJECTED"


def test_floats():
    assert sort(99.9, 99.9, 99.9, 5) == "STANDARD"
    assert sort(10, 10, 10, 19.99) == "STANDARD"
    assert sort(10, 10, 10, 20.0) == "SPECIAL"
    assert sort(100.0, 100.0, 100.0, 1) == "SPECIAL"


def test_zeroes():
    assert sort(0, 0, 0, 0) == "STANDARD"
    assert sort(0, 0, 0, 20) == "SPECIAL"
    assert sort(150, 150, 150, 0) == "SPECIAL"


def test_rejects_negative_values():
    with pytest.raises(ValueError):
        sort(-1, 10, 10, 5)
    with pytest.raises(ValueError):
        sort(10, 10, 10, -5)


def test_rejects_bad_types():
    with pytest.raises(TypeError):
        sort("ten", 10, 10, 5)
    with pytest.raises(TypeError):
        sort(10, 10, 10, None)
