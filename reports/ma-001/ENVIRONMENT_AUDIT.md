# MA-001 — ENVIRONMENT_AUDIT
Повторный READ-ONLY preflight 16.11.2026 перед изменениями.
Account luxhypnomaster, User ID351374601, совпадает с owner обоих видимых repo:
- https://github.com/luxhypnomaster/sulfi-hypnotherapy — private.
- https://github.com/luxhypnomaster/master-alchemica — теперь PUBLIC, ID1460251832, не archived. Видимость изменил владелец; отличие от исходного PRIVATE описано в docs/MA-001_OWNER_DECISIONS.md. Прежнее private — исторический факт preflight, не текущая видимость.
User permissions обоих: admin/maintain/pull/push/triage. App installation182378375, selection=all: contents/actions/workflows/issues/pull_requests write; checks/metadata/statuses read. Administration/secrets permission отсутствуют. User admin flag не расширяет scope App. Создание repo больше не требуется.
gh auth status/API подтверждены; GH_TOKEN не извлекался. Git author проверен: Sergey Bondaruk, email соответствует владельцу первоначального README commit.

Cloud, bash, начальный cwd /workspace. Environment ID ccarenv_b64_Y2NhcmVudl9mYThiODM4YzUzYTQ4MTkxYjRmYzkzZmNkYzNjYWJmYw.
Status: running/connected, observations_current=true, network unrestricted/enforced; source_config_id/source_config_version_id=null.
MA checkout /workspace/master-alchemica; origin https://github.com/luxhypnomaster/master-alchemica.git. Исходная main ab7e9f673070b016e75ec13c8d9303d2d61fe995 теперь история; PR1 merged, проверенный main cf8e0255c60711eb0081af9486acdf760591d335 с SUCCESS CI43931467982. Для отчётного уточнения создана chore/ma-001-final-acceptance без изменения scope.
Сохранившийся workspace чата не доказывает постоянную конфигурацию. Повторно проверены текущие tools и поиск интеграций: create/launch/config/publish новой Codex среды и browser tools не предоставлены; UI проекта не наблюдался. Имя проекта известно от владельца, независимо не проверено. Чистый local checkout main без GH_TOKEN/GITHUB_TOKEN/credential helper прошёл stdlib checker; это воспроизводимость документов на той же машине, не новая Codex среда.

Sulfi analysis /workspace/sulfi-analysis, sparse/shallow detached363a0244ce761e317dd09a6c5cb366d1e8ba7315, чистый. Fetch origin реальный Sulfi URL, push URL=/dev/null — локальная защита, не GitHub API запрет.
git ls-remote подтвердил main b88637a105b2182c7b836311ebb3de7ad037b08f и task18 ref363a0244ce761e317dd09a6c5cb366d1e8ba7315. В первом аудите совпали51 refs; в продолжении проверены эти два ключевых ref. Не полный GitHub audit log.
MASTER/CLIENT используют общее Flutter дерево; отдельного MASTER repo в списке нет. Source тела не добавлены в MA.

| Возможность | Факт |
|---|---|
| Read Sulfi | PASS: remote refs и source checkout |
| Новый MA | Owner/privacy/read/push scopes PASS; фактическая запись отдельно в bootstrap |
| Текущий MA checkout | PASS как clone этой машины |
| Постоянный environment | BLOCKED/не подтверждён, source_config=null и нет управляющего инструмента |
| Технический read-only Sulfi | Не установлен; процедурный запрет |

Evidence в локальном пакете /workspace/ma-001/evidence: resume-2026-11-16.json, source-index.json. Не включают source bodies или credentials.
