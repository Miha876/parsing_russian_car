import requests
from bs4 import BeautifulSoup

url = "https://greenway.icnet.ru/cars-sales-actual-russia.html"

headers = {
    'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()


    soup = BeautifulSoup(response.text, 'html.parser')

    popular_cars = []

    car_data_rows = soup.find_all('tr')
    for row in car_data_rows:
        columns = row.find_all('td')
        if len(columns) >= 2:
            model = columns[1].get_text(strip=True)
            if model and model not in ["Марка", "Модель"]:
                popular_cars.append(model)


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