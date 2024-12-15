## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Tafatok/telegram-bot-with-api

    После перейдите в дерикторию cd telegram-bot-with-api

    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv myenv или python3 -m venv myenv (зависит от версии python установленной на ваш компьютер)
    source myenv/bin/activate  # Для Windows используйте `myenv\Scripts\activate`

    # Установите зависимости
    pip install -r requirements.txt
    ```

3. Запустите проект:
    ```bash
    Для запуска бота
    python main.py
    Дальше находим бота в телеграме @elegramufaapibot и запускаем.

    Для запуска API после перейдите по ссылке 
    uvicorn main:app --reload
    Дальше переходим http://127.0.0.1:8000/docs и запускаем нужные нам функции
    ```
