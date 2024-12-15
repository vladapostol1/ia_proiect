import pytest
from math import comb
from Newton import newton_binomial

def test_base_n():
    steps, expanded_result, numeric_result = newton_binomial(2, 3, 1)
    assert expanded_result == "2 + 3"
    assert numeric_result == 5.0
    assert len(steps) > 0 

def test__n2():
    steps, expanded_result, numeric_result = newton_binomial(1, 1, 2)
    assert expanded_result == "1 * 1^2 * 1^0 + 2 * 1^1 * 1^1 + 1 * 1^0 * 1^2"
    assert numeric_result == 4.0

def test__n3():
    a, b, n = 2, 3, 3
    steps, expanded_result, numeric_result = newton_binomial(a, b, n)
    expected_expansion = (
        f"{comb(n, 0)} * {a}^{n - 0} * {b}^{0} + "
        f"{comb(n, 1)} * {a}^{n - 1} * {b}^{1} + "
        f"{comb(n, 2)} * {a}^{n - 2} * {b}^{2} + "
        f"{comb(n, 3)} * {a}^{n - 3} * {b}^{3}"
    )
    assert expanded_result == expected_expansion
    expected_numeric_result = sum(
        comb(n, k) * (a ** (n - k)) * (b ** k) for k in range(n + 1)
    )
    assert numeric_result == expected_numeric_result

def test_ase_n0():
    steps, expanded_result, numeric_result = newton_binomial(5, 5, 0)
    assert expanded_result == "1 * 5^0 * 5^0"
    assert numeric_result == 1.0

def test_large_n():
    a, b, n = 1, 2, 10
    steps, expanded_result, numeric_result = newton_binomial(a, b, n)
    expected_numeric_result = sum(
        comb(n, k) * (a ** (n - k)) * (b ** k) for k in range(n + 1)
    )
    assert numeric_result == expected_numeric_result

def test_invalid_n():
    with pytest.raises(Exception):
        newton_binomial(2, 3, -1)