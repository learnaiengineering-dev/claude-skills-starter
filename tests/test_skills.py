import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from validate_skills import check_skill, main  # noqa: E402


def test_repo_skills_are_valid():
    assert main() == 0


def test_detects_bad_name(tmp_path):
    d = tmp_path / "skills" / "foo"
    d.mkdir(parents=True)
    f = d / "SKILL.md"
    f.write_text("---\nname: bar\ndescription: short\n---\nbody\n")
    problems = check_skill(f)
    assert len(problems) == 2


def test_detects_missing_frontmatter(tmp_path):
    d = tmp_path / "foo"
    d.mkdir()
    f = d / "SKILL.md"
    f.write_text("no frontmatter")
    assert check_skill(f)

