
### Внимание у вас уже должен быть установлен Python(https://www.python.org/downloads/) и Sqlite3
## Установка

1. Клонируйте репозиторий:
    
    ```git clone https://github.com/Tafatok/telegram-bot-with-api```

    После перейдите в дерикторию cd telegram-bot-with-api

    

2. Создайте и активируйте виртуальное окружение:
    
    ```python -m venv myenv``` или ```python3 -m venv myenv``` (зависит от версии python установленной на ваш компьютер)
   
   Теперь активируем наше окружение:
   ```source myenv/bin/activate```  # Для Windows используйте ```myenv\Scripts\activate```

   Установите зависимости
    ```pip install -r requirements.txt```
   

4. Запустите проект:
    
    Для запуска бота
    ```python main.py```
    Дальше находим бота в телеграме ```@elegramufaapibot``` и запускаем.
    ###База данных поднимается вместе с ботом.
   
    Для запуска API
    ```uvicorn main:app --reload```
    Дальше переходим http://127.0.0.1:8000/docs и запускаем нужные нам функции
    


5. SQL-дамп с тестовыми даннами
    После запуска телеграм бота, появляется база данных telegram_message.db
    Мы открывае cmd и пишем:
    ```sqlite3 telegram_message.db```
    После вставляем код из файла sql_d.txt
    `
