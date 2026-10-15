# price-radar

Ürün fiyatlarını takip eden, fiyat geçmişini SQLite veritabanında saklayan ve fiyat düştüğünde bildirim gönderen hafif, harici bağımlılıksız Python aracı.

## Özellikler (Planlanan & Geliştirilmekte Olan)
- Sıfır harici bağımlılık (saf Python standart kütüphanesi: `urllib`, `sqlite3`, `unittest`).
- Fiyat geçmişini yerel SQLite veritabanında saklama.
- Takip edilen ürünleri eklemek, listelemek ve kontrol etmek için sade CLI arayüzü.
- Modüler bildirim yapısı (terminal uyarıları, loglar, webhook bildirimleri).
- Farklı e-ticaret siteleri için metin ve HTML fiyat ayrıştırıcıları.

## Hızlı Başlangıç
```bash
python -m unittest discover tests
python -m src.cli --help
```
