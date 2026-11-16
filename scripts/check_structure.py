"""MA-001: offline organizational checks; no dependencies or network."""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
required = {
    "README.md", "AGENTS.md", ".gitignore",
    "docs/REPOSITORY_POLICY.md", "docs/CONTRACTS_DRAFT.md",
    ".github/workflows/docs-check.yml", "scripts/check_structure.py",
}
allowed = {".md", ".json", ".yml", ".yaml", ".py"}
blocked = {".env", ".pem", ".key", ".p12", ".pfx", ".jks", ".keystore",
           ".db", ".sqlite", ".sqlite3", ".wav", ".mp3", ".m4a", ".mp4", ".apk"}
errors = []
found = set()
for p in sorted(root.rglob("*")):
    relative = p.relative_to(root)
    if ".git" in relative.parts or "__pycache__" in relative.parts:
        continue
    name = relative.as_posix()
    if p.is_symlink():
        errors.append(f"Symlink not allowed: {name}")
        continue
    if not p.is_file():
        continue
    found.add(name)
    if (p.suffix.lower() in blocked or p.name.startswith(".env")
            or "service-account" in p.name.lower()):
        errors.append(f"Prohibited file type/name: {name}")
        continue
    if p.suffix.lower() not in allowed and name != ".gitignore":
        errors.append(f"Unexpected organizational file: {name}")
        continue
    if p.stat().st_size > 256_000:
        errors.append(f"Oversized organizational text: {name}")
        continue
    try:
        content = p.read_text(encoding="utf-8")
        if "\x00" in content or not content.strip() or not content.endswith("\n"):
            errors.append(f"Invalid text: {name}")
        if p.suffix.lower() == ".json":
            json.loads(content)
    except (UnicodeError, ValueError) as exc:
        errors.append(f"Unreadable text/JSON: {name}: {type(exc).__name__}")
errors.extend(f"Required file missing: {name}" for name in sorted(required - found))
if errors:
    raise SystemExit("\n".join(errors))
print(f"MA-001 organizational structure PASS: {len(found)} text files")
print("This check does not certify absence of secrets or contract compatibility.")
