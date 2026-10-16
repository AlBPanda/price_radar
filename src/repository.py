"""Ürünler ve fiyat geçmişi için veri erişim (repository) katmanı."""
import sqlite3
from datetime import datetime
from typing import List, Optional
from src.models import Product, PriceSnapshot


class ProductRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def add_product(self, name: str, url: str, target_price: Optional[float] = None) -> Product:
        """Yeni bir takip edilecek ürün ekler."""
        created_at = datetime.now()
        created_at_str = created_at.isoformat()
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, url, target_price, created_at) VALUES (?, ?, ?, ?)",
            (name, url, target_price, created_at_str)
        )
        self.conn.commit()
        return Product(
            id=cursor.lastrowid,
            name=name,
            url=url,
            target_price=target_price,
            created_at=created_at
        )

    def get_product(self, product_id: int) -> Optional[Product]:
        """ID'ye göre ürün arar."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, name, url, target_price, created_at FROM products WHERE id = ?",
            (product_id,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        created_at = datetime.fromisoformat(row[4]) if row[4] else None
        return Product(id=row[0], name=row[1], url=row[2], target_price=row[3], created_at=created_at)

    def list_products(self) -> List[Product]:
        """Kayıtlı tüm ürünleri döner."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, url, target_price, created_at FROM products ORDER BY id DESC")
        products = []
        for row in cursor.fetchall():
            created_at = datetime.fromisoformat(row[4]) if row[4] else None
            products.append(Product(id=row[0], name=row[1], url=row[2], target_price=row[3], created_at=created_at))
        return products

    def add_price_snapshot(self, product_id: int, price: float, currency: str, in_stock: bool) -> PriceSnapshot:
        """Bir ürün için anlık fiyat kaydı ekler."""
        recorded_at = datetime.now()
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO price_snapshots (product_id, price, currency, in_stock, recorded_at) VALUES (?, ?, ?, ?, ?)",
            (product_id, price, currency, 1 if in_stock else 0, recorded_at.isoformat())
        )
        self.conn.commit()
        return PriceSnapshot(
            id=cursor.lastrowid,
            product_id=product_id,
            price=price,
            currency=currency,
            in_stock=in_stock,
            recorded_at=recorded_at
        )

    def get_price_history(self, product_id: int, limit: int = 30) -> List[PriceSnapshot]:
        """Bir ürünün geçmiş fiyat kayıtlarını tarihe göre sıralı getirir."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, product_id, price, currency, in_stock, recorded_at "
            "FROM price_snapshots WHERE product_id = ? ORDER BY recorded_at DESC LIMIT ?",
            (product_id, limit)
        )
        history = []
        for row in cursor.fetchall():
            rec_at = datetime.fromisoformat(row[5]) if row[5] else datetime.now()
            history.append(PriceSnapshot(
                id=row[0],
                product_id=row[1],
                price=row[2],
                currency=row[3],
                in_stock=bool(row[4]),
                recorded_at=rec_at
            ))
        return history
