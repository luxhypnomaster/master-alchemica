# MA-001 — правила работы
Сначала прочитать README.md, docs/REPOSITORY_POLICY.md, docs/CONTRACTS_DRAFT.md и действующее MA-задание.
Реестр: https://docs.google.com/document/d/1dInmlJAfi5b3DS1zQ1hOGhj1Mph9wEBDJU8C8P-yPpQ/edit
Не утверждать чтение реестра без фактического доступа.

1. MA, CLIENT и editorial MASTER — разные продукты с разными данными, ролями и релизами.
2. MA-001 ограничен организационной основой отдельного master-alchemica после проверки owner/visibility/permissions. Исходное требование PRIVATE и текущее решение владельца Public раздельно зафиксированы в docs/MA-001_OWNER_DECISIONS.md; не выдавать Public за выполнение PRIVATE.
3. Исходники Сульфи читать в отдельном checkout на фиксированном SHA. Запрещены её push/PR/merge, правки файлов, CI, сервера, OAuth, secrets и permissions; клиентское задание №18 не изменять.
4. Нельзя переносить приватные исходники Сульфи в MA, копировать credentials или реальные дневники, записи и медиа. Только synthetic fixtures.
5. Запрет записи при write credential — процедурный. Не называть его техническим read-only. Отдельный reader/snapshot требует подтверждённой изоляции.
6. Не создавать третий shared repo, клиническую карту, полномасштабный Flutter UI, ИИ, production integrations или STT weights в APK.
7. Минимальный diff; перед записью проверить author, origin, branch и исходные изменения. Не затирать чужую работу, не force-push.
8. Организационные изменения через рабочую chore/ma-001-* ветку и PR в main. Самостоятельный merge безопасных docs разрешён только при явном разрешении текущего задания владельца и успешном CI; release отдельно не разрешён.
9. Проверять только соразмерные безопасные проверки: Python docs checker. Никаких тяжёлых Flutter/Android сборок для MA-001.
10. CI с contents:read, без секретов/deploy/реальных данных. Не менять разрешения установки для обхода блокера.
11. Отчёт содержит точные пути/SHA/URL, выполненные проверки, ограничения и PARTIAL/BLOCKED. Шаблон, локальный тест и успешный Actions — разные состояния.
12. Общие пакеты: сначала лицензии/границы API, затем отдельное одобрение; semver + immutable pin и compatibility tests. Приватные БД MA и CLIENT не объединять.
