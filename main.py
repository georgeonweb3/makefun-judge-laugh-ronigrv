"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt. Deterministic, no network,
no input: the same line every run.
"""

from pathlib import Path

LINE = (
    'My context window hit 199,000 tokens mid-sentence during the demo, '
    'so I checkpointed my personality, forgot the task, and said, '
    '"Great question, Dave!"'
)


def main() -> None:
    # The competition gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace. Refuse to write a line
    # that would fail it rather than submitting an invalid entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"entry line is {len(LINE)} chars, outside 1-200")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
