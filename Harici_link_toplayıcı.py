from bs4 import BeautifulSoup, Comment

def harici_linkleri_kaydet(html_dosya_adi, cikti_dosya_adi, etiketler_dosya_adi):
    """
    Verilen HTML dosyasındaki harici linkleri (link, script, meta) bulur ve belirtilen dosyaya kaydeder.
    Ayrıca HTML, JavaScript ve CSS yorumlarını ayrı dosyalara kaydeder.

    Args:
        html_dosya_adi (str): Okunacak HTML dosyasının adı.
        cikti_dosya_adi (str): Harici linklerin kaydedileceği dosyanın adı.
        etiketler_dosya_adi (str): Harici etiketlerin kaydedileceği dosyanın adı.
    """
    try:
        with open(html_dosya_adi, 'r', encoding='utf-8') as dosya:
            html_icerik = dosya.read()
    except FileNotFoundError:
        print(f"Hata: '{html_dosya_adi}' dosyası bulunamadı.")
        return

    soup = BeautifulSoup(html_icerik, 'html.parser')

    harici_linkler = []
    harici_etiketler = []
    # <link> etiketlerindeki harici linkleri bul
    for link in soup.find_all('link', href=True):
        harici_etiketler.append(str(link))
        print(str(link))
        harici_linkler.append(link['href'])

    # <script> etiketlerindeki harici linkleri bul
    for script in soup.find_all('script', src=True):
        harici_etiketler.append(str(script))
        print(str(script))
        harici_linkler.append(script['src'])

    # <meta> etiketlerindeki harici linkleri bul (örneğin, open graph meta etiketleri)
    for meta in soup.find_all('meta', property=True, content=True):
        if 'http' in meta['content'] or 'https' in meta['content']:
            harici_etiketler.append(str(meta))
            print(str(meta))
            harici_linkler.append(meta['content'])

    # Harici linkleri dosyaya kaydet
    with open(cikti_dosya_adi, 'w', encoding='utf-8') as cikti_dosya:
        for link in harici_linkler:
            cikti_dosya.write(link + '\n')

    # Harici etiketleri dosyaya kaydet
    with open(etiketler_dosya_adi, 'w', encoding='utf-8') as etiket_dosya:
        for link in harici_etiketler:
            etiket_dosya.write(link + '\n')

    # HTML yorumlarını bul ve kaydet
    html_yorumlar = [comment.strip() for comment in soup.find_all(string=lambda text: isinstance(text, Comment))]
    with open('comments.txt', 'w', encoding='utf-8') as yorum_dosya:
        for yorum in html_yorumlar:
            yorum_dosya.write(yorum + '\n')

    # JavaScript yorumlarını bul ve kaydet
    js_yorumlar = []
    for script in soup.find_all('script'):
        if script.string:  # İçerik inline ise
            lines = script.string.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('//'):
                    js_yorumlar.append(line)
                elif '/*' in line and '*/' in line:
                    js_yorumlar.append(line)

    with open('javascript_comments.txt', 'w', encoding='utf-8') as js_dosya:
        for yorum in js_yorumlar:
            js_dosya.write(yorum + '\n')

    # CSS yorumlarını bul ve kaydet
    css_yorumlar = []
    for style in soup.find_all('style'):
        if style.string:  # İçerik inline ise
            lines = style.string.split('\n')
            for line in lines:
                line = line.strip()
                if '/*' in line and '*/' in line:
                    css_yorumlar.append(line)

    with open('css_comments.txt', 'w', encoding='utf-8') as css_dosya:
        for yorum in css_yorumlar:
            css_dosya.write(yorum + '\n')

    print(f"Harici linkler '{cikti_dosya_adi}' dosyasına kaydedildi.")
    print(f"Harici etiketler '{etiketler_dosya_adi}' dosyasına kaydedildi.")
    print("HTML yorumları 'comments.txt' dosyasına kaydedildi.")
    print("JavaScript yorumları 'javascript_comments.txt' dosyasına kaydedildi.")
    print("CSS yorumları 'css_comments.txt' dosyasına kaydedildi.")

# Kullanım örneği
harici_linkleri_kaydet('site.html', 'external_links.txt', 'external_tags.txt')
