import pytest
from app.split_integer import split_integer  # <-- ОСНОВНЕ ВИПРАВЛЕННЯ


def test_specific_examples() -> None:
    """
    Перевіряє конкретні приклади, наведені в умові завдання.
    """
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (3, 5),
        (100, 10),
        (0, 3),
        (25, 4),
    ]
)
def test_split_integer_properties(value: int, number_of_parts: int) -> None:
    """
    Перевіряє ключові властивості результату
    для різних вхідних даних.
    """
    result = split_integer(value, number_of_parts)

    # 1. Кількість частин має бути правильною
    assert len(result) == number_of_parts

    # 2. Сума частин має дорівнювати вихідному значенню
    assert sum(result) == value

    # 3. Різниця між max і min не більше 1
    if len(result) > 1:
        assert max(result) - min(result) <= 1

    # 4. Результат має бути відсортовано
    assert result == sorted(result)
