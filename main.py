"""Analyse backup job results: failure rate per job.

Usage: python3 main.py backups.csv
CSV columns: job,date,result (success/failed).
Failure rate per job, highest first, plus the overall rate. Jobs with
fewer than 5 runs are flagged as small samples.
"""
import argparse, csv, sys
from collections import Counter


def analyze(rows):
    totals, failed = Counter(), Counter()
    for row in rows:
        job = row["job"].strip()
        totals[job] += 1
        if row["result"].strip().lower() == "failed":
            failed[job] += 1
    out = []
    for job, total in totals.items():
        note = " (small sample)" if total < 5 else ""
        out.append((job, failed[job] / total, total, note))
    overall = (sum(failed.values()) / sum(totals.values())) if totals else 0.0
    return sorted(out, key=lambda r: -r[1]), overall


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        per_job, overall = analyze(list(csv.DictReader(f)))
    for job, rate, total, note in per_job:
        print(f"{job}: {rate:.0%} failed ({total} runs){note}")
    print(f"Overall failure rate: {overall:.0%}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
