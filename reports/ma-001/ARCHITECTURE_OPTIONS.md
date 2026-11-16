# MA-001 — ARCHITECTURE_OPTIONS
Рекомендация: отдельный private master-alchemica и отдельная воспроизводимая MA среда. Это соответствует владельцу и не связывает профессиональные записи с CLIENT diary.

| Модель | Польза | Цена/риск | Решение |
|---|---|---|---|
| Отдельные repo | Разные роли, БД, CI и релизы; минимальный риск для текущей Сульфи | Нужно версионировать контракты/зависимости | Выбрать |
| Monorepo | Атомарные изменения общих packages, общий tooling | Нужна миграция существующего repo; права видят сразу три продукта; сложнее независимые релизы | Для MA-001 не подходит; преимущества не оправдывают изменение границ |
| Вечная ветка Sulfi | Быстрый старт на похожем коде | Дрейф, конфликты, общие credentials/CI, риск CLIENT/MASTER | Отвергнуть |

Текущее дерево Sulfi — один Flutter application без packages/. ContentRevision/модульные модели выглядят кандидатами на чистый Dart core; transport/storage/Android bridge привязаны к существующим SQLite, owner identity и native namespace. Не следует объявлять их готовой shared library.
Порядок: сначала спецификация wire contracts и synthetic golden fixtures; затем лицензии/границы API; только после отдельного согласования — выделение первого малого pure Dart package. Не создавать третий repo заранее. Возможное временное размещение пакета в MA допустимо лишь по новому заданию с правами на перенос; сейчас никакой перенос не сделан.
Будущий package: semver, immutable tag и exact commit pin, самостоятельные проверки, compatibility matrix поддерживаемых CLIENT/MASTER/MA версий, независимые release cycles.
Профессиональный UI, клинические материалы и согласия — MA-only. Каталог и обмен — shared by API. Внешние credentials и signing не переиспользуются.

## Постоянный доступ к исходникам
Сейчас работает отдельный sparse/shallow checkout на immutable commit, не межпроектная память. При уничтожении текущей машины его наличие не гарантировано.
Предпочтение: изолированный reader/snapshot publisher с contents:read к Sulfi; в MA среду передавать отобранный source-only snapshot без секретов/медиа и без write credential Сульфи. Для snapshot фиксировать upstream URL, ref, SHA, список файлов и digest; обновлять по новому одобренному SHA, не использовать moving HEAD как dependency.
Текущая App repository_selection=all и contents:write означает остаточный риск API-записи. Даже добавление второго checkout в MA не создаёт read-only границу. /dev/null push URL ограничивает только обычный git push.
Вариант с отдельным read-only токеном безопасен только при реальной изоляции от уже доступного all-repositories write credential. Snapshot предпочтительнее, если эту изоляцию нельзя обеспечить.
UI текущей версии для нескольких repos не наблюдался; гарантировать его поддержку нельзя. Если конфигурация поддерживает только один repo, основным выбрать MA, а Sulfi держать отдельным безопасным checkout/snapshot. Не клонировать его внутрь MA git tree.
Обновление: сверить чистоту analysis checkout → получить новый одобренный ref штатным reader → detached SHA → проверить source paths/schema diff → обновить SOURCE record в отчётах. Не push, не запускать CI Sulfi, не менять её конфигурацию.
