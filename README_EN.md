# Greenway Car Sales Parser

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-2.28.1-green?logo=)](https://pypi.org/project/requests/)
[![BeautifulSoup4](https://img.shields.io/badge/Beautiful_Soup-4.11.1-lightgrey?logo=)](https://pypi.org/project/beautifulsoup4/)

English | [Русский](README.md)

A Python web scraper for parsing actual car sales data in Russia from the greenway.icnet.ru website.

## 🚀 Features

*   **Data Collection:** Automated scraping of the most popular car models.
*   **HTML Processing:** Utilizes BeautifulSoup for efficient parsing and data extraction from HTML tables.
*   **Error Handling:** Robust handling of network errors and exceptions for reliable script execution.
*   **Human-Readable Output:** Displays results in a user-friendly format in the console.

## 📦 Installation & Dependencies

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/greenway-car-parser.git
    cd greenway-car-parser
    ```

2.  **Install required libraries (it's recommended to use a virtual environment):**
    ```bash
    pip install -r requirements.txt
    ```
    *Contents of the `requirements.txt` file:*
    ```
    requests==2.28.1
    beautifulsoup4==4.11.1
    ```

## 🛠 Usage

Run the script directly from the command line:

```bash
python car_parser.py
Upon successful execution, the script will output a list of popular car models to the console:

text
Самые популярные автомобили: (The most popular cars:)
Модель: Hyundai Creta
Модель: Lada Vesta
Модель: Kia Rio
...
📁 Project Structure
text
greenway-car-parser/
├── car_parser.py      # Main parser script
├── requirements.txt   # Dependencies file
├── README.md          # Documentation in Russian
├── README_EN.md       # This file (English)
└── LICENSE            # License file
⚙️ How It Works
The script sends an HTTP GET request to the target URL https://greenway.icnet.ru/cars-sales-actual-russia.html, using predefined headers (User-Agent) to mimic a real web browser.

The retrieved HTML page content is passed to BeautifulSoup for parsing.

The parser finds all table rows (<tr>) and within each row, it searches for data cells (<td>).

The text (car model name) is extracted from the second cell of each row.

Filtering is applied: table headers ("Марка", "Модель" which mean "Brand", "Model") and empty values are excluded.

The final list of models is printed to the screen.

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements:

Fork the repository.

Create a feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

⚠️ Important Notice
This script is intended for educational purposes only. Before using it on any website, please:

Check the target website's robots.txt file (e.g., https://greenway.icnet.ru/robots.txt).

Ensure your actions comply with the website's Terms of Service.

Implement delays between requests to avoid overloading the server.

Respect data ownership and copyright.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
