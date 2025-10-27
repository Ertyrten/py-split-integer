import pytest
from app.split_integer import split_integer


# --- Конкретні, детерміновані тести для читабельності ---

def test_split_into_single_part() -> None:
    """Перевіряє випадок з однією частиною."""
    assert split_integer(8, 1) == [8]


def test_split_evenly_when_divisible() -> None:
    """Перевіряє випадок рівного поділу."""
    assert split_integer(6, 2) == [3, 3]


def test_split_unevenly() -> None:
    """Перевіряє загальний випадок нерівного поділу."""
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_value_equals_number_of_parts() -> None:
    """Перевіряє властивість, що при n/n результат - це n одиниць."""
    n = 5
    result = split_integer(n, n)
    assert len(result) == n
    assert all(part == 1 for part in result)


def test_value_less_than_parts_produces_zeros() -> None:
    """Перевіряє, що для 3/5 результат містить нулі: [0, 0, 1, 1, 1]."""
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


# --- Властивісний тест для перевірки загальних правил ---

@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (32, 6),     # Загальний випадок
        (100, 10),   # Ідеальне ділення
        (0, 3),      # Нульове значення
        (25, 4),     # Ще один загальний випадок
    ]
)
def test_split_integer_properties(value: int, number_of_parts: int) -> None:
    """
    Перевіряє ключові властивості результату
    для різних вхідних даних.
    """
    result = split_integer(value, number_of_parts)

    # Властивість 1: Кількість частин має бути правильною
    assert len(result) == number_of_parts

    # Властивість 2: Сума частин має дорівнювати вихідному значенню
    assert sum(result) == value

    # Властивість 3: Різниця між max і min не більше 1
    if len(result) > 1:
        assert max(result) - min(result) <= 1

    # Властивість 4: Результат має бути відсортовано
    assert result == sorted(result)
    
    # Властивість 5: Всі елементи - цілі невід'ємні числа
    assert all(isinstance(x, int) and x >= 0 for x in result)
