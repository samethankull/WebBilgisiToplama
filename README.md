# WebBilgisiToplama
# 🔍 Harici Link ve Yorum Ayıklayıcı (HTML Parser)

Bu Python betiği, verilen bir HTML dosyasındaki harici kaynakları (link, script, meta) ve yorumları (HTML, JavaScript, CSS) tespit ederek bunları ayrı dosyalara kaydeder. Özellikle güvenlik analizi, SEO taramaları ya da HTML optimizasyon çalışmaları için oldukça kullanışlıdır.

## 📂 Neler Yapıyor?

- Harici bağlantıları (`<link>`, `<script>`, `<meta>`) tespit eder ve ayrı bir dosyaya kaydeder.
- Harici etiketleri (`<link>`, `<script>`, `<meta>`) ayrı bir dosyada tutar.
- HTML yorumlarını `comments.txt` dosyasına yazar.
- JavaScript yorumlarını `javascript_comments.txt` dosyasına yazar.
- CSS yorumlarını `css_comments.txt` dosyasına yazar.

---

## 🛠 Kurulum Aşaması

### 1. Python Ortamını Kur

Python 3 yüklü değilse, [Python'un resmi sitesinden](https://www.python.org/downloads/) indirip kurabilirsin.

### 2. Sanal Ortam (Opsiyonel ama önerilir)

Proje için izole bir ortam oluşturmak istersen:

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

