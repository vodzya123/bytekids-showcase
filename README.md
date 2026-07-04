# ByteKids — платформа для школы программирования

Веб-платформа для управления учебным процессом: ученики, группы, расписание, оплаты, уведомления, роли администратора, преподавателя и ученика.

**Исходный код не публикуется.** Продукт предоставляется как облачный сервис (SaaS) или развёртывание под ключ.

---

## Попробовать бесплатно

| | |
|---|---|
| **Демо-доступ (12 часов)** | [bytekids.online/demo](https://bytekids.online/demo) |
| **После регистрации** | 3 роли: администратор, преподаватель, ученик |
| **Данные в демо** | Вымышленные, без реальных клиентов |

Демо имеет ознакомительный характер: часть операций недоступна (изменение настроек, реальные платежи и т.п.).

---

## Основные возможности

- **Админ-панель** — ученики, группы, монеты, оплаты, аналитика, договоры, мастер-классы
- **Преподаватель** — свои группы, расписание, карточки учеников, доход
- **Ученик** — личный кабинет, модули, задания
- **Расписание** — общее и личное для преподавателя
- **Демо-режим** — изолированная среда для партнёров и заинтересованных школ
- **Уведомления** — заявки с форм, персонал, родительский бот (в продакшене)

Подробнее: [docs/features.md](docs/features.md)

---

## Скриншоты

Все снимки — из [демо-доступа](https://bytekids.online/demo), вымышленные данные.

### Демо и вход

| | |
|---|---|
| Страница входа | ![Вход](screenshots/demo/02-login.png) |

### Администратор

| Раздел | |
|--------|---|
| Главная панель | ![Админка](screenshots/admin/01-dashboard.png) |
| Расписание | ![Расписание](screenshots/admin/02-schedule.png) |
| Оплаты | ![Оплаты](screenshots/admin/03-payments.png) |
| Аналитика | ![Аналитика](screenshots/admin/04-analytics.png) |
| Заказы из магазина | ![Заказы](screenshots/admin/05-booking-orders.png) |
| Замечания и поощрения | ![Замечания](screenshots/admin/06-remarks.png) |
| Посещаемость | ![Посещаемость](screenshots/admin/07-attendance.png) |
| Опросы и формы | ![Формы](screenshots/admin/08-forms.png) |
| Домашние задания | ![ДЗ](screenshots/admin/09-homework.png) |
| Отчёты о детях | ![Отчёты](screenshots/admin/10-student-reports.png) |
| Карточка ученика | ![Карточка](screenshots/admin/11-student-card.png) |
| Группа | ![Группа](screenshots/admin/12-group.png) |
| Назначенные проекты | ![Проекты](screenshots/admin/13-assigned-projects.png) |
| Уведомления | ![Уведомления](screenshots/admin/14-notifications.png) |

### Преподаватель

| Раздел | |
|--------|---|
| Главная | ![Преподаватель](screenshots/teacher/01-dashboard.png) |
| Расписание | ![Расписание](screenshots/teacher/02-schedule.png) |
| Доход | ![Доход](screenshots/teacher/03-income.png) |
| Замечания | ![Замечания](screenshots/teacher/04-remarks.png) |
| Карточка ученика | ![Карточка](screenshots/teacher/05-student-card.png) |
| Группа | ![Группа](screenshots/teacher/06-group.png) |
| Заказы | ![Заказы](screenshots/teacher/07-booking-orders.png) |

### Ученик

| Раздел | |
|--------|---|
| Модули — обзор | ![Модули](screenshots/student/01-modules-overview.png) |
| Модуль Python | ![Python](screenshots/student/02-module-python.png) |
| Модуль Turtle | ![Turtle](screenshots/student/03-module-turtle.png) |
| Модуль Pygame | ![Pygame](screenshots/student/04-module-pygame.png) |
| Домашние задания | ![ДЗ](screenshots/student/05-homework.png) |
| Магазин монет | ![Магазин](screenshots/student/06-shop.png) |
| Профиль ученика | ![Профиль](screenshots/student/07-profile.png) |
| Статистика прогресса | ![Статистика](screenshots/student/08-stats.png) |
| Проекты Scratch/Python | ![Проекты](screenshots/student/09-projects.png) |
| Портфолио (Моя лаборатория) | ![Портфолио](screenshots/student/10-portfolio.png) |
| Доп. занятия Word | ![Доп Word](screenshots/student/11-extra-lessons-word.png) |
| Задание Hello World | ![Задание 1](screenshots/student/13-task-hello-world.png) |
| Задание Turtle | ![Turtle задание](screenshots/student/14-task-turtle.png) |

Обновить скрины: `python3 scripts/capture_screenshots.py` (см. [screenshots/README.md](screenshots/README.md)).

---

## Для кого

- Школы программирования и робототехники  
- Небольшие учебные центры с несколькими группами  
- Филиальные сети (мультиофис)

---

## Подключение и сотрудничество

- **ВКонтакте:** [vk.com/alexsandrovvit](https://vk.com/alexsandrovvit)  
- **Сайт:** [bytekids.online](https://bytekids.online)  
- **Демо:** [bytekids.online/demo](https://bytekids.online/demo)

Напишите в сообщения: город, количество учеников, нужны ли филиалы — ответим с вариантами подключения.

---

## Технологии (обзор)

| Слой | |
|------|---|
| Backend | Python, Flask, Gunicorn |
| База данных | PostgreSQL |
| Frontend | HTML, Tailwind, JavaScript |
| Интеграции | Telegram, VK, оплаты |

Детали реализации и исходники — только по договорённости (лицензия / white-label).

---

## Репозитории

| Репозиторий | Доступ | Содержимое |
|-------------|--------|------------|
| **bytekids-showcase** (этот) | Публичный | Описание, скрины, ссылки на демо |
| **bytekids** | Приватный | Исходный код платформы |

---

## Лицензия

© ByteKids. Все права защищены.  
Материалы в этом репозитории (тексты, скриншоты) можно цитировать со ссылкой на [bytekids.online](https://bytekids.online).  
Использование торговой марки и копирование интерфейса без согласия запрещено.
