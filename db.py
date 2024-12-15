import sqlite3
import atexit
import datetime
def init_db():
    global connection, cursor

    # Подключение к базе данных
    connection = sqlite3.connect('telegram_message.db', check_same_thread=False)
    cursor = connection.cursor()

    # Создание таблицы chats (если она отсутствует)
    command_chats = """
    CREATE TABLE IF NOT EXISTS chats (
        chat_id INTEGER PRIMARY KEY
    )
    """
    cursor.execute(command_chats)

    # Создание таблицы users (если она отсутствует)
    command_users = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        lastname TEXT,
        chat_id INTEGER,
        FOREIGN KEY (chat_id) REFERENCES chats(chat_id) ON DELETE CASCADE
    )
    """
    cursor.execute(command_users)

    # Создание таблицы messages (если она отсутствует)
    command_messages = """
    CREATE TABLE IF NOT EXISTS messages (
        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        chat_id INTEGER,
        message TEXT,
        timestamp TEXT,
        media_type TEXT,   -- Тип медиа (фото, видео, аудио и т. д.)
        media_url TEXT,    -- Ссылка на медиафайл или путь
        file_id TEXT,      -- Идентификатор медиафайла (например, для фото)
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
        FOREIGN KEY (chat_id) REFERENCES chats(chat_id) ON DELETE CASCADE
    )
    """

    cursor.execute(command_messages)

    connection.commit()


def get_db_connection():
    return sqlite3.connect('telegram_message.db', check_same_thread=False)

# Проверка, существует ли пользователь в базе данных чата
def check(user_id, chat_id):
    cursor.execute("SELECT 1 FROM users WHERE user_id = ? AND chat_id = ?", (user_id, chat_id))
    result = cursor.fetchone()
    return result is not None

# Добавление нового чата
def add_chat(chat_id):
    cursor.execute("INSERT INTO chats (chat_id) VALUES (?)", (chat_id,))
    connection.commit()
    print(f"Новый чат добавлен с chat_id: {chat_id}")
    return chat_id

# Добавление нового пользователя в чат
def add_user(user_id, name, lastname, chat_id):
    if not check(user_id, chat_id):
        cursor.execute("INSERT INTO users (user_id, name, lastname, chat_id) VALUES (?, ?, ?, ?)", 
                       (user_id, name, lastname, chat_id))
        connection.commit()
        print(f"Новый пользователь добавлен с user_id: {user_id} в чат {chat_id}")
        return user_id
    else:
        print(f"Пользователь с user_id: {user_id} уже существует в чате {chat_id}")

def add_message(user_id, chat_id, message, media_type=None, media_url=None, file_id=None):
    # Получаем имя и фамилию пользователя
    cursor.execute("SELECT name, lastname FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    
    if user:
        name, lastname = user
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute("""
        INSERT INTO messages (user_id, chat_id, message, timestamp, media_type, media_url, file_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user_id, chat_id, message, timestamp, media_type, media_url, file_id))

        connection.commit()
        print(f"Сообщение добавлено для {name} {lastname} в чат {chat_id} с временной меткой {timestamp}")
    else:
        print(f"Пользователь с user_id: {user_id} не найден.")

# Закрытие соединения с базой данных
def close_db():
    global connection
    if connection:
        connection.close()









init_db()

atexit.register(close_db)
