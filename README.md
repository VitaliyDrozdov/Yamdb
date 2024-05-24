# api_yamdb

## О проекте:

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:greg2707/api_yamdb.git
```

Cоздать и активировать виртуальное окружение:


* Если у вас Linux/macOS

    ```
    python3 -m venv env
    source env/bin/activate
    python3 -m pip install --upgrade pip
    ```

* Если у вас windows

    ```
    python -m venv venv
    source venv/scripts/activate
    python -m pip install --upgrade pip
    ```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции и запустить проект:

  * Если у вас Linux/macOS

    ```
    python3 manage.py migrate
    python3 manage.py runserver
    ```

  * Если у вас windows
  
    ```
    python manage.py migrate
    python manage.py runserver
    ```


### Документация к API по адресу `http://localhost:8000/redoc/`


## Примеры запросов к API:

- Просмотр списка произведений:
``` GET /api/v1/titles/ ```

- Добавление новой категории:  
``` POST /api/v1/categories/ ```  

- Просмотр списка жанров:  
``` GET /api/v1/genres/{slug} ```

- Просмотр данных о конкретном произведении:
``` GET /api/v1/titles/{titles_id}/ ```
  
- Просмотр списка отзывов:  
``` GET /api/v1/titles/{title_id}/reviews/ ``` 

- Просмотр данных юзера:  
``` GET /api/v1/users/{username}/ ``` 


## Использованные технологии:
- Python
- Django
- Django REST framework


## Информация об авторах:
- Кирилл Воробьев
- Виталий Дроздов [VitaliyDrozdov](https://github.com/VitaliyDrozdov)
- Григорий Грачев