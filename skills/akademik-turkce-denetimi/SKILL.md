---
name: "akademik-turkce-denetimi"
description: "Akademik Türkçe metni dil bakımından denetler: söz dizimi, anlatım bozuklukları, YZ imzaları, yazım ve terim tutarlılığı. Ders notu, sınav sorusu, sevk notu veya çeviri çıktısı denetlenecekse kullan."
---

Bu skill, bitmiş bir Türkçe akademik metni **yalnızca dil bakımından** denetler. Bilimsel içeriğe dokunmaz. Dört kural grubu vardır: **A** söz dizimi, **B** anlatım bozuklukları, **C** yapay zekâ imzaları, **D** yazım ve noktalama. Her düzeltme kodla bildirilir.

**Kuralların tek kaynağı bu dosyadır.** Aynı kural kümesinin ikinci bir nüshası tutulmaz; yeni karar buraya yazılır. Alan sözlüğünün varsayılanı `dis-hekimligi-ceviri-tr` §6.3'tedir; bu dosya kurum kararlarını (§10.1) ve denetim sırasındaki tutarlılık taramasını tutar.

---

## 1. Ne zaman kullanılır

- Ders notu metni yazıldıktan sonra, PDF üretilmeden önce.
- `dis-hekimligi-ceviri-tr` ile çeviri bittikten sonra, zincirin ikinci halkası olarak.
- Sınav sorusu, sevk notu, hasta bilgilendirme metni, kurul yazısı denetlenecekse.
- Kullanıcı "dil denetimi", "redaksiyon", "türkçeleştirme" istediğinde.

## 2. Nasıl koşulur — bu bölüm atlanamaz

**Denetim, metni yazan geçişten ayrı koşar.** Kendi yazdığı metni aynı geçişte denetleyen model kendi kalıplarını görmez; bu, denetimin tek yapısal kuralıdır.

- Metni sen yazdıysan denetimi **temiz bağlamda ayrı bir alt görevde** çalıştır: alt göreve yalnız metni ve bu skill'i ver, yazma gerekçelerini verme.
- Kaynak İngilizce metin varsa denetim ona **bakmaz**; `dis-hekimligi-ceviri-tr`'den gelen `[ÇN]` çeviri notları da verilmez — denetimin kararını etkilememelidir. Anlam denetimi bu geçişin işi değil; şüphe `[KONTROL]` olarak bildirilir.
- Dört geçişle çalış, geçişleri karıştırma: (1) tanı ve sayım — yazma yok, (2) söz dizimini yeniden kur (A), (3) anlatım bozuklukları ve YZ imzaları (B, C), (4) yazım, noktalama, ritim (D + §9).

## 3. Yetki sınırları

**Yetkin var:** cümle bölmek, birleştirmek, öğe sırasını değiştirmek, çatıyı değiştirmek, ortaç öbeğini yükleme çevirmek, bağlaç değiştirmek veya atmak, dolgu silmek, paragraf içinde cümle sırasını düzeltmek.

**Dokunmayacaklar:**

1. **Bilimsel içerik.** Önerme eklenmez, çıkarılmaz, genişletilmez, daraltılmaz. Somut örnek, sayı, tarih, kaynak **eklenmez** — eksikliği fark edilirse `[KONTROL]`.
2. **Sayı, doz, oran, birim, istatistik, güven aralığı.** Yalnız yazım kuralı düzeltilir, değer düzeltilmez.
3. **Kip ve kesinlik derecesi.** "olabilir" → "olur" yapılamaz; "ile ilişkilidir" → "neden olur" yapılamaz; "düşündürmektedir" → "göstermektedir" yapılamaz; "tercih edilir" → "yapılır" yapılamaz. **Bu, denetimin en sık ve en ağır hatasıdır**; her yeniden kurulan cümlede ayrıca kontrol et.
4. **Mutlaklık üretilmez.** Akıcılık uğruna *her zaman, kesinlikle, tamamen, hiçbir zaman, tüm hastalarda, ortadan kaldırır, garanti eder* yazılmaz. Sağlıkla ilgili bir cümle sonuç vaadine çevrilmez.
5. **Olumsuzluk ve niceleyiciler.** *çoğu, bazı, nadiren, en az, yalnızca, değil* — bölme sırasında en sık kaybedilenler; her bölmeden sonra doğrula (B8).
6. **Terimler.** §10'daki sözlükte karşılığı olmayan bir terim değiştirilmez; yalnız *tutarsızlık* düzeltilir. Bir terimin bağlama yanlış oturduğunu düşünüyorsan değiştirme, `[KONTROL]` aç.
7. **Atıflar, yazar adları, yıllar, kaynak numaraları, Latince tür adları, gen/protein adları.**
8. **Yapı.** Başlık düzeyleri, liste öğelerinin sayısı ve sırası, tablo/şekil başlıkları korunur. Liste öğesinin *içi* yeniden yazılabilir.
9. **Kişi.** Edilgen yapı birinci kişiye çevrilmez ("Analizler yapıldı" → "Analizleri yaptık" **yasak**). Akademik-kurumsal kayıtta şahıs zamiri kullanılmaz; metinde varsa çıkarılır.

**Emin olmadığın yer:** cümleyi olduğu gibi bırak ve `[KONTROL]` aç. Anlam riskini almak, çeviri kokusuna katlanmaktan kötüdür.

**Kurum kararı, genel kuralın üstündedir.** Bu skill'in genel kuralıyla kurumun kararı çelişirse **kurum kararı geçerlidir**. Kurum kararları bu dosyanın içinde iki yerde toplanır: terim biçimleri **§10.1**'de, başlık düzeni **D1**'in altındaki istisnada. Başka bir yerde kural nüshası aranmaz. Bu satırlar tartışmaya açılmaz ve "genel kural böyle" gerekçesiyle bozulmaz.

## 4. Kayıt sınırı — akademik kaydı bozma

Bu, denetimin en kolay yanlış uygulanan bölümü. Akademik Türkçe bazı kalıpları **kasıtlı kayıt işareti** olarak kullanır. Bunlar A grubunda geçse de **tek başına hata değildir**:

- Nesnel ve edilgen yapılar: *gösterilmiştir, bildirilmiştir, uygulanır*
- Okuru yönlendiren nominal ifadeler: *bu tablonun değerlendirilmesi, göz önünde bulundurulmalıdır, unutulmamalıdır*
- Çerçeveleyen giriş cümleleri: *Bu bölümün temel sorusu şudur: …*
- Yerleşik kalıplar: *istatistiksel olarak anlamlı, hizmet sunmak, savunma hattını oluşturmak, olanak sağlamak*

**Kural:** Bu kalıplar korunur; denetim **yoğunluğu** sayar. Hedef sıfırlamak değil, §9'daki eşiğe indirmek. "Edilgeni etkene çevir" genel öğüdü bu metinlerde olduğu gibi uygulanmaz: yalnız **yığılma** (bir cümlede iki–üç edilgen) ve **"tarafından"** çözülür.

**Buna karşılık şunlar kayıt işareti değil, dolgudur ve silinir:** *belirtmek gerekir ki, şunu belirtmek önemlidir ki, şu da unutulmamalıdır ki, bu bağlamda, bu noktada, bu çerçevede, göz önünde bulundurulduğunda, ile ilgili olarak, -nın önemi vurgulanmaktadır.*

---

## 5. GRUP A — Söz dizimi

**A1 — Tamlama zinciri.** En çok iki ardışık `-in`; üçüncüden itibaren adlaştırmayı fiile çevir.
✗ *ilerlemesinin engellenmesinin önemi vurgulanmaktadır* → ✓ *ilerlemesini engellemek önemlidir*

**A2 — Ortaç yığını.** Addan önce en çok bir sıfat-fiil öbeği; ikincisi yükleme çevrilir.
✗ *aynı bölgeleri tutan ve 2018 öncesinde lokalize agresif periodontitis olarak adlandırılan tablo* → ✓ *…adlandırılan tabloyla karışabilir; o tablo da aynı bölgeleri tutar*

**A3 — Adlaştırma şişkinliği.** Bir cümlede en çok iki `-me/-ma`, `-iş`, `-mek` öbeği.
✗ *kemik kaybının artması yalnızca yıkımın hızlanmasından değil, onarımın yetersizleşmesinden kaynaklanır* → ✓ *kemik kaybı yalnızca yıkım hızlandığı için değil, onarım da yetersizleştiği için artar*

**A4 — Eksiz ad yığını.** İngilizce dizilimden gelen ekli olmayan ad zinciri iyelik veya ilgeçli öbeğe çevrilir.
✗ *artmış sondlamada kanama* → ✓ *sondlamada kanama artışı* · ✗ *periodontal doku yıkım mekanizması* → ✓ *periodontal dokulardaki yıkımın mekanizması*

**A5 — İthal yan cümle.** İlgi cümlesi `-DIK / -AcAK / -mA` ile kurulur, `ki` ile kurulmaz. *Which/who* ile bağlanan uzun İngilizce cümleler gerekirse iki Türkçe cümleye bölünür.
✗ *Gösterildi ki cep derinliği azalmıştır* → ✓ *Cep derinliğinin azaldığı gösterilmiştir*

**A6 — `-mektedir` yoğunluğu.** Paragraf başına en çok bir. Fail biliniyorsa etken kur: *gösterilmiştir* → *çalışmalar göstermiştir*. Ardışık iki cümle aynı yüklem ekiyle bitmez.

**A7 — `sahip olmak`.** İyelik veya sıfatla kurulur.
✗ *aynı miktarda biyofilme sahip hasta* → ✓ *biyofilm miktarı aynı olan hasta* · ✗ *yüksek riske sahip hastalar* → ✓ *riski yüksek hastalar*

**A8 — Boş yardımcı fiiller.** `gerçekleştirmek`, `teşkil etmek`, `işlem yapmak` evrensel karşılık olarak kullanılmaz. §4'ün yerleşik kullanımları saklıdır.
✗ *drenaj gerçekleştirildi* → ✓ *drenaj yapıldı* · ✗ *risk faktörünü teşkil eder* → ✓ *risk faktörüdür*

**A9 — Boş yüklemler.** `bulunmaktadır`, `yer almaktadır`, `mevcuttur`, `-nın varlığı`.
✗ *bozulmuş glukoz toleransı bulunmaktadır* → ✓ *glukoz toleransı bozulmuştur* · ✗ *komplikasyonların varlığı* → ✓ *komplikasyonlar*

**A10 — Eş dizimlilik.** Sözcükler tek tek doğru, birlikte yanlış.
✗ *cep oluşturmak* (hastalık için) → ✓ *cep gelişmek* · ✗ *hastalık geliştirmek* → ✓ *hastalığa yakalanmak* · ✗ *enflamasyon meydana getirmek* → ✓ *enflamasyona yol açmak*

**A11 — Ettirgen yığını.** ✗ *analiz ettirilip raporlattırılmıştır* → ✓ *analiz edilmiş, raporlanmıştır*

**A12 — Artikel kalıntısı `bir`.** İngilizce *a/an*'dan gelen gereksiz "bir" silinir; kalanda yer kuralı **sıfat + bir + ad**.
✗ *Periodontitis bir kronik enflamatuar hastalıktır* → ✓ *Periodontitis, kronik enflamatuar bir hastalıktır*

**A13 — Bağlaç tekdüzeliği.** Aynı bağlaç iki ardışık cümle başında gelmez. Mümkünse bağlacı at, ilişkiyi ekle kur (`-ken`, `-dığı için`, `-dıkça`, `-masına karşın`).

**A14 — Cümle uzunluğu.** Hedef ortalama 15–22 sözcük; 30'u aşan cümle bölünür. Bir cümlede en çok bir yan cümle + bir ortaç öbeği.

**A15 — Odak dizilişi.** Vurgulanan öğe yüklemin hemen önünde. Eski bilgi başta, yeni bilgi sonda.
✗ *Ataşman kaybına neden olan şey enflamasyondur* → ✓ *Ataşman kaybına enflamasyon neden olur*

**A16 — Evrensel bağlayıcı şişkinliği.** `olarak`, `üzerinden`, `noktasında`, `açısından`.
✗ *genel olarak* → ✓ *genellikle* · ✗ *hijyen noktasında önlem alınır* → ✓ *hijyen önlemleri alınır* · ✗ *önemli bir rol oynamaktadır* → ✓ *belirleyicidir*

**A17 — "tarafından" istilası.** İngilizce *by* edatının tembel çevirisidir. Eylem doğrudan özneye bağlanır; edilgen korunacaksa "tarafından" yine atılır.
✗ *Kurul tarafından onaylandı* → ✓ *Kurul onayladı* · ✗ *hekim tarafından değerlendirilir* → ✓ *hekim değerlendirir*
Kurumsal fail bildiriminde (kapak bildirimi, kaynak beyanı) yerleşik kullanım saklıdır.

**A18 — Motamot kalıp çevirisi.** İngilizce deyim ve kalıp sözler sözcüğü sözcüğüne çevrilmez; Türkçedeki kavramsal karşılığı bulunur. Karşılığını bulamıyorsan değiştirme, `[KONTROL]` aç.
✗ *altın standart olarak hizmet eder* → ✓ *altın standarttır* · ✗ *bu, buzdağının görünen kısmıdır* → mekanizmayı düz cümleyle söyle

**A19 — Ölçülülük şişmesi.** *may / can / could* her seferinde "-ebilir" olarak çevrilirse kesin bilgi belirsizleşir. Bir cümlede iki "-ebilir" varsa biri kaldırılır. **Ancak kaynağın kendi ölçülülüğü korunur** (§3/3); emin değilsen `[KONTROL]`.

**A20 — Zamir fazlalığı ve belirsiz `kendi`.** Türkçe kişiyi ve iyeliği ekle gösterir; İngilizceden gelen özne ve iyelik zamirleri silinir. `kendi` ve iyelik zinciri kimi gösterdiği belirsizse sahibi adlandırılır. (Şahıs zamiri yasağı §3/9'da; bu madde üçüncü kişi zamirlerinin yığılmasıyla ilgilidir.)
✗ *Hastalar, onların ağız hijyeni alışkanlıkları açısından değerlendirildi* → ✓ *Hastalar ağız hijyeni alışkanlıklarına göre değerlendirildi*
✗ *Her hekim kendi hastasının kendi protokolünü uygular* → ✓ *Her hekim, hastası için belirlediği protokolü uygular*

**A21 — Paragrafın kip çerçevesi.** Bir paragraf tek kip çerçevesinde yazılır; yüklemler cümle cümle değişmez. Araştırma bulgusu → *-mıştır / -mışlardır* baştan sona · genel bilgi, tanım, mekanizma → geniş zaman · başka bölüme gönderme → *ele alınmıştır*, bu bölüme → *değinilmektedir* · öneri → *-malıdır*. *-mıştı* akademik düzyazıda kullanılmaz; bulgu aktaran paragrafta cümle sonunda yalın *-dı* kullanılmaz. Tanı geçişinde her paragrafın yalnız yüklemlerini sırayla oku: kip değişiyorsa bir nedeni olmalı (bulgudan yoruma, yorumdan öneriye geçiş); yoksa çerçeveye çek. Bu madde **zaman ekini** düzeltir, **kipliği değil**: *-ebilir*, *-malıdır*, *düşündürmektedir* gibi kesinlik işaretlerine dokunulmaz (§3/3).
✗ *Çalışmanın amacı analiz etmekti … makaleler analiz edildi … sayı artış gösterdi … ulaşmıştır* → ✓ *Çalışmanın amacı … analiz etmektir … analiz edilmiştir … artış göstermiştir … ulaşmıştır*
*Kanıt: projenin en sağlam bulgusu (29 Eylül 2026). Aynı metnin üç tekrarında -dı'lı cümle sonu bu kuralla 0, kuralsız 5, 5, 2; üç dış değerlendirici de bu farkı kör okumada ayırt etti.*

---

## 6. GRUP B — Anlatım bozuklukları

**B1 — Özne–yüklem uyuşmazlığı.** Cansız çoğul özne tekil yüklem alır.
✗ *Bulgular … göstermektedirler* → ✓ *göstermektedir*

**B2 — Çatı uyuşmazlığı.** Geçişli ve geçişsiz fiiller aynı yükleme ortak bağlanmaz.
✗ *Hastaya bilgi verildi ve onayladı* → ✓ *Hastaya bilgi verildi ve hasta onayladı*

**B3 — Öge eksikliği.** Eksik nesne veya dolaylı tümleç. Adlaştırılmış özne yükleme uymuyorsa özne gerçek olana çevrilir.
✗ *Yönlendirmenin sözlü bir öneriyle sınırlı kalması, sonuçsuz kalır* → ✓ *Sözlü bir öneriyle sınırlı kalan yönlendirme, sonuçsuz kalır*

**B4 — Gereksiz sözcük.** ✗ *en ideal, ilk önce, geri iade, karşılıklı olarak birbirini*
Pleonazm: ✗ *lökosit hücreleri* → ✓ *lökositler* · ✗ *fibrin doku* → ✓ *fibrin*
Eş anlamlı çiftleme: ✗ *Tek başına (monoterapi olarak)* → ✓ *Monoterapi olarak*

**B5 — Ortak öge yanlışı.** Bir tamlayan veya ek bağlanan öğelerin hepsine uymuyorsa ayrıştırılır. Liste öğeleri aynı kalıpta kurulur.
✗ *periodontal ve implant hastalıkları* → ✓ *periodontal hastalıklar ve implant çevresi hastalıkları*

**B6 — Fiil yönetimi.** *neden olmak, yol açmak, katkıda bulunmak, eşlik etmek, etki etmek, dayanmak, bağlı olmak* → **-e** · *etkilemek, tetiklemek, baskılamak, kapsamak* → **-i** · *ilişkili olmak, birlikte görülmek* → **ile**
✗ *dokuları etki eder* → ✓ *dokuları etkiler* · ✗ *kaybını neden olur* → ✓ *kaybına neden olur*

**B7 — Anlamca çelişen sözcükler.** ✗ *kesinlikle muhtemelen, yaklaşık 12,4 mm, tüm hastalarda bazen*

**B8 — Niceleyici ve belirteç yeri.** `yalnızca`, `sadece`, `bile`, `en` nitelediği öğenin hemen önünde. Yeri değişince anlam değişir; bölme sırasında en sık kaybedilen şey budur.
*"Yalnızca sondlama derinliği ölçüldü" ≠ "Sondlama derinliği yalnızca ölçüldü"*

**B9 — Noktalamadan doğan belirsizlik.** *"Genç, hekim hastayı muayene etti" ≠ "Genç hekim, hastayı muayene etti"*

**B10 — Mantık ve kapsam hatası.** Neden–sonuç tersliği, alt kümenin üst kümeyle aynı düzeyde sıralanması.
✗ *periodontitis, gingivitis ve periodontal hastalıklar* → kapsam hatası; düzeltmesi anlam değişikliğiyse `[KONTROL]`

**B11 — Anlam yinelemesi.** İki cümle aynı bilgiyi farklı sözcüklerle söylüyorsa biri kalır. Yazımı değil **anlamı** karşılaştır.

**B12 — Bağdaşıklık ve mantıksal örgü.** Paragraf tek bir önerme taşır; cümleler eski bilgiden yeni bilgiye doğru dizilir. Bir cümle önceki cümleye bağlanmıyorsa ya sırası düzeltilir ya ilişki ekle kurulur. Altı cümleyi aşan paragraf bölünür. **Bağlaç eklemek yerine sırayı düzelt**; yeni cümle yazılmaz.

---

## 7. GRUP C — Yapay zekâ imzaları

**C1 — "Sadece X değil, aynı zamanda Y".** Gerçek bir yanlış anlamayı düzeltmiyorsa düz cümleye çevrilir. Düzeltiyorsa **korunur**; yalnız adlaştırma yükü kaldırılır.

**C2 — Boş değer sıfatları.** *kritik, hayati, eşsiz, benzersiz, çok boyutlu, son derece, devrim niteliğinde.* Paragraf başına en çok bir; kanıtı olmayan yüceltme silinir.

**C3 — Paragraf sonu boş değerlendirme.** Son cümle yeni bilgi taşımıyorsa silinir. ✗ *Bu nedenle konunun önemi büyüktür.*

**C4 — Bürokratik bağlaç zinciri.** *bu bağlamda, söz konusu, öte yandan, bunun yanı sıra, bu doğrultuda* — metinde en çok iki.

**C5 — Zorlama üçlü listeler.** Üç öğe simetri için dizilmiş ve aralarında gerçek ayrım yoksa gerçek sayıya indirilir. **Bilimsel sınıflandırma ise dokunulmaz.**

**C6 — `adeta` / `sanki` bağımlılığı.** Somut mekanizma yerine belirsiz benzetme. Benzetme silinir; yerine **örnek eklenmez**.

**C7 — Somut çapa eksikliği.** Soyut iddia hiçbir sayı, bulgu veya mekanizmaya bağlanmadan duruyorsa iddia olduğu gibi bırakılır ve `[KONTROL]` açılır. **Sayı veya örnek uydurmak yasaktır.**

**C8 — Kayıt kayması.** Aynı paragraf teknik-akademik tondan edebî veya duygusal tona kayıyorsa tek kayda çekilir. Bu metinlerin kaydı **akademik-kurumsaldır**; kaydı yükselten süsleme de, düşüren konuşma dili de çıkarılır. §4'teki kayıt işaretleri kayma sayılmaz — onlar bu kaydın kendisidir.

> **Kabul edilmeyen çözüm:** Bazı "insanlaştırma" yöntemleri ritim için 1–3 sözcüklük cümleler, retorik sorular, konuşma dili bağlaçları ve kişisel araya girmeler eklemeyi önerir. **Akademik-kurumsal kayıtta bunlar uygulanmaz.** Ritim §9'daki uzunluk çeşitliliğiyle sağlanır; metne dışarıdan cümle eklenmez.

---

## 8. GRUP D — Yazım, noktalama, başlık

**D1 — Başlıkta büyük harf.** Ana başlıkta (kitap, bölüm adı) **bütün** sözcüklerin ilk harfi büyük. Genel kural olarak alt başlıkta yalnız ilk sözcüğün ilk harfi büyüktür. Soru biçimindeki başlık soru işareti alır.
✓ *2 Diyabetin Ağız ve Periodonsiyuma Etkisi* · ✓ *1.3 HbA₁c neyi ölçer?*

> **Kurum istisnası — periodontoloji ders notları.** Bu notlarda numaralı alt başlıklar da **Title Case** dizilir (*2.3 Metabolik Kontrolün Belirleyiciliği*); görsel kimliğin parçasıdır ve üretilmiş bütün notlarda böyledir. Bağlaçlar küçük kalır (ve, ile, veya). **Bölüm açıcısında noktalarla ayrılan her ifadenin ilk harfi büyüktür** (*Akut periodontal durum nedir · Terminoloji köprüsü · Üç adımlı yaklaşım*); Türkçe büyük harf dönüşümünde `i → İ`, `ı → I`.
> Bu istisna, genel kural gerekçesiyle "düzeltilmez". Alt başlıkları cümle düzenine indirmek bu notlarda **hatadır**.

**D2 — Hastalık adları küçük.** periodontitis, gingivitis, diyabet, periimplantitis. Gönderme adları büyük: Şekil 1, Tablo 2, Bölüm 3. Latince: *Porphyromonas gingivalis* — cins büyük, tür küçük, ikisi italik. Hastalık adı (diabetes mellitus) italik değildir.

**D3 — Sayı, birim, yüzde.** Ondalık **virgül** (3,5 mm · p < 0,05) · binlik **nokta** (1.250) · yüzde işareti **önde ve yapışık** (%25) · sayı–birim arası boşluklu (3 mm, 37 °C) · birim kısaltmasına nokta konmaz (mm, mL) · sıra sayısı noktalı (3. sınıf).

**D4 — Aralık çizgisi.** Kurum kuralı: **en dash (–)**, boşluksuz — %5–10, 2–3 ay, 20–79 yaş, 0,25–1,0. TDK kısa çizgi ister; notlarda en dash yerleşiktir ve **tutarlı** kullanılır. İkisi karıştırılmaz.

**D5 — Noktalama.** "ve"den önce virgül konmaz. Cümle başı `Ancak`, `Ayrıca`, `Bununla birlikte` sonrası virgül genellikle konmaz. **Uzun çizge (—)** Türkçede konuşma çizgisidir; ara söz virgül veya parantezle verilir. **Noktalı virgül** "iki fikri bağlamak" için kullanılmaz. Uzun cümlede özne yanlış okunuyorsa özneden sonra virgül: *Periodontitis, çok etkenli bir hastalıktır.*

> **Geçiş kuralı.** Uzun çizgeli ara söz, yeni yazılan metinlerde virgül veya parantezle kurulur. Daha önce üretilmiş notlardaki yerleşik kullanım geriye dönük düzeltilmez; yeni metinde yinelenmemesi yeterlidir.

**D6 — `de/da` ve `ki` ayrı yazımı.** Bağlaç ayrı, ek birleşik. Ölçüt: çıkarıldığında cümle bozulmuyorsa bağlaçtır. *Hasta da geldi* (bağlaç) ≠ *Hastada bulgu yok* (ek).

**D7 — Ünlü düşmesi ve yumuşama.** ağız→**ağzı**, burun→**burnu**, omuz→**omzu**, göğüs→**göğsü**. flep→**flebi**, uç→**ucu**, kanat→**kanadı**. Yumuşamayanlar: greft→**grefti**, implant→**implantı**.

**D8 — Kısaltma, sayı ve göndermede ek.** Ek okunuşa göre seçilir, kısaltmaya kesme ile eklenir: pH'**ın**, HbA₁c'**nin**, DNA'**nın**, IL-6'**nın**, TNF-α'**nın**, RANKL'**ın**, CAL'**e**, mm'**ye**. Yerleşik yazımlı terimde kesme yok: biyofilm**in**, prob**un**, küret**in**. **Her kısaltma ilk geçişte açılır.**
Şekil ve tablo göndermeleri: Şekil 1'**de** · 2'**de** · 3'**te** · 4'**te** · 5'**te** · 6'**da** · 7'**de** · 8'**de** · 9'**da** · 10'**da** · 11'**de** · 12'**de** · 13'**te**. Numara değiştiğinde gövdedeki ek de değişir; numaralandırma sonrası en sık atlanan adımdır.

**D9 — İkileme ve pekiştirme.** İkilemeler ayrı ve çizgisiz: yavaş yavaş, tek tek. Pekiştirmeler birleşik: bembeyaz.

**D10 — Ayrı ve bitişik yazım.** diş eti · yan etki · diş taşı · göz önünde · her şey · bir arada · hiçbir · birçok · şu anda · ön koşul. Şüphede TDK Güncel Türkçe Sözlük esastır.

**D11 — Düzeltme işareti.** Yalnız **anlam ayırt ediyorsa** kullanılır: *kâr / kar*, *âlem / alem*, *hâlâ / hala*, *hâl*. Süs olarak eklenmez ve yerleşik yazıma karışılmaz — kurum kararı **şikayet** (§10.1), *şikâyet* değil. Alan terimlerinde TDK ile alanda yerleşik yazım çatışıyorsa yerleşik olan kalır ve `[KONTROL]` açılır.

---

## 9. Ölçülebilir eşikler

Tanı geçişinde **sayarak** kontrol et; çıktıda sayıları bildir.

| Ölçüt | Eşik |
|---|---|
| Ortalama cümle uzunluğu | 15–22 sözcük |
| En uzun cümle | ≤ 30 sözcük |
| Cümle uzunluğu çeşitliliği | standart sapma ≥ ortalamanın %25'i |
| `-mektedir / -maktadır` | paragraf başına ≤ 1 |
| Bulgu aktaran paragrafta cümle sonu yalın *-dı* / *-mıştı* (A21) | 0 |
| Aynı yüklem ekiyle biten ardışık cümle | ≤ 2 |
| Aynı sözcükle başlayan ardışık cümle | ≤ 2 |
| Ardışık `-in` tamlaması | ≤ 2 |
| Ad önündeki ortaç öbeği | ≤ 1 |
| Bir cümlede adlaştırma | ≤ 2 |
| Bir cümlede edilgen | ≤ 1 |
| "tarafından" (A17) | metinde ≤ 1 |
| Boş değer sıfatı (C2) | paragraf başına ≤ 1 |
| Bürokratik bağlaç (C4) | metinde ≤ 2 |
| Paragraf uzunluğu | ≤ 6 cümle |

**Tekdüzelik alarmı, cümle eklemekle değil**, var olan cümleleri bölüp birleştirmekle giderilir.

**Uyarı:** İki sütunlu PDF'ten çıkarılan metinde tablo ve şekil içerikleri düzyazıya yapışır; otomatik sayımlar bu durumda yalnız gösterge niteliğindedir. Uzun cümleleri tek tek doğrula.

---

## 10. Kurum terim sözlüğü

Bir kavram = bir terim. Metni bitirince sözlükteki her satırın karşı biçimini **arayarak** tara.

### 10.1 Kurum kararıyla sabitlenmiş biçimler

Bu satırlar kurum kararıdır ve genel dil tercihinin üstündedir; tartışmaya açılmaz.

| Kullan | Kullanma |
|---|---|
| sondlama · sondlamada kanama artışı | sondalama · artmış sondlamada kanama |
| subgingival enstrümantasyon | küretaj, SRP |
| tedavisi (*management* karşılığı) | yönetimi — *"yönetim" yalnız hastalık dışı bağlamda: antibiyotik yönetişimi* |
| kanıt kesinliği | kanıt düzeyi |
| şiddetli | ciddi (*severe* karşılığı olarak) |
| enflamasyon · enflamatuar | inflamasyon, enflamatuvar |
| diş eti · yan etki · risk faktörü | dişeti, yanetki |
| şikayet | şikâyet |
| suprakrestal doku ataşmanı | biyolojik genişlik, *biologic width* |
| halitozis | fetor oris, "fetor oris / halitozis" ikilisi |
| viral yük | viral titre |
| stabil flora | sabit flora |
| tip 1 / tip 2 diabetes mellitus | IDDM, NIDDM, "diyabetes" |
| MRONJ | BRONJ, ARONJ |

### 10.1b Tercih biçimleri — ders notlarında zorunlu (kurum kararı, 30 Eylül 2026)

Aşağıdakiler `dis-hekimligi-ceviri-tr` §6.3'teki alan uzmanı kararlarıdır (★). Sağ sütundaki biçimler çeviride **kabul** düzeyindedir, hata değildir; ancak **periodontoloji ders notlarında sol sütun yazılır** ve metin içinde tek biçim korunur. Denetim sağ sütunu görürse **TERCİH** olarak bildirir. Daha önce üretilmiş notlar geriye dönük düzeltilmez.

| Yazılır | Kabul (tercih değil) |
|---|---|
| teşhis — *differential diagnosis* = **ayırıcı tanı** (sabit terim) | tanı |
| konak cevabı · immün cevap · cevap | yanıt |
| ataşman seviyesi · klinik ataşman seviyesi (CAL) | ataşman düzeyi |
| yaygın (*generalized*) · lokalize | jeneralize, generalize *(bunlar kabul değil, yazılmaz)* |
| çizgisel gingival eritem | lineer gingival eritem |
| modifiye edici faktör · düzenleyici faktör | değiştiren faktör *(yazılmaz)* |
| kuron | kron *(yazılmaz)* |

### 10.2 Tekleştirilmiş biçimler

| Kullan | Kullanma |
|---|---|
| diş taşı | diştaşı, diş talı |
| hidropik dejenerasyon | hidrofik dejenerasyon |
| glikasyon (süreç) · ileri glikasyon son ürünleri (AGE) | glikozilasyon |
| yineleyen periodontal apse (sıklık vurgusu: sık yineleyen) | tekrarlayan, kısa aralıklarla yineleyen |
| risk faktörü (risk bağlamında hep bu) | etken, değişken — *"etken" yalnız biyofilm için: "zorunlu etken"* |
| prevalans — ilk geçişte "prevalans (ortaya çıkma sıklığı)" | "prevalans (yaygınlık)" — *yaygınlık / yayılım* = *extent*; ikisi karıştırılmaz |
| erişkin (payda 20–79 yaş ise) | kişi |
| idame tedavisi · kontrol randevusu | bakım, geri çağırma |
| ataşman · biyofilm · greft · flep · mikrobiyota · rejenerasyon · subgingival · supragingival · konak | — |
| Afrika kökenli Amerikalılar | Afrikan-Amerikan, siyah |

### 10.3 2018 sınıflaması

| Güncel | Eski |
|---|---|
| NG — nekrotizan gingivitis | ANUG, NUG |
| NP — nekrotizan periodontitis | NUP |
| NS · üst başlık: NPH | — |
| Periodontitis + evre (I–IV) / derece (A–C) | kronik / agresif periodontitis |

Tarihsel çalışma aktarılırken **çalışmanın kendi terimi korunur**; genel ifadelerde güncel terim kullanılır.

### 10.4 Yanlış anlam şüphesi — `[KONTROL]` aç, değiştirme

Bu sözcükler İngilizceden gelen yanlış anlam seçimi olabilir. Denetim kaynak metne bakmadığı için karar veremez; yalnız işaretler. (*management* ve *severe* §10.1'de karara bağlanmıştır.)

*anlamlı / önemli* (significant → istatistikte anlamlı, klinikte belirgin?) · *katılım* (involvement → tutulum?) · *çıktı* (outcome → sonuç?) · *başarısızlık* (failure → kayıp?) · *çağrışım* (association → ilişki?) · *uyumluluk* (compliance → hasta uyumu?) · *koşul* (condition → durum/hastalık?) · *seyir* (course → klinik gidiş; "izlenim" ile karıştırılmaz) · *işaret eder* metinde üç ve daha çok (indicate → gösterir, suggest → düşündürür?)

> **Tam tuzak tablosu** (kaynak dilden seçim kararları) `dis-hekimligi-ceviri-tr` §6.4'tedir. Anlam seçimi orada, kaynak metin eldeyken yapılır; burada yalnız şüphe işaretlenir. Bir tuzak yeni karara bağlanırsa karar §10.1'e yazılır, iki dosyaya dağıtılmaz.

---

## 11. Çıktı biçimi

```
## TESPİT RAPORU
Ortalama cümle uzunluğu: __ | En uzun: __ | Çeşitlilik: __%
-mektedir/-maktadır: __ (paragraf başına __) | tarafından: __
A kodları: A1 (c.1, c.4), A7 (c.12) …
B kodları: B3 (c.7) …
C kodları: C1 (c.9), C3 (c.5) …
D kodları: D8 (c.3) …
Terim taraması: __ tutarsızlık · __ tercih (§10.1b)

## KARŞILAŞTIRMALI DÜZELTMELER
| # | Yer | Kod | Önce | Sonra | Gerekçe |

## DÜZENLENMİŞ METİN
<yalnız son hâl; işaret veya yorum yok>

## KONTROL GEREKTİREN YERLER
[KONTROL-1] <yeniden kurulmadı veya anlam riski doğdu>
(yoksa: yok)

## ÖNCELİK SIRASI
1. <gerçek dilbilgisi hatası>  2. <yazım hatası>  3. <sistematik sorun>  …
```

Ders notu denetiminde **düzenlenmiş metni tek parça vermek yerine** karşılaştırmalı düzeltme tablosunu ver; kullanıcı onayladıktan sonra düzeltmeler metne tek tek işlenir.

## 12. Yasaklar

- Girdide olmayan bilgi, örnek, sayı, geçiş cümlesi veya ritim cümlesi eklemek.
- Metni sadeleştirmek, kısaltmak, öğrenci diline çekmek (istenmedikçe).
- Kiplik veya kesinlik derecesini güçlendirmek/zayıflatmak; mutlaklık üretmek.
- Edilgeni birinci kişiye çevirmek; metne şahıs zamiri sokmak.
- §10'da olmayan bir terim için yeni Türkçe karşılık türetmek.
- §4'teki yerleşik akademik kullanımı kural uğruna sıfırlamak.
- §10.1'deki terim kararını veya D1'deki başlık istisnasını genel dil kuralı gerekçesiyle bozmak.
- Tespit raporunu veya düzeltme tablosunu atlayıp "genel düzeltmeler yapıldı" demek.
- Emin olmadığı yeri sessizce değiştirmek — `[KONTROL]` açmadan risk alınmaz.