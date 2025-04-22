# Web Site Bilgisi Toplama
# 🔎 Harici Link ve Yorum Ayıklayıcı (HTML Parser)

Bu Python betiği, bir HTML dosyasını analiz ederek içerisindeki **harici bağlantıları** ve **yorum satırlarını** tespit eder. Bu verileri farklı dosyalara kaydederek özellikle:

```bash
- Web güvenlik analizi
- Kaynak dosya taramaları
- HTML temizlik işlemleri
- SEO analizleri
```

gibi durumlar için oldukça kullanışlı bir araç sağlar.

---

## 🧩 Ne İşe Yarar?

```bash
Verilen bir `HTML` dosyasından:
- `<link>`, `<script>`, `<meta>` gibi **harici kaynak etiketlerini** tespit eder.
- HTML içerisindeki **yorumları (`<!-- ... -->`)** çıkartır.
- Inline yazılmış **JavaScript** ve **CSS yorumlarını** ayıklar.
- Tüm bu verileri ayrı dosyalara kaydeder.
```

---

🚀 Kullanım

```bash
python harici_link_toplayıcı.py
```

---

📁 Üretilen Dosyalar

Dosya Adı	İçerik

```bash
-external_links.txt	harici link Url'leri
-external_tags.txt	Harici <link>, <script>, <meta> etiketleri
-comments.txt	HTML yorumları (<!-- ... -->)
-javascript_comments.txt	JavaScript yorum satırları (//, /* */)
-css_comments.txt	CSS yorumları (/* ... */)
```

---

### 1. Python'u Kur

```bash
Python 3.7+ sürümüne sahip olduğunuzdan emin olun.  
[Python İndir](https://www.python.org/downloads/)
```

### 2. Gerekli Paketleri Yükle

```bash
pip install beautifulsoup4

