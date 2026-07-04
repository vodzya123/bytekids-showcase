# Скриншоты для витрины

Автоматический набор из демо `/demo` (вымышленные данные, 1440×900).

## Структура

```
screenshots/
├── demo/          — вход (2)
├── admin/         — админка (14)
├── teacher/       — преподаватель (7)
└── student/       — ученик (13)
```

**Всего: 37 скриншотов**

## Обновить

```bash
# все роли
BYTEKIDS_BASE_URL=https://bytekids.online python3 scripts/capture_screenshots.py

# только ученик
BYTEKIDS_BASE_URL=https://bytekids.online python3 scripts/capture_screenshots.py --only-role student
```

## Ученик (`student/`)

| Файл | Раздел |
|------|--------|
| 01-modules-overview | Главная с модулями курса |
| 02-module-python | Модуль «Основы Python» |
| 03-module-turtle | Модуль «Turtle» |
| 04-module-pygame | Модуль «Pygame» |
| 05-homework | Домашние задания |
| 06-shop | Магазин |
| 07-profile | Карточка ученика |
| 08-stats | Статистика и прогресс |
| 09-projects | Проекты |
| 10-portfolio | Моя лаборатория |
| 11-extra-lessons-word | Доп. занятия Word |
| 13-task-hello-world | Задание Hello World |
| 14-task-turtle | Задание Turtle |
