CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER PRIMARY KEY);
INSERT INTO chats VALUES (1);

CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, name TEXT, lastname TEXT, chat_id INTEGER, FOREIGN KEY (chat_id) REFERENCES chats(chat_id) ON DELETE CASCADE);
INSERT INTO users VALUES (1, 'Alice', 'Smith', 1);

CREATE TABLE IF NOT EXISTS messages (message_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, chat_id INTEGER, message TEXT, timestamp TEXT, media_type TEXT, media_url TEXT, file_id TEXT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, FOREIGN KEY (chat_id) REFERENCES chats(chat_id) ON DELETE CASCADE);
INSERT INTO messages VALUES (1, 1, 1, 'Hello!', '2024-12-15 10:00:00', 'text', NULL, NULL);
