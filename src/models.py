"""Ürün ve fiyat geçmişini tutan temel veri modelleri."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Product:
    """Takip edilen ürünü temsil eder."""
    id: Optional[int]
    name: str
    url: str
    target_price: Optional[float] = None
    created_at: Optional[datetime] = None


@dataclass(frozen=True)
class PriceSnapshot:
    """Belirli bir andaki fiyat ve stok bilgisini tutar."""
    id: Optional[int]
    product_id: int
    price: float
    currency: str
    in_stock: bool
    recorded_at: datetime


@dataclass(frozen=True)
class AlertRule:
    """Ürün için belirlenen bildirim/alarm kuralı."""
    id: Optional[int]
    product_id: int
    threshold_price: float
    notify_on_drop_only: bool = True
