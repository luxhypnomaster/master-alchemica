# Мастер Алхимик / Master Alchemica
Professional hypnotherapy workspace — Master Alchemica.

Организационный фундамент MA-001, редакция 1.1. Функциональное приложение и backend пока не создаются.

Видимость: Public по текущему решению владельца; это [отступление от исходного PRIVATE](docs/MA-001_OWNER_DECISIONS.md), а не результат приватного bootstrap.

- **MA** — профессиональный Android/Flutter кабинет специалиста, собственные данные, роли и релизы.
- **Сульфи CLIENT** — самогипноз, личные программы и дневник.
- **Редакционный MASTER** — редактор контента Сульфи, самостоятельная продуктовая поверхность.

[Правила агента](AGENTS.md) · [Политика](docs/REPOSITORY_POLICY.md) · [Контракты DRAFT](docs/CONTRACTS_DRAFT.md) · [Отчёты MA-001](reports/ma-001/RESULT.md) · [Доступ к исходникам](docs/CODEX_ACCESS.md).

[Реестр заданий MA](https://docs.google.com/document/d/1dInmlJAfi5b3DS1zQ1hOGhj1Mph9wEBDJU8C8P-yPpQ/edit). Его содержимое данным аудитом не проверено.
Нумерация: MA-001, MA-002; MA-F и MA-K — отдельные реестры.

Проверка: `python3 scripts/check_structure.py`. Actions проверяет только организационные тексты с `contents: read`, без deploy, секретов, APK и реальных данных. Фактический результат — в Checks соответствующего PR.
Исходники Сульфи не входят в MA. Общие компоненты пока не выделены; приватные БД не объединяются.
