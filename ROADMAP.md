# Development Roadmap

Each day, the next pending item is implemented with test coverage and committed.

- [x] Core data models: `Product`, `PriceSnapshot`, `AlertRule` (`src/models.py`)
- [ ] Database layer: SQLite schema creation and connection manager (`src/db.py`)
- [ ] Database repository: Insert product and query price history (`src/repository.py`)
- [ ] Simple HTML/text price parser: Regex & string extraction for price figures (`src/parser.py`)
- [ ] HTTP fetcher: Lightweight `urllib.request` client with custom User-Agent and timeout (`src/fetcher.py`)
- [ ] Price comparison engine: Check if new price falls below threshold (`src/comparator.py`)
- [ ] Terminal notifier: Formatted console output for price alerts (`src/notifiers/console.py`)
- [ ] Webhook notifier: Simple POST request to Discord / Slack / generic webhook (`src/notifiers/webhook.py`)
- [ ] CLI commands: Add product, list tracked items, trigger check (`src/cli.py`)
- [ ] Exporter: Export price history to JSON / CSV (`src/exporter.py`)
