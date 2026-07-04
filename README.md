# ByteKids — Coding School Management Platform

> **English** below · **Русский:** [перейти к русской версии](#русский)

---

## English

> [!WARNING]
> **Actively in development.** Features are updated regularly; the [demo](https://bytekids.online/demo) may include incomplete or temporarily unavailable sections.
>
> **Contact the developer:** [vk.com/alexsandrovvit](https://vk.com/alexsandrovvit) — questions about the platform, demo access, and onboarding for schools.

ByteKids is an all-in-one environment for coding schools: admins, teachers, and students work in a single system. Scheduling, course modules with assignments, gamification via coins, payments, and parent reporting — without juggling spreadsheets and third-party tools.

Web platform for running a coding school: students, groups, schedule, payments, notifications, and three roles — administrator, teacher, and student.

**Source code is not public.** Available as a cloud service (SaaS) or turnkey deployment.

### Try it free

| | |
|---|---|
| **Demo access (12 hours)** | [bytekids.online/demo](https://bytekids.online/demo) |
| **After signup** | 3 roles: admin, teacher, student |
| **Demo data** | Fictional, no real customer data |

The demo is for exploration only: some actions are disabled (settings changes, real payments, etc.).

### Key features

ByteKids covers the full workflow of a coding school — from website inquiries to daily classes, payments, student motivation, and parent updates. Overview by role; the [demo](https://bytekids.online/demo) uses fictional data and a limited write scope.

**Administrator** — central dashboard for a school or branch: students and groups, printable QR student cards, office schedule, payments and lesson balance, coin economy, homework, remarks and rewards, attendance (including QR check-in), form submissions, training contracts (PDF), shop orders, child reports, assigned projects, analytics, staff notifications, office settings.

**Teacher** — workspace scoped to own groups: dashboard, shared and personal schedule, group roster, student cards with QR, income tracking, remarks, shop order handling.

**Student** — gamified learning portal: login or QR card, course modules (Python, Turtle, Pygame, etc.), interactive coding tasks with auto-grading, homework, Scratch/Python projects, personal portfolio (“My Lab”), extra lessons, coin shop, profile with progress map, detailed stats.

**Cross-cutting** — role-based access, multi-branch (multi-office) support, isolated 12-hour demo for partners, staff notifications, integrations (Telegram parent bot, VK, payments, QR attendance).

Partner overview: [docs/features.md](docs/features.md) (Russian).

### Screenshots

All captures from the [demo](https://bytekids.online/demo) with fictional data.

| Section | |
|---------|---|
| Login | ![Login](screenshots/demo/02-login.png) |

**Admin:** dashboard, schedule, payments, analytics, shop orders, remarks, attendance, forms, homework, child reports, student card, group, assigned projects, notifications — see full gallery in the [Russian section](#скриншоты).

**Teacher:** dashboard, schedule, income, remarks, student card, group, orders.

**Student:** modules, Python/Turtle/Pygame tracks, homework, coin shop, profile, stats, projects, portfolio, extra lessons, coding tasks.

### Who it is for

- Coding and robotics schools  
- Small learning centers with several groups  
- Multi-branch networks

### Contact

- **VK (developer):** [vk.com/alexsandrovvit](https://vk.com/alexsandrovvit)  
- **Website:** [bytekids.online](https://bytekids.online)  
- **Demo:** [bytekids.online/demo](https://bytekids.online/demo)

Message with your city, number of students, and whether you need multiple branches — we will reply with onboarding options.

### Tech stack

| Layer | |
|-------|---|
| Backend | Python, Flask, Gunicorn |
| Database | PostgreSQL |
| Frontend | HTML, Tailwind, JavaScript |
| Integrations | Telegram, VK, payments |

Implementation details and source code — by agreement (license / white-label).

### Repositories

| Repository | Access | Contents |
|------------|--------|----------|
| **bytekids-showcase** (this repo) | Public | Description, screenshots, demo links |
| **bytekids** | Private | Application source code |

### License

© ByteKids. All rights reserved. Materials in this repository may be quoted with a link to [bytekids.online](https://bytekids.online). Trademark use and UI copying without permission is prohibited.

---

## Русский

> [!WARNING]
> **Платформа в активной разработке.** Функционал регулярно обновляется; в [демо-версии](https://bytekids.online/demo) могут встречаться неработающие или незавершённые разделы.
>
> **Связь с разработчиком:** [vk.com/alexsandrovvit](https://vk.com/alexsandrovvit) — вопросы по платформе, демо, подключению школы.

ByteKids — единая среда для школы программирования: администрация, преподаватели и ученики работают в одной системе. Расписание, модули с заданиями, мотивация через монеты, оплаты, отчёты для родителей — без набора разрозненных таблиц и сторонних сервисов.

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

ByteKids закрывает полный цикл работы школы программирования: от первой заявки с сайта до ежедневных занятий, оплат, мотивации учеников и отчётности для родителей. Ниже — обзор по ролям; в [демо](https://bytekids.online/demo) доступны вымышленные данные и ограниченный набор операций.

### Администратор

Центральная панель управления школой или филиалом.

- **Ученики и группы** — единый список, распределение по группам, архив удалённых, быстрый поиск, карточка ученика с контактами родителей, балансом и историей занятий.
- **Карточки и QR** — печать карточек ученика с QR-кодом для входа и отметки на занятии; массовая печать по группе.
- **Расписание** — общее расписание офиса: группы, преподаватели, аудитории, переносы и повторяющиеся слоты.
- **Оплаты и баланс** — учёт оплаченных занятий, история начислений и списаний, контроль задолженностей, аналитика по выручке.
- **Монеты** — внутренняя валюта школы: начисление за успехи, списание в магазине, история операций по каждому ученику.
- **Домашние задания** — назначение и проверка ДЗ, статусы выполнения, связь с модулями курса.
- **Замечания и поощрения** — фиксация поведения и достижений с видимостью для преподавателя и администратора.
- **Посещаемость** — журнал присутствия на занятиях, в том числе через QR-отметку.
- **Заявки и формы** — входящие записи с сайта, опросы, анкеты мастер-классов; уведомления о новых заявках.
- **Договоры** — формирование договоров на обучение, подписание, выгрузка PDF, отправка на e-mail.
- **Магазин** — заказы призов и мерча за монеты: статусы, выдача, ожидающие обработки.
- **Отчёты о детях** — сводки для родителей и администрации по прогрессу и активности.
- **Назначенные проекты** — постановка творческих и итоговых проектов ученикам и группам.
- **Аналитика** — дашборд с ключевыми показателями: ученики, группы, оплаты, активность.
- **Уведомления** — лента событий для персонала: заявки, заказы, системные сообщения.
- **Настройки офиса** — параметры филиала, доступы, демо-ссылки для партнёров (в продакшене).

### Преподаватель

Рабочее место педагога — только свои группы и ученики, без лишнего шума из других филиалов.

- **Главная** — обзор ближайших занятий, групп и быстрых действий на сегодня.
- **Расписание** — общее расписание школы плюс личные события и заметки преподавателя.
- **Группы** — состав группы, переход в карточку ученика, контроль прогресса.
- **Карточка ученика** — профиль, контакты, монеты, замечания, QR для входа.
- **Доход** — прозрачный учёт начислений и выплат по проведённым занятиям.
- **Замечания и поощрения** — отметки по ученикам в рамках выданных прав.
- **Заказы из магазина** — обработка заказов учеников своих групп.

### Ученик

Личный кабинет с игровой механикой: модули, задания, монеты и портфолио работ.

- **Вход** — логин и пароль или сканирование QR-карточки на занятии.
- **Модули курса** — структурированные треки: Python, Turtle, Pygame и другие направления; карта прогресса по темам.
- **Интерактивные задания** — встроенный редактор кода, пошаговые задачи с автоматической проверкой решений.
- **Домашние задания** — список назначенных ДЗ, сроки, статусы сдачи и обратная связь.
- **Проекты** — Scratch- и Python-проекты: создание, сохранение, демонстрация работ.
- **Моя лаборатория** — личное портфолио ученика: опубликованные проекты и достижения.
- **Доп. занятия** — дополнительные материалы и мини-курсы (например, Word, Python) вне основной программы.
- **Магазин монет** — обмен заработанных монет на призы, стикеры и бонусы школы.
- **Профиль** — аватар, имя, баланс монет, карта прогресса, Face ID, ссылки на лабораторию.
- **Статистика** — детальный прогресс по модулям, выполненным заданиям и активности.

### Сквозные функции

- **Три роли в одной системе** — администратор, преподаватель и ученик с разграничением прав и единой базой данных.
- **Мультиофис** — несколько филиалов с изолированными учениками, расписанием и настройками; подходит для сетей школ.
- **Демо-режим** — изолированная среда на 12 часов с тремя тестовыми аккаунтами для партнёров и заинтересованных школ.
- **Уведомления** — оповещения персонала о заявках и событиях; в продакшене — каналы для родителей.
- **Интеграции** — Telegram-бот для родителей, VK (панель и напоминания), приём оплат, QR-отметка посещений.

Подробный технический обзор для партнёров: [docs/features.md](docs/features.md).

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
