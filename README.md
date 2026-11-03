# backup-job-failure-analyzer

Find the backup jobs that fail most: failure rate per job, highest first, with the overall rate for context.

## How to run

```sh
python3 main.py backups.csv
```

## Example output

```
Nightly-DB: 50% failed (10 runs)
Overall failure rate: 25%
```

Standard library only. Run the tests with `python3 -m unittest discover`.
