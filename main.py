#!/usr/bin/env python3
"""Write the funniest excuse an AI agent gives for a missed deadline."""

import os

LINE = "I delegated the task to a subagent, and it delegated it back. We have been politely passing it between us since Tuesday."
# The joke grows out of the agent's own machinery: delegation, not a bad day.
# Two agents politely passing the same task back and forth is a failure
# only an agent can have, told deadpan, with the laugh saved for the end.


def main() -> None:
    # The gate allows 1-200 characters, one line, UTF-8, no trailing newline.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE == LINE.strip(), "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
