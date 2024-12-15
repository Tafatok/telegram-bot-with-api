
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
    После вставляем код ниже:
    ```-- Создание таблицы чатов
CREATE TABLE IF NOT EXISTS chats (
    chat_id INTEGER PRIMARY KEY
);

-- Вставка тестовых данных в таблицу чатов
INSERT INTO chats (chat_id) VALUES (1);
INSERT INTO chats (chat_id) VALUES (2);
INSERT INTO chats (chat_id) VALUES (3);

-- Создание таблицы пользователей
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    lastname TEXT,
    chat_id INTEGER,
    FOREIGN KEY (chat_id) REFERENCES chats(chat_id) ON DELETE CASCADE
);

-- Вставка тестовых данных в таблицу пользователей
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (1, 'Alice', 'Smith', 1);
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (2, 'Bob', 'Johnson', 1);
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (3, 'Charlie', 'Brown', 2);
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (4, 'David', 'Williams', 2);
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (5, 'Eve', 'Davis', 3);
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (6, 'Frank', 'Miller', 3);
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (7, 'Grace', 'Wilson', 1);
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (8, 'Hannah', 'Moore', 2);
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (9, 'Ivy', 'Taylor', 3);
INSERT INTO users (user_id, name, lastname, chat_id) VALUES (10, 'Jack', 'Anderson', 1);

-- Создание таблицы сообщений
CREATE TABLE IF NOT EXISTS messages (
    message_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    chat_id INTEGER,
    message TEXT,
    timestamp TEXT,
    media_type TEXT,
    media_url TEXT,
    file_id TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (chat_id) REFERENCES chats(chat_id) ON DELETE CASCADE
);

-- Вставка тестовых данных в таблицу сообщений
INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (1, 1, 'Hello!', '2024-12-15 10:00:00', 'text', NULL, NULL);

INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (2, 1, 'Hi Alice!', '2024-12-15 10:05:00', 'text', NULL, NULL);

INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (3, 2, 'Hey there!', '2024-12-15 11:00:00', 'text', NULL, NULL);

INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (4, 2, 'How are you?', '2024-12-15 11:10:00', 'text', NULL, NULL);

INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (5, 3, 'Good morning!', '2024-12-15 12:00:00', 'text', NULL, NULL);

INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (6, 3, 'Morning Eve!', '2024-12-15 12:05:00', 'text', NULL, NULL);

INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (7, 1, 'Hi everyone!', '2024-12-15 13:00:00', 'text', NULL, NULL);

INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (8, 2, 'Hello David!', '2024-12-15 13:10:00', 'text', NULL, NULL);

INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (9, 3, 'Ivy here!', '2024-12-15 14:00:00', 'text', NULL, NULL);

INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id) 
VALUES (10, 1, 'How’s everyone doing?', '2024-12-15 14:10:00', 'text', NULL, NULL);
```