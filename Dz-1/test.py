import pytest
from unittest.mock import Mock
import requests
from main import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    # Мокаем метод requests.get
    mock_response = Mock()
    expected_url = "https://cdn2.thecatapi.com/images/123.jpg"
    mock_response.status_code = 200
    mock_response.json.return_value = [{"url": expected_url}]

    # Заменяем requests.get на нашу замоканную версию
    mocker.patch('requests.get', return_value=mock_response)

    # Вызываем тестируемую функцию
    result = get_random_cat_image()

    # Проверяем, что результат соответствует ожидаемому URL
    assert result == expected_url


def test_get_random_cat_image_failure(mocker):
    # Мокаем метод requests.get, чтобы он возвращал статус код 404
    mock_response = Mock()
    mock_response.status_code = 404

    # Заменяем requests.get на нашу замоканную версию
    mocker.patch('requests.get', return_value=mock_response)

    # Вызываем тестируемую функцию
    result = get_random_cat_image()

    # Проверяем, что результат - None при статусе 404
    assert result is None


def test_get_random_cat_image_exception(mocker):
    # Мокаем метод requests.get, чтобы он вызывал исключение RequestException
    mocker.patch('requests.get', side_effect=requests.RequestException)

    # Вызываем тестируемую функцию
    result = get_random_cat_image()

    # Проверяем, что результат - None при исключении
    assert result is None
