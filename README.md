# ByteKids — Coding School Management Platform

[![Website](https://img.shields.io/badge/website-bytekids.online-0e5a43?style=for-the-badge)](https://bytekids.online)
[![Demo](https://img.shields.io/badge/demo-12h_free-2563eb?style=for-the-badge)](https://bytekids.online/demo)
[![Telegram](https://img.shields.io/badge/Telegram-@vodzya-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vodzya)

**ByteKids** — веб-платформа для школ программирования и робототехники: ученики, группы, расписание, оплаты, модули Python/Scratch, монеты, QR-посещаемость, отчёты для родителей.

| | |
|---|---|
| **Сайт** | [bytekids.online](https://bytekids.online) |
| **Демо (12 ч)** | [bytekids.online/demo](https://bytekids.online/demo) |
| **Контакты** | [VK](https://vk.com/alexsandrovvit) · [Telegram @vodzya](https://t.me/vodzya) |

> **English** below · **Русский:** [перейти к русской версии](#русский)

---

## English

> [!WARNING]
> **Actively in development.** Features are updated regularly; the [demo](https://bytekids.online/demo) may include incomplete or temporarily unavailable sections.
>
> **Contact the developer:** [VK](https://vk.com/alexsandrovvit) · [Telegram @vodzya](https://t.me/vodzya) — questions about the platform, demo access, and onboarding for schools.

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

ByteKids covers the full workflow of a coding school — from website inquiries to daily classes, payments, student motivation, and parent reporting. Overview by role; the [demo](https://bytekids.online/demo) uses fictional data and a limited set of write operations.

#### Administrator

Central dashboard for a school or branch.

- **Students and groups** — unified list, group assignment, archive of removed students, quick search, student card with parent contacts, balance, and lesson history.
- **Cards and QR** — printable student cards with QR codes for login and class check-in; bulk printing by group.
- **Schedule** — office-wide schedule: groups, teachers, rooms, rescheduling, and recurring time slots.
- **Payments and balance** — paid lessons tracking, credit and debit history, debt control, revenue analytics.
- **Coins** — in-school currency: rewards for achievements, shop spending, per-student transaction history.
- **Homework** — assignment and review, completion status, linked to course modules.
- **Remarks and rewards** — behavior and achievement notes visible to teachers and admins.
- **Attendance** — class presence log, including QR check-in.
- **Forms and inquiries** — website sign-ups, surveys, masterclass applications; alerts for new submissions.
- **Contracts** — training agreements: signing, PDF export, e-mail delivery.
- **Shop** — prize and merch orders paid with coins: status, fulfillment, pending queue.
- **Child reports** — progress and activity summaries for parents and administration.
- **Assigned projects** — creative and capstone projects assigned to students and groups.
- **Analytics** — dashboard with key metrics: students, groups, payments, activity.
- **Notifications** — staff event feed: inquiries, orders, system messages.
- **Office settings** — branch parameters, access control, partner demo links (in production).

#### Teacher

A focused workspace — only own groups and students, without noise from other branches.

- **Dashboard** — overview of upcoming classes, groups, and quick actions for today.
- **Schedule** — school-wide schedule plus personal events and teacher notes.
- **Groups** — group roster, jump to student card, progress overview.
- **Student card** — profile, contacts, coins, remarks, login QR.
- **Income** — transparent tracking of earnings and payouts per delivered lesson.
- **Remarks and rewards** — student notes within granted permissions.
- **Shop orders** — processing orders from students in own groups.

#### Student

Personal portal with gamification: modules, tasks, coins, and a project portfolio.

- **Login** — username/password or QR card scan at class.
- **Course modules** — structured tracks: Python, Turtle, Pygame, and more; topic progress map.
- **Interactive tasks** — built-in code editor, step-by-step challenges with automatic solution checking.
- **Homework** — assigned tasks, deadlines, submission status, and feedback.
- **Projects** — Scratch and Python projects: create, save, showcase work.
- **My Lab** — personal portfolio: published projects and achievements.
- **Extra lessons** — supplementary materials and mini-courses (e.g. Word, Python) outside the main program.
- **Coin shop** — exchange earned coins for prizes, stickers, and school rewards.
- **Profile** — avatar, name, coin balance, progress map, Face ID, lab links.
- **Statistics** — detailed progress across modules, completed tasks, and activity.

#### Cross-cutting

- **Three roles in one system** — administrator, teacher, and student with permission boundaries and a shared database.
- **Multi-office** — multiple branches with isolated students, schedules, and settings; suitable for school networks.
- **Demo mode** — isolated 12-hour environment with three test accounts for partners and interested schools.
- **Notifications** — staff alerts for inquiries and events; parent channels in production.
- **Integrations** — Telegram parent bot, VK (panel and reminders), payment processing, QR attendance.

Partner overview: [docs/features.md](docs/features.md) (Russian).

### Screenshots

All captures from the [demo](https://bytekids.online/demo) with fictional data.

#### Demo and login

| | |
|---|---|
| Login page | ![Login](screenshots/demo/02-login.png) |

#### Administrator

| Section | |
|---------|---|
| Dashboard | ![Admin](screenshots/admin/01-dashboard.png) |
| Schedule | ![Schedule](screenshots/admin/02-schedule.png) |
| Payments | ![Payments](screenshots/admin/03-payments.png) |
| Analytics | ![Analytics](screenshots/admin/04-analytics.png) |
| Shop orders | ![Orders](screenshots/admin/05-booking-orders.png) |
| Remarks and rewards | ![Remarks](screenshots/admin/06-remarks.png) |
| Attendance | ![Attendance](screenshots/admin/07-attendance.png) |
| Surveys and forms | ![Forms](screenshots/admin/08-forms.png) |
| Homework | ![Homework](screenshots/admin/09-homework.png) |
| Child reports | ![Reports](screenshots/admin/10-student-reports.png) |
| Student card | ![Student card](screenshots/admin/11-student-card.png) |
| Group | ![Group](screenshots/admin/12-group.png) |
| Assigned projects | ![Projects](screenshots/admin/13-assigned-projects.png) |
| Notifications | ![Notifications](screenshots/admin/14-notifications.png) |

#### Teacher

| Section | |
|---------|---|
| Dashboard | ![Teacher](screenshots/teacher/01-dashboard.png) |
| Schedule | ![Schedule](screenshots/teacher/02-schedule.png) |
| Income | ![Income](screenshots/teacher/03-income.png) |
| Remarks | ![Remarks](screenshots/teacher/04-remarks.png) |
| Student card | ![Student card](screenshots/teacher/05-student-card.png) |
| Group | ![Group](screenshots/teacher/06-group.png) |
| Orders | ![Orders](screenshots/teacher/07-booking-orders.png) |

#### Student

| Section | |
|---------|---|
| Modules overview | ![Modules](screenshots/student/01-modules-overview.png) |
| Python module | ![Python](screenshots/student/02-module-python.png) |
| Turtle module | ![Turtle](screenshots/student/03-module-turtle.png) |
| Pygame module | ![Pygame](screenshots/student/04-module-pygame.png) |
| Homework | ![Homework](screenshots/student/05-homework.png) |
| Coin shop | ![Shop](screenshots/student/06-shop.png) |
| Student profile | ![Profile](screenshots/student/07-profile.png) |
| Progress stats | ![Stats](screenshots/student/08-stats.png) |
| Scratch/Python projects | ![Projects](screenshots/student/09-projects.png) |
| Portfolio (My Lab) | ![Portfolio](screenshots/student/10-portfolio.png) |
| Extra lessons (Word) | ![Extra Word](screenshots/student/11-extra-lessons-word.png) |
| Hello World task | ![Task 1](screenshots/student/13-task-hello-world.png) |
| Turtle task | ![Turtle task](screenshots/student/14-task-turtle.png) |

### Who it is for

- Coding and robotics schools  
- Small learning centers with several groups  
- Multi-branch networks

### Contact

- **VK (developer):** [vk.com/alexsandrovvit](https://vk.com/alexsandrovvit)  
- **Telegram:** [@vodzya](https://t.me/vodzya)  
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

© ByteKids. All rights reserved.  
Materials in this repository (text, screenshots) may be quoted with a link to [bytekids.online](https://bytekids.online).  
Trademark use and copying of the interface without permission is prohibited.

---

## Русский

> [!WARNING]
> **Платформа в активной разработке.** Функционал регулярно обновляется; в [демо-версии](https://bytekids.online/demo) могут встречаться неработающие или незавершённые разделы.
>
> **Связь с разработчиком:** [ВКонтакте](https://vk.com/alexsandrovvit) · [Telegram @vodzya](https://t.me/vodzya) — вопросы по платформе, демо, подключению школы.

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
- **Telegram:** [@vodzya](https://t.me/vodzya)  
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
