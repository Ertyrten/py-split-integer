import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (3, 5),
        (100, 10),
        (0, 3),
    ]
)
def test_split_integer_properties(value: int, number_of_parts: int) -> None:
    """
    ## ПОКРАЩЕНО:
    Цей тест перевіряє ключові властивості результату
    для різних вхідних даних.
    """
    result = split_integer(value, number_of_parts)

    # 1. Перевірка, що кількість частин правильна
    assert len(result) == number_of_parts

    # 2. Перевірка, що сума частин дорівнює вихідному значенню
    assert sum(result) == value

    # 3. Перевірка, що різниця між max і min не більше 1
    if len(result) > 1:
        assert max(result) - min(result) <= 1

    # 4. Перевірка, що результат відсортовано
    assert result == sorted(result)
