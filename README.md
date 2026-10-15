# price-radar

Lightweight, dependency-free Python tool to track product prices, record history in SQLite, and trigger alerts when prices drop.

## Features (Planned & In Progress)
- Zero external dependencies (uses standard library `urllib`, `sqlite3`, `unittest`).
- SQLite storage for price tracking history.
- Simple CLI interface for adding, removing, and inspecting tracked products.
- Pluggable alert dispatcher (webhooks, terminal alerts, logs).
- HTML/JSON price parsers for common store formats.

## Quick Start
```bash
python -m unittest discover tests
python -m src.cli --help
```
