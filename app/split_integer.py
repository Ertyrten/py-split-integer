from app.split_integer import split_integer  # <-- ОСНОВНЕ ВИПРАВЛЕННЯ


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


# --- НОВІ ТЕСТИ, ЯКІ ВИ ЗАПРОПОНУВАЛИ ---

def test_result_has_correct_length() -> None:
    """Перевіряє, що масив має правильну кількість частин."""
    value = 17
    parts = 4
    result = split_integer(value, parts)
    assert len(result) == parts


def test_parts_sum_equals_original_value() -> None:
    """Перевіряє, що сума частин дорівнює вихідному значенню."""
    value = 32
    parts = 6
    result = split_integer(value, parts)
    assert sum(result) == value


def test_zero_value() -> None:
    """Додатковий тест: перевірка з нульовим значенням."""
    assert split_integer(0, 3) == [0, 0, 0]
