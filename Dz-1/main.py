import requests


def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        # Отправляем GET-запрос к TheCatAPI
        response = requests.get(url)
        # Проверяем, что статус код ответа 200 (OK)
        if response.status_code == 200:
            data = response.json()
            # Проверяем, что данные не пустые и возвращаем URL изображения
            if data:
                return data[0]['url']
        return None
    except requests.RequestException:
        # В случае исключения возвращаем None
        return None
