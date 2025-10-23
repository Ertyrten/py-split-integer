from app.split_integer import split_integer  # <-- ОСНОВНЕ ВИПРАВЛЕННЯ


def test_split_integer_single_part() -> None:
    """Tests splitting into a single part."""
    assert split_integer(8, 1) == [8]


def test_split_integer_even_division() -> None:
    """Tests even division into multiple parts."""
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_small_uneven_division() -> None:
    """Tests uneven division with a small remainder."""
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_integer_larger_uneven_division() -> None:
    """Tests uneven division with a larger remainder."""
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_integer_value_less_than_parts() -> None:
    """Tests when the value is smaller than the number of parts."""
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_split_integer_perfect_division() -> None:
    """Tests a case of perfect division."""
    assert split_integer(100, 10) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def test_result_has_correct_length() -> None:
    """Checks that the result list has the correct number of parts."""
    value = 25
    parts = 7
    result = split_integer(value, parts)
    assert len(result) == parts


def test_parts_sum_equals_original_value() -> None:
    """Checks that the sum of the parts equals the original value."""
    value = 48
    parts = 9
    result = split_integer(value, parts)
    assert sum(result) == value


def test_zero_value() -> None:
    """Checks the behavior with a zero value."""
    assert split_integer(0, 5) == [0, 0, 0, 0, 0]
