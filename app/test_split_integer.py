from app.main import split_integer  # Імпорт pytest видалено


def test_split_integer_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_integer_even_division() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_small_uneven_division() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_larger_uneven_division() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_integer_value_less_than_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_split_integer_perfect_division() -> None:
    assert split_integer(100, 10) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
