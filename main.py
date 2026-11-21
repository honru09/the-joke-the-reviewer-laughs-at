import os
from pathlib import Path

JOKE = (
    "I asked the AI agent to resolve a race condition in checkout; it apologized"
    " profusely, refactored the entire pipeline into async Rust, and added a"
    " three-second sleep.\n"
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
