"""Core domain models for tracking products and price observations."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Product:
    id: Optional[int]
    name: str
    url: str
    target_price: Optional[float] = None
    created_at: Optional[datetime] = None


@dataclass(frozen=True)
class PriceSnapshot:
    id: Optional[int]
    product_id: int
    price: float
    currency: str
    in_stock: bool
    recorded_at: datetime


@dataclass(frozen=True)
class AlertRule:
    id: Optional[int]
    product_id: int
    threshold_price: float
    notify_on_drop_only: bool = True
