from src.main import add
import pytest

def test_add():
    assert add(2, 3) == 5

def test_add_basic():
    assert add(1, 1) == 2
    assert add(0, 5) == 5
    assert add(10, -3) == 7

def test_add_large_numbers():
    assert add(1000000, 1000000) == 2000000
    assert add(-1000000, -1000000) == -2000000

def test_add_with_zero():
    assert add(0, 0) == 0
    assert add(0, 100) == 100
    assert add(100, 0) == 100


def test_add_invalid_inputs():
    with pytest.raises(TypeError):
        add("hello", 5)
    with pytest.raises(TypeError):
        add(5, None)
    with pytest.raises(TypeError):
        add([1, 2], 3)

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)  # 小数の計算は誤差を許容する
    assert add(-0.1, 0.1) == pytest.approx(0.0)

def test_add_negative_numbers():
    assert add(-5, -3) == -8
    assert add(-10, 5) == -5
