# MA-001 — GITHUB_AUTOMATION_MATRIX
Продолжение16.11.2026. User permissions, App scopes и разрешение задания различаются.
| Операция | Требуется | Технически | Разрешено MA-001 | Выполнение/evidence |
|---|---|---|---|---|
| list | metadata/read | Да | Да | Два repo, connector+gh |
| clone/read private Sulfi | contents read | Да | Только чтение | Checkout и ls-remote |
| create private repo | administration write | Нет App scope | При наличии права | Не нужно: owner создал repo |
| clone MA | contents read | Да | Да | /workspace/master-alchemica |
| branch/commit | git/author/contents | Git/author/scopes проверены | Только MA | chore/ma-001-setup; bootstrap report |
| push | contents/workflows write | Scopes есть | Только MA | Факт отдельно в bootstrap report |
| PR | pull_requests write | Scope есть | Только MA | Факт отдельно в bootstrap report |
| safe Actions | workflow file/actions read | Scopes есть | Только MA docs CI | Реальный run отдельно; настройки не менялись |
| Actions settings | endpoint-specific admin | Не подтверждено; ранее Sulfi READ403 | Sulfi запрещена | Не повторяли/не меняли |
| environment publish | UI/config tool | Нет доступного tool | Только отдельная MA среда | BLOCKED, source_config=null |
| secrets | secrets permission | App scope отсутствует | Изменения запрещены | Не запрашивались/не менялись |
| merge/release | owner decision | Не проверяли | Не выбран для автоматического выполнения | Не выполнялось |
| server/OAuth/production | отдельное полномочие | Не проверяли | Запрещено | Не выполнялось |
Пробных writes в Сульфи нет. App installation/permissions/credentials не изменялись.
