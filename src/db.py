"""SQLite veritabanı bağlantısı ve tablo oluşturma işlemleri."""
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    target_price REAL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS price_snapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    price REAL NOT NULL,
    currency TEXT NOT NULL,
    in_stock INTEGER NOT NULL,
    recorded_at TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id)
);

CREATE TABLE IF NOT EXISTS alert_rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    threshold_price REAL NOT NULL,
    notify_on_drop_only INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (product_id) REFERENCES products (id)
);
"""


def get_connection(db_path: str = "price_radar.db") -> sqlite3.Connection:
    """Veritabanı bağlantısını açar ve foreign key desteğini etkinleştirir."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    """Uygulama için gerekli tabloları oluşturur."""
    with conn:
        conn.executescript(SCHEMA)
