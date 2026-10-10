# Performance improvements demo

This repository is a small, intentionally practical example of performance work. It includes a list of 10 realistic performance improvements you can apply to most Python services and one targeted optimization we shipped in a PR.

## 10 practical performance improvements

1. Cache repeated string normalization in hot paths.
2. Precompute lookup tables instead of scanning lists repeatedly.
3. Use `Counter` and `defaultdict` for aggregation instead of ad hoc dict logic.
4. Avoid building temporary objects inside loops.
5. Move expensive work out of request/iteration boundaries where possible.
6. Prefer set membership checks over list membership checks for large collections.
7. Reuse compiled regexes and avoid re-creating patterns in loops.
8. Batch I/O and reduce round-trips to external services.
9. Use lazy evaluation for large result sets and only materialize as needed.
10. Add focused benchmarks to prove a change improved latency or throughput.

## Included optimization

The release includes a low-effort, high-impact fix: cache repeated category normalization inside the product summary pipeline so repeated labels are normalized once and reused.

## Running tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Benchmarks

Use `PYTHONPATH=src python3 -m timeit -s "from perf_demo.analytics import normalize_label;" "normalize_label('  Mobile Apps  ')"` to confirm the cache is effective.
