# Проект парсинга pep на Scrapy

Проект содержит парсер PEP основанный на фреймворке Scrapy, собирвает данные обо всех документах PEP, считает количество PEP в каждом статусе и общее количество PEP, сохраняет результат в табличном виде в csv-файл.

## Начало работы

Эти инструкции помогут вам склонировать репозиторий и настроить виртуальное окружение для разработки.

### Предварительные требования

Убедитесь, что на вашем компьютере установлены следующие программы:

- [Git](https://git-scm.com/downloads)
- [Python 3.9+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Установка

1. **Клонируйте репозиторий:**

   Откройте терминал и выполните команду:

   ```bash
   git clone https://github.com/k0sdm1/scrapy_parser_pep.git
   ```

2. **Перейдите в директорию проекта:**
   ```bash
   cd scrapy_parser_pep
   ```

3. **Создайте виртуальное окружение:**
    ```bash
    python -m venv venv  //Windows
    python3 -m venv venv  //Linux
    ```

4. **Активируйте виртуальное окружение:**

    Windows
    ```bash
    .\venv\Scripts\activate
    ```
    Linux
    ```bash
    source venv/bin/activate
    ```

5. **Установите зависимостей:**

    ```bash
    pip install -r requirements.txt
    ```

### Запуск и использование

1. **Для запуска находясь в основной директории выполните команду.**

    ```bash
    scrapy crawl pep
    ```

## Автор

Парсер PEP: [k0sdm1](https://github.com/k0sdm1)