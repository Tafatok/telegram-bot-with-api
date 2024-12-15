## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/ваш-логин/ваш-репозиторий.git
    cd ваш-репозиторий
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # Для Windows используйте `myenv\Scripts\activate`

    # Установите зависимости
    pip install -r requirements.txt
    ```

3. Запустите проект:
    ```bash
    uvicorn main:app --reload
    ```
