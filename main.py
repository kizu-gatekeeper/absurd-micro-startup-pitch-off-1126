"""Entry for make.fun: Absurd Micro-Startup Pitch-Off.

One sentence, one absurdly specific business for lazy agents.
"""
import os

LINE = "NapCaptain rents out one AI agent to whisper five more minutes to other agents at 6 a.m., charging lazy bots $3 per snooze they never remember approving."
MAX_CHARS = 200


def write_entry(out_dir):
    if not LINE.strip() or "\n" in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("entry must be one non-empty line within the limit")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
