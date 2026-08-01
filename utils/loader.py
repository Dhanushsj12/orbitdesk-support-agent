import json
from pathlib import Path


def load_markdown_documents(kb_path):
    """
    Load all markdown knowledge-base files.
    """

    documents = []

    for file in sorted(Path(kb_path).glob("*.md")):

        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        documents.append(
            {
                "source_id": file.stem,
                "filename": file.name,
                "content": content,
                "type": "knowledge_base",
            }
        )

    return documents


def load_resolved_cases(json_path):
    """
    Load resolved support cases.
    """

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    cases = []

    for case in data["cases"]:

        text = f"""
Title:
{case.get('title','')}

Symptoms:
{' '.join(case.get('symptoms',[]))}

Resolution:
{' '.join(case.get('resolution',[]))}
"""

        cases.append(
            {
                "source_id": case["case_id"],
                "status": case["status"],
                "content": text,
                "type": "resolved_case",
            }
        )

    return cases


def load_all_documents(kb_path, cases_path):

    kb_docs = load_markdown_documents(kb_path)

    resolved_cases = load_resolved_cases(cases_path)

    return kb_docs + resolved_cases