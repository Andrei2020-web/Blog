Проект Django(3.2.4) с именем Blog.
В проекте создано приложение с именем blogs и моделью BlogPost. Модель содержит
такие поля, как title, text и date_added. Создана домашняя страница, на которой 
выводятся все сообщения в хронологическом порядке.
Сделана одна форма для создания новых сообщений и форма для редактирования
существующих сообщений.

Добавлена система аутентификации и регистрации в проект Blog. 
Пользователь, выполнивший вход, может видеть свое имя на экране,
а незарегистрированные пользователи видят ссылку на страницу регистрации.

Каждое сообщение в блоге связано с конкретным пользователем.
Чтение всех сообщений доступно всем пользователям, но только зарегистрированные
пользователи могут создавать новые и редактировать существующие сообщения.

В проекте были использованы стили Bootstrap 4.