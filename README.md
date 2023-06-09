# yamdb_final
yamdb_final
Проект YaMDb

# Общее описание проекта:
Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории, такие как Книги, Фильмы, Музыка. Например, в категории Книги могут быть произведения Винни-Пух и все-все-все и Марсианские хроники, а в категории Музыка — песня Давеча группы Жуки и вторая сюита Баха. Список категорий может быть расширен. 


# Техническое описание проекта YaMDb:

Ресурсы API YaMDb:

    Ресурс auth: аутентификация.
    Ресурс users: пользователи.
    Ресурс titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
    Ресурс categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»). Одно произведение может быть привязано только к одной категории.
    Ресурс genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
    Ресурс reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
    Ресурс comments: коммента

Пользовательские роли и права доступа:

    Аноним — может просматривать описания произведений, читать отзывы и комментарии.
    Аутентифицированный пользователь (user) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
    Модератор (moderator) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
    Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
    Суперюзер Django должен всегда обладать правами администратора, пользователя с правами admin. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.

# Установка:

## Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/Alex90G/yamdb_final.git
```

```bash
cd api_yamdb/
```

- Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

```bash
python3 -m pip install --upgrade pip
```

- Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

- Запустить приложение в контейнерах:

*перейти в `infra/`*
```bash
docker-compose up -d --build
```

- Выполнить миграции:

*из `infra/`*
```bash
docker-compose exec web python manage.py migrate
```

- Создать суперпользователя:

*из `infra/`*
```bash
docker-compose exec web python manage.py createsuperuser
```

- Собрать файлы статики:

*из `infra/`*
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

- Остановить приложение в контейнерах:

*из `infra/`*
```bash
docker-compose down -v
```

### шаблон наполнения env-файла
см.
```bash
infra/.env
```

### Команда заполнения базы данными
```bash
cd api_yamdb && python manage.py loaddata ../infra/fixtures.json
```

# Документация API и примеры:

```json
/redoc/
```

# Адрес для подключения к проекту:
http://51.250.109.215/admin/login/

# Статус бэйджа (настройки приватности репозитория - "Public")
![main workflow](https://github.com/Alex90G/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
