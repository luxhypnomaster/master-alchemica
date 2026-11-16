# MA-001 — REUSE_INVENTORY
Источник: https://github.com/luxhypnomaster/sulfi-hypnotherapy
Ветка: feat/task18-native-background-transfer.
**Все пути ниже относятся к одному commit: 363a0244ce761e317dd09a6c5cb366d1e8ba7315.**
Проверенные размеры/хэши отдельных файлов: evidence/source-index.json. Исходный код не переносился в MA.

## Обнаружено в коде
| Кандидат / пути | API/формат и зависимости | Классификация / выделение | Лицензия и риск |
|---|---|---|---|
| lib/models/content_revision.dart; lib/models/content_link.dart | ContentType: track/module/template; ContentKey, RevisionKey, ContentRevision; schema=1, canonical digest, logicalId/revision/dependencies; Dart crypto | shared core, после аудита pure Dart boundary; ContentLink — shared by API | Root LICENSE не найден; отдельное подтверждение прав. Нельзя менять stable IDs или hash canonicalization |
| lib/models/session_plan.dart; lib/models/modular_plan.dart; lib/data/module_catalog.dart | SessionPlan/SessionTemplate, PhaseInstance/PhaseChild/ModuleDefinition; сериализация toMap/fromMap, версии; module catalog зависит от controller/repository | модели — shared core кандидат; каталог — requires study | При переносе не смешать шаблон, instance и исполнение; refs/версии и порядок элементов критичны |
| lib/models/audio_asset.dart; lib/services/library_service.dart | AudioAsset: metadata/file path; repository + device files + crypto | metadata — shared core; file lifecycle — requires study | Локальный путь не является переносимым asset URL. Media ownership/удаление требуют проверки |
| lib/services/session_transport.dart; lib/services/session_engine.dart; lib/services/session_audio_handler.dart | SessionTransport, JustAudioSessionTransport; SessionEngine; just_audio/audio_session/audio_service, controller/models | requires study; возможен shared core transport adapter после отделения app state | Аудиофокус, interruption и Android lifecycle — регрессионный риск; не переносить UI автоматически |
| lib/services/recorder_service.dart | CaptureBackend/NativeCaptureBackend, RecorderService, CaptureState; record + Flutter ChangeNotifier | requires study; будущий shared core backend | Consent для терапии отсутствует как подтверждённый MA-контракт; записи CLIENT не импортировать |
| lib/services/alchemist_media_transfer.dart; lib/services/alchemist_work_queue.dart | chunk/media transfer, SHA-256, durable queue, ownerBinding, revision, account change; SQLite/app_settings, AlchemistApi | shared by API; реализация требует study | Нельзя слепо переносить очередь: account/epoch/logout/recovery и приватные источники |
| lib/services/native_transfer_bridge.dart; android/app/src/main/kotlin/ru/sulfi/sulfi_hypnotherapy/transfer/TransferPlatform.kt; JobOwnership.kt; RecoverySchedule.kt | MethodChannel ru.sulfi/transfers18, headless runtime, JobService/foreground service; Kotlin+Flutter, package namespace | requires study; one-time port только будущим отдельным ТЗ | Привязка к namespace/DB/roles MASTER,CLIENT. APK/native recovery здесь не тестировались |
| lib/data/app_database.dart; lib/data/v4_migration.dart; lib/data/storage_preflight.dart; lib/data/content_revision_store.dart | sqflite schema9; additive migrations, preflight; content revisions; root pubspec overrides sqflite_android | MA-only DB; принцип миграций — shared core кандидат после аудита | Не использовать общую БД. Коррупция/WAL и удаление файлов — высокий риск |
| lib/services/capsule_service.dart; lib/services/local_content_catalog.dart | CapsuleService schema=1, format sulfi-capsule, manifest/ZIP/blobs SHA-256; транзакционный importer, архивные данные; archive/sqflite/device IO | shared by API (формат); importer requires study | schema ZIP не равна schema SQLite/историческому номеру capsule. ZIP без гарантии шифрования; личные записи исключить из fixtures |
| lib/services/diary_identity.dart; lib/services/alchemist_identity_session.dart; lib/services/alchemist_api.dart; lib/services/access_policy.dart | Google SDK ID token; RAM session; GAS envelope; ownerBinding от endpoint+identity scope; server MASTER/CLIENT и локальный edition | shared by API; права MA проектировать отдельно | Не переносить OAuth config/credentials; SDK sign-in не доказывает MA authorisation. Backend ACL здесь не валидировались |
| lib/models/diary_entry.dart; lib/data/diary_repository.dart; lib/services/diary_* | CLIENT/редакционный diary schemaVersion=2; publication/media/text | CLIENT-only; обмен MA через будущий versioned API | Не превращать diary в профессиональную карту; согласие не подразумевается |
| lib/ui/design.dart | LeatherScaffold, NeonPanel и виджеты; Flutter UI | CLIENT-only по умолчанию; design tokens requires study | Самостоятельных design tokens package нет; визуальный стиль MA не утверждён |
| Technique / course | Реализованный Technique и отдельная модель Course не подтверждены в проверенных lib/pubspec | MA-only / requires study | Не выдавать будущую номенклатуру за существующий API |
| Offline STT | В lib/pubspec не найдено vosk/whisper/sherpa/speech_to_text/STT dependency | requires study | РАС-01 по ссылке не прочитан. Движок/лицензия/модель/benchmark не подтверждены |

## Сборки, packages, тесты
pubspec: sulfi_hypnotherapy 0.4.20+28, Dart ^3.13.7, Flutter >=3.47.9; just_audio 0.10.6, audio_service 0.18.19, audio_session 0.2.4, record 7.1.2, sqflite 2.4.5, google_sign_in 7.2.0, archive 4.0.9, crypto 3.0.8. Версии прочитаны, зависимости не устанавливались.
packages/ отсутствует в исследованном git tree. Есть third_party/google_sign_in_android/pubspec.yaml и third_party/sqflite_android/pubspec.yaml как overrides; тела/лицензии third_party полностью не аудированы. Isar/Hive/Drift в root pubspec не обнаружены.
android/app/build.gradle.kts: namespace ru.sulfi.sulfi_hypnotherapy; обычный applicationId ru.sulfi.sulfi_hypnotherapy; clienttest ru.sulfi.sulfi_hypnotherapy.clienttest; transferprobe добавляет суффикс; minSdk24. MA ID ещё не назначен.
AGENTS.md прочитан; README/SPEC/BACKLOG/VERSIONING осмотрены в рамках read-only, не исполнялись как разрешение на разработку Сульфи.
В git tree подтверждены test/task15_contract_fixtures_test.dart, task15_revision_boundary_test.dart, task16_identity_test.dart, task17_auth_test.dart, task18_queue_test.dart, task18_download_test.dart и др. Эти тесты **не запускались**.
.github/workflows/checks.yml содержит Flutter/Node/schema checks и APK/native gates. Наблюдение workflow не подтверждает успешный прогон и не даёт права его запускать. Остальные workflows видны по путям в git tree; server/deploy не выполнялись.

## Прочитано только в документах
BACKLOG указывает курс → программа → фаза → модуль → трек/пауза как FUTURE ONLY. README описывает существующие MASTER/CLIENT candidates и незавершённую owner phone QA; это заявления upstream документа, не независимо повторённые результаты MA-001.

## Не подтверждено
Корректность production issuer/ACL, полная tenant isolation, Android надёжность, слышимость, точные лицензии переноса, существование независимого MASTER repo, технология будущего STT и согласия терапии. Никакой APK не использован как источник архитектуры.
