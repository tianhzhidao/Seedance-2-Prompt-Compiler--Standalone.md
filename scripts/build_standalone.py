#!/usr/bin/env python3
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
OUTPUT = ROOT / "Seedance-2-Prompt-Compiler-Standalone.md"

REFERENCE_ORDER = [
    "segmentation.md",
    "segment-boundaries.md",
    "shot-language.md",
    "emotion-shot-library.md",
    "advanced-camera-moves.md",
    "prompt-output.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)


def normalize_links(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\(references/[^)]+\)", r"\1（见本文件对应章节）", text)
    text = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]+\.md\)", r"\1（见本文件对应章节）", text)
    return text


def standalone_skill_body(text: str) -> str:
    text = strip_frontmatter(text)
    text = re.sub(
        r"\n## 必须读取的参考\n.*?(?=\n## 输入识别\n)",
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r"\n## 单文件兼容版\n.*\Z",
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    return normalize_links(text).strip()


def main() -> None:
    parts = [
        "# Seedance 2.0 Prompt Compiler｜单文件通用版",
        "",
        "> 适用于不支持 Skills 目录结构的 AI。将本文件全文作为系统指令或项目指令使用。",
        "> 本文件由技能包自动合并生成；不依赖外部 reference 文件。",
        "",
        standalone_skill_body(read_text(SKILL)),
    ]

    for name in REFERENCE_ORDER:
        path = ROOT / "references" / name
        if not path.is_file():
            raise FileNotFoundError(f"Missing reference: {path}")
        parts.extend([
            "",
            "---",
            "",
            normalize_links(read_text(path)),
        ])

    content = "\n".join(parts).rstrip() + "\n"
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUTPUT} ({len(content)} characters)")


if __name__ == "__main__":
    main()
