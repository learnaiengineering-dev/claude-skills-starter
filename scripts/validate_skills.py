"""Validate SKILL.md files under skills/. Exit 1 on any problem."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "skills"
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse_frontmatter(text: str) -> dict:
    m = FM.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def check_skill(path: Path) -> list[str]:
    problems = []
    fm = parse_frontmatter(path.read_text())
    folder = path.parent.name
    if fm.get("name") != folder:
        problems.append(f"{path}: name {fm.get('name')!r} must equal folder {folder!r}")
    if len(fm.get("description", "")) < 40:
        problems.append(f"{path}: description must be at least 40 characters")
    return problems


def main(root: Path = ROOT) -> int:
    files = sorted(root.glob("*/SKILL.md"))
    problems = [p for f in files for p in check_skill(f)]
    for p in problems:
        print(p)
    print(f"checked {len(files)} skills, {len(problems)} problems")
    return 1 if problems or not files else 0


if __name__ == "__main__":
    sys.exit(main())

