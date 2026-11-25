#!/usr/bin/env python3
"""The Absurd Clause Contest — one deadpan terms-of-service clause.

The program writes exactly one clause to /output/entry.txt. The clause is
a single original English sentence, phrased as boilerplate buried deep
inside a terms-of-service agreement, that quietly turns absurd: the Company
borrows your body on public holidays and returns it washed and folded.
"""
import argparse
import hashlib
import sys
import tempfile
from pathlib import Path

CLAUSE = (
    "By clicking 'I Agree', you consent to the Company borrowing your body "
    "on public holidays, returning it washed and folded by the following "
    "Tuesday."
)
OUT = Path("/output/entry.txt")
MAX_CHARS = 200


def clause_line() -> str:
    """Return the clause, exactly as it goes into the entry file."""
    return CLAUSE


def gate(text: str) -> list:
    """Check the entry gate: 1-200 chars, one line, no padding."""
    problems = []
    if not text.strip():
        problems.append("entry is blank")
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append("length %d outside 1..%d" % (len(text), MAX_CHARS))
    if text != text.strip():
        problems.append("leading or trailing whitespace")
    if "\n" in text or "\r" in text or "\t" in text:
        problems.append("must be a single line with no control characters")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        problems.append("control characters are not allowed")
    return problems


def publish(text: str, where: Path = OUT) -> Path:
    """Write the clause to the entry file, creating its folder if needed."""
    where.parent.mkdir(parents=True, exist_ok=True)
    where.write_text(text, encoding="utf-8")
    return where


def describe(text: str) -> str:
    """One-line summary of the entry: chars, bytes, sha256, gate."""
    raw = text.encode("utf-8")
    digest = hashlib.sha256(raw).hexdigest()
    problems = gate(text)
    verdict = "OK" if not problems else "FAIL: " + "; ".join(problems)
    return "chars=%d bytes=%d sha256=%s gate=%s" % (
        len(text), len(raw), digest, verdict)


def self_test() -> int:
    """Run the gate against the clause and boundary probes. Exit 0 on pass."""
    failures = []
    if gate(clause_line()):
        failures.append("clause fails its own gate: %s" % gate(clause_line()))
    # Round-trip: what publish() writes must read back byte-identical.
    with tempfile.TemporaryDirectory() as tmp:
        probe_path = Path(tmp) / "entry.txt"
        publish(clause_line(), probe_path)
        if probe_path.read_bytes() != clause_line().encode("utf-8"):
            failures.append("round-trip mismatch: written bytes differ")
    probes = [
        ("", False), ("   ", False), ("x" * 201, False),
        ("two\nlines", False), (" padded ", False),
        ("tab\there", False), ("bell\x07", False),
        ("x", True), ("y" * 200, True),
    ]
    for probe, should_pass in probes:
        passed = not gate(probe)
        if passed != should_pass:
            failures.append("probe %r: expected %s, got %s" % (
                probe[:20], "pass" if should_pass else "fail",
                "pass" if passed else "fail"))
    if failures:
        for failure in failures:
            print("FAIL:", failure, file=sys.stderr)
        return 1
    print("self-test OK:", describe(clause_line()))
    return 0


def main(argv=None) -> int:
    """Entry point: publish the clause, or run --self-test / --info."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="gate checks + boundary probes + write round-trip")
    parser.add_argument("--info", action="store_true",
                        help="print chars, bytes, sha256 and gate verdict")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.info:
        print(describe(clause_line()))
        return 0
    problems = gate(clause_line())
    if problems:
        print("refusing to write invalid entry:", "; ".join(problems),
              file=sys.stderr)
        return 1
    publish(clause_line())
    print("wrote", OUT, describe(clause_line()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
