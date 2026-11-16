# MA-001 — CONTRACTS_DRAFT
**DRAFT v0.1; предложение для MA-002, не утверждённая JSON Schema, не реализованный API.**
Основа: Sulfi commit 363a0244ce761e317dd09a6c5cb366d1e8ba7315; реальные исходные пути перечислены в REUSE_INVENTORY. Ранее опубликованный draft ZIP уточнён, но production contracts не менялись.

## Идентичность и каталог
Будущие Program, Phase, Module, Track, MediaAsset, Technique, CatalogVersion получают собственные versioned JSON Schema: стабильные $id с major версией и schemaVersion. Product namespace отделён от user/tenant namespace: sulfi-client, sulfi-editorial-master, master-alchemica. Новые объекты — UUID; импортируемые прежние logicalId сохраняются как source reference, а не переписываются UUID миграцией.
Общая оболочка: objectId, schemaVersion, objectType, sourceProduct, sourceObjectType/sourceLogicalId/sourceRevisionId, authorId, revisionId, createdAt/updatedAt, dependencies[]. Составной source key предотвращает совпадение ID разных продуктов. Список разрешённых типов versioned; неизвестный major отклоняется без потери исходного payload.
Program содержит упорядоченные ссылки Phase; Phase — Module; Module — Track/Pause. Course отдельно только после утверждения: в текущем source не подтверждён. Pause — типизированный элемент с длительностью/единицей, не фиктивный аудиофайл.
CatalogVersion — manifest ревизий и хэшей, без credentials и приватных client records. Technique — идентичность/метаданные и ссылки на библиотеку, без данных пациента и без привязки к CLIENT UI.

## Соответствие реальному Sulfi
lib/models/content_revision.dart сейчас поддерживает только track/module/template, schema=1, RevisionKey и digest. Программа в UI не даёт оснований переименовывать wire template в program в существующей Сульфи. Нужен adapter template→предлагаемый Program, сохраняющий sourceLogicalId и sourceRevision.
PhaseInstance/PhaseChild/ModuleDefinition из modular_plan.dart — источник для изучения семантики, не готовая schema нового API.
ContentRevision schema=1, DiaryEntry schemaVersion=2, SQLite version9 и CapsuleService schema=1 — независимые версии; одной цифрой их заменять нельзя.

## MediaAsset и Import/Export
MediaAsset: assetId/schemaVersion, source key, revision, sha256, bytes, mimeType, durationMs при наличии, owner/tenant, protection class. Метаданные отделены от защищённого источника и краткоживущего авторизованного download descriptor. Локальные filePath и credentials никогда не передаются как общий catalog contract.
Скачивание во временный staging; проверка bytes/hash; атомарное подключение к локальному объекту; отмена/повтор не заменяют чужой файл. SHA для целостности не является правом доступа.
Import envelope: format/schemaVersion, sourceProduct, exportId, manifest/revisions/dependencies, checksums. Идемпотентность по exportId+source key+revision; конфликт одинакового ID с другими bytes/hash завершается ошибкой без тихой перезаписи. Защита ZIP path traversal, лимиты размера/количества, транзакционность, тестируемая миграция. Нынешний sulfi-capsule изучать через adapter, не менять его schema в этом задании.

## AuthIdentity, roles и согласие
AuthIdentity: issuer+subject, audience, tenantId, actorProduct, role/scopes, expiry; сервер проверяет подпись/issuer/audience/expiry и ACL. Общий subject не означает общий токен. Не копировать существующий Google client config или signing.
Scope roles: owner/therapist/client/admin с явными действиями, ресурсом и tenant; deny by default. Роль editorial MASTER не даёт therapist прав; локальный CLIENT edition не является доказательством server ACL.
Consent: consentId/schemaVersion, subjectId, therapistId, purpose, data classes, policyVersion, grantedAt, expiresAt при наличии, revokedAt, evidence reference. Отдельные назначения для записи, транскрипции, обмена и хранения. Отзыв блокирует новые операции и запускает утверждённую политику retention; обещать мгновенное удаление всех копий нельзя.
MA case records и CLIENT private diary — разные БД/хранилища/ключи доступа. Пользователь/специалист и tenant изолированы. Обмен по согласованному subset; журналы аудита без содержимого записей/токенов. Запись/отправка только после явного согласия, видимая индикация, управляемое локальное удаление; фоновые transfers привязаны к owner+epoch.

## ClientTherapistExchange v1
Предлагаемый /v1 namespace, не существующий production endpoint. Message envelope: messageId/schemaVersion, sender/recipient, tenantId, correlationId, sentAt, consentId, resource references, attachment descriptors, idempotencyKey.
Методы: отправить scoped message, получить authorized attachment, подтвердить получение, отозвать доступ. Никакого прямого чтения приватной БД другого продукта. Авторизация проверяется для каждого ресурса, а не только сообщения. Retry не создаёт дубль; смена аккаунта останавливает старую очередь. Мультимедиа отделены от текста и доступны по ограниченным дескрипторам. Не выдавать сведения о чужих клиентах через ошибки.

## STT
Отдельный manifest engine/model/modelVersion/license/hash/languages/requirements, модель загружается по явному выбору и проверяется; weights не включать в APK. Результат содержит sourceRecordingId, consentId, engine/model versions, segments/timing и отметку ручной правки. Реальные записи не отправлять во внешние системы без отдельного согласия. Никакого утверждения, что STT уже реализован.

## Совместимость и проверка будущей реализации
- Матрица producer/consumer CLIENT/MASTER/MA по поддерживаемым major/minor; минимум текущий и предыдущий поддерживаемый формат. Неизвестный major — безопасный отказ.
- Только synthetic fixtures: legacy track/module/template→новый envelope→roundtrip со стабильными ID/hash/dependencies.
- Golden canonicalization/digest; тот же ID с другими bytes; повторный импорт; dangling references; unsupported schema; ZIP traversal/bomb limits; crash mid-import без частичной записи.
- Negative auth: другой tenant/owner, истёкший/wrong audience токен, роль MASTER вместо therapist, revoked consent, смена аккаунта во время transfer.
- Миграции копий synthetic SQLite/JSON: payload/ID/media hash сохраняются, downgrade и несовместимые migrations отклоняются. Клиентские дневники не становятся MA картами.
- Contract change PR проверяет consumers по pinned версиям; shared Dart package использует semver + immutable tag/exact commit. Изменение одного repo не требует синхронного релиза остальных.
Эти тесты предложены, не реализованы/запущены MA-001. Локальная проверка организационных файлов не подменяет их.
