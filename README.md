# Random Action Selector API

Простой REST API на FastAPI для хранения и случайного выбора действий.  
Данные сохраняются в `action.json`.  
Поддерживается добавление/удаление/просмотр всех действий и получение случайного (без повтора подряд).

## Требования

- Python 3.8+
- FastAPI (0.135.0)
- Uvicorn (для запуска сервера)

## Установка зависимостей

Рекомендуется использовать виртуальное окружение.

```bash
# 1. Создать виртуальное окружение (если нужно)
python -m venv venv
source venv/bin/activate      # Linux/macOS
# или
venv\Scripts\activate         # Windows

# 2. Установить FastAPI и Uvicorn (конкретная версия)
pip install fastapi==0.135.0 uvicorn