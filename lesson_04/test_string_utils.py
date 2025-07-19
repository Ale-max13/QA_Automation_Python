import pytest
from string_utils import StringUtils

string_utils = StringUtils()


def test_capitalize_positive():
    result = string_utils.capitalize("skypro")
    assert result == "Skypro"


def test_capitalize_negative():
    result = string_utils.capitalize("skypro")
    assert result != "skypro"


def test_trim_positive():
    result = string_utils.trim("   skypro")
    assert result == "skypro"


def test_trim_negative():
    result = string_utils.trim("   skypro")
    assert result != "   skypro"


def test_contains_positive():
    result = string_utils.contains("SkyPro", "S")
    assert result is True


def test_contains_negative():
    result = string_utils.contains("SkyPro", "U")
    assert result is False


def test_delete_symbol_positive():
    result = string_utils.delete_symbol("SkyPro", "k")
    assert result == "SyPro"


def test_delete_symbol_negative():
    result = string_utils.delete_symbol("SkyPro", "z")
    assert result == "SkyPro"


def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


def test_contains_none_symbol():
    with pytest.raises(TypeError):
        string_utils.contains("SkyPro", None)


def test_delete_symbol_none_symbol():
    with pytest.raises(TypeError):
        string_utils.delete_symbol("SkyPro", None)
