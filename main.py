import requests
from bs4 import BeautifulSoup

# URL страницы
url = "https://greenway.icnet.ru/cars-sales-actual-russia.html"

# Запрос к странице с заголовком User-Agent
headers = {
    'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Запрос к странице
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Проверяем статус ответа

    # Парсим HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Список для хранения данных
    popular_cars = []

    # Ищем данные о марках и моделях
    car_data_rows = soup.find_all('tr')  # Пример: строки таблицы
    for row in car_data_rows:
        # Ищем конкретные ячейки таблицы
        columns = row.find_all('td')  # Пример: ячейки строки
        if len(columns) >= 2:  # Убедимся, что есть как минимум 2 колонки (марка и модель)
            model = columns[1].get_text(strip=True)  # Получаем только модель
            if model and model not in ["Марка", "Модель"]:  # Проверяем, что модель не пустая и не является заголовком
                popular_cars.append(model)  # Добавляем только модель в список

    # Выводим результат
    if popular_cars:
        print("Самые популярные автомобили:")
        for model in popular_cars:
            print(f"Модель: {model}")
    else:
        print("Нет доступных моделей для отображения.")
except requests.RequestException as e:
    print(f"Ошибка при запросе данных: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")