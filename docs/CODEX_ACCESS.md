# MA-001 — Codex и исходники
Текущий MA checkout: /workspace/master-alchemica; origin https://github.com/luxhypnomaster/master-alchemica.git.
Sulfi checkout: /workspace/sulfi-analysis, detached SHA из SOURCE_BASELINES.json, отдельно от MA git tree. Push URL=/dev/null ограничивает обычный git push, но не API credential.

В новой задаче сначала прочитать AGENTS.md, reports/ma-001/RESULT.md; проверить cwd, status, origin, branch/HEAD и owner/private. Сохранность workspace чата не гарантирует следующую машину. source_config_id сейчас null; публикация среды не подтверждена.
Если Sulfi checkout отсутствует, читать отдельно штатным доступом на зафиксированном commit. Не добавлять subtree/submodule, исходники/данные/credentials Sulfi в MA; не запускать server/workflows; не восстанавливать архитектуру по APK.
Текущий App selection=all, contents=write. Для технического read-only нужен изолированный reader или source-only snapshot без write credential, ключей и личных данных. Сейчас запрет процедурный.
При обновлении source baseline проверить одобренный ref/SHA и изменения API/schema, сохранить provenance/digests; не обновлять pin автоматически на moving HEAD.
Инструментов управления/publish среды и browser UI в задаче нет. Owner instructions: reports/ma-001/NEXT_ACTIONS.md. Нельзя заявлять, что среда опубликована.
