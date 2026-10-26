#!/usr/bin/env python3
"""
denetim.py — dis-hekimligi-ceviri-tr için teslim öncesi otomatik denetim.

Kaynak ile Türkçe çeviriyi karşılaştırır ve ÖLÇÜLMÜŞ hata sınıflarını arar.
Her kontrol, yedi Lindhe bölümünün karşılaştırmasında gerçekten görülmüş bir
hataya dayanır (ölçüm kayıtları telifli metin içerdiği için pakette yok). Kontrol ne bulursa bulsun, KARAR
insanındır: HATA = kural ihlali neredeyse kesin; İNCELE = bak, yanlış alarm olabilir.

Kullanım:
    python3 denetim.py --tr ceviri.md --en kaynak.txt [--out rapor.md]

Yakalamadığı şey (baştan bilinmeli): İLK KEZ karşılaşılan bir terimin yanlış
karşılığı. Ölçülmüş 28 terim kaybının 27'si bu türdendi. Betik tekrarları ve
disiplin hatalarını yakalar; terim bilgisinin yerini tutmaz.
"""
import argparse, collections, csv, functools, os, re

# ───────────────────────────── yardımcılar ─────────────────────────────

def govde(tr):
    """Çeviri dosyasından yalnız çeviri gövdesini al: ÇEVİRİ NOTLARI ve TERİM ÇİFTLERİ
    hariç (bunlar kaynağı alıntılar, İngilizce terim içerir). '## ÇEVİRİ' başlığı
    yoksa (eski biçim: '## s. 256' …) baştan başlar."""
    son = re.search(r'^## (ÇEVİRİ NOTLARI|TERİM ÇİFTLERİ)', tr, re.M)
    tr = tr[:son.start()] if son else tr
    bas = re.search(r'^## ÇEVİRİ\s*$', tr, re.M)
    return tr[bas.end():] if bas else tr

def baglam(metin, bas, son, gen=45):
    a = max(0, bas - gen); b = min(len(metin), son + gen)
    return ('…' + metin[a:b].replace('\n', ' ') + '…').strip()

Bulgu = collections.namedtuple('Bulgu', 'sinif siddet mesaj baglam')

def normallestir_en(en):
    """PDF çıkarımının bozduğu İngilizce kaynağı düzelt: yumuşak tire (U+00AD) ve
    satır sonu bölmeleri birleşir, U+2010–2012 tireler '-' olur, boşluk tekleşir.
    Doğrulamada B13'te 'delayed‐type' (U+2010) ve 'hyper\xad\n' yüzünden tetikleyici kaçmıştı."""
    en = re.sub(r'\xad\s*', '', en)
    en = re.sub(r'[\u2010\u2011\u2012]', '-', en)
    en = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', en)
    en = re.sub(r'\s+', ' ', en)
    return en

def kucuk(s):
    """Türkçeye uygun küçük harf: İ → i, I → ı (str.lower() 'İ'yi 'i̇' yapar, eşleşme kaçar)."""
    return s.replace('İ', 'i').replace('I', 'ı').lower()

def ara(desen, metin, flags=0):
    return list(re.finditer(desen, metin, flags))

# ───────────────────── 1. üslup imzaları (§7.1) ─────────────────────

KI_IZINLI = re.compile(r'(öyle|ne var|ne yazık|madem|halbu|oysa|sanki|belki)\s*ki\b', re.I)

def imzalar(tr):
    b = []
    for m in ara(r'\btarafından\b', tr):
        b.append(Bulgu('imza', 'HATA', '`tarafından` ile kurulmuş (§7.1)', baglam(tr, m.start(), m.end())))
    for m in ara(r'\bsahip(tir|tirler|ti|tiler|tır)?\b|\bsahip ol\w*|\bsahibi ol\w*', tr):
        b.append(Bulgu('imza', 'HATA', '`sahip olmak` (§7.1)', baglam(tr, m.start(), m.end())))
    for m in ara(r'\b(oluşturmaktadır|bulunmaktadır|yer almaktadır|teşkil\w*|gerçekleştir\w*)\b', tr):
        b.append(Bulgu('imza', 'İNCELE', 'olası boş yüklem (§7.1)', baglam(tr, m.start(), m.end())))
    for m in ara(r'\bki\b', tr):
        onc = tr[max(0, m.start()-12):m.end()]
        if not KI_IZINLI.search(onc):
            b.append(Bulgu('imza', 'İNCELE', '`ki` ile kurulmuş ilgi cümlesi olabilir (§7.1)', baglam(tr, m.start(), m.end())))
    soz = len(tr.split()) or 1
    # v10 — motamot kalıplar (§7.2b; B20 öbek işaretlemesi, uzman 28.09)
    isaret = ara(r'\bişaret (eder|ederler|etmiştir|etmişlerdir|etti|ettiler|etmektedir|ediyor|edebilir|edecektir)\b', tr)
    if len(isaret) >= 3 and len(isaret) * 1000 / soz > 1:
        b.append(Bulgu('imza', 'İNCELE', f'"…e işaret eder" {len(isaret)} kez (§7.2b): indicate → gösterir; suggest → düşündürür (kiplik korunur); point to → gösterir. Basım B20\'de ≈0,7/1000', baglam(tr, isaret[0].start(), isaret[0].end())))
    for m in ara(r'\b(kısa bir )?tartışması (verilmiştir|verilmektedir|verilecektir|sunulmuştur)\b', tr):
        b.append(Bulgu('imza', 'İNCELE', '"… tartışması verilmiştir" motamot (§7.2b): *a brief discussion … is given* → "kısaca değinilmektedir"', baglam(tr, m.start(), m.end())))
    # v11 — paragrafın kip çerçevesi ve akıcılık kalıpları (§7.0, §7.2b; uzman tercih anketi 29.09)
    for m in ara(r'\b\w+m[ıiuü]şt[ıiuü](lar|ler)?\b', tr):
        b.append(Bulgu('imza', 'İNCELE', '-mıştı (hikâye birleşik kipi): akademik düzyazıda kip çerçevesini bozar → -mıştır (§7.0)', baglam(tr, m.start(), m.end())))
    for m in ara(r'\b(gözlen|görül|izlen|saptan|belirlen)ebilmiş\w*', tr):
        b.append(Bulgu('imza', 'İNCELE', '"could be observed" bulgu aktarıyorsa → "gözlenmiştir" (§5/3, §7.2b)', baglam(tr, m.start(), m.end())))
    for m in ara(r'\bBölüm \d+\S*\s+(?:\S+\s+){0,4}?(ele alınır|tartışılır|anlatılır|incelenir|değinilir)\b', tr):
        b.append(Bulgu('imza', 'İNCELE', 'metin içi gönderme geniş zamanla: başka bölüm → "ele alınmıştır", bu bölüm → "değinilmektedir" (§7.0)', baglam(tr, m.start(), m.end())))
    # 26.10 — uzman kararı: metin içi göndermede gelecek zaman yazılmaz (§7.0)
    for m in ara(r'\b(değinilecektir|durulacaktır|anlatılacaktır|ele alınacaktır|tartışılacaktır|incelenecektir)\b', tr):
        b.append(Bulgu('imza', 'İNCELE', 'metin içi gönderme gelecek zamanla: bu bölüm → "değinilmektedir", başka bölüm → "ele alınmıştır" (§7.0; uzman kararı 26.10)', baglam(tr, m.start(), m.end())))
    for m in ara(r'\b(en büyük önemi taşı\w*|kazara hasar|ileri hassasiyet\w*)', tr):
        b.append(Bulgu('imza', 'İNCELE', 'sıfat kalkı (§7.2b): utmost → "son derece önemli"; advanced precision → "hassasiyeti artmış"; accidental → "istenmeden"', baglam(tr, m.start(), m.end())))
    # 1.0 — Panel-1 dış değerlendirici bulguları (29.09): 16 çeviride / 41 bin sözcükte sınandı
    for m in ara(r'\bdüşük kalite\w*', tr):
        b.append(Bulgu('imza', 'İNCELE', 'sıfat kalkı: low-quality / poor oral hygiene → "zayıf / yetersiz oral hijyen" (taban); "düşük kaliteli" Türkçede klinik ifade değil', baglam(tr, m.start(), m.end())))
    for m in ara(r'\bilk (on|beş|yirmi|elli|yüz|\d+) (makale|çalışma|dergi|yazar|kurum|ülke|yayın)\w*', tr):
        if re.search(r'(atıf alan|sıra\w*|en çok \w+)\s*$', tr[max(0, m.start()-30):m.start()]):
            continue
        b.append(Bulgu('imza', 'İNCELE', 'top N → "en çok atıf alan ilk on" / "en üst sıradaki on"; yalın "ilk on" kronolojik okunur', baglam(tr, m.start(), m.end())))
    for m in ara(r'[;:]\s+(?!(?:bu|şu|o|bunlar|ayrıca|ancak|yine|böylece|hem)\b)(\w+) (da|de)\b', tr):
        b.append(Bulgu('imza', 'İNCELE', 'noktalı virgülden sonra "X da/de": İngilizcede also/too yoksa başka bir etken varmış gibi okunur (ör. "sigara da artırabilir")', baglam(tr, m.start(), m.end())))
    n = len(ara(r'\w+(maktadır|mektedir|maktadırlar|mektedirler)\b', tr))
    yog = n * 1000 / soz
    if yog > 8:
        b.append(Bulgu('imza', 'İNCELE', f'`-maktadır` yoğunluğu {yog:.1f}/1000 sözcük (eşik 8; basım ≈25–30)', ''))
    return b, {'sözcük': soz, '-maktadır': n, '-maktadır/1000': round(yog, 1)}

# ───────────────────── 2. sayı yazımı (§5/5) ─────────────────────

YIL_HARF = re.compile(r'(19|20)\d\d[a-z]$')

def sayilar(tr):
    b = []
    for m in ara(r'(?<![\d.,§])\d+\.\d{1,2}(?![\d])', tr):   # § numarası (§5.2) geri bakışla dışarıda
        b.append(Bulgu('sayı', 'HATA', 'ondalık ayırıcı nokta — virgül olmalı (§5/5)', baglam(tr, m.start(), m.end())))
    for m in ara(r'\d\s*%', tr):
        b.append(Bulgu('sayı', 'HATA', '`%` sayıdan sonra — önde olmalı (§5/5)', baglam(tr, m.start(), m.end())))
    for m in ara(r"(?<![\w'])(\d+)(de|da|te|ta|den|dan|ten|tan|e|a|i|ı|u|ü|in|ın|un|ün|ini|ını|unu|ünü|inde|ında|unda|ünde)\b", tr):
        if YIL_HARF.match(m.group(0)):  # 1993a, 2010b — atıf
            continue
        onceki = tr[max(0, m.start()-1):m.start()]
        if onceki in ('-', '(', '–'):     # Şekil 8-1a, (2i), B-1a — panel/hücre etiketi
            continue
        b.append(Bulgu('sayı', 'HATA', 'sayıya gelen ek kesmesiz (§5/5)', baglam(tr, m.start(), m.end())))
    for m in ara(r"[\d%]\s+'[a-zçğıöşü]", tr):
        b.append(Bulgu('sayı', 'HATA', 'kesme işaretinden önce boşluk', baglam(tr, m.start(), m.end())))
    return b

# ───────────────────── 3. özel adlar (§5/7) ─────────────────────

# (kaynakta arananan, çeviride olması gereken, çeviride olmaması gereken, şiddet, not)
OZEL_AD = [
    (r'John Wiley\s*&\s*Sons', r'John Wiley & Sons', r'Wiley ve Sons', 'HATA', 'yayıncı adı; `&` çevrilmez (B7, B8)'),
    (r'WHO Global Oral Data Bank', r'WHO Global Oral Data Bank', r'Küresel Ağız|Global Ağız', 'HATA', 'veri bankası adı çevrilmez (B7 — bu skill)'),
    (r'Human Oral Microbiome Database', r'Human Oral Microbiome Database', r'İnsan Oral Mikrobiyom Veritaban', 'HATA', 'veritabanı adı çevrilmez (B8)'),
    (r'Human Microbiome Project', r'Human Microbiome Project', r'İnsan Mikrobiyom Proje', 'HATA', 'proje adı çevrilmez (B8)'),
    (r'Human Oral Microbiome"? project|"Human Oral Microbiome"', r'Human Oral Microbiome', r'İnsan Oral Mikrobiyom', 'HATA', 'proje adı çevrilmez (B8)'),
    (r'Community Periodontal Index', None, r'Community Periodontal İndeks', 'HATA', 'İngilizce özel ad içinde Türkçe İ (B7)'),
    (r'\bFDI\b', r'\bFDI\b', r'\(FDA\)|\bFDA\b', 'HATA', 'FDI ≠ FDA (B29)'),
    (r'American Academy of Periodontology', r'American Academy of Periodontology', None, 'İNCELE', 'dernek adı — çevrilsin mi, karar bekliyor (B8)'),
]
KURUM_SONEK = r'(Project|Database|Bank|Society|Association|Academy|Federation|Organization|Foundation|Institute|Workshop)'

def ozel_adlar(en, tr):
    b = []
    for kaynak, gerek, yasak, sid, notu in OZEL_AD:
        if not re.search(kaynak, en):
            continue
        if yasak:
            for m in ara(yasak, tr):
                b.append(Bulgu('özel ad', sid, f'çevrilmiş/bozulmuş: {notu}', baglam(tr, m.start(), m.end())))
        if gerek and not re.search(gerek, tr):
            b.append(Bulgu('özel ad', 'İNCELE', f'kaynaktaki özel ad çeviride aynen yok (atlanmış ya da çevrilmiş olabilir): {notu}', ''))
    for m in ara(r'Elsevier(in|ın|den|dan|e)\b', tr):
        b.append(Bulgu('özel ad', 'HATA', 'özel ada gelen ek kesmesiz', baglam(tr, m.start(), m.end())))
    # Sezgisel: kaynakta kurum sonekli çok sözcüklü adlar
    gorulen = set()
    for m in ara(r'((?:[A-Z][a-z]+\s){1,5}' + KURUM_SONEK + r')', en):
        ad = re.sub(r'^The\s+', '', m.group(1).strip())
        if ad in gorulen or len(ad.split()) < 2 or re.search(r'\bThe\b', ad):
            continue
        gorulen.add(ad)
        if ad not in tr and not any(re.search(k, ad) for k, *_ in OZEL_AD):
            b.append(Bulgu('özel ad', 'İNCELE', f'kaynaktaki kurum/proje adı çeviride aynen yok: "{ad}"', ''))
    return b

# ───────────────────── 4. kısaltmalar (§6.2, B0d) ─────────────────────

TR_KALAN = [  # (kaynak kısaltma, Türkçe kısaltma) — §6.2 istisnası
    ('GCF', 'DOS'), ('CBCT', 'KIBT'), ('SPT', 'DPT'),
]
TURKCELESMIS_YASAK = r'\((KAS|CD|AS|AK|MSB|SK|FT|DM|MİK|MBK|YUP)\)|\b(KAS|MSB|MİK|MBK|YUP)\b'
ULUSLARARASI = ['CAL', 'PPD', 'PAL', 'CEJ', 'BOP', 'MIC', 'MBC', 'CSP', 'FISH', 'ESI', 'CPITN', 'CPI']

def kisaltmalar(en, tr):
    b = []
    for kay, trk in TR_KALAN:
        if re.search(r'\b' + kay + r'\b', en):
            trk_var = re.search(r'\b' + trk + r'\b', tr)
            for m in ara(r'\b' + kay + r'\b', tr):
                # İzinli: özgün terimin ilk geçiş parantezi içinde, Türkçe kısaltma da metinde varsa
                # örn. "diş eti oluğu sıvısı (DOS; gingival crevicular fluid, GCF)"
                onc = tr[max(0, m.start()-45):m.start()]
                if trk_var and re.search(r'[a-z]{4,}(,|;)?\s*$', onc) and '(' in onc:
                    continue
                b.append(Bulgu('kısaltma', 'HATA', f'{kay} yazılmış — §6.2 istisnası: {trk} olmalı', baglam(tr, m.start(), m.end())))
            if not trk_var:
                b.append(Bulgu('kısaltma', 'HATA', f'kaynakta {kay} var, çeviride {trk} hiç yok (§6.2 istisnası)', ''))
    for m in ara(TURKCELESMIS_YASAK, tr):
        b.append(Bulgu('kısaltma', 'HATA', 'Türkçeleştirilmiş kısaltma — uzman kararı B0d: uluslararası biçim korunur', baglam(tr, m.start(), m.end())))
    for k in ULUSLARARASI:
        if re.search(r'\b' + k + r'\b', en) and not re.search(r'\b' + k + r'\b', tr):
            b.append(Bulgu('kısaltma', 'İNCELE', f'kaynakta {k} var, çeviride yok', ''))
    return b

# ───────────────────── 5. yanlış-dost bankası (§6.4, karar listesi D) ─────────────────────
# (kimlik, kaynak tetikleyici, çeviride YANLIŞ biçim, çeviride GEREKEN biçim, şiddet, kaynak)
Kural = collections.namedtuple('Kural', 'kim tetik yanlis gerek siddet kaynak')
YANLIS_DOST = [
    ('measures', r'\bmeasures\b', r'\bölçüm(ler|leri|lerin)\b', None, 'İNCELE', 'B39, B7'),
    ('succession', r'\bsuccession\b', r'\bmiras\b', r'süksesyon', 'HATA', 'B8: miras anlam hatası'),
    ('succession zincir', r'\bsuccession\b', r'mikrobiyal zincir', None, 'TERCİH', 'uzman 24.09: süksesyon ("zincir" tam ifade etmiyor)'),
    ('emergent', r'\bemergent\b', r'\bbeklenmeyen özellik', r'beliren', 'HATA', 'B8'),
    ('sequencing', r'\bsequencing\b', r'\bsıralan\w*|\bsıralama\b', r'dizile', 'HATA', 'B8'),
    ('indifference', r'\bindifference\b', None, r'ilgisizli', 'İNCELE', 'B8'),
    ('communism', r'commensal communism', r'komensal yaşam', r'komünizm', 'HATA', 'B8'),
    ('detachment', r'\bdetachment\b', r'\bçözülme', r'ayrıl', 'HATA', 'B8'),
    ('scavenge', r'\bscavenge\b', r'arayarak bul', None, 'HATA', 'B8'),
    ('certain', r'\bcertain Gram-negative', r'zorunlu gram', None, 'HATA', 'B8'),
    ('spp', r'\bspp\.', r'\bsuşu\b', None, 'HATA', 'B8'),
    ('familial aggregation', r'familial aggregation', r'ailesel geçiş', r'ailesel kümelenme', 'HATA', 'B7'),
    ('natural history', r'natural history', r'doğasına uygun', r'doğal seyir', 'HATA', 'B7'),
    ('median', r'\bmedian\b', r'ortalama birey', r'ortanca|medyan', 'HATA', 'B7'),
    ('percentile', r'\bpercentile\b', r'yüzdelik', r'persentil', 'TERCİH', 'B7'),
    ('skewed', r'\bskewed\b', r'eğri dağılım', r'çarpık', 'HATA', 'B7'),
    ('screening', r'\bscreening method', r'görüntüleme yöntem', r'tarama', 'HATA', 'B7'),
    ('age-adjusted', r'age-adjusted', r'yaşa-bağlı|yaşa bağlı yaklaşım', r'düzeltilmiş', 'HATA', 'B7'),
    ('companion paper', r'companion paper', r'ortak (bir )?çalışma', None, 'HATA', 'B7'),
    ('conditions (sınıflama)', r'deformities and conditions', r'deformiteler ve koşullar', r'durumlar', 'HATA', 'B7'),
    ('conventional', r'\bconventional\b', r'\bsıradan\b', None, 'HATA', 'v5'),
    ('blunt', r'\bblunt\b', r'\bkör (bir |uçlu )?alet', None, 'TERCİH', 'v5'),
    ('predictive value', r'predictive value', r'kestirim değer', r'prediktif', 'TERCİH', 'v6'),
    ('dentition', r'\bdentition\b', r'dişlenme', r'dentisyon', 'HATA', 'v5'),
    ('host defense', r'host defen[cs]e|defen[cs]e mechanism', r'\bdefans\b', None, 'TERCİH', 'v4'),
    ('permeability', r'\bpermeability\b', r'permeabilite', r'geçirgenlik', 'TERCİH', 'v4'),
    ('adaptive', r'\badaptive immun', r'\bedinsel\b', r'kazanılmış', 'TERCİH', 'v4'),
    ('cell-mediated', r'cell-mediated', r'hücre aracılı', r'hücresel', 'TERCİH', 'v4'),
    ('delayed-type', r'delayed[- ]type', r'gecikmiş tip', r'geç tip', 'TERCİH', 'v4'),
    ('scalpel', r'\bscalpel\b', r'\bskalpel', r'bistüri', 'TERCİH', 'v5'),
    ('releasing incision', r'releasing incision', r'gevşetici', r'rahatlatıcı', 'TERCİH', 'v5'),
    ('angular', r'\bangular\b', r'\bangüler\b', r'açısal', 'TERCİH', 'v6 ★'),
    ('pseudo-pocket', r'pseudo-?pocket', r'psödo', r'yalancı cep', 'TERCİH', 'v6 ★'),
    ('root coverage', r'root coverage', r'kök yüzeyi kapatma', r'kök yüzeyinin örtülmesi', 'TERCİH', 'B46 ★'),
    ('crown', r'\bcrowns?\b', r'\bkron(u|a|da|dan|un|lar|ları|ların)?\b', r'\bkuron', 'TERCİH', 'B46 ★'),
    ('lining mucosa', r'lining mucosa', r'astar mukoza', r'örtücü mukoza', 'TERCİH', 'B46 ★'),
    ('partial-thickness flap', r'partial-thickness|split-thickness|split flap', r'kısmi kalınlık', r'yarım-kalınlık|yarım kalınlık', 'TERCİH', 'B46 ★'),
    ('pedicle graft', r'\bpedicle', r'(?<!saplı \()pediküllü', r'\bsaplı', 'İNCELE', 'B46 ★ — saplı (pediküllü) greft'),
    ('recall', r'\brecall\b', r'geri çağır', None, 'TERCİH', 'B39'),
    ('recontouring', r'\brecontour', r'yeniden şekillendir', r'yeniden konturla', 'TERCİH', 'v5'),
    ('semilunar', r'\bsemilunar\b', r'yarım ay biçim', r'semilüner', 'TERCİH', 'v5'),
    ('maxillary', r'\bmaxillary\b', r'üst çene diş', r'maksiller', 'İNCELE', 'v5'),
    ('history taking', r'history taking|taking (a|the) history', r'öykü al', r'anamnez', 'İNCELE', 'v6 ★'),
    ('consistently correlate', r'consistently correlate', r'uyumlu korelasyon', None, 'HATA', 'B7'),
    ('exclusively', r'\bexclusively\b', r'kapsamlı olarak', None, 'İNCELE', 'B7'),
    ('physiological', r'physiological condition', r'fiziksel bir durum', r'fizyolojik', 'HATA', 'B7'),
    ('of that time', r'of that time', r'^Zamanında|\. Zamanında', None, 'HATA', 'B7'),
    ('among the first', r'\b(is|are) among the (first|earliest|most)', r'arasında \w+(ler|lar)? (da|de) (vardır|bulunur|yer alır)', None, 'İNCELE', 'uzman öbek işaretlemesi B12: "X, ilk Y arasındadır" → "ilk Y arasında X de vardır" vurguyu kaydırıyor; X özne kalmalı'),
    # ── basılı kitabın 9 sayfalık gövde taramasından (24.09 gece) — ölçülmüş kitap hataları ──
    ('innate → kalıtsal', r'\binnate\b', r'\bkalıtsal\b.{0,30}(bağışık|immün)', r'doğal|doğuştan', 'HATA', 'basımda ölçüldü: innate immunity → "kalıtsal immünite"'),
    ('deregulation', r'\bderegulat', r'ortadan kaldır', r'düzensiz|bozul', 'HATA', 'basımda ölçüldü: deregulation → "ortadan kaldırılması"'),
    ('cytolethal distending toxin', r'cytolethal distending', r'sitotelyal|yayılma toksin', r'sitoletal', 'HATA', 'basımda ölçüldü'),
    ('inherent', r'\binherent\b', r'\bbariz\b', None, 'İNCELE', 'basımda ölçüldü: inherent → "bariz"'),
    ('formal genetic studies', r'formal genetic', r'değerli (pek çok )?genetik', None, 'HATA', 'basımda ölçüldü'),
    ('concussion', r'\bconcussions?\b', None, r'konküzyon|sarsıl', 'İNCELE', 'basımda ölçüldü: concussion → genel "travma"'),
    ('autoimmunization', r'autoimmuni[sz]ation', r'doğuştan bir hastalığa bağışık', r'otoimmün', 'HATA', 'basımda ölçüldü: yanlış tanım eklenmiş'),
    ('significantly (istatistik)', r'significantly (greater|higher|lower|more|less|elevated|reduced|increased|decreased|different|better|worse)', r'önemli ölçüde', r'anlamlı', 'TERCİH', 'basımda ölçüldü; Cilt 2: "önemli" 19 el, "anlamlı" 16 el — eş anlamlı; istatistikte anlamlı tercih'),
    # ── açılış sayfaları taraması (25.09): 25 bölüm, 295 kitap bulgusu ──
    ('physiology', r'\bphysiolog', r'psikoloji', r'fizyoloji', 'HATA', 'basımda ölçüldü: human physiology → "insan psikolojisi"'),
    ('bacterial challenge', r'(bacterial|microbial) challenge', r'bakteriyel savaş|mikrobiyal savaş', None, 'HATA', 'basımda ölçüldü: "bakteriyel savaş"; §6.3: bakteriyel uyarı'),
    ('modifying factors', r'modifying factors?', r'modifiye edilebilen', r'modifiye edici|düzenleyici', 'HATA', 'basımda ölçüldü: "modifiye edilebilen" anlamı ters çevirir'),
    ('ash weight', r'ash weight', r'kuru ağırlık', r'kül ağırlı', 'HATA', 'basımda ölçüldü'),
    ('cell-mediated uyarılı', r'cell-mediated', r'hücresel uyarılı', None, 'HATA', 'basımda ölçüldü'),
    ('blade (el aleti)', r'\bblades?\b', r'\bağ(zın|zı|ız|zını)\s+(alt|üst|kesici|koronal|kenar)|mini ağız|\bağız\s+koronal|(sap|boyun),?\s+ağız', r'bıça[kğ]|keskin yüzey', 'İNCELE', 'B38 uzman öbek işaretlemesi: blade → "ağız" doğal değil; kitap: keskin yüzey / bıçak'),
    # ── uzman kararları 24.09: kitap biçimi kazanır (D1–D6), C1/C2/B ──
    ('diagnosis', r'\bdiagnos(is|es|ed|e|ing)\b', r'(?<!ayırıcı )\btanı(sı|sını|sına|sında|sından|yı|ya|nın|nı|da|dan|lar|ları|ların|dır)?\b', r'teşhis|ayırıcı tanı', 'TERCİH', 'uzman D1 — kitap: teşhis'),
    ('attachment level', r'attachment levels?', r'ataşman düzey', r'ataşman seviye', 'TERCİH', 'uzman D2 — kitap: seviye'),
    ('junctional epithelium', r'junctional epitheli', r'bağlantı epitel', r'birleşim epitel', 'TERCİH', 'uzman D3 — kitap'),
    ('case definition', r'case definitions?', r'olgu tanım', r'vaka tanım', 'TERCİH', 'uzman D4 — kitap'),
    ('immune response', r'immune responses?', r'imm[üu]n yanıt|bağışıklık yanıt', r'imm[üu]n cevap|imm[üu]n cevab', 'TERCİH', 'uzman D5 (24.09): immün cevap — kitap gövdesinde 9 elden 8'),
    ('descriptive epidemiology', r'descriptive (epidemiolog|stud)', r'betimleyici', r'tanımlayıcı', 'TERCİH', 'uzman D6 — kitap'),
    ('odds ratio', r'odds ratio', r'olasılık oran', r'odds oran', 'HATA', 'uzman C1 — kitap anlam hatası'),
    ('hazard ratio', r'hazard ratio', r'tehlike oran', r'hazard oran', 'TERCİH', 'uzman C2'),
    ('antigen-presenting', r'antigen[- ]presenting', r'antijen sunan', r'antijen sunucu', 'TERCİH', 'uzman B — kitap'),
    ('sinus floor', r'sinus floor', r'sinüs duvar', r'sinüs taban', 'HATA', 'kitap içi tutarsızlık + anlam'),
    ('response', r'\b(host|inflammatory|immune|immunologic|vascular|cellular|clinical) responses?\b', r'\b(konak|enflamatuar|inflamatuar|imm[üu]n|immünolojik|vasküler|hücresel|klinik) yanıt\w*', None, 'TERCİH', 'uzman D5 ailesi (24.09): response → cevap'),
    # ── Cilt 2 gövde taraması (26.09): 129 sayfa, 1.410 kitap bulgusu — "olmayacak" kullanımlar ──
    ('measures (önlem)', r'\b(preventive|therapeutic|cause-related|initial|control|hygiene|interceptive|protective) measures\b', r'\b(önleyici|terapötik|terapotik|tedavi edici|nedene[- ]bağlı|ilk|kontrol|hijyen|koruyucu) ölçüm', r'önlem|uygulama|işlem', 'HATA', 'basımda ölçüldü: measures → "ölçümler" (3 el); doğrusu önlem/uygulama'),
    ('survival rate', r'survival rates?', r'idame oran', r'sağkalım|hayatta kalma|başarı', 'HATA', 'basımda ölçüldü: survival → "idame"'),
    ('resolution', r'resolution of (the )?(inflammation|lesion|peri-implantitis|disease)|(complete|degree of) resolution', r'çözünürlü', r'gerile|iyileş|çözül|ortadan kalk|düzel', 'HATA', 'basımda ölçüldü: resolution → "çözünürlük"'),
    ('substantivity', r'\bsubstantiv', r'\(temel\)|temel ilaç|temel bileşik', r'substantif|sübstantif|tutun|bağlan', 'HATA', 'basımda ölçüldü: substantive → "temel"'),
    ('homeostasis', r'homeosta', r'\bhemosta', r'homeosta|denge', 'HATA', 'basımda ölçüldü: homeostasis → "hemostaz"'),
    ('criteria', r'\bcriteri(a|on)\b', r'eleştiri', r'ölçüt|kriter', 'HATA', 'basımda ölçüldü: criteria → "eleştiri"'),
    ('climax community', r'climax communit', r'giderek artan topluluk', r'klimaks|zirve', 'HATA', 'basımda ölçüldü'),
    ('root tears', r'root tears?', r'kök inci', r'yırtı|çatla', 'HATA', 'basımda ölçüldü: root tears → "kök incileri"'),
    ('risk marker', r'risk markers?', None, r'belirte|göstergesi|risk işaret|marker', 'İNCELE', 'basımda ölçüldü: risk marker → "risk faktörü"; marker ≠ factor'),
    ('not infrequently', r'not (in)?frequently|not uncommon(ly)?|not rare(ly)?', r'nadir', None, 'HATA', 'basımda ölçüldü (A): not infrequently → "nadiren de olsa" — anlam ters'),
    ('little evidence', r'\blittle (information|evidence|data|is known)|\bfew (studies|data)', r'\bçok (bilgi|kanıt|veri|çalışma)', None, 'HATA', 'basımda ölçüldü (A): little information → "çok bilgi" — anlam ters'),
    ('not to mention', r'not to mention', r'kastedilme', None, 'HATA', 'basımda ölçüldü (A): anlam ters'),
    ('the former', r'\bthe former\b', r'\bsonraki (durum|vaka)|\bikinci (durum|vaka)', None, 'İNCELE', 'basımda ölçüldü (A): the former → "sonraki durumda"'),
    ('the latter', r'\bthe latter\b', r'\bönceki (durum|vaka)|\bilk (durum|vaka)', None, 'İNCELE', 'former/latter karışması'),
]

YANLIS_DOST = [Kural(*k) for k in YANLIS_DOST]

SIDDET_SIRA = {'HATA': 0, 'İNCELE': 1, 'TERCİH': 2}

def yanlis_dost(en, tr):
    """Aynı metin parçası bir kez raporlanır: örtüşen eşleşmelerden en ağır şiddetli, eşitse listede önce gelen kalır
    (ör. "immün yanıt" hem 'immune response' hem 'response' kuralına; "önleyici ölçümler" hem 'measures' hem
    'measures (önlem)' kuralına uyar)."""
    b, adaylar, bulunan = [], [], set()
    etkin = [k for k in YANLIS_DOST if re.search(k.tetik, en, re.I)]
    for k in etkin:
        if k.yanlis:
            for m in ara(k.yanlis, tr, re.I):
                adaylar.append((m, k)); bulunan.add(k.kim)
    alinan = []
    sira = {k.kim: i for i, k in enumerate(YANLIS_DOST)}   # eşit şiddette listede önce gelen (daha özel) kural kalır
    for m, k in sorted(adaylar, key=lambda x: (SIDDET_SIRA[x[1].siddet], sira[x[1].kim], x[0].start())):
        if any(m.start() < son and bas < m.end() for bas, son in alinan):
            continue
        alinan.append(m.span())
        if k.siddet == 'TERCİH':   # eş anlamlı: hata değil, baskın/uzman biçimi önerilir
            b.append((m.start(), Bulgu('yanlış dost', k.siddet, f'{k.kim}: eş anlamlı biçim (hata değil); tercih edilen: "{k.gerek or "—"}" ({k.kaynak})', baglam(tr, m.start(), m.end()))))
        else:
            b.append((m.start(), Bulgu('yanlış dost', k.siddet, f'{k.kim}: bilinen yanlış karşılık ({k.kaynak})', baglam(tr, m.start(), m.end()))))
    b = [x for _, x in sorted(b, key=lambda y: y[0])]
    for k in etkin:
        if k.siddet == 'TERCİH' and k.kim in bulunan:
            continue
        if k.gerek and not re.search(k.gerek, tr, re.I):
            b.append(Bulgu('yanlış dost', 'İNCELE', f'{k.kim}: kaynakta var, beklenen karşılık ("{k.gerek}") çeviride yok ({k.kaynak})', ''))
    return b

# ───────────────────── 5b. olgu bilgisi eşlemesi (Cilt 2 taraması, 26.09) ─────────────────────
# Kitapta ölçülen "olmayacak" hatalar: ilaç adı değişmiş (minosiklin → doksisiklin, s.454), cinsiyet
# değişmiş (female → erkek, s.651), diş tipi değişmiş (implant/premolar/molar, s.327, 1147),
# anlamlılık olumsuzu düşmüş (P > 0,05 → "anlamlı fark görülmüştür", s.454), eşitsizlik yönü dönmüş
# (≤%25 → "%25'in üzerine", s.621).
ILACLAR = {'minocycline': 'minosiklin', 'doxycycline': 'doksisiklin', 'tetracycline': 'tetrasiklin', 'metronidazole': 'metronidazol',
           'amoxicillin': 'amoksisilin', 'chlorhexidine': r'klorheksidin|\bCHX|\bKHX', 'azithromycin': 'azitromisin', 'clindamycin': 'klindamisin',
           'ciprofloxacin': 'siprofloksasin', 'nystatin': 'nistatin', 'penicillin': 'penisilin', 'ibuprofen': 'ibuprofen'}
OLUMSUZ_ANLAMLI_EN = r'\b(no|not|non-?)\s*(statistically\s+)?significant|did not (differ|reach) significan|P\s*[>≥]\s*0[.,]05'
OLUMSUZ_ANLAMLI_TR = r'anlamlı\s+(bir\s+)?(fark|farklılık|değişiklik|ilişki|etki|azalma|artış|üstünlük)\w*\s+(\w+\s+){0,2}\w*m[ae](m[ıi]ş|d[ıi]|z|yan|d[ıi]ğ)|anlamlı\s+(bir\s+)?(fark|farklılık)\w*\s+(yok|değil|olma)|anlamlı olma|anlamsız|anlamlılığa ulaşma'

def olgu_bilgisi(en, tr):
    b = []
    for e, t in ILACLAR.items():
        if re.search(r'\b' + e, en, re.I) and not re.search(t, tr, re.I):
            b.append(Bulgu('olgu bilgisi', 'İNCELE', f'kaynakta {e} var, çeviride "{t}" yok — ilaç adı değişmiş olabilir (basımda ölçüldü)', ''))
    if re.search(r'\b(female|woman|women)\b', en, re.I) and not re.search(r'\b(male|man|men)\b', en, re.I) \
            and re.search(r'\berkek', tr, re.I) and not re.search(r'\bkadın', tr, re.I):
        b.append(Bulgu('olgu bilgisi', 'İNCELE', 'kaynakta kadın, çeviride erkek (basımda ölçüldü)', ''))
    if re.search(r'\b(male|man)\b', en, re.I) and not re.search(r'\b(female|woman|women)\b', en, re.I) \
            and re.search(r'\bkadın', tr, re.I) and not re.search(r'\berkek', tr, re.I):
        b.append(Bulgu('olgu bilgisi', 'İNCELE', 'kaynakta erkek, çeviride kadın', ''))
    npm_en, nm_en = len(re.findall(r'premolar', en, re.I)), len(re.findall(r'(?<!pre)molar', en, re.I))
    npm_tr, nm_tr = len(re.findall(r'premolar|küçük azı', tr, re.I)), len(re.findall(r'(?<!pre)molar|büyük azı', tr, re.I))
    if (npm_tr < npm_en and nm_tr > nm_en) or (npm_tr > npm_en and nm_tr < nm_en):   # biri azalıp öbürü artıyorsa: yer değiştirme
        b.append(Bulgu('olgu bilgisi', 'İNCELE', f'diş tipi sayısı tutmuyor: premolar {npm_en}→{npm_tr}, molar {nm_en}→{nm_tr} (basımda ölçüldü)', ''))
    ne, nt = len(re.findall(OLUMSUZ_ANLAMLI_EN, en, re.I)), len(re.findall(OLUMSUZ_ANLAMLI_TR, tr, re.I))
    if ne > nt:
        b.append(Bulgu('olgu bilgisi', 'İNCELE', f'kaynakta {ne} "anlamlı değil / P > 0,05" ifadesi, çeviride {nt} olumsuz anlamlılık — olumsuz düşmüş olabilir (basımda ölçüldü, A)', ''))
    # eşitsizlik yönü: aynı sayı için "küçük" ifadeleri azalıp "büyük" ifadeleri artmışsa (sayfa düzeyi sayım)
    def say(metin, desenler):
        c = collections.Counter()
        for d in desenler:
            for m in re.finditer(d, metin, re.I):
                c[m.group('n').replace('.', ',')] += 1
        return c
    LT_EN = [r'(≤|<|less than|below|under|at most|up to)\s*%?\s*(?P<n>\d+(?:[.,]\d+)?)']
    GT_EN = [r'(≥|>|more than|greater than|above|over|at least|exceed\w*)\s*%?\s*(?P<n>\d+(?:[.,]\d+)?)']
    LT_TR = [r'(≤|<)\s*%?\s*(?P<n>\d+(?:,\d+)?)', r"%?(?P<n>\d+(?:,\d+)?)\S*\s+(?:\w+\s+)?(altı|altın|az|küçük|geçmeyen|aşmayan|dek|kadar)"]
    GT_TR = [r'(≥|>)\s*%?\s*(?P<n>\d+(?:,\d+)?)', r"%?(?P<n>\d+(?:,\d+)?)\S*\s+(?:\w+\s+)?(üzerin|üstün|fazla|büyük|aşan)"]
    lte, gte, ltt, gtt = say(en, LT_EN), say(en, GT_EN), say(tr, LT_TR), say(tr, GT_TR)
    for n in set(lte) | set(gte):
        if ltt[n] < lte[n] and gtt[n] > gte[n]:
            b.append(Bulgu('olgu bilgisi', 'İNCELE', f'"{n}" eşiğinde yön dönmüş olabilir: kaynak küçük {lte[n]}/büyük {gte[n]}, çeviri küçük {ltt[n]}/büyük {gtt[n]} (basımda ölçüldü, A)', ''))
    return b

# ───────────────────── 6. metin içi tutarlılık (§6.2, §7.4/#10) ─────────────────────
# Her grup: aynı kavramın ölçülmüş farklı karşılıkları. İki ya da daha çok biçim birlikte geçiyorsa bayrak.
TUTARLILIK = {
    'gradient':      [r'\beğim(ler|leri|lerin|i|in)?\b', r'gradyan\w*|gradyent\w*|gradient\w*'],
    'spatially':     [r'\buzamsal', r'\bmekansal', r'\buzaysal', r'\bboyutsal'],
    'diagnosis':     [r'\btanı(sı|sını|yı|ya|nın|da|sında)?\b', r'\bteşhis\w*'],
    'response':      [r'\byanıt\w*', r'\bcevap\w*'],
    'innate':        [r'doğal (bağışıklık|immün)', r'doğuştan (gelen )?(bağışıklık|immün)'],
    'host':          [r'\bkonak(?!çı)\w*', r'\bkonakçı\w*'],
    'microbiota':    [r'\bmikrobiyota\w*', r'\bmikroflora\w*'],
    'expression':    [r'\banlatım\w*', r'\bekspresyon\w*'],
    'adhesin':       [r'\badezin\w*', r'\badhezin\w*'],
    'horizontal':    [r'\byatay gen', r'\bhorizontal gen'],
    'commensal':     [r'\bkommensal', r'\bkomensal'],
    'reversible':    [r'geri dönüşlü', r'geri dönüşümlü'],
    'stable':        [r'\bkararlı\w*', r'\bdurağan\w*'],
    'dentition':     [r'\bdentisyon\w*', r'\bdiş dizisi', r'\bdişlenme'],
    'extent':        [r'\byaygınlı\w*', r'\byayılım\w*'],
    'gingiva':       [r'\bdiş eti', r'\bdişeti'],
    'inflammation':  [r'\benflama\w*', r'\binflama\w*'],
    'biofilm':       [r'\bbiyofilm\w*', r'\bbiofilm\w*'],
    'diagram':       [r'\bdiyagram\w*', r'\bdiagram\w*'],
    'co-adhesion':   [r'\bkoadezyon\w*', r'\bko-adezyon\w*', r'\bkoadhe\w*'],
    'conditioning':  [r'\bkoşullandırıcı', r'\bşartlandırıcı'],
    'pellicle':      [r'kazanılmış pelik', r'edinilmiş pelik'],
    'unculturable':  [r'kültüre edilemeyen', r'kültür edilemeyen', r'kültür ile tespit edilemeyen'],
    'Gram':          [r'\bGram-(negatif|pozitif)', r'\bgram[- ](negatif|pozitif)'],
    'dichotomous':   [r'var/yok', r'iki yönüyle|çift yönlü', r'\bdikotom', r'\bdikromoz'],
    'constituent':   [r'oluşturan tür', r'koruyucu tür', r'kurucu tür'],
}

BUYUK_KUCUK_AYIRT = {'Gram'}   # bu grupta biçimler yalnız büyük/küçük harfle ayrılır

def tutarlilik(tr):
    """Aynı kavram için birden çok biçim. Cümle başındaki büyük harfli biçim de sayılır ("Tanı … teşhis")."""
    b = []
    kucuk_tr = kucuk(tr)
    for kav, desenler in TUTARLILIK.items():
        metin = tr if kav in BUYUK_KUCUK_AYIRT else kucuk_tr
        var = []
        for d in desenler:
            bulunan = collections.Counter(m.group(0) for m in re.finditer(d, metin))
            if bulunan:
                var.append((bulunan.most_common(1)[0][0], sum(bulunan.values())))
        if len(var) >= 2:
            ozet = ' · '.join(f'{bicim} ×{n}' for bicim, n in var)
            b.append(Bulgu('tutarlılık', 'İNCELE', f'"{kav}" için {len(var)} farklı biçim: {ozet}', ''))
    return b

# ───────────────────── 7. Latince ikili adlar (§5/8) ─────────────────────
CINSLER = r'(Streptococcus|Porphyromonas|Prevotella|Fusobacterium|Aggregatibacter|Tannerella|Treponema|Actinomyces|Veillonella|Neisseria|Eubacterium|Corynebacterium|Parvimonas|Lactobacillus|Candida|[SPFATVNECL]\.)'
EPITETLER = r'(mutans|oralis|mitis|gingivalis|intermedia|nucleatum|forsythia|actinomycetemcomitans|pneumoniae|salivarius|sanguinis|denticola|endodontalis|micra|matruchotii|albicans|sobrinus|gordonii|naeslundii|viscosus)'

def latince(tr):
    b = []
    for m in ara(CINSLER + r'\*?\s+\*?' + EPITETLER, tr, re.I):   # re.I: büyük harfli epiteti de yakala
        epitet = m.group(2)
        if epitet[0].isupper():
            b.append(Bulgu('Latince', 'HATA', 'tür epiteti büyük harfle — küçük yazılır (§5/8)', baglam(tr, m.start(), m.end())))
    for m in ara(r'\bTannarella\b|\bStreptococcuslar\b|\bactinomyces\b', tr):
        b.append(Bulgu('Latince', 'HATA', 'cins adı yanlış yazılmış ya da Türkçe ekle kaynaşmış', baglam(tr, m.start(), m.end())))
    return b

# ───────────────────── 8. atıflar (§5/6) ─────────────────────

ATIF_DISI = {'Fig', 'Table', 'Chapter', 'Edition', 'Published', 'The', 'In', 'Sixth', 'Since', 'From', 'By',
             'After', 'Before', 'Until', 'During', 'Between', 'Of', 'Circa'}   # yıl önünde duran, soyadı olmayan sözcükler

def atiflar(en, tr):
    b = []
    for m in ara(r'\bet al\.', tr):
        b.append(Bulgu('atıf', 'HATA', '`et al.` Türkçe metinde — `ve ark.` olmalı', baglam(tr, m.start(), m.end())))
    for m in ara(r'ark\.\d|\wve ark\.|ve ark \d|veark\.', tr):
        b.append(Bulgu('atıf', 'HATA', '`ve ark.` dizgisi bozuk (boşluk/nokta)', baglam(tr, m.start(), m.end())))
    # İki yazarlı atıfta & → ve (B38 v8'de 15 kez kaçtı). Yayıncı/kurum adlarındaki & (John Wiley & Sons) korunur.
    for m in ara(r"\b[A-ZÀ-Ý][A-Za-zà-ÿ'\-]+ & [A-ZÀ-Ý][A-Za-zà-ÿ'\-]+,? \(?(?:19|20)\d\d", tr):
        b.append(Bulgu('atıf', 'HATA', 'iki yazarlı atıfta `&` — Türkçe metinde `ve` olmalı', baglam(tr, m.start(), m.end())))
    # Yazar–yıl çiftleri: kaynaktaki her (soyad, yıl) çeviride yan yana geçiyor mu?
    ciftler = set()
    for m in ara(r"([A-Z][A-Za-zà-ÿ'\-]{2,})(?: et al\.| & [A-Z][A-Za-zà-ÿ'\-]+)?,? \(?((?:19|20)\d\d)[a-z]?", en):
        ciftler.add((m.group(1), m.group(2)))
    for soyad, yil in sorted(ciftler):
        if soyad in ATIF_DISI:
            continue
        if soyad not in tr:
            b.append(Bulgu('atıf', 'İNCELE', f'kaynaktaki yazar çeviride yok ya da farklı yazılmış: {soyad} {yil}', ''))
            continue
        if not re.search(re.escape(soyad) + r'.{0,60}?' + yil, tr, re.S):
            b.append(Bulgu('atıf', 'İNCELE', f'{soyad} çeviride var ama {yil} yanında değil — yıl değişmiş olabilir', ''))
    return b


# ───────────────────── 9. kitap terim tabanı (dizin hizalaması, 24.09) ─────────────────────
# İngilizce terim kaynakta geçiyor → kitabın hedef biçimi çeviride aranır. Yoksa İNCELE.
# Yalnız çok sözcüklü ve 'guvenli' satırlar: tek sözcüklü genel girdiler (process, free, cells) gürültü üretir.
EKLER = sorted(['ları', 'leri', 'lar', 'ler', 'sının', 'sinin', 'nın', 'nin', 'sı', 'si', 'su', 'sü',
                'ı', 'i', 'u', 'ü', 'ın', 'in', 'a', 'e'], key=len, reverse=True)
KOK_DISI = {'ve', 'ile', 'bir', 'olarak', 'için'}

def kok(sozcuk):
    w = kucuk(sozcuk).strip("(),.;:'’")
    for e in EKLER:
        if len(w) - len(e) >= 3 and w.endswith(e):
            w = w[:-len(e)]; break
    return w[:-1] if len(w) >= 5 else w          # ünsüz yumuşaması payı: kemik/kemiğ, flep/flebi

BURASI = os.path.dirname(os.path.abspath(__file__))
TABAN_ADAYLARI = [   # açık paket: yanındaki terim-listesi.tsv · kod deposu · proje düzeni (araclar/ ↔ terim-tabani/)
    os.path.join(BURASI, 'terim-listesi.tsv'),
    os.path.join(BURASI, 'veri', 'terim-tabani.tsv'),
    os.path.join(BURASI, '..', 'terim-tabani', 'terim-tabani.tsv'),
    os.path.join(BURASI, '..', 'dizin', 'terim-tabani.tsv'),
]

def taban_yolu():
    """TERIM_TABANI ortam değişkeni verilmişse o (var olmasa bile — yanlış yol sessizce geçilmesin); yoksa ilk bulunan aday."""
    if os.environ.get('TERIM_TABANI'):
        return os.environ['TERIM_TABANI']
    return next((y for y in TABAN_ADAYLARI if os.path.exists(y)), None)

Taban = collections.namedtuple('Taban', 'yol hedef kabul anahtar enuzun')

# Çoğul → tekil (taban.py de bunu kullanır; iki dosyada ayrı kural olmasın — kod incelemesi 29.09, 2. tur)
TEKIL_KALAN = {'diabetes', 'caries', 'series', 'species', 'herpes', 'means', 'lens', 'news', 'mumps', 'measles',
               'bias', 'gas', 'pancreas', 'atlas', 'chaos', 'rabies', 'scabies'}

TEKIL_E = {'niche', 'cache', 'ache', 'headache', 'toothache', 'earache', 'backache', 'psyche', 'cliche', 'avalanche'}   # niches → niche

def tekil(w):
    """İngilizce sözcüğün tekili: studies → study, abscesses → abscess, approaches → approach, implants → implant.
    -ss/-is/-us ile bitenlere (gingivitis, sinus) ve TEKIL_KALAN'a dokunulmaz."""
    if len(w) <= 3 or w in TEKIL_KALAN or not w.endswith('s') or w.endswith(('ss', 'is', 'us')):
        return w
    if w.endswith('es') and w[:-2] in TEKIL_KALAN:                  # biases → bias, lenses → lens
        return w[:-2]
    if w.endswith('ies') and len(w) > 4:
        return w[:-3] + 'y'
    if w.endswith(('sses', 'xes', 'ches', 'shes')) and w[:-1] not in TEKIL_E:
        return w[:-2]
    return w[:-1]

def _anahtar(terim):
    """Terimin sözcük dizisi: kısa çizgi ve boşluk aynı sayılır; son sözcük tekilleşir. Böylece
    'healing phases' terimi kaynaktaki 'healing phase' ile de eşleşir (kaynak öbekleri de tekilleştirilir)."""
    w = re.findall(r'[a-z]+', terim.lower())
    if w:
        w[-1] = tekil(w[-1])
    return ' '.join(w)

def taban_yukle(yol=None):
    """Tabanı okur (yol başına bir kez). Dosya yoksa None döner — çağıran bunu raporlamalıdır."""
    yol = yol or taban_yolu()
    if not yol or not os.path.exists(yol):
        return None
    return _taban_oku(os.path.abspath(yol), os.path.getmtime(yol))

@functools.lru_cache(maxsize=8)
def _taban_oku(yol, _degisim):   # _degisim: dosya değişince önbellek tazelenir
    hedef, kabul = collections.defaultdict(set), collections.defaultdict(set)
    with open(yol, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            en = re.sub(r'\s*\(.*?\)', '', r['ingilizce']).strip().lower()
            if r.get('durum', 'guvenli') != 'guvenli' or len(en.split()) < 2 or not re.match(r'^[a-z][a-z \-]+$', en):
                continue
            for b in (r.get('hedef') or r['kitap']).split(' | '):   # ' | ' = uzmanın kabul ettiği eş biçimler
                hedef[en].add(re.sub(r'\s*\(.*?\)', '', b).strip())
            for b in (r.get('kabul') or '').split(' | '):           # kitapta ≥2 kez geçen eş anlamlı biçim (26.09)
                if b.strip():
                    kabul[en].add(re.sub(r'\s*\(.*?\)', '', b).strip())
    # tekil/çoğul satırlar (probing attachment level / levels) tek terimde birleşir: aynı kaynak öbeği iki kez raporlanmaz
    birlesik_h, birlesik_k, ad = collections.defaultdict(set), collections.defaultdict(set), {}
    for t in sorted(hedef, key=len):
        a = _anahtar(t)
        ad.setdefault(a, t); birlesik_h[ad[a]] |= hedef[t]; birlesik_k[ad[a]] |= kabul.get(t, set())
    anahtar = {t: _anahtar(t) for t in birlesik_h}
    return Taban(yol, dict(birlesik_h), dict(birlesik_k), anahtar, max((a.count(' ') + 1 for a in anahtar.values()), default=0))

def _kaynak_obekleri(en, enuzun):
    """Kaynaktaki bütün 1..enuzun sözcüklük öbekler; son sözcüğün çoğulu tekil biçimiyle de eklenir (tekil())
    (eski desen: terim + (s|es)?). Terim başına düzenli ifade kurmaktan ≈20 kat hızlı (kod incelemesi 29.09)."""
    obek = set()
    for parca in re.split(r'[^a-z\s\-]+', en.lower()):   # noktalama öbeği böler ("bone. Tissue" terim değildir)
        w = re.findall(r'[a-z]+', parca)
        for n in range(1, enuzun + 1):
            for i in range(len(w) - n + 1):
                g = w[i:i + n]
                obek.add(' '.join(g))
                obek.add(' '.join([*g[:-1], tekil(g[-1])]))
                for ek in ('es', 's'):                       # eski desen terim + (s|es)? ile uyum (biases → bias)
                    if g[-1].endswith(ek) and len(g[-1]) > len(ek):
                        obek.add(' '.join([*g[:-1], g[-1][:-len(ek)]]))
    return obek

def kitap_terimleri(en, tr, taban):
    b = []
    tr_tok = [kucuk(w) for w in re.findall(r"[\wçğıöşüâîû]+", tr)]
    def var(bicim):
        kokler = [kok(w) for w in re.split(r'[\s\-/]+', bicim) if w and kucuk(w) not in KOK_DISI]
        if not kokler:
            return True
        n = len(kokler)
        for i, w in enumerate(tr_tok):
            if w.startswith(kokler[0]):
                pencere = tr_tok[i + 1:i + n + 3]; j = 0
                for k in kokler[1:]:
                    while j < len(pencere) and not pencere[j].startswith(k):
                        j += 1
                    if j == len(pencere):
                        break
                    j += 1
                else:
                    return True
        return False
    obek = _kaynak_obekleri(en, taban.enuzun)
    for terim, bicimler in taban.hedef.items():
        if taban.anahtar[terim] not in obek:
            continue
        if not any(var(bc) for bc in bicimler):
            kab = [bc for bc in taban.kabul.get(terim, ()) if var(bc)]
            if kab:
                b.append(Bulgu('kitap terimi', 'TERCİH', f'"{terim}": "{kab[0]}" kitapta da geçen eş anlamlı (hata değil); baskın biçim → {" / ".join(sorted(bicimler))}', ''))
            else:
                b.append(Bulgu('kitap terimi', 'İNCELE', f'"{terim}" kaynakta var; kitabın biçimi çeviride yok → {" / ".join(sorted(bicimler))}', ''))
    return b

# ───────────────────────────── rapor ─────────────────────────────

def denetle(en, tr_tam, taban=None):
    """taban: None → varsayılan tabanı yükle; bir Taban → onu kullan; False ya da TABANSIZ=1 → kitap terimi denetimi kapalı."""
    en = normallestir_en(en)
    tr = govde(tr_tam)
    bulgular = []
    b, istat = imzalar(tr); bulgular += b
    bulgular += sayilar(tr)
    bulgular += ozel_adlar(en, tr)
    bulgular += kisaltmalar(en, tr)
    bulgular += yanlis_dost(en, tr)
    bulgular += olgu_bilgisi(en, tr)
    bulgular += tutarlilik(tr)
    bulgular += latince(tr)
    bulgular += atiflar(en, tr)
    if taban is False or os.environ.get('TABANSIZ'):
        istat['taban'] = 'kapalı (TABANSIZ)'
    else:
        t = taban or taban_yukle()
        if t is None:
            istat['taban'] = 'YÜKLENEMEDİ'
            bulgular.append(Bulgu('kitap terimi', 'HATA', f'terim tabanı bulunamadı ({taban_yolu() or "yol yok"}) — kitap terimi denetimi YAPILMADI; TERIM_TABANI ile doğru yolu verin', ''))
        elif not t.hedef:
            istat['taban'] = f'BOŞ ({t.yol})'
            bulgular.append(Bulgu('kitap terimi', 'HATA', f'terim tabanı boş ({t.yol}): güvenli terim yok — kitap terimi denetimi YAPILMADI', ''))
        else:
            istat['taban'] = f'{t.yol} ({len(t.hedef)} terim)'
            bulgular += kitap_terimleri(en, tr, t)
    return bulgular, istat

def rapor(bulgular, istat, baslik):
    satir = [f'# Denetim — {baslik}', '']
    satir.append(f"Sözcük: {istat['sözcük']} · `-maktadır`: {istat['-maktadır']} ({istat['-maktadır/1000']}/1000)")
    satir.append(f"Terim tabanı: {istat.get('taban', '—')}")
    h = sum(1 for x in bulgular if x.siddet == 'HATA'); t = sum(1 for x in bulgular if x.siddet == 'TERCİH'); i = len(bulgular) - h - t
    satir += [f'**HATA: {h} · İNCELE: {i} · TERCİH: {t}**', '',
              '_HATA = anlam alanı dışında, "olmayacak" kullanım. TERCİH = kitapta ya da alanda geçen eş anlamlı; hata sayılmaz, baskın biçim önerilir (uzman, 26.09)._', '']
    gruplar = collections.OrderedDict()
    for x in bulgular:
        gruplar.setdefault(x.sinif, []).append(x)
    for sinif, xs in gruplar.items():
        satir.append(f'## {sinif} ({len(xs)})')
        for x in xs:
            s = f'- **{x.siddet}** — {x.mesaj}'
            if x.baglam:
                s += f'\n  > {x.baglam}'
            satir.append(s)
        satir.append('')
    return '\n'.join(satir)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='dis-hekimligi-ceviri-tr teslim öncesi denetimi')
    ap.add_argument('--tr', required=True); ap.add_argument('--en', required=True)
    ap.add_argument('--out'); ap.add_argument('--baslik', default='')
    ap.add_argument('--taban', help='terim tabanı yolu (verilmezse TERIM_TABANI ya da varsayılan adaylar)')
    a = ap.parse_args()
    with open(a.en, encoding='utf-8') as f:
        en = f.read()
    with open(a.tr, encoding='utf-8') as f:
        tr = f.read()
    t = None
    if a.taban:
        t = taban_yukle(a.taban)
        if t is None:
            ap.error(f'terim tabanı bulunamadı: {a.taban}')
    bl, ist = denetle(en, tr, t)
    r = rapor(bl, ist, a.baslik or a.tr)
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(r)
    print(r)
