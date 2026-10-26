#!/usr/bin/env python3
"""
test_denetim.py — denetim.py'nin doğrulaması.

İki yönlü:
  (1) POZİTİF: basılı Lindhe çevirisinde BELGELENMİŞ hatalar (ölçüm raporlarından
      kısa alıntı) — betik bunları YAKALAMALI.
  (2) NEGATİF: aynı kavramların doğru biçimleri — betik bunlara HATA DEMEMELİ.
Bir test başarısızsa betik yanlıştır, çeviri değil.
"""
import os, sys, time
BURASI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURASI)
import denetim as d

# Testler üretim tabanına değil, depodaki küçük örnek tabana bakar (üretim tabanının test metinlerinde geçen satırları):
# taban değişse de testin sonucu değişmez.
ORNEK_TABAN = d.taban_yukle(os.path.join(BURASI, 'testveri', 'taban-ornek.tsv'))

# (ad, İngilizce kaynak, Türkçe metin, sınıf, beklenen)
#   beklenen = 'HATA' / 'İNCELE' / 'TERCİH' → o sınıfta bu şiddette (İNCELE için HATA da olur) bulgu OLMALI
#   beklenen = None    → o sınıfta HATA OLMAMALI (İNCELE/TERCİH serbest)
#   beklenen = 'TEMİZ' → o sınıfta ne HATA ne İNCELE olmalı
VAKALAR = [
    # ── özel adlar ──
    ('B8 Wiley', 'Reproduced with permission from John Wiley & Sons.', 'John Wiley ve Sons\'dan uyarlanmıştır.', 'özel ad', 'HATA'),
    ('B8 HOMD', 'the Human Oral Microbiome Database (http://www.homd.org)', 'İnsan Oral Mikrobiyom Veritabanı\'na', 'özel ad', 'HATA'),
    ('B8 HMP', 'the larger Human Microbiome Project.', 'daha büyük İnsan Mikrobiyom Projesi\'ne', 'özel ad', 'HATA'),
    ('B7 WHO bank (bu skill)', 'accumulated in the WHO Global Oral Data Bank (Miyazaki', 'DSÖ Küresel Ağız Sağlığı Veri Bankasında toplanmıştır', 'özel ad', 'HATA'),
    ('B7 CPI İndeks', 'termed Community Periodontal Index (WHO 1997)', 'Toplumda Periodontal İndeks (Community Periodontal İndeks)', 'özel ad', 'HATA'),
    ('B29 FDA', 'World Dental Federation (FDI) two-digit system', 'Dünya Diş Hekimliği Federasyonu (FDA) iki haneli', 'özel ad', 'HATA'),
    ('NEG Wiley doğru', 'Reproduced with permission from John Wiley & Sons.', 'John Wiley & Sons izniyle çoğaltılmıştır.', 'özel ad', None),
    # ── kısaltmalar ──
    ('B8 GCF (bu skill)', 'increased flow of gingival crevicular fluid (GCF) in', 'diş eti oluğu sıvısı (gingival crevicular fluid, GCF) akışını', 'kısaltma', 'HATA'),
    ('NEG DOS doğru', 'increased flow of gingival crevicular fluid (GCF) in', 'diş eti oluğu sıvısı (DOS) akışını', 'kısaltma', None),
    ('B8 MİK', 'minimum inhibitory concentration (MIC)', 'minimum inhibitör konsantrasyonu (MİK)', 'kısaltma', 'HATA'),
    ('B8 YUP', 'competence stimulating peptide (CSP)', 'yetkin uyarıcı peptit (YUP)', 'kısaltma', 'HATA'),
    ('B7 KAS', 'clinical attachment level (CAL)', 'klinik ataşman seviyesi (KAS)', 'kısaltma', 'HATA'),
    # ── yanlış dost ──
    ('B8 succession', '(a process termed microbial succession)', '(bu süreç mikrobiyal miras olarak adlandırılır)', 'yanlış dost', 'HATA'),
    ('B8 emergent', 'microbial communities display emergent properties', 'mikrobiyal topluluklar beklenmeyen özellikler gösterir', 'yanlış dost', 'HATA'),
    ('B8 sequencing', 'amplification, cloning, and sequencing of the 16S rRNA gene', 'amplifikasyonuna, klonlanmasına ve sıralanmasına', 'yanlış dost', 'HATA'),
    ('B8 detachment', '6. Detachment of attached cells', '6. tutunan hücrelerin çözülmesi', 'yanlış dost', 'HATA'),
    ('B8 spp', 'Clusters of Fusobacterium spp. (magenta)', 'Kümeler halinde Fusobacterium suşu (magenta)', 'yanlış dost', 'HATA'),
    ('B8 certain', 'a higher frequency of certain Gram-negative periodontal pathogens', 'zorunlu gram negatif periodontal patojenlere', 'yanlış dost', 'HATA'),
    ('B7 aggregation', 'shows familial aggregation', 'ailesel geçiş gösterir', 'yanlış dost', 'HATA'),
    ('B7 natural history', 'data on the natural history of periodontal disease', 'hastalığın doğasına uygun veri', 'yanlış dost', 'HATA'),
    ('B7 median', 'the median subject (50th percentile)', 'ortalama birey (50\'lik yüzde)', 'yanlış dost', 'HATA'),
    ('B7 screening', 'as screening methods for detecting', 'görüntüleme yöntemleri olarak', 'yanlış dost', 'HATA'),
    ('v6 kestirim (bu skill)', 'the predictive value of BOP', 'BOP\'un kestirim değeri', 'yanlış dost', 'TERCİH'),
    ('NEG prediktif doğru', 'the predictive value of BOP', 'sondlamada kanamanın prediktif değeri', 'yanlış dost', None),
    # ── Latince ──
    ('B8 S. Mutans', 'In S. mutans, quorum sensing', 'S. Mutans\'ın genetik yeterliliğini', 'Latince', 'HATA'),
    ('B8 Oralis', '(Streptococcus mitis, Streptococcus oralis)', '(Streptococcus mitis, Streptococcus Oralis)', 'Latince', 'HATA'),
    ('B8 Tannarella', 'Tannerella, F. nucleatum', '*Tannarella*, *F. nucleatum*', 'Latince', 'HATA'),
    ('NEG Latince doğru', 'In S. mutans', '*S. mutans*\'ta', 'Latince', None),
    # ── atıf ──
    ('B8 et al.', '(Gilbert et al. 2002)', '(Gilbert et al. 2002)', 'atıf', 'HATA'),
    ('B8 ark.boşluk', '(Hasegawa et al. 2007)', '(Hasegawa ve ark.2007)', 'atıf', 'HATA'),
    ('B8 Wade yılı', 'in the laboratory (Wade 1999, 2002)', 'tahmin edilebilmektedir (Wade 1992, 2002)', 'atıf', 'İNCELE'),
    ('B8 Buscher', '(Busscher et al. 2008; Nobbs et al. 2011)', '(Buscher ve ark. 2008; Nobbs ve ark. 2011)', 'atıf', 'İNCELE'),
    # ── sayı ──
    ('B8 ondalık', 'rises to between pH 7.2 and 7.4', 'pH değeri 7.2 ile 7.4 arasına', 'sayı', 'HATA'),
    ('B7 kesme', 'at <20% of the surfaces', 'yüzeylerin <%20 \'sinde', 'sayı', 'HATA'),
    ('NEG sayı doğru', 'rises to between pH 7.2 and 7.4', 'pH 7,2 ile 7,4 arasına yükselir', 'sayı', None),
    ('NEG atıf yılı harfli', '(Baelum et al. 1993a)', '(Baelum ve ark. 1993a)', 'sayı', None),
    ('NEG şekil paneli', 'x', 'bkz. Şekil 8-1a ve Şekil 46-22a; (2i) evresi; B-1a hücreleri', 'sayı', None),
    ('NEG § göndermesi', 'x', '§6.3 uyarınca ve §5.6 gereği', 'sayı', None),
    ('NEG notlar gövdeye girmez', 'gingival crevicular fluid (GCF)', '## ÇEVİRİ\ndiş eti oluğu sıvısı (DOS).\n## ÇEVİRİ NOTLARI\n[ÇN-1] GCF yerine DOS kullanıldı (Gemmel et al. 2006).', 'kısaltma', None),
    ('NEG eski biçim dosya', 'gingival crevicular fluid (GCF)', '## s. 259\ndiş eti oluğu sıvısı (DOS).\n## ÇEVİRİ NOTLARI\n[ÇN-1] GCF → DOS.', 'kısaltma', None),
    ('B13 U+2010 tire', 'delayed\u2010type hyper\xad\n  sensitivity (DTH)', 'gecikmiş tip hipersensitivite', 'yanlış dost', 'TERCİH'),
    ('B39 kör bir alet', 'using a blunt instrument', 'kör bir aletle embrazürden', 'yanlış dost', 'TERCİH'),
    ('B39 recontouring', 'bone recontouring', 'kemiğin yeniden şekillendirilmesi', 'yanlış dost', 'TERCİH'),
    ('B39 semilunar', 'a semilunar incision', 'yarım ay biçiminde bir insizyon', 'yanlış dost', 'TERCİH'),
    ('B46 kron', 'the crown margin', 'kron kenarı subgingival', 'yanlış dost', 'TERCİH'),
    ('NEG kronik değil kron', 'chronic periodontitis and the crown', 'kronik periodontitis ve kuron kenarı', 'yanlış dost', None),
    ('B13 defans', 'the defence mechanisms of the host', 'konağın defans mekanizmaları', 'yanlış dost', 'TERCİH'),
    ('NEG DOS + özgün GCF parantezi', 'increased flow of gingival crevicular fluid (GCF)', 'diş eti oluğu sıvısı (DOS; gingival crevicular fluid, GCF) akışında artış', 'kısaltma', None),
    ('NEG Since yılı', 'Since 1976, studies have shown', '1976\'dan bu yana çalışmalar', 'atıf', None),
    ('B8 sahiptir (bu skill)', 'x', 'gelişmiş bir savunma dizisine sahiptir; bu savunmanın', 'imza', 'HATA'),
    # ── imza ──
    ('imza tarafından', 'x', 'bakteriler tarafından proteolize uğratılır', 'imza', 'HATA'),
    ('imza sahip', 'x', 'daha kompleks bir mimariye sahiptir', 'imza', 'HATA'),
    ('NEG öyle ki', 'x', 'kompetansı da uyarır; öyle ki biyofilmde', 'imza', None),
    # ── tutarlılık ──
    ('B8 spatially ×3', 'x', 'mekansal olarak. uzaysal-düzende. boyutsal olarak düzenlenir', 'tutarlılık', 'İNCELE'),
    ('B8 konak/konakçı', 'x', 'konak savunması ve konakçı makromolekülleri', 'tutarlılık', 'İNCELE'),
    ('NEG tek biçim', 'x', 'uzamsal olarak. uzamsal gelişim.', 'tutarlılık', None),
    # ── uzman kararları 24.09 (kitap biçimi) ──
    ('D1 tanı', 'a diagnosis of aggressive periodontitis', 'agresif periodontitis tanısı', 'yanlış dost', 'TERCİH'),
    ('NEG D1 ayırıcı tanı', 'the differential diagnosis includes', 'ayırıcı tanıda şunlar yer alır; teşhis', 'yanlış dost', None),
    ('D2 düzey', 'clinical attachment level (CAL)', 'klinik ataşman düzeyi (CAL)', 'yanlış dost', 'TERCİH'),
    ('D3 bağlantı epiteli', 'the junctional epithelium migrates', 'bağlantı epiteli göç eder', 'yanlış dost', 'TERCİH'),
    ('C1 olasılık oranı', 'an odds ratio of 2.3', 'olasılık oranı 2,3', 'yanlış dost', 'HATA'),
    ('NEG C1 odds oranı', 'an odds ratio of 2.3', 'odds oranı 2,3', 'yanlış dost', None),
    ('B sunan', 'antigen-presenting cells', 'antijen sunan hücreler', 'yanlış dost', 'TERCİH'),
    ('NEG ne var ki', 'x', 'Ne var ki bu evrede lezyon sınırlıdır.', 'imza', None),
    ('B12 öbek: among the first', 'Streptococci are among the first organisms to colonize the acquired pellicle', 'Plak gelişirken kazanılmış pelikılı kolonize eden ilk organizmalar arasında streptokoklar da vardır.', 'yanlış dost', 'İNCELE'),
    ('NEG among the first', 'Streptococci are among the first organisms to colonize the acquired pellicle', 'Streptokoklar, kazanılmış pelikılı ilk kolonize eden organizmalar arasındadır.', 'yanlış dost', None),
    ('basımda ölçüldü kalıtsal', 'sexual dimorphism in elements of both the innate and the acquired immunity', 'kalıtsal ve edinsel immünitenin elemanlarında', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü deregulation', 'Deregulation of host immune and inflammatory response', 'Konak immune ve inflamatuar yanıtın ortadan kaldırılması', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü Cdt', 'Cytolethal distending toxin: Cdt', 'Sitotelyal yayılma toksini: Cdt', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü formal', 'demonstrated by formal genetic studies', 'değerli pek çok genetik çalışma ile gösterilmiş', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü otoimmünizasyon', 'autoimmunization has also been mentioned as a risk', 'otoimmunizasyondan (doğuştan bir hastalığa bağışık olma) da bir risk olarak', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü significantly', 'significantly greater reductions', 'önemli ölçüde büyük azalmalar', 'yanlış dost', 'TERCİH'),
    ('NEG significantly anlamlı', 'significantly greater reductions', 'anlamlı ölçüde daha büyük azalmalar', 'yanlış dost', None),
    ('D5 bağışıklık yanıtı', 'the immune response', 'bağışıklık yanıtı', 'yanlış dost', 'TERCİH'),
    ('D5 immün yanıt', 'the immune response', 'immün yanıtın etkileri', 'yanlış dost', 'TERCİH'),
    ('NEG D5 immün cevap', 'the immune response', 'immün cevabın etkileri', 'yanlış dost', None),
    ('D5 ailesi konak yanıtı', 'the host response to plaque', 'plağa karşı konak yanıtı', 'yanlış dost', 'TERCİH'),
    ('NEG konak cevabı', 'the host response to plaque', 'plağa karşı konak cevabı', 'yanlış dost', None),
    ('succession zincir', 'a process termed microbial succession', 'mikrobiyal zincir adı verilen süreç', 'yanlış dost', 'TERCİH'),
    ('NEG succession', 'a process termed microbial succession', 'mikrobiyal süksesyon adı verilen süreç', 'yanlış dost', None),
    ('B38 v8 atıf &', 'x', 'yapışabildiği gösterilmiştir (Listgarten & Ellegaard 1973).', 'atıf', 'HATA'),
    ('NEG atıf ve', 'x', 'yapışabildiği gösterilmiştir (Listgarten ve Ellegaard 1973).', 'atıf', None),
    ('NEG Wiley &', 'x', 'John Wiley & Sons izniyle.', 'atıf', None),
    ('basımda ölçüldü psikoloji', 'a profound impact on human physiology', 'insan psikolojisi üzerinde derin etki', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü modifiye edilebilen', 'modifying factors', 'modifiye edilebilen faktörler', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü savaş', 'the bacterial challenge', 'bakteriyel savaş', 'yanlış dost', 'HATA'),
    ('B38 blade ağız', 'identified with the lower edge of the blade', 'cebin tabanı ağzın alt kenarıyla bulunduktan sonra', 'yanlış dost', 'İNCELE'),
    ('NEG blade bıçak', 'identified with the lower edge of the blade', 'cebin tabanı bıçağın alt kenarıyla belirlendikten sonra', 'yanlış dost', None),
    ('taban kabul: ağız hijyeni', 'poor oral hygiene was common', 'kötü ağız hijyeni yaygındı', 'kitap terimi', 'TERCİH'),
    ('taban kabul: ağız boşluğu', 'bacteria of the oral cavity', 'ağız boşluğundaki bakteriler', 'kitap terimi', 'TERCİH'),
    ('NEG taban: çekim ekli', 'poor oral hygiene was common', 'zayıf oral hijyenin yaygın olduğu', 'kitap terimi', None),
    # ── 26.09 uzman kararı: eş anlamlı ≠ hata; "olmayacak" kullanım = hata ──
    ('succession miras', 'a process termed microbial succession', 'mikrobiyal miras adı verilen süreç', 'yanlış dost', 'HATA'),
    ('NEG tanı hata değil', 'a diagnosis of aggressive periodontitis', 'agresif periodontitis tanısı', 'yanlış dost', None),
    ('NEG konak yanıtı hata değil', 'the host response to plaque', 'plağa karşı konak yanıtı', 'yanlış dost', None),
    ('C1 olasılık oranı hâlâ HATA', 'an odds ratio of 2.3', 'olasılık oranı 2,3', 'yanlış dost', 'HATA'),
    ('sinüs duvarı hâlâ HATA', 'sinus floor elevation', 'sinüs duvarı elevasyonu', 'yanlış dost', 'HATA'),
    # ── Cilt 2 taraması (26.09) — kitapta ölçülmüş olmayacak kullanımlar ──
    ('basımda ölçüldü önleyici ölçümler', 'anti-infective preventive measures', 'enfeksiyona karşı önleyici ölçümleri', 'yanlış dost', 'HATA'),
    ('NEG önleyici önlemler', 'anti-infective preventive measures', 'enfeksiyona karşı önleyici önlemler', 'yanlış dost', None),
    ('basımda ölçüldü idame oranı', 'yielding a 100% survival rate', '%100 idame oranı vererek', 'yanlış dost', 'HATA'),
    ('NEG sağkalım', 'yielding a 100% survival rate', '%100 sağkalım oranıyla', 'yanlış dost', None),
    ('basımda ölçüldü çözünürlük', 'complete resolution of peri-implantitis lesions', 'peri-implantitis lezyonlarında tam çözünürlük', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü temel', 'substantive drugs such as tetracyclines', 'tetrasiklin gibi sübstantif (temel) ilaçların', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü hemostaz', 'necessary for bone homeostasis', 'kemik hemostazisi için gerekli', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü eleştiri', 'the two sets of criteria are not in conflict', 'iki farklı eleştiri grubu çatışmaz', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü nadiren (A)', 'Hence, not infrequently, tissue augmentation procedures must be performed', 'Dolayısıyla nadiren de olsa doku ogmentasyonu yapılmalıdır', 'yanlış dost', 'HATA'),
    ('NEG not infrequently sık', 'Hence, not infrequently, tissue augmentation procedures must be performed', 'Bu nedenle doku ogmentasyonu sık sık gerekir', 'yanlış dost', None),
    ('basımda ölçüldü çok bilgi (A)', 'There is little information about treatment based on controlled studies.', 'Kontrollü çalışmalara dayanan tedavi ile ilgili çok bilgi mevcuttur.', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü kastedilme (A)', 'not to mention invaded soft tissues', 'yumuşak doku içindekiler kastedilmemektedir', 'yanlış dost', 'HATA'),
    ('basımda ölçüldü former (A)', 'In the former case, prognosis is bleak', 'Sonraki durumda prognoz kötüdür', 'yanlış dost', 'İNCELE'),
    ('basımda ölçüldü ilaç adı', 'SRP + topical minocycline ointment in all pockets', 'SRP + tüm ceplere topikal doksisiklin merhem', 'olgu bilgisi', 'İNCELE'),
    ('NEG ilaç adı', 'SRP + topical minocycline ointment in all pockets', 'SRP + tüm ceplere topikal minosiklin merhem', 'olgu bilgisi', None),
    ('basımda ölçüldü cinsiyet', '45-year-old female patient with generalized chronic periodontitis', 'Generalize kronik periodontitisli 45 yaşında erkek hasta', 'olgu bilgisi', 'İNCELE'),
    ('basımda ölçüldü diş tipi', 'two mandibular premolars in the monkey', 'maymunda iki mandibular molar arasındaki', 'olgu bilgisi', 'İNCELE'),
    ('basımda ölçüldü anlamlı değil (A)', 'Non-significant difference between groups (P > 0.05)', 'Gruplar arasında anlamlı fark görülmüştür (P>0,05)', 'olgu bilgisi', 'İNCELE'),
    ('NEG anlamlı değil', 'Non-significant difference between groups (P > 0.05)', 'Gruplar arasında anlamlı fark bulunmamıştır (P > 0,05)', 'olgu bilgisi', None),
    ('basımda ölçüldü eşitsizlik (A)', 'a full-mouth mean BoP of ≤25% should be reached', "tüm ağız SK skoru %25'in üzerine ulaşmalıdır", 'olgu bilgisi', 'İNCELE'),
    ('B20 işaret eder (v9)', 'The literature consistently indicates a positive association. Twin studies have indicated a high inherited component. Data indicate that gingivitis precedes periodontitis.', 'Literatür tutarlı biçimde pozitif bir ilişkiye işaret eder. İkiz çalışmaları yüksek kalıtsal bileşene işaret etmiştir. Veriler gingivitisin periodontitisten önce geldiğine işaret eder.', 'imza', 'İNCELE'),
    ('B20 tartışması verilmiştir (v9)', 'Only a brief discussion of smoking as a risk factor is thus given here.', 'Bu nedenle burada sigaranın bir risk faktörü olarak yalnızca kısa bir tartışması verilmiştir.', 'imza', 'İNCELE'),
    ('NEG işaret eder tek', 'Widened spaces indicate that forces may be working.', 'Genişlemiş aralıklar kuvvetlerin etkili olabileceğini gösterir; bu bulgu bir soruna işaret eder.', 'imza', None),
    ('B48 -mıştı (v10)', 'Consolidation of the osteotomy gap was in many cases almost complete.', 'Osteotomi aralığının konsolidasyonu birçok olguda neredeyse tamamlanmıştı; bazı olgularda ise yeni kemik yapıları lameller bir oryantasyon göstermiştir.', 'imza', 'İNCELE'),
    ('B48 gözlenebilmiştir (v9)', 'small islands could be observed near the osteotomy rims.', 'Bazı olgularda küçük ve dağınık adacıklar gözlenebilmiştir.', 'imza', 'İNCELE'),
    ('B20 ele alınır (v9)', 'The association is dealt with in detail in Chapter 12.', 'Periodontal hastalık ile sigara arasındaki ilişki Bölüm 12\'de ayrıntılı olarak ele alınır.', 'imza', 'İNCELE'),
    ('B48 en büyük önemi (v10)', 'are of utmost importance.', 'biyolojik sonuçlar en büyük önemi taşır.', 'imza', 'İNCELE'),
    ('P1 düşük kaliteli (v11a)', 'which, together with low-quality oral hygiene, may have helped', 'Bu raporlar ve çalıştaylar, düşük kaliteli oral hijyenle birlikte farkındalığın artmasına yardımcı olmuş olabilir.', 'imza', 'İNCELE'),
    ('P1 ilk on makale (v11a)', 'most of the top ten articles were published over 10 years ago', 'Şunu da belirtmek gerekir: ilk on makalenin çoğu 10 yıldan uzun süre önce yayımlanmıştır.', 'imza', 'İNCELE'),
    ('P1 sigara da (v11a)', 'and smoking may increase salivary NO levels.', 'Bu tutarsızlık hastaların bir kısmının sigara içmesinden kaynaklanıyor olabilir; sigara da tükürük NO seviyelerini artırabilir.', 'imza', 'İNCELE'),
    ('NEG İ büyük harf (1.0)', 'The immune response increased.', 'İmmün cevap artmıştır.', 'kitap terimi', None),
    ('B8 değinilecektir (1.0)', 'The properties of dental biofilms will be described in the rest of this chapter.', 'Bölümün geri kalanında dental biyofilmlerin özellikleri üzerinde durulacaktır.', 'imza', 'İNCELE'),
    ('NEG değinilmektedir', 'These are discussed later in this chapter.', 'Bunlara bu bölümün ilerisinde değinilmektedir.', 'imza', None),
    ('NEG ele alınmıştır', 'The association is dealt with in detail in Chapter 12.', 'Periodontal hastalık ile sigara arasındaki ilişki Bölüm 12\'de ayrıntılı olarak ele alınmıştır.', 'imza', None),
    ('NEG eşitsizlik', 'a full-mouth mean BoP of ≤25% should be reached', 'tüm ağız ortalama BOP değeri ≤%25 olmalıdır', 'olgu bilgisi', None),
    # ── 1.0: yanlış alarm olmamalı (eskiden ayrı NEG_INCELE listesindeydi) ──
    ('NEG zayıf oral hijyen', 'poor oral hygiene', 'Zayıf oral hijyen periodontitis için bir risk faktörüdür.', 'imza', 'TEMİZ'),
    ('NEG en çok atıf alan ilk on', 'the top ten articles', 'En çok atıf alan ilk on makalenin çoğu 10 yıldan önce yayımlanmıştır.', 'imza', 'TEMİZ'),
    ('NEG İ büyük harf', 'The immune response increased.', 'İmmün cevap artmıştır.', 'kitap terimi', 'TEMİZ'),
    ('NEG ; bu da', 'which in turn', 'Periodontitis CRP üretimini artırabilir; bu da enflamatuar medyatörleri uyarabilir.', 'imza', 'TEMİZ'),
    # ── kod incelemesi 29.09 ──
    ('tutarlılık cümle başı', 'Diagnosis was made; the diagnosis was confirmed.', 'Tanı konmuştur; teşhis kesinleşmiştir.', 'tutarlılık', 'İNCELE'),
    ('tutarlılık İ büyük harf', 'inflammation and inflammation', 'Enflamasyon artar. İnflamasyon azalır.', 'tutarlılık', 'İNCELE'),
    ('NEG tek bulgu: immün yanıt', 'The immune response increased.', 'İmmün yanıt artmıştır.', 'yanlış dost', 'TEK'),
    ('tekil/çoğul -es tek bulgu', 'Periodontal abscesses were drained.', 'Periodontal kistler boşaltıldı.', 'kitap terimi', 'TEK'),
    ('NEG tekil/çoğul -es', 'Periodontal abscesses were drained.', 'Periodontal apseler boşaltıldı.', 'kitap terimi', 'TEMİZ'),
    ('bias çoğulu (biases)', 'Publication biases were found.', 'Yayın hataları bulundu.', 'kitap terimi', 'İNCELE'),
    ('NEG noktalama öbeği böler', 'loss of attachment and bone. Tissue destruction follows.', 'ataşman ve kemik kaybı. Doku yıkımı izler.', 'kitap terimi', 'TEMİZ'),
]


def calistir():
    basla = time.time()
    basarisiz = []
    for ad, en, tr, sinif, beklenen in VAKALAR:
        bl, _ = d.denetle(en, tr, ORNEK_TABAN)
        ilgili = [x for x in bl if x.sinif == sinif]
        if beklenen is None:
            ok = not any(x.siddet == 'HATA' for x in ilgili)
        elif beklenen == 'TEMİZ':
            ok = not any(x.siddet in ('HATA', 'İNCELE') for x in ilgili)
        elif beklenen == 'TEK':          # aynı metin parçası bir kez raporlanmalı
            ok = len(ilgili) == 1
        else:
            ok = any(x.siddet == beklenen or (beklenen == 'İNCELE' and x.siddet == 'HATA') for x in ilgili)
        if not ok:
            basarisiz.append(ad)
            print(f'  ✗ {ad:28s} beklenen {sinif}/{beklenen or "HATA yok"} · bulunan: {[(x.siddet, x.mesaj[:50]) for x in ilgili]}')
    # boş taban da sessiz geçmemeli (kod incelemesi 29.09, 2. tur)
    bos = os.path.join(BURASI, 'testveri', 'taban-bos.tsv')
    bl, ist = d.denetle('The immune response increased.', 'Bağışıklık artmıştır.', d.taban_yukle(bos))
    if not any(x.siddet == 'HATA' and 'tabanı boş' in x.mesaj for x in bl):
        basarisiz.append('boş tabanda uyarı')
    # taban yoksa sessiz geçmemeli (kod incelemesi 1.2)
    eski = os.environ.get('TERIM_TABANI'); os.environ['TERIM_TABANI'] = os.path.join(BURASI, 'yok.tsv')
    try:
        bl, ist = d.denetle('The immune response increased.', 'Bağışıklık artmıştır.')
        if not (ist['taban'] == 'YÜKLENEMEDİ' and any(x.siddet == 'HATA' and 'tabanı bulunamadı' in x.mesaj for x in bl)):
            basarisiz.append('taban yokken uyarı')
            print('  ✗ taban yokken uyarı yok')
    finally:
        os.environ.pop('TERIM_TABANI')
        if eski is not None:
            os.environ['TERIM_TABANI'] = eski
    toplam = len(VAKALAR) + 1
    print(f'\n{toplam - len(basarisiz)}/{toplam} vaka geçti ({time.time() - basla:.1f} sn).')
    return len(basarisiz)

if __name__ == '__main__':
    sys.exit(1 if calistir() else 0)
