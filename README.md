<div align=center>
    
# Приложение Coin Flow

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/fastapi-005571?style=for-the-badge&logo=fastapi)
![Pydantic](https://img.shields.io/badge/Pydantic-black?style=for-the-badge&logo=pydantic&logoColor=red)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=black&logoSize=auto)

</div>

## Описание проекта

API позволяет создавать, просматривать и обновлять кошельки. Все операции выполняются асинхронно с использованием FastAPI и SQLAlchemy для взаимодействия с базой данных.

### Технологии

- **Python**

- **FastAPI**: Веб-фреймворк для создания API на Python.
- **SQLAlchemy**: Библиотека для работы с базами данных.
- **Pydantic**: Для валидации данных и сериализации моделей.
- **Alembic**: Инструмент для управления миграциями баз данных.
- **Uvicorn**: - ASGI веб-сервер для python.
- **PostgreSQL**: - База данных.

<details>

<summary>
<h4>Как запустить проект локально:</h4>
</summary>

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:JustLight1/coin-flow.git
```

```bash
cd coin-flow
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

или для пользователей Windows

```bash
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Создать файл `.env` и заполнить его по примеру из файла `.env.example.dev`

Применить миграции

```bash
alembic upgrade head
```

Запустить проект:

```bash
uvicorn app.main:app --reload
```

После запуска станет доступна документация с доступными запросами и их примерами по адресу:

```
http://localhost:8000/docs
```

</details>

<details>

<summary>
<h4>Как запустить проект с помощью docker:</h4>
</summary>

Клонировать репозиторий:

```bash
git clone git@github.com:JustLight1/coin-flow.git
```

Создать файл `.env-non-dev` и заполнить его по примеру из файла `.env.example.non-dev`

Запустить проект:

- По команде `docker compose up` Docker Compose: получит готовые образы, указанные в `image`, соберёт все образы, указанные в `build`, запустит все контейнеры, описанные в конфиге.
- Флаг `--build` соберет образы.
- Флаг `-d` запустит `docker compose` в режиме демона.

```bash
docker compose up --build -d
```

После запуска станет доступна документация с доступными запросами и их примерами по адресу:

```
http://localhost:8000/docs
```

</details>

# Автор:

**Форов Александр**

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
