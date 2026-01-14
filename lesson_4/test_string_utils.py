import pytest
from string_utils import StringUtils



string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

#Позитивная проверка для метода trim
@pytest.mark.parametrize("input_str, expected", [
    ("    skypro", "skypro"),
])
def test_trim_positive(input_str, expected):
    result = string_utils.trim(input_str)
    assert result == expected

#Негативная проверка для метода trim
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
])
def test_trim_negative(input_str, expected):
    result = string_utils.trim(input_str)
    assert result == expected

#Позитивные тесты для метода contains
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "P", True), #Символ "P" присутствует
    ("SkyPro", "S", True), #Символ "S" присутствует
])
def test_contains_positive(input_str, symbol, expected):
    utils = StringUtils()
    result = utils.contains(input_str, symbol)
    assert result == expected

#Негативные тесты для метода contains
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False), #Символ "U" отсутствует
    ("SkyPro", "5", False), #Символ "5" отсутствует
])
def test_contains_negative(input_str, symbol, expected):
    utils = StringUtils()
    result = utils.contains(input_str, symbol)
    assert result == expected

#Тесты для метода delete_symbol
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"), #Удаляем символ "k"
    ("SkyPro", "Pro", "Sky"), #Удаляем подстроку "Pro"
])
def test_delete_symbol_positive(input_str, symbol, expected):
    utils = StringUtils()
    result = utils.delete_symbol(input_str, symbol)
    assert result == expected

@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),  # Символ "x" отсутствует, строка остаётся неизменной
    ("SkyPro", "", "SkyPro"),  # Пустая подстрока, строка остаётся неизменной
])
def test_delete_symbol_positive(input_str, symbol, expected):
    utils = StringUtils()
    result = utils.delete_symbol(input_str, symbol)
    assert result == expected




















