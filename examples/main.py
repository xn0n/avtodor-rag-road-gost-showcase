"""Illustrative portfolio example: static stage labels, no private implementation."""

import json


def main() -> None:
    """Print synthetic project metadata without processing documents or services."""
    overview = {
        "project": "Автодор · RAG для проектной документации",
        "example_kind": "illustrative_static_description",
        "implements_document_validation": False,
        "stages": [
            "Подготовка нормативных источников",
            "Извлечение проектного документа",
            "Поиск релевантных фрагментов",
            "Модельный анализ",
            "Описание результата и отчёта",
        ],
    }
    print(json.dumps(overview, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
