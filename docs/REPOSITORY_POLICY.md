# MA-001 — политика репозиториев
MA — отдельный private master-alchemica в подтверждённом namespace владельца. CLIENT и редакционный MASTER остаются без изменений и имеют самостоятельные права и релизы.
Сульфи читается только для анализа в отдельном контуре; её исходники, реальные данные и credentials не переносятся в MA.
Текущая App имеет contents:write к Сульфи: read-only пока процедурный. Локальный запрет git push не ограничивает API. Для технической границы нужен изолированный reader или source-only snapshot.
MA case records и CLIENT diary — раздельные БД/хранилища, явные роли/consent; общий subject не даёт общего доступа.
MA-001 не создаёт backend, клиническую карту, transfers, ИИ или приложение. Общие библиотеки возможны после аудита paths/commit/licensing и отдельного задания, с semver/pin/contract tests. Третий shared repo не создавать автоматически.
Ветки будущего bootstrap: main и chore/ma-001-setup. Не merge и не publish releases автоматически; не force push.
Шаблон Actions проверяет только организационные тексты, с contents:read. Не использовать существующий CI Сульфи.
