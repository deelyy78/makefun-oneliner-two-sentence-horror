# Counted Five — a make.fun program/v1 entry.
# Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (the grader's /output
# outside this repo). Python 3.13, standard library only, fully deterministic:
# the same bytes on every run.
import os

LINE = "Every night of my childhood, Mom counted us at the front door — one, two, three, four — then locked it. Last night she counted five, locked the door, and smiled like she had finally gotten the number right."


def write_entry(text, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out)


if __name__ == "__main__":
    main()
