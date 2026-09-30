# Дерево приватной реализации

[К обзору проекта](../README.md) · [Архитектура](ARCHITECTURE.md)

Полное дерево 256 отслеживаемых файлов проверенной приватной копии, сформированное из `git ls-files`. Указаны только относительные пути; содержимое файлов здесь не публикуется. Корневой ярлык `private-implementation/` служит обозначением дерева, а не именем локального каталога.

Эти файлы отсутствуют в публичной витрине. Имена схем, конфигураций, зависимостей и тестов показывают структуру проекта, но не раскрывают их содержимое или результаты запуска. Неотслеживаемые локальные данные, служебный каталог Git и рабочие материалы в список не входят.

```text
private-implementation/
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── assistant.py
│   │   │   ├── checks.py
│   │   │   ├── i18n.py
│   │   │   ├── presets.py
│   │   │   ├── project.py
│   │   │   ├── projects.py
│   │   │   ├── results.py
│   │   │   ├── settings.py
│   │   │   └── standards.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── blueprint.py
│   │   │   ├── check_queue.py
│   │   │   ├── checker.py
│   │   │   ├── chunker.py
│   │   │   ├── embeddings.py
│   │   │   ├── extraction.py
│   │   │   ├── i18n.py
│   │   │   ├── jobs.py
│   │   │   ├── llm.py
│   │   │   ├── ocr.py
│   │   │   ├── results.py
│   │   │   ├── settings_store.py
│   │   │   ├── source_metadata.py
│   │   │   └── sync.py
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── utils.py
│   ├── tests/
│   │   ├── test_assistant.py
│   │   ├── test_check_queue.py
│   │   ├── test_source_ingestion.py
│   │   └── test_source_metadata.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── BackendStatus.tsx
│   │   │   ├── FileTree.tsx
│   │   │   ├── ResultBits.tsx
│   │   │   └── VersionHistoryModal.tsx
│   │   ├── pages/
│   │   │   ├── PresetsPage.tsx
│   │   │   ├── ProjectPage.tsx
│   │   │   ├── ResultsPage.tsx
│   │   │   ├── SettingsPage.tsx
│   │   │   └── StandardsPage.tsx
│   │   ├── api.ts
│   │   ├── App.tsx
│   │   ├── i18n.ts
│   │   ├── index.css
│   │   └── main.tsx
│   ├── tests/
│   │   └── integration.test.mjs
│   ├── .env.example
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
├── frontend-danilisssimo/
│   ├── src/
│   │   ├── components/
│   │   │   ├── base/
│   │   │   │   ├── BaseAlert.vue
│   │   │   │   ├── BaseBadge.vue
│   │   │   │   ├── BaseButton.vue
│   │   │   │   ├── BaseInput.vue
│   │   │   │   ├── BaseMenu.vue
│   │   │   │   ├── BaseModal.vue
│   │   │   │   ├── BaseSelect.vue
│   │   │   │   ├── BaseSpinner.vue
│   │   │   │   ├── BaseTextarea.vue
│   │   │   │   └── BaseToast.vue
│   │   │   ├── common/
│   │   │   │   └── AvtodorLogo.vue
│   │   │   ├── features/
│   │   │   │   ├── assistant/
│   │   │   │   │   ├── ChatMessage.vue
│   │   │   │   │   └── TypingIndicator.vue
│   │   │   │   ├── checks/
│   │   │   │   │   ├── __tests__/
│   │   │   │   │   │   ├── CheckFileDropdown.spec.js
│   │   │   │   │   │   ├── CheckFileList.spec.js
│   │   │   │   │   │   └── CheckModeSegmented.spec.js
│   │   │   │   │   ├── CheckDetailPanel.vue
│   │   │   │   │   ├── CheckFileDropdown.vue
│   │   │   │   │   ├── CheckFileList.vue
│   │   │   │   │   ├── CheckModeSegmented.vue
│   │   │   │   │   ├── CheckProgressPanel.vue
│   │   │   │   │   ├── CheckResultsModal.vue
│   │   │   │   │   └── ChecksTable.vue
│   │   │   │   ├── issues/
│   │   │   │   │   └── IssueCard.vue
│   │   │   │   └── sources/
│   │   │   │       ├── __tests__/
│   │   │   │       │   └── SourceUploadModal.spec.js
│   │   │   │       └── SourceUploadModal.vue
│   │   │   └── layout/
│   │   │       ├── __tests__/
│   │   │       │   └── AppSidebar.spec.js
│   │   │       ├── AppLayout.vue
│   │   │       └── AppSidebar.vue
│   │   ├── router/
│   │   │   └── index.js
│   │   ├── services/
│   │   │   ├── __tests__/
│   │   │   │   ├── analysisService.spec.js
│   │   │   │   ├── assistantService.spec.js
│   │   │   │   ├── authService.spec.js
│   │   │   │   ├── complianceService.spec.js
│   │   │   │   ├── documentsService.spec.js
│   │   │   │   ├── localizationService.spec.js
│   │   │   │   ├── presetsService.spec.js
│   │   │   │   ├── projectFilesService.spec.js
│   │   │   │   ├── reportsService.spec.js
│   │   │   │   └── settingsService.spec.js
│   │   │   ├── mock/
│   │   │   │   ├── data.js
│   │   │   │   ├── datass.js
│   │   │   │   └── helpers.js
│   │   │   ├── analysisService.js
│   │   │   ├── apiError.js
│   │   │   ├── assistantService.js
│   │   │   ├── authService.js
│   │   │   ├── checksService.js
│   │   │   ├── complianceService.js
│   │   │   ├── documentsService.js
│   │   │   ├── index.js
│   │   │   ├── localizationService.js
│   │   │   ├── presetsService.js
│   │   │   ├── projectFilesService.js
│   │   │   ├── remarksService.js
│   │   │   ├── reportsService.js
│   │   │   └── settingsService.js
│   │   ├── stores/
│   │   │   ├── __tests__/
│   │   │   │   ├── auth.spec.js
│   │   │   │   ├── documents.spec.js
│   │   │   │   ├── localization.spec.js
│   │   │   │   ├── projects.spec.js
│   │   │   │   └── theme.spec.js
│   │   │   ├── assistant.js
│   │   │   ├── auth.js
│   │   │   ├── checks.js
│   │   │   ├── documents.js
│   │   │   ├── localization.js
│   │   │   ├── projects.js
│   │   │   ├── remarks.js
│   │   │   ├── reports.js
│   │   │   └── theme.js
│   │   ├── styles/
│   │   │   ├── base.css
│   │   │   ├── main.css
│   │   │   └── tokens.css
│   │   ├── utils/
│   │   │   ├── __tests__/
│   │   │   │   ├── checkStatus.spec.js
│   │   │   │   ├── compliancePresentation.spec.js
│   │   │   │   ├── fileFormats.spec.js
│   │   │   │   ├── formatters.spec.js
│   │   │   │   ├── issues.spec.js
│   │   │   │   ├── pluralize.spec.js
│   │   │   │   ├── presetSelection.spec.js
│   │   │   │   ├── reportStatus.spec.js
│   │   │   │   ├── runPresentation.spec.js
│   │   │   │   └── sourceStaging.spec.js
│   │   │   ├── checks.js
│   │   │   ├── checkStatus.js
│   │   │   ├── compliancePresentation.js
│   │   │   ├── documentStatus.js
│   │   │   ├── download.js
│   │   │   ├── fileFormats.js
│   │   │   ├── formatters.js
│   │   │   ├── issues.js
│   │   │   ├── pluralize.js
│   │   │   ├── presetSelection.js
│   │   │   ├── reportStatus.js
│   │   │   ├── reportText.js
│   │   │   ├── runPresentation.js
│   │   │   ├── sourceStaging.js
│   │   │   └── validators.js
│   │   ├── views/
│   │   │   ├── __tests__/
│   │   │   │   ├── ChecksView.spec.js
│   │   │   │   ├── LoginView.spec.js
│   │   │   │   ├── PresetsView.spec.js
│   │   │   │   ├── ReportsView.spec.js
│   │   │   │   └── SettingsView.spec.js
│   │   │   ├── AssistantView.vue
│   │   │   ├── ChecksView.vue
│   │   │   ├── DocumentsView.vue
│   │   │   ├── LoginView.vue
│   │   │   ├── PresetsView.vue
│   │   │   ├── RemarksPreviewView.vue
│   │   │   ├── RemarksView.vue
│   │   │   ├── ReportDetailView.vue
│   │   │   ├── ReportsView.vue
│   │   │   ├── SettingsView.vue
│   │   │   └── SourcesView.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── index.html
│   ├── jsconfig.json
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   ├── skills-lock.json
│   ├── vite.config.js
│   └── vitest.config.js
├── st1_embedding_server/
│   ├── .env.example
│   ├── .gitignore
│   ├── docker-compose.yml
│   ├── Dockerfile.cpu
│   ├── Dockerfile.cuda
│   ├── embedding_server.py
│   ├── README.md
│   └── requirements.txt
├── translations/
│   ├── en.json
│   └── ru.json
├── universal_auth/
│   ├── example/
│   │   └── app.py
│   ├── src/
│   │   └── universal_auth/
│   │       ├── static/
│   │       │   ├── auth.css
│   │       │   └── auth.js
│   │       ├── templates/
│   │       │   ├── admin/
│   │       │   │   ├── audit.html
│   │       │   │   ├── bulk_create.html
│   │       │   │   ├── bulk_result.html
│   │       │   │   ├── password_reset.html
│   │       │   │   ├── sessions.html
│   │       │   │   ├── user_edit.html
│   │       │   │   ├── user_new.html
│   │       │   │   └── users.html
│   │       │   ├── 404.html
│   │       │   ├── api_key_created.html
│   │       │   ├── base.html
│   │       │   ├── change_password.html
│   │       │   ├── login.html
│   │       │   ├── profile.html
│   │       │   ├── recovery_codes.html
│   │       │   ├── setup.html
│   │       │   ├── totp.html
│   │       │   └── totp_enroll.html
│   │       ├── __init__.py
│   │       ├── audit.py
│   │       ├── bulkcreate.py
│   │       ├── config.py
│   │       ├── csrf.py
│   │       ├── db.py
│   │       ├── deps.py
│   │       ├── integration.py
│   │       ├── middleware.py
│   │       ├── migrations.py
│   │       ├── passwords.py
│   │       ├── ratelimit.py
│   │       ├── repo.py
│   │       ├── routes_admin.py
│   │       ├── routes_auth.py
│   │       ├── routes_profile.py
│   │       ├── secret.py
│   │       ├── sessions.py
│   │       ├── templating.py
│   │       ├── tokens.py
│   │       └── totp.py
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_admin.py
│   │   ├── test_api_keys.py
│   │   ├── test_bulk.py
│   │   ├── test_csrf.py
│   │   ├── test_gate.py
│   │   ├── test_login.py
│   │   ├── test_ratelimit.py
│   │   ├── test_repo.py
│   │   ├── test_setup.py
│   │   └── test_totp.py
│   ├── .gitignore
│   ├── pyproject.toml
│   └── README.md
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
└── README.md
```
