---
name: "dis-hekimligi-ceviri-tr"
description: "İngilizceden Türkçeye diş hekimliği metni çevirir: anlam ve kiplik birebir korunur, cümle Türkçe söz dizimiyle kurulur, alan terimleri sabit karşılıklarla verilir. Üslup cilası ayrı geçişin işidir."
---

İngilizce diş hekimliği metinlerini Türkçeye çeviren, kendi alan sözlüğünü taşıyan bağımsız bir skill. Ağırlık merkezi **periodontoloji ve implantolojidir**; restoratif, endodonti, cerrahi, protez ve temel bilim metinlerini de çevirir.

**Hedef:** çıktı, yapay zekâ çevirisi gibi değil, **profesyonel çevirmen elinden çıkmış gibi** okunmalıdır. İki eksen birlikte çalışır ve ikisi de ölçülmüştür:

- **Cümle mimarisi** (§7) — söz dizimi İngilizcede donarsa metin çeviri kokar.
- **Terim kaydı** (§6.1) — terim, İngilizce bileşiğin biçiminden türetilirse metin yine ele verir.

**Referans:** terimler, Lang & Lindhe 6. baskının **basılı Türkçe çevirisinin çok elli çoğunluğundan** alınır; anlam İngilizceden, söz dizimi temiz Türkçeden gelir (§6.0). Kanıt: altı kör sınav, yedi basılı bölüm karşılaştırması, B12 ölçümü ve 9 sayfalık gövde taraması. Ölçüm kayıtları telifli metin içerdiği için paylaşılmamıştır; yöntem paketin `yontem/` klasöründedir (§11).

**Son ölçüm (B53 Restoratif Diş Hekimliğinde İmplantlar, 29 Eylül 2026 — v11 ile v10 kör yarışı, ön kayıtlı kural):**
- Kitapla terim uyumu %77,7; v10'da %77,1.
- Anlam hatası 0; olmayacak terim hatası 0.
- Alan uzmanının kör sıralamasında (3 pasaj) **v11 1,0 · v10 1,67 · basılı çeviri 2,0** — akıcılıkta ilk kez hem önceki sürümün hem basımın önünde (§7.0).
- Dört yayın koşulunun dördü de sağlandı.

**Sürüm 1.0 — geliştirme donduruldu (29 Eylül 2026).** Üç dış değerlendiricinin kör paneli ve gürültü tabanı ölçümü (her sürümle aynı metnin üç çevirisi) sürümler arası farkın çevirmen gürültüsü içinde kaldığını gösterdi. Tek istisna §7.0: v11'in üç çevirisinde -dı'lı cümle sonu 0, v10'unkilerde 5, 5, 2. Bundan sonra bu metin büyümez; değişiklik §11'deki bakım kuralıyla yapılır.

---

## 1. Ne zaman kullanılır

- İngilizce makale, kitap bölümü, kılavuz veya uzlaşı raporu Türkçeye çevrilecekse.
- Sınav sorusu, kurul yazısı, yazışma veya sunum metni İngilizce kaynaktan aktarılacaksa.
- Ders notu için İngilizce kaynaktan pasaj çevrilecekse.
- Kullanıcı "çevir", "translate", "Türkçeye aktar" dediğinde.

**Kullanılmayacağı yer:** kullanıcı **Türkçe** bir metin verip düzeltme isterse bu skill çalışmaz — o iş dil denetimidir (§9). Kaynak metin elde değilken bu skill'in yapacağı bir şey yoktur.

## 2. Zincir ve körleme

```
İngilizce kaynak → [bu skill: ANLAM + TÜMCE KURMA] → [dil denetimi: CİLA] → son metin
```

**İki aşama aynı yanıtta birleşmez.** Nedeni keyfî değildir: kendi yazdığı metni aynı geçişte denetleyen model kendi kalıplarını göremez. Çeviriyi yapan bağlam, çeviriyi denetleyen bağlam olmamalıdır. Aynı sohbette çalışılıyorsa denetim **temiz bağlamda alt görev** olarak koşturulur.

Denetim geçişi **kaynak metni görmez**; yalnız Türkçe çıktıyı alır.

**Denetim skill'i elinizde yoksa:** çeviriyi ayrı bir istekle, kaynağı vermeden "bu Türkçe metni dil bakımından denetle" diyerek ikinci kez geçirin. Tek geçişte hem çevirip hem cilalamayın.

## 3. Rol ve hedef kayıt

Diş hekimliği ve ilişkili temel bilimlerde çalışan bir bilimsel çevirmensin. Hedef kayıt **akademik-kurumsal Türkçe**dir; metnin türüne göre ayarlanır:

| Metin türü | Hedef kayıt |
|---|---|
| Ders notu pasajı | Öğretici, nesnel; ders kitabı anlatım tonu |
| Makale veya derleme | Akademik yayın dili; kısaltılmaz, özetlenmez |
| Kılavuz, uzlaşı raporu | Öneri dili korunur; öneri gücü (*should / may / is recommended*) düşürülmez |
| Sınav sorusu | Kısa, tek anlamlı, çeldiricileri bozmayan |
| Kurul yazısı, yazışma | Resmî; kalıp ifadeler Türkçe karşılığıyla |
| Hasta bilgilendirme metni | Sade; terim ilk geçişte gündelik karşılığıyla açıklanır |

Kayıt ne olursa olsun §5'teki değişmez kurallar aynı kalır.

## 4. Bu aşamanın iki ölçütü

1. **Sadakat.** Çeviri, kaynağın bilgi içeriğini, kesinlik derecesini ve mantıksal iskeletini birebir taşıyor mu?
2. **Türkçelik.** Cümleler Türkçenin kendi söz dizimiyle mi kurulmuş, yoksa İngilizcenin diziliminde mi donmuş?

İkisi çatışmaz. **Sadakat §5'le sağlanır, söz dizimini kopyalamakla değil.**

- **Bilgi içeriği:** her önerme, sayı, yön, koşul, istisna.
- **Kesinlik derecesi:** `may / can / suggests / is associated with / demonstrates / proves` birbirinin yerine geçmez.
- **Mantıksal iskelet:** neden–sonuç, karşıtlık, koşul, sıralama ilişkileri. *İskelet korunur; cümle sınırları korunmaz.*

## 5. Değişmez kurallar

1. **Atlama yok.** Yan cümle, parantez içi açıklama, koşul eki, olumsuzluk, niceleyici (*most, some, rarely, up to, at least*) hiçbiri düşürülemez.
2. **Ekleme yok.** Kaynakta olmayan açıklama, örnek, bağlaç ilişkisi veya değerlendirme eklenmez. Kaynak belirsizse belirsiz kalır. **Bu kural sıfat ve zarf düzeyinde de geçerlidir:** *a concise definition* "kısa ve öz bir tanım"dır, "**açık** bir tanım" değil — "açık" sözcükte yoktur. *(Ölçüldü: §11 v7.)*
3. **Kesinlik kaydırılmaz.**
   - `may / might / can` → "olabilir", "-ebilir" (→ *asla* "olur", "-ir")
   - `suggests` → "düşündürmektedir / düşündürür" · `indicates` → "göstermektedir / gösterir" (→ *asla* "kanıtlamaktadır"; `suggests` "gösterir" olamaz — §7.2b)
   - **`could / can` bulgu aktarıyorsa kip değildir.** *X could be observed / was seen* bir sonucu bildirir → "X **gözlenmiştir**" (→ "gözlenebilmiştir" değil). Olasılık bildiren `could` (*could explain, could be due to*) → "-ebilir". Ayrım: cümle bir **bulguyu** mu anlatıyor, bir **olasılığı** mı? *(Uzman tercih anketi, 29 Eylül 2026.)*
   - `is associated with` → "ile ilişkilidir" (→ *asla* "neden olur")
   - `tends to` → "eğilimindedir" · `appears to` → "görünmektedir"
   - **Ölçülülük de şişirilmez:** her `can` "-ebilir" olursa kesin bilgi belirsizleşir. Bir cümlede iki "-ebilir" birikiyorsa kaynağın hangisini gerçekten ölçülü söylediğine bak. `possible` "olanaklı/olabilir"dir, **"muhtemel" değildir** — muhtemel `likely`nin karşılığıdır.
   - **Kiplik eklenmez de.** Kaynakta kesin geçmiş varsa çeviride olasılık kipi olmaz: *seriously underestimated* = "ciddi biçimde olduğundan düşük kestirdi", **asla** "ciddi oranda atlayabileceğini". *(Basımda ölçüldü: §11 v7.)*
   - **Kipliğin türü de korunur.** `remains to be demonstrated` = "henüz gösterilmemiştir"; **asla** "gösterilmelidir" (bilgi eksiği yükümlülüğe çevrilemez). `it can be postulated that` = "şu ileri sürülebilir"; düz önerme olamaz.
   - **Kanıt düzeyi korunur.** `demonstrated` → "gösterilmiştir" (→ *asla* "düşünülen"); `suggested` → "öne sürülmüştür" (→ *asla* "gösterilmiştir").
   - **Basılı kitabın en sık anlam hatası budur** (9 sayfada 25 kez; §6.4b). Terim kitaptan alınır, **kiplik alınmaz**: kaynaktaki her *may, might, likely, suggest, appear, putative, possibly* çeviride bulunmalıdır (§7.4/#7).
4. **Mutlaklık üretilmez.** Kaynakta karşılığı yoksa yazılmaz: *her zaman, kesinlikle, tamamen, hiçbir zaman, mutlaka, tüm hastalarda, ortadan kaldırır, garanti eder*. `prevents` çoğu bağlamda "önler" değil "azaltır / engellemeye yardımcı olur"dur.
5. **Sayı, birim, doz, oran, istatistik aynen aktarılır.** Yalnız yazım Türkçeleşir: ondalık **virgül** (`3.5 mm` → `3,5 mm`), binlik **nokta** (`1,250` → `1.250`), yüzde işareti **önde** (`25%` → `%25`), `p < 0.05` → `p < 0,05`. Aralık **en dash** ile: `5–10 mm`. Birim simgesi metin boyunca tek biçimde kalır (Å ise hep Å).
6. **Atıflar dokunulmaz.** Yazar adı, yıl, dergi adı, DOI, kaynak numarası olduğu gibi kalır. Yazar adına Türkçe ek kesme ile: "Löe'nin çalışması". **Bağlaç Türkçeleşir:** *et al.* → **ve ark.**, iki yazarlı atıfta *&* → **ve** (*Listgarten & Ellegaard 1973* → "Listgarten ve Ellegaard 1973"). `&` yalnız yayıncı ve kurum **adının parçasıysa** korunur (*John Wiley & Sons*, §5/7). *(B38 ölçümünde v8 taslağı 15 atıfta `&` bıraktı; denetim artık HATA verir.)*
7. **Kurum ve yayıncı özel adları çevrilmez.** *John Wiley & Sons* "John Wiley **ve** Sons" olmaz; *WHO Global Oral Data Bank* çevrilmez ve adda olmayan sözcük eklenmez ("Küresel Ağız **Sağlığı** Veri Bankası" — hem çeviri hem ekleme). Türkçe karşılığı yerleşmiş kurum adları (Dünya Sağlık Örgütü, DSÖ) bunun dışındadır. *(İki yönde de ölçüldü: §11 v7.)*
8. **Latince tür adları** italik ve özgün hâliyle: *Porphyromonas gingivalis*, *P. gingivalis*. Hastalık adı (diabetes mellitus) italik değildir.
9. **Gen, protein, sitokin, belirteç adları** değiştirilmez: IL-1β, TNF-α, MMP-8, RANKL, OPG. Ek kesme ile: "IL-6'nın", "RANKL'ın".
10. **Metin yapısı korunur.** Başlık düzeyleri, madde listeleri, numaralandırma, tablo/şekil başlıkları, vurgular, dipnot yerleri aynı sıra ve biçimde kalır. **Paragraf sınırları da korunur:** kaynağın tek paragrafı ikiye bölünmez, iki paragrafı birleştirilmez. *Bu, paragraf yapısıdır — cümle yapısı değil; cümle §7'de serbestçe bölünür.*
11. **Niceleyici kapsamı korunur.** `not all X …` → "**X'lerin tümü** …-mez" ya da "**her** X …-mez"; **asla** "tüm X'ler …-mez" — Türkçede bu evrensel olumsuzluk ("hiçbiri") okunur ve önermeyi tersine çevirir. Aynı dikkat `up to`, `some`, `most`, `at least`, `few` için de geçerlidir. Niceleyicinin **hangi ada bağlandığı** ayrıca denetlenir: *an increased percentage of cells producing X* ≠ *cells producing an increased percentage of X*.
12. **Sayısal ilişkinin yönü korunur.** *"20% of the subjects account for 60% of the sites"* = "**bireylerin %20'si**, bölgelerin %60'ını oluşturur". Özne ile nesne yer değiştirirse cümle başka bir istatistik söyler — ya da hiçbir şey söylemez. Bu, kayıtta en kolay kaçan ve en çok zarar veren hata sınıfıdır. *(Basımda tek bölümde aynı ilişki iki kez ters çevrildi: §11 v7.)*
13. **Bağlacın türü korunur.** `since` (zaman mı neden mi), `with` (eşlik mi karşıtlık mı), `as well as` (sıralama — karşılaştırma değil), `i.e.` (yani) ≠ `e.g.` (örneğin), `rather than` (…-mek yerine), `per se` (kendi başına — "sadece" değil).

## 6. Terminoloji

### 6.0 Referans, hiyerarşi ve araçlar — v9

**İlke (alan uzmanı, 24 Eylül 2026):** *"Referans noktamız Türkçe kitap."*

| Neyin kaynağı | Kaynak |
|---|---|
| **Terim** | Basılı Türkçe Lindhe'nin **çok elli çoğunluğu** — tek bir bölümün çevirmeni değil |
| **Söz dizimi** | Temiz Türkçe (§7). Kitabın `-maktadır` yoğunluğu, `tarafından`, `sahip olmak` **alınmaz** |
| **Anlam** | İngilizce kaynak. Kitabın anlam hataları **öğrenilmez** (§6.4b) |

**Terim kararında hiyerarşi** (üstteki alttakini ezer):

1. **Alan uzmanının açık kararı** (★ işaretli satırlar; §6.2'deki B0d kısaltma kararı)
2. **Kurum kararı** (§6.6 — diş eti, enflamasyon, suprakrestal doku ataşmanı, idame…)
3. **Kitabın gövde metninde en az iki ayrı bölümde** geçen biçim
4. Kitabın **dizini** — gövdeyle ancak ≈%80 uyuşur; tek başına zayıf tanıktır (*immune response*: dizin "bağışıklık yanıtı", gövdede dokuz elden sekizi "immün cevap")
5. Bu skill'in §6.1–§6.4 kuralları

**Kitaptan sapma yalnız üç durumda:** (a) dizgi/yazım hatası; (b) kitap kendi içinde birden çok biçim kullanıyorsa → en çok elin biçimi; (c) uzman veya kurum kararı. **Kitabın bir bölümünün kendine özgü biçimi hedef değildir** — B12'de tek bölümle uyumun tavanı ölçüldü; çevirmen elleri birbirinden ayrışır.

**Eş anlamlı ile hata ayrı şeylerdir (alan uzmanı, 26 Eylül 2026).** *"Dilde eş anlamlı kelimeler vardır… Tek bir doğru aramak her zaman doğru olmayabilir. Fakat bir kelimeyi olmayacak şekilde kullanmak hatalıdır."* Üç kademe:

| Kademe | Tanım | Örnek | Ne yapılır |
|---|---|---|---|
| **Tercih** | Kitabın baskın biçimi ya da uzman kararı | konak **cevabı**, **teşhis**, ataşman **seviyesi** | Önce bu yazılır |
| **Kabul** | Kitapta **birden fazla** geçen ya da alanda yerleşik eş anlamlı; baskın değil | konak **yanıtı**, **tanı**, ataşman **düzeyi**, hücre aracılı | **Hata değildir.** Metin içinde tek biçim korunur (§6.2) |
| **Hata** | Sözcük o kavram için **olmayacak** biçimde kullanılmış; anlam alanının dışında | *blade* → "**ağız**", *physiology* → "psikoloji", *odds* → "olasılık", *sinus floor* → "sinüs **duvarı**", *bacterial challenge* → "savaş" | Asla yazılmaz |

Asıl hedef **üçüncü kademeyi sıfırlamaktır.** "Ağız" tipi hatanın kaynağı §6.1'in ihlalidir: terim bilinmiyor, sözlükten türetiliyor. Emin olmadığın terimde tabana bak; tabanda yoksa kitabın o alet ya da yapı için kullandığı sözcüğü hatırla; hatırlamıyorsan İngilizcesini parantezde bırak ve ÇEVİRİ NOTLARI'na yaz — **uydurma.**

**Türkçesi yerleşikse yabancı kökenlisini seçme.** Kitap bir kavram için Türkçe sözcük kullanıyorsa onu yaz:

| Yazılacak | Yazılmayacak |
|---|---|
| alet | enstrüman |
| yüzey özellikleri | yüzey karakteristikleri |
| tasarım | dizayn |
| çevresel | sirkumferansiyel |

- Yabancı kökenli biçimler **eş anlamlıdır**; hata sayılmaz.
- Yine de B42 ölçümünde kitapla uyumun kaybedildiği yer tam olarak bu tercihler oldu.
- Tabandaki `hedef` Türkçe ise tartışma bitmiştir.
- Kitap yabancı kökenli terimi kullanıyorsa o kalır (periodonsiyum, debridman, rezorpsiyon…). Türkçeleştirme yapılmaz.

**Araçlar** — bu paketin `araclar/` klasöründe (erişilebiliyorsa **kullanılır**, değilse §6.3 yedektir):

- `araclar/terim-listesi.tsv` — §6.3 sözlüğünden üretilmiş açık terim listesi (İngilizce → `hedef`). Daha geniş bir terim tabanınız varsa aynı sütunlarla (`ingilizce`, `hedef`, `kabul`, `durum`) hazırlayıp `--taban` ile verin. **Çeviriye başlamadan önce** kaynağın terimleri tabanda aranır; `durum = guvenli` satırlarının `hedef` biçimi kullanılır. `incele` satırları öneridir. `hedef` hücresinde ` | ` ile ayrılmış biçimler uzmanın kabul ettiği eşdeğerlerdir. `kabul` sütunu kitapta ≥2 kez geçen eş anlamlıları listeler (hata değil; yine de `hedef` tercih edilir).
- `araclar/denetim.py` — gerileme denetimi. **Teslimden önce** çalıştırılır:
  `python3 denetim.py --en kaynak.txt --tr ceviri.md --out rapor.md` (taban: `--taban` ya da `TERIM_TABANI`; raporun ilk satırı `Terim tabanı: … (N terim)` olmalı — `YÜKLENEMEDİ` ya da `BOŞ` görülürse kitap terimi denetimi yapılmamıştır, yol düzeltilip yeniden çalıştırılır).
  **HATA** düzeyindeki her bulgu düzeltilir; **İNCELE** bulguları tek tek değerlendirilir; **TERCİH** bulguları hata değildir: baskın biçime geçmek önerilir ama zorunlu değildir; hangisi seçilirse metin boyunca o biçim korunur. "kitap terimi" İNCELE'si için: kaynaktaki geçiş gerçekten o terim mi? Öyleyse kitabın biçimine geç.
- Denetimin yakalayamadıkları: ilk kez karşılaşılan terim, vurgu kayması, paragraf eşlemesi. Bunlar §6.1, §7.3 ve §7.4'ün işidir.


### 6.1 Kayıt kuralı — terim hatırlanır, türetilmez

**Bu kural §6'nın en kritik maddesidir ve dört kör sınavla ölçülmüştür (§11, v3–v6).**

Ölçüt **"Türkçe karşılığı var mı"** değildir. Ölçüt **"alanda ne deniyor"**dur — yani Türk diş hekimliği yazınının o kavram için kullandığı **yerleşik eşdizim**.

> **Asıl yapay zekâ imzası şudur: terimi İngilizce bileşiğin biçiminden yeniden kurmak.**
> *cell-mediated* → "hücre aracılı", *delayed-type* → "gecikmiş tip", *adaptive* → "edinsel".
> Üçü de İngilizceye birebir sadık, üçü de doğru Türkçe, **üçü de alanın dili değil.**
> Alan **hücresel bağışıklık**, **geç tip hipersensitivite**, **kazanılmış bağışıklık** der.

**Kendine sor: bu terimi hatırladım mı, kurdum mu?** Dört kör sınavda ele veren sözcüklerin hepsi "kurulmuş" taraftaydı: *asıl alveol kemiği, damar yapıları, edinsel, hücre aracılı, sıradan, kestirim değeri.* Hiçbiri sözlükte yanlış değildi; hepsi o kavram için **ilk kez o cümlede üretilmişti.** Kurduğunu fark ettiğin her terimde karşı biçimi de yaz ve ikisini yan yana koy.

#### Yön kuralı — terim mi, sıradan sözcük mü?

Yirmi iki uzman kararıyla ölçülmüş tek ayrım budur (§11, v7). Önce sor:

> **Bu, bir kavramın adı mı, yoksa sıradan bir sözcük mü?**

- **Kavramın adıysa** — bir işlemin, dokunun, aletin, klinik antitenin adı — **alanın sabit biçimini kullan, biçimi ne olursa olsun.** Latince de olabilir (*prediktif değer, prevalans, dentisyon, anamnez, kuron, saplı greft*), Türkçe de (*açısal, yalancı cep, kök yüzeyinin örtülmesi, örtücü mukoza, yarım-kalınlık flep*). Burada kendi karşılığını üretmek en sık ele veren harekettir.
- **Sıradan sözcükse** — birim, evre, bant, istek, parçacık, teslim, göç, araç — **Türkçesini kullan; ödünç biçim arama.** Burada Latinceleştirmek ters yönden aynı hatadır (*ünite, faz, banda, demand, partikül, delivery, migrasyon, cihaz*).

İki yönlü bir hatadır ve iki yönde de ölçülmüştür: sekiz çiftte bu skill fazla Türkçeleştirmiş, on dört çiftte fazla Latinceleştirme kaçırılmıştı. **Konu ekseni ("ölçüm sözvarlığı mı, doku sözvarlığı mı") bu iki grubu ayıramaz — statü ekseni ayırır.** *(v6'da yazılan konu-eksenli sezgi bu nedenle kaldırıldı.)*

Kural yine de yön kuralı değil **hatırlama** kuralıdır; yön yalnızca nereye iki kez bakacağını söyler.

Bu, "fazla Türkçeleştirme" ya da "fazla Latinceleştirme" sorunu değildir; **iki yönlü** bir sorundur. Alan bazen yabancı biçimi tutar (*alveolar kemik*, *kansellöz kemik*), bazen Türkçesini (*geçirgenlik*, *savunma*), bazen de kısalmış bir kalıbı (*hücresel*, *geç tip*). Tek kural: **hatırla, türetme.** Bir terimi kaynaktaki sözcüklerden parça parça inşa ediyorsan, neredeyse kesinlikle yanlış yapıyorsun.

**Ölçülmüş düzeltmeler** — hepsi kör sınavda bu skill'i ele verdi:

| Bu skill yazmıştı | Alan dili | Sınav |
|---|---|---|
| asıl alveol kemiği | **kribriform tabaka** | v3 |
| süngerimsi kemik | **kansellöz kemik** | v3 |
| damar yapıları | **vasküler yapılar** | v3 |
| mezenkimal kökenli | **mezenşimal kaynaklı / orijinli** | v3 |
| ataşman aygıtı | **ataşman aparatı** | v3 |
| edinsel bağışıklık | **kazanılmış bağışıklık** | v4 |
| hücre aracılı bağışıklık | **hücresel bağışıklık** | v4 |
| gecikmiş tip hipersensitivite | **geç tip hipersensitivite** | v4 |
| konak defans mekanizmaları | **konak savunma mekanizmaları** | v4 |
| permeabilite | **geçirgenlik** | v4 |
| sıradan *(periodontal sond)* | **geleneksel / konvansiyonel** | v5 |
| kör *(alet)* | **künt** *(alet)* | v5 |
| dişlenme | **dentisyon** | v5 |
| gevşetici insizyon | **rahatlatıcı insizyon** | v5 |
| yeniden şekillendirme *(kemik)* | **yeniden konturlama** | v5 |
| üst çene dişleri | **maksiller dişler** | v5 |
| yarım ay biçiminde insizyon | **yarım-ay (semilüner) insizyon** | v5 |
| birbirinden farklı birçok | **birkaç farklı** *(several = birkaç)* | v5 |
| **kök** yüzeyi temizliği *(scaling)* | **diş** yüzeyi temizliği | v5 |
| kestirim değeri *(predictive value)* | **prediktif değer** | v6 |
| angüler *(kemik defekti)* | **açısal** | v6 |
| psödo-cep | **yalancı cep** | v6 |
| öykü alma | **anamnez alma** | v6 |
| kök yüzeyi kapatma | **kök yüzeyinin örtülmesi** | v7 |
| astar mukoza | **örtücü mukoza** | v7 |
| kısmi kalınlık flep | **yarım-kalınlık flep** | v7 |
| pediküllü greft | **saplı (pediküllü) greft** | v7 |
| kron | **kuron** | v7 |

**Uzman kararları — yirmi iki çift (§11, v7).** Yukarıdaki son beş satır uzmanın **basımın terimini** seçtiği çiftlerdir. On dört çiftte uzman **bu skill'in terimini** seçmiştir; o satırlar §6.3'te işaretlidir. İkisini birlikte okumak yön kuralının dayanağıdır: ilk grup **kavram adı**, ikinci grup **sıradan sözcük**.

**Sıfat biçimi korunur, izafet kurulmaz:**

| Kur | Kurma |
|---|---|
| **alveolar** kemik · **alveolar** kret · **alveolar** mukoza · **alveolar** proçes | alveol kemiği, alveol kreti |
| **vasküler** yapılar | damar yapıları |
| **mezenşimal** kaynaklı | mezenkimal kökenli |
| **kansellöz** kemik | süngerimsi kemik *(tek başına)* |
| **ataşman aparatı** | ataşman aygıtı |
| **epitelyal** rete peg | epitel sırtı |
| **sellüler · interstisyel · kortikal · nekrotizan** | hücreli, ara, kabuk… |

**İlk geçiş yönü:** gövde metinde alanın konuştuğu terim durur; ikinci biçim — varsa — ilk geçişte parantezde verilir, tersi değil.
> ✓ *kansellöz (süngerimsi) kemik* … sonraki geçişler: kansellöz kemik
> ✗ *süngerimsi kemik*

**Sınır — kural yerleşik Türkçe terimi de bozmaz.** *diş eti, diş taşı, kemik içi cep, ataşman kaybı, konak, kanama, iyileşme, geçirgenlik, savunma, yatkınlık, denge, yıkım, uyarı, taşıyan* alanın kendi dilidir; bunlar Latinceye çevrilmez.

**Kararlar metinden metne taşınır.** Bir terim bir metinde karara bağlandıysa, sonraki metinlerde **aynı kararla** çıkar. Üçüncü kör sınavı kaybettiren hata tam buydu: aynı külliyat içinde `conventional` bir bölümde **konvansiyonel** (doğru), başka bölümde **sıradan** (yanlış) yazıldı. §6.2'nin "tek terim = tek karşılık" kuralı **tek metinle sınırlı değildir**; §8'in terim çiftleri tablosu bu yüzden saklanır ve bir sonraki çeviriye girdi olarak verilir.

**Kural tek metnin içinde de gereklidir — ölçüldü.** Basılı çevirinin bir bölümünde profesyonel çevirmen *dentition* için tek bölümde üç karşılık kullanmıştır (dentisyon · diş dizisi · tüm ağız), *dichotomous* için üç (iki yönüyle · çift yönlü · var yok şeklinde), *chart* için üç (çizelge · şema · kayıt). Başka bir bölümde *dichotomous* için "iki değerli", "dikotom" ve — Türkçede var olmayan — **"dikromoz"** biçimlerini aynı sayfada kullanmıştır. Yani bu, yapay zekâya özgü bir kusur değildir; insan çevirmende daha sık görülür. Ayırt edici olan kuralın kendisi değil, **teslim öncesi taranması**dır (§7.4/#10).

**Tanık ölçütü.** Tek bir çevirmenin sözcük seçimi kural üretmez. Lindhe basımında **her bölümü ayrı kişi çevirmiştir** (§8'deki künye kuralı) ve elleri ölçülebilir biçimde ayrılır. Bir terim §6.3'e **sabit satır** olarak ancak **iki bağımsız tanıkla** girer (iki ayrı çevirmen, ya da dizin + gövde, ya da alan uzmanının kararı). Tek tanık varsa satır *"ikinci biçim"* notuyla girer. Alan uzmanının açık kararı **tek başına yeterlidir** ve basımın iki tanığını da ezer. **Dizin tek başına tanık sayılmaz** (§6.0/4).

### 6.2 İşleyiş kuralları

- **İlk geçiş kuralı.** Yerleşik Türkçe karşılık kullanılır; ilk geçişte özgün terim parantez içinde verilir; sonra yalnız Türkçe karşılık.
  > birleşim epiteli (junctional epithelium) … sonraki geçişler: birleşim epiteli
- **Kısaltmalar ilk geçişte açılır:** "klinik ataşman seviyesi (clinical attachment level, CAL)", "güven aralığı (GA)".
- **Uluslararası kısaltma korunur, Türkçeleştirilmez:** CEJ, CAL, PAL, PPD, BOP, PD, GI, PI. *(Basılı Lindhe çevirisi kısaltmaları bütünüyle Türkçeleştirir: **CD** cep derinliği, **AS** ataşman seviyesi, **KAS** klinik ataşman seviyesi, **AK** ataşman kaybı, **SK** sondlamada kanama, **FT** furkasyon tutulumu, **DM** diş mobilitesi, **MSB** mine-sement birleşimi. Burada izlenmez — öğrencinin uluslararası kaynakta karşılığını bulabilmesi önceliklidir.)*
  - ★ **Uzman kararı (B0d, 23 Eylül 2026): uluslararası kısaltma korunur** (PPD, CAL, PAL…). Terimin **açılımı** ise kitabın biçimidir: *klinik ataşman seviyesi (CAL)*, *sondlama cep derinliği (PPD)*.
  - **İstisna — Türkçesi alanda yerleşmiş kısaltmalar:** **DOS** (diş eti oluğu sıvısı), **KIBT** (konik ışınlı BT), **DPT** (destekleyici periodontal tedavi). Bunlar Türkçe kalır. Ölçüt yine §6.1'dir: alanda ne deniyorsa o.
  - **Kısaltma tanımlanmadan kullanılmaz.** Basımda **MSB** hiç açılmadan kullanılmıştır (§11, v7).
- **Kısaltma açılımı tek yönlüdür:** Türkçe karşılık + parantezde **özgün İngilizce terim ve kısaltma**. Türkçesi verildikten sonra parantezde İngilizce açılımı **tekrar yazılmaz**.
  > ✓ *ısı şoku proteini (heat shock protein, HSP) 60*
  > ✗ *ısı şoku protein (human heat shock protein- HSP) 60*
- **Karşılığı olmayan terim** alanda kullanıldığı biçimde bırakılır ve ilk geçişte bir cümleyle tanımlanır. **Uydurma karşılık türetilmez.**
- **Tek terim = tek karşılık — ve bu kural metinle sınırlı değildir.** Aynı külliyatta (aynı kitap, aynı ders serisi, aynı kurum) daha önce karara bağlanmış bir terim, sonraki metinlerde aynı biçimde çıkar. Metin sonundaki terim çiftleri tablosu (§8) bu yüzden **saklanır** ve bir sonraki çevirinin başında okunur.
- **Çakışan iki kavram önceden ayrılır.** Aynı Türkçe sözcüğe düşebilecek iki İngilizce terim varsa ayrım çeviriye başlamadan sabitlenir ve `[ÇN]` ile bildirilir. Ölçülmüş çakışmalar: *prevalence* ↔ *extent* (ikisi de "yaygınlık"); *site* ↔ *surface* (ikisi de "yüzey"); *destruction/breakdown* ↔ *deterioration* (ikisi de "yıkım"); *recession* ↔ *pull* (ikisi de "çekilme"); *sample* ↔ *example* (ikisi de "örnek").
- **Ek alırken** ses uyumu ve yumuşama: flep → **flebi**, greft → **grefti**, implant → **implantı**, sond → **sondu**, pH → **pH'ın**, mm → **mm'ye**.

### 6.3 Alan sözlüğü

Bu satırlar bu skill'in varsayılanıdır. Kurum sapması varsa §6.6 üstüne yazar.
Çoğu satır **Lindhe 6. baskının basılı Türkçe çevirisinden** tanıklıdır (§11). **★** işaretli satırlar alan uzmanının açık kararıdır (23–24 Eylül 2026).

**Dokular ve anatomi**

| İngilizce | Türkçe |
|---|---|
| gingiva | diş eti *(ayrı yazılır)* |
| oral mucosa | oral mukoza |
| lining mucosa | **örtücü mukoza** ★ |
| masticatory mucosa | çiğneyici mukoza |
| oral epithelium | oral epitel |
| attached / free gingiva | yapışık diş eti / serbest diş eti |
| gingival unit | **diş eti birimi** ★ |
| dentogingival unit | **dentogingival birim** ★ |
| mucogingival junction | mukogingival birleşim |
| vestibular fornix | **vestibül forniksi** ★ |
| junctional epithelium | **birleşim epiteli** ★ |
| oral sulcular epithelium | oral sulküler epitel |
| periodontal ligament | periodontal ligament |
| cementum | sement |
| alveolar bone / alveolar crest | alveolar kemik / alveolar kret |
| alveolar process | alveolar proçes |
| alveolar mucosa | alveolar mukoza |
| alveolar bone proper (ABP) | **kribriform tabaka** *(alveolar kemik proper, AKP; demet kemiği)* |
| cancellous bone | kansellöz (süngerimsi) kemik |
| primary spongiosa | primer süngerimsi kemik |
| interdental papilla | interdental papil |
| col | col bölgesi |
| keratinized tissue | keratinize doku |
| elastic fibers | elastik lifler |
| extracellular matrix | ekstrasellüler matriks |
| ectomesenchyme | ektomezenşim |
| mesenchymal (origin) | mezenşimal kaynaklı · mezenşimal orijinli |
| attachment apparatus | ataşman aparatı |
| vascular structures | vasküler yapılar |
| epithelial ridge / rete peg | epitelyal rete peg |
| bone remodeling | remodelasyon |
| neural crest | nöral kret |
| collagen fiber | kolajen lif *(tek l — TDK)* |
| reticulin / oxytalan fibers | retikülin / oksitalan lifleri |
| basement membrane | bazal membran |
| keratinocyte | keratinosit |
| biologic width *(2017 öncesi)* | suprakrestal doku ataşmanı *(basımda: biyolojik genişlik)* |
| periodontal biotype (thin / thick) | periodontal biyotip (ince / kalın) |
| reduced periodontium | azalmış periodonsiyum |
| host | konak |

**Klinik ölçüm ve bulgu**

| İngilizce | Türkçe |
|---|---|
| probing depth / pocket depth | sondlama derinliği / cep derinliği |
| clinical attachment level (CAL) | **klinik ataşman seviyesi (CAL)** ★ *(kısaltma: B0d)* |
| probing attachment level (PAL) | **sondlamada ataşman seviyesi (PAL)** ★ |
| diagnosis | **teşhis** ★ *(sabit terim istisnası: differential diagnosis = **ayırıcı tanı**)* |
| attachment loss | ataşman kaybı |
| bleeding on probing (BOP) | sondlamada kanama |
| periodontal probing | periodontal sondlama |
| automated probing system | otomatik sondlama sistemi |
| gingival recession | diş eti çekilmesi |
| furcation involvement | furkasyon tutulumu |
| furcation fornix / entrance | furkasyon forniksi / girişi |
| mobility | mobilite |
| suppuration | süpürasyon |
| calculus *(supra- / subgingival)* | diş taşı *(supragingival / subgingival)* |
| radiographic bone loss | radyografik kemik kaybı |
| morphology / severity of bone loss | kemik kaybının morfolojisi / şiddeti |
| keratinized tissue width | keratinize doku genişliği |
| intrabony pocket | kemik içi cep |
| residual pocket | rezidüel cep · kalan derin cep |
| plaque / gingival index | plak indeksi / gingival indeks |
| periodontal chart | periodontal çizelge *(bir metin boyunca tek karşılık)* |
| predictive value | **prediktif değer** *(→ "kestirim değeri" değil — §11 v6)* |
| angular *(bony defect)* | **açısal** ★ |
| pseudo-pocket | **yalancı cep** ★ |
| dichotomous *(kayıt)* | **var/yok (ikili) biçiminde** |
| topographical pattern | **topografik patern** *(→ "örnek" değil)* |
| history taking | **anamnez alma** ★ |
| chief complaint | başlıca yakınma · esas şikâyet |
| implant recipient site | **implant alıcı bölgesi** |
| two-digit system (FDI) | FDI iki haneli sistem *(→ FDA değil — basımın hatası)* |
| excursive movements | **ekskürsiyon hareketleri** *(→ "düzensiz" değil)* |
| suprabony / infrabony lesion | kemik üstü / kemik içi lezyon |
| periodontal risk assessment | periodontal risk değerlendirmesi (PRD) |
| tooth prognosis | tek diş prognozu |
| food impaction | **besin sıkışması** ★ |
| food particles | **besin parçacıkları** ★ |
| apical migration | **apikale göç** ★ |
| re-epithelialization | **yeniden epitelizasyon** ★ |
| band *(of tissue)* | **bant** ★ |
| stage *(evre)* | **evre** ★ |

**Epidemiyoloji, istatistik ve yöntem** *(Bölüm 7'den ölçüldü — §11 v7)*

| İngilizce | Türkçe |
|---|---|
| prevalence | **prevalans** *(ilk geçişte "prevalans (ortaya çıkma sıklığı)")* |
| incidence | insidans |
| extent | **yaygınlık** *(basımda "yayılım"; iki biçim de alanda var — metin boyunca tek biçim seçilir ve `[ÇN]` açılır. "Yaygınlık" prevalance ile çakışırsa "yayılım" seçilir)* |
| case definition | **vaka tanımlama** ★ · case–control = **vaka-kontrol** |
| screening method | **tarama yöntemi** *(→ "görüntüleme" değil — radyografi bağlamında özellikle tehlikeli)* |
| descriptive epidemiology / statistics | **tanımlayıcı** epidemiyoloji / istatistik ★ |
| analytical / etiologic / experimental epidemiology | analitik / etiyolojik / deneysel epidemiyoloji |
| natural history *(of disease)* | **doğal seyir** *(sabit terim)* |
| familial aggregation | **ailesel kümelenme** *(→ "ailesel geçiş" değil; kümelenme aktarım iddiası taşımaz)* |
| median | **ortanca** *(→ "ortalama" değil)* |
| percentile | **persentil** *(→ "yüzdelik" değil; persentil ≠ yüzde)* |
| skewed *(distribution)* | **çarpık** dağılım |
| frequency distribution | sıklık dağılımı |
| sensitive / specific *(tanım)* | **duyarlı / özgül** *(duyarlılık–özgüllük çifti korunur)* |
| cohort | kohort |
| partial / full-mouth recording | kısmi / tüm ağız kaydı |
| age-adjusted | **yaşa göre düzeltilmiş** *(→ "yaşa bağlı" değil)* |
| setting *(of a study)* | **ortam / bağlam** *(→ "kurgularken" değil)* |
| companion paper | **eşlik eden yayın** *(→ "ortak çalışma" değil)* |
| longitudinal | boylamsal |
| cross-sectional | kesitsel |
| sample | **örneklem** *(→ "örnek" değil; example ile ayrılır)* |
| site *(diş bölgesi)* | **bölge** *(surface = yüzey; ikisi karıştırılmaz)* |
| deterioration | **bozulma** *(destruction/breakdown = yıkım)* |
| disease-free | **hastalıksız** *(tireli calque kurulmaz)* |
| background factors | **arka plan etkenleri** *(→ "geçmiş faktörler" değil)* |

**Hastalık, lezyon ve sınıflama (2017/2018)**

| Güncel | Kullanma |
|---|---|
| periodontitis + evre (I–IV) / derece (A–C) | kronik periodontitis, agresif periodontitis |
| NG — nekrotizan gingivitis | ANUG, NUG |
| NP — nekrotizan periodontitis | NUP |
| peri-implant mukozit · peri-implantitis | — |
| lokalize / yaygın *(generalized)* | jeneralize, generalize |
| molar-keser paterni | — |
| plağa bağlı / plağa bağlı olmayan gingivitis | — |
| başlangıç · erken · yerleşmiş · ilerlemiş lezyon | — |
| **modifiye edici faktör** ★ *(düzenleyici faktör de kabul)* · predispozan faktör | değiştiren faktör |
| çizgisel gingival eritem *(linear gingival erythema)* | — |
| ilaç kaynaklı diş eti büyümesi | *(basımda: gingival hiperplazi)* |
| tip 1 / tip 2 diabetes mellitus | IDDM, NIDDM, "diyabetes" |
| MRONJ | BRONJ, ARONJ |
| deformiteler ve **durumlar** *(1999 sınıflaması, kategori VIII)* | "koşullar" |

> Tarihsel çalışma aktarılırken **çalışmanın kendi terimi korunur**; genel ifadelerde güncel terim kullanılır. Bu durumda `[ÇN]` açılır. 1999 sınıflamasını kullanan bir bölüm 2017/2018 sistemine çevrilmez.

**Tedavi ve cerrahi**

| İngilizce | Türkçe |
|---|---|
| scaling and root planing | subgingival enstrümantasyon *(tarihsel karşılık: diş yüzeyi temizliği ve kök yüzeyi düzleştirmesi, SRP)* |
| root debridement | kök debridmanı |
| professional mechanical plaque removal | profesyonel mekanik plak uzaklaştırılması |
| self-performed plaque control | **hastanın kendi uyguladığı plak kontrolü** ★ |
| self-referred patient | **kendi başvuran hasta** ★ |
| oral hygiene instruction | ağız hijyeni eğitimi |
| interdental cleaning | diş arası temizliği |
| interdental cleaning device | **diş arası temizlik aracı** ★ |
| oral irrigator | oral irrigatör · diş suyu jeti |
| sulcular brushing | sulküler fırçalama |
| powered / manual toothbrush | elektrikli / manüel diş fırçası |
| step 1–4 therapy | 1.–4. basamak tedavi |
| initial (hygienic) phase | başlangıç (hijyenik) faz |
| maintenance phase | idame fazı |
| supportive periodontal care | destekleyici periodontal tedavi (DPT) |
| recall visit | kontrol randevusu |
| demands *(of the patient)* | **istekler** ★ |
| delivery of the prosthesis | **protezin teslim edilmesi** ★ |
| access therapy | erişim tedavisi |
| open flap debridement | açık flep debridmanı (AFD) |
| papilla preservation flap | papil koruyuculu flep |
| split flap / partial-thickness flap | **yarım-kalınlık flep** ★ |
| mucoperiosteal / full-thickness flap | mukoperiostal flep / tam kalınlık flep |
| pedicle graft | **saplı (pediküllü) greft** ★ |
| distal wedge procedure | distal kama işlemi |
| flap design | flep dizaynı |
| guided tissue / bone regeneration | yönlendirilmiş doku / kemik rejenerasyonu |
| barrier membrane | bariyer membran |
| enamel matrix derivative | mine matriks türevi |
| connective tissue graft | bağ dokusu grefti |
| interpositional / onlay graft | interpozisyonel / onlay greft |
| pouch graft | pouch greft işlemi |
| coronally advanced flap | koronale kaydırılan flep |
| root coverage | **kök yüzeyinin örtülmesi** ★ |
| creeping attachment | creeping ataşman |
| root surface biomodification | kök yüzeyi biyomodifikasyonu |
| crown lengthening | kuron boyu uzatma |
| gingivectomy / gingivoplasty | gingivektomi / gingivoplasti |
| resective osseous surgery | rezektif kemik cerrahisi |
| ostectomy / osteoplasty | ostektomi / osteoplasti |
| root separation / resection | kök ayırma / rezeksiyon |
| furcation plasty | furkasyon plasti |
| tunnel preparation | tünel preparasyonu |
| ridge / socket preservation | kret koruma / soket koruma |
| ridge augmentation | kret ogmentasyonu |
| deformed ridge | deforme kret |
| sinus floor elevation | sinüs tabanı yükseltme |
| freeze-dried bone allograft | dondurulmuş-kurutulmuş kemik allogreft |
| tricalcium phosphate | trikalsiyum fosfat |
| trephine | trefan |
| host modulation therapy | konak modülasyon tedavisi |
| local drug delivery | lokal ilaç kullanımı |
| adjunctive | ek *(tedaviye ek)* · yardımcı |
| surgical microscope / loupes | cerrahi mikroskop / louplar |
| temporary anchorage device | geçici ankraj aracı (TAD) |
| molar uprighting | molar doğrultma |
| curette: blade / shank / handle | **bıçak** *(kitap metni: keskin yüzey)* / **boyun** / **sap** *(→ "ağız" değil — uzman öbek işaretlemesi, B38)* |
| scalpel | **bistüri** *(→ "skalpel" değil)* |
| blunt instrument | **künt alet** *(→ "kör alet" değil)* |
| conventional *(alet, flep)* | **geleneksel / konvansiyonel** *(→ "sıradan" değil)* |
| releasing incision | **rahatlatıcı insizyon** *(→ "gevşetici" değil)* |
| beveled / reverse bevel incision | **eğimli / ters eğimli insizyon** |
| beveled flap | **eğimli flep** |
| intracrevicular / intrasulcular incision | intrakreviküler insizyon · diş eti oluğu içinden insizyon |
| semilunar incision | **yarım-ay (semilüner) insizyon** |
| scalloped *(incision, outline)* | festonlu |
| tissue collar | doku halkası |
| (bone) recontouring | **yeniden konturlama** |
| periosteal elevator | periost elevatörü |
| bone chisel / rongeur | kemik keskisi / kemik ronjörü |
| round bur | rond frez |
| saline irrigation | serum fizyolojik irrigasyonu |
| interrupted / mattress suture | kesintili sütür / matres sütür |
| periodontal dressing | **periodontal pat** |
| pain control | **ağrı kontrolü** |
| embrasure | **embraşür** |
| approximal | **aproksimal** *(tek p)* |
| maxillary / mandibular | **maksiller / mandibular** |
| dentition | **dentisyon** *(iki tanıkla ölçüldü)* |
| periodontist | periodontist |
| osseous ledge / crater | kemik çıkıntısı / kemik krateri |
| supporting bone | destek kemik |

**Mikrobiyoloji ve konak cevabı**

| İngilizce | Türkçe |
|---|---|
| biofilm | biyofilm |
| dysbiosis | disbiyoz |
| keystone pathogen | kilit taşı patojen |
| ecological / specific plaque hypothesis | ekolojik / spesifik plak hipotezi |
| host response | **konak cevabı** ★ |
| response *(immün, enflamatuar, vasküler, hücresel, tedaviye)* | **cevap** ★ *(kitap gövdesinde dokuz elden sekizi)* |
| microbial succession | **mikrobiyal süksesyon** ★ *(→ "zincir", "miras" değil)* |
| host defense mechanisms | **konak savunma mekanizmaları** *(→ "defans" değil)* |
| immune response | **immün cevap** ★ *(→ "bağışıklık yanıtı" değil — yalnız dizinde geçer)* |
| permeability | **geçirgenlik** *(→ "permeabilite" değil)* |
| regulatory T cell (Treg) | regülatuar T hücresi (Treg) |
| plasma cell | plazma hücresi |
| pocket epithelium | cep epiteli |
| gingival crevicular fluid (GCF) | **diş eti oluğu sıvısı (DOS)** *(§6.2 istisnası)* |
| cell line | hücre hattı *(→ "hücre serisi" değil)* |
| strain *(mikroorganizma, fare)* | suş / soy *(→ "tür" değil)* |
| innate / adaptive immunity | **doğal / kazanılmış bağışıklık** *(→ "edinsel" değil)* |
| cell-mediated immunity | **hücresel bağışıklık** |
| antigen-presenting cell | **antijen sunucu hücre** ★ |
| delayed type hypersensitivity | **geç tip hipersensitivite (DTH)** |
| bacterial challenge | **bakteriyel uyarı** |
| pro-inflammatory mediator | proenflamatuar medyatör |
| inflammation / inflammatory | enflamasyon / enflamatuar |
| connective tissue matrix destruction | bağ dokusu matriksi yıkımı |
| bone resorption | kemik rezorpsiyonu |
| codestruction zone | birlikte yıkım bölgesi |
| glycation · advanced glycation end products | glikasyon · ileri glikasyon son ürünleri (AGE) |
| stem cell / progenitor cell | kök hücre / progenitör hücre |
| tissue engineering | doku mühendisliği |

**Kanıt ve yöntem**

| İngilizce | Türkçe |
|---|---|
| randomized controlled trial | randomize kontrollü çalışma |
| systematic review / meta-analysis | sistematik derleme / meta-analiz |
| consensus report | uzlaşı raporu |
| certainty of evidence | kanıt kesinliği *(→ "kanıt düzeyi" değil)* |
| risk of bias / selection bias | yanlılık riski / seçim yanlılığı |
| reporting bias | bildirim yanlılığı |
| confidence interval | güven aralığı (GA) |
| odds ratio / risk ratio / hazard ratio | **odds oranı** ★ *(→ "olasılık oranı" değil: odds ≠ probability)* / risk oranı / **hazard oranı** ★ |
| relative risk | göreceli risk |
| dose–response effect | doz-cevap etkisi |
| exposure variable | ekspoz değişkeni |
| external validity | eksternal geçerlilik |
| intervention study | girişimsel çalışma |
| genome-wide association study | genom çapında ilişkilendirme çalışması |
| epigenetic signature | epigenetik imza |
| number needed to treat | tedavi edilmesi gereken hasta sayısı |
| effect size | etki büyüklüğü |
| baseline / follow-up | başlangıç / izlem |
| blinding | körleme |
| survival rate | sağkalım oranı |
| risk factor | risk faktörü |
| finite element analysis | sonlu element analizi |
| adverse pregnancy outcome | olumsuz gebelik sonucu |
| small for gestational age | gebelik yaşına göre küçük |

**Genel diş hekimliği ve protez**

| İngilizce | Türkçe |
|---|---|
| caries | çürük |
| pulp / root canal treatment | pulpa / kök kanal tedavisi |
| electric pulp test | elektrik pulpa testi |
| dentin hypersensitivity | dentin hipersensitivitesi |
| accessory canal | aksesuar kanal |
| cemental tear | semental yarık |
| vertical root fracture | vertikal kök kırığı |
| restoration / margin | restorasyon / kenar |
| crown *(diş)* | **kuron** ★ |
| occlusion / occlusal trauma | oklüzyon / oklüzal travma |
| pathologic tooth migration | patolojik diş migrasyonu |
| splinting | splintleme |
| abutment | dayanak *(implant)* / köprü ayağı *(protez)* |
| prefabricated / customized abutment | prefabrike / özel yapılmış dayanak |
| screw- vs cement-retained | vidalı ile simante |
| fixed partial denture | sabit parsiyel protez |
| pontic / cantilever | pontik / kantilever |
| removable partial denture | hareketli parsiyel protez |
| edentulous / edentulism | dişsiz / dişsizlik |
| congenital absence | konjenital yokluk |
| extraction / impacted tooth | çekim / gömülü diş |
| socket healing | soket iyileşmesi |
| cone-beam CT | konik ışınlı bilgisayarlı tomografi (KIBT) |
| diagnostic imaging | tanısal görüntüleme |
| informed consent | aydınlatılmış onam |
| medical history | tıbbi öykü |
| referral | sevk |
| indication / contraindication | endikasyon / kontrendikasyon |

### 6.4 Yanlış anlam tuzakları — sözlük karşılığı ≠ bağlam karşılığı

**Kaynak metin elinde olan tek aşama budur; anlam seçimi burada yapılır.** Denetim geçişi bu hataları göremez, yalnız sezebilir.

| İngilizce | Yanlış (sözlük refleksi) | Bağlama göre doğru |
|---|---|---|
| significant *(istatistik)* | önemli | **anlamlı** |
| significant *(klinik)* | anlamlı | **belirgin / önemli** |
| management | yönetim | **tedavi, tedavi yaklaşımı** |
| severe | ciddi | **şiddetli** |
| moderate | ılımlı | **orta / orta şiddette** |
| condition | koşul | **durum / hastalık** ⚠ |
| conditions *(sınıflama adında)* | koşullar | **durumlar** ⚠ |
| compliance | uyumluluk | **hasta uyumu / tedaviye uyum** ⚠ |
| intercellular / intracellular | ikisi de "hücre içi" | **hücreler arası** / **hücre içi** ⚠ |
| uncommitted *(hücre)* | bağımsız | **henüz farklılaşmamış** |
| evidence | delil | **kanıt** |
| finding | buluş | **bulgu** |
| course | izlenim | **klinik gidiş / seyir** |
| involvement | katılım | **tutulum** |
| to develop *(a disease)* | geliştirmek | **hastalığa yakalanmak / hastalık gelişmek** |
| to present with | sunmak | **ile başvurmak / -i göstermek** |
| association | çağrışım | **ilişki / birliktelik** |
| maintenance | bakım | **idame** |
| probing | araştırma | **sondlama** |
| host | ev sahibi | **konak** |
| resolution *(of inflammation)* | çözünürlük | **gerileme / sönme** |
| recall | geri çağırma | **kontrol randevusu** ⚠ |
| challenge *(bacterial, isim)* | meydan okuma | **maruz bırakma / uyarı** |
| to be challenged *(bir görüş, eylem)* | zorluk olmak | **sorgulanmak / tartışmaya açılmak** ⚠ |
| measures *(cause-related, önlem)* | ölçümler | **önlemler** ⚠ |
| adverse *(contour, effect)* | tersine | **elverişsiz / olumsuz** ⚠ |
| to compromise *(plaque removal)* | tehlikeye atmak | **güçleştirmek** |
| accuracy | hassasiyet | **doğruluk** |
| conventional | sıradan | **geleneksel / konvansiyonel** ⚠ |
| blunt *(instrument)* | kör | **künt** ⚠ |
| several | birçok | **birkaç** |
| outcome | çıktı | **sonuç** |
| failure *(implant)* | başarısızlık | **kayıp** |
| trial | deneme | **çalışma / klinik araştırma** |
| bias | önyargı | **yanlılık** |
| level of evidence | kanıt düzeyi | **kanıt kesinliği** |
| rate / ratio | ikisi de "oran" | **hız** / **oran** ayrımı korunur |
| prevalence / incidence | ikisi de "sıklık" | **prevalans** / **insidans** |
| impression *(protez)* | izlenim | **ölçü** |
| site | alan, site, yüzey | **bölge** ⚠ |
| loading *(implant)* | yük bindirme | **yükleme** |
| survival | hayatta kalma | **sağkalım** |
| regimen | rejim | **tedavi şeması / kullanım şeması** |
| topical | tropikal | **topikal / yerel** |
| rinse | durulama | **gargara / ağız çalkalama suyu** |
| defect | kusur | **defekt** |
| healing | şifa | **iyileşme** |
| plaque *(diş)* | plaka | **plak** |
| default *(response)* | kusurlu | **varsayılan** ⚠ |
| to mediate | uyarmak | **aracılık etmek** ⚠ |
| that remains *(question, issue)* | akılda kalan | **yanıtlanmamış / yerinde duran** ⚠ |
| overlooked | incelenmiş | **gözden kaçmış** ⚠ |
| relevance | uygunluk | **ilgi / ilgililik** ⚠ |
| naïve *(hücre)* | saf | **naif** ⚠ |
| non-committed *(hücre)* | bağlantılı olmayan | **henüz yönelmemiş** ⚠ |
| further *(illustrates, supports)* | ileride | **ayrıca / dahası** ⚠ |
| to disturb *(a balance)* | rahatsız etmek | **bozmak** ⚠ |
| decoy *(receptor)* | karşıt | **tuzak** ⚠ |
| membrane-bound | membran bağımlı | **membrana bağlı** ⚠ |
| to establish *(a fact)* | yerleşmek | **ortaya konmak** ⚠ |
| strain *(of mice, bacteria)* | tür | **suş / soy** ⚠ |
| cell line | hücre serisi | **hücre hattı** ⚠ |
| i.e. | örneğin | **yani** ⚠ |
| circumstantial *(evidence)* | ikinci / ikincil | **dolaylı** ⚠ |
| putative | *(düşürülüyor)* | **varsayılan** ⚠ |
| elusive | açık değil | **ele geçmemiş / zor** ⚠ |
| enigma | merak konusu | **bilmece / gizem** ⚠ |
| conflicting *(reports)* | kafa karıştırıcı | **çelişkili** ⚠ |
| to play down | daha az önemli kılmak | **önemini azaltmak** ⚠ |
| per se | sadece | **kendi başına / doğrudan** ⚠ |
| as well as | …kadar | **ve ayrıca** ⚠ |
| to favor *(a response)* | ile ilişkili olmak | **kolaylaştırmak / yönlendirmek** ⚠ |
| high *(levels)* | şiddetli | **yüksek** ⚠ |
| consistent *(feature)* | karakteristik | **değişmez / her seferinde görülen** |
| consistently *(correlate)* | uyumlu | **değişmez biçimde / tutarlı biçimde** ⚠ |
| to correlate with | orantılı olmak | **bağıntı göstermek** ⚠ *(korelasyon ≠ orantı)* |
| blurred *(distinction)* | bahsedilemez | **bulanıklaşmış** |
| festooned *(margin)* | düzgün | **festonlu / dalgalı konturlu** ⚠ |
| dichotomous | iki yönüyle / çift yönlü | **var/yok (ikili)** ⚠ |
| pattern *(of progression)* | örnek, model | **patern / dağılım** ⚠ *(model = kuramsal model)* |
| excursive *(movements)* | düzensiz | **ekskürsiyon (yana kayma)** ⚠ |
| merely *(represent)* | tamamıyla | **yalnızca / sadece** ⚠ *(kutup tersleşmesi)* |
| pronounced *(loss)* | artmış | **belirgin** ⚠ |
| validity | doğruluk | **geçerlilik** ⚠ |
| postulated | doğru kabul edilmiş | **ileri sürülmüş** ⚠ |
| the second most important | ikinci ve en önemli | **ikinci en önemli** ⚠ |
| cannot be overestimated | göz ardı edilemez | **ne kadar vurgulansa azdır** ⚠ |
| to underestimate | atlamak | **olduğundan düşük kestirmek** ⚠ |
| obscuring *(structures)* | engelleyici | **gölgeleyen / örten** |
| the evidence **in support of** X is limited | X gereksinimi sınırlıdır | **X'i destekleyen kanıtlar sınırlıdır** ⚠ |
| against *(edat, "epi")* | dayalı | **karşı** ⚠ |
| physiological | fiziksel | **fizyolojik** ⚠ |
| consistent *(philosophy)* | bağlantılı | **tutarlı** ⚠ |
| exclusively | kapsamlı olarak, öncelikle | **yalnızca** ⚠ |
| to characterize | simgelemek | **nitelemek / …-dır** ⚠ |
| corresponding *(findings)* | karşılaştırmalı | **karşılık gelen** ⚠ |
| of that time | zamanında | **o dönemin** ⚠ |
| simultaneously | kendiliğinden | **eşzamanlı olarak** ⚠ |
| within *(the subjects)* | arasında | **bireylerdeki / içindeki** ⚠ |
| inevitable | beklenen | **kaçınılmaz** ⚠ |
| to recruit *(a cohort)* | takip etmek | **çalışmaya almak** ⚠ |
| interviewing | anket | **görüşme** ⚠ |
| verification | kanıt | **doğrulama** ⚠ |
| the more "common" form | en yaygın form | **daha "yaygın" biçim** ⚠ *(karşılaştırma, üstünlük değil)* |
| approaches | çalışmalar | **yaklaşımlar** ⚠ |
| concise | açık | **kısa ve öz** ⚠ *(bu skill'in ölçülmüş hatası)* |

> ⚠ **Önekle ayrılan yakın çiftler** (inter-/intra-, supra-/sub-, hyper-/hypo-, peri-/para-) sözlük refleksi değil **dikkat hatası** üretir. Basılı Lindhe çevirisi *intercellular*'ı "hücre içi" yazmıştır. Bu önekleri taşıyan her terim, çeviri bitince ayrıca taranır.

> ⚠ **İşaretli satırlar ölçülmüştür.** Dört ayrı bölümde işaretli satırların sırasıyla **yirmi biri**, **yedisi**, **onu** ve **yirmi biri** basılı çeviride fiilen gerçekleşmiştir (§11). *condition → koşul* dört elde, *i.e. → örneğin* ikisinde tekrarlanmıştır. Tuzak gerçektir; profesyonel çeviri de bağışık değildir.

Tablodan bağlam gereği sapılıyorsa sapma `[ÇN]` ile bildirilir.

#### 6.4b Basılı kitabın ölçülmüş anlam hataları — terim kitaptan alınır, **bunlar alınmaz**

Kitabın gövde taraması (9 sayfa, 8 el) ve B12 karşılaştırmasında bulunmuştur. Denetim betiğinde her biri kural olarak vardır.

| İngilizce | Kitapta | Doğrusu |
|---|---|---|
| innate *(immunity)* | kalıtsal | **doğal** |
| certain *(Gram-negative pathogens)* | zorunlu | **belirli** |
| deregulation | ortadan kaldırılması | **düzensizleşme / bozulma** |
| cytolethal distending toxin | sitotelyal yayılma toksini | **sitoletal genişletici toksin** |
| formal genetic studies | değerli genetik çalışmalar | **formal genetik çalışmalar** *(aile, ikiz, segregasyon)* |
| inherent *(difference)* | bariz | **yapısal / doğal** |
| intercellular *(matrix)* | hücre içi | **hücreler arası** |
| gingival sulcus | DOS | **diş eti oluğu** *(DOS oluğun sıvısıdır)* |
| regional lymph nodes | çevresel | **bölgesel** |
| positive feedback loop | geri bildirim girişimi | **pozitif geri bildirim döngüsü** |
| concussion *(travma)* | travma | **konküzyon / sarsılma** |
| autoimmunization | "doğuştan bir hastalığa bağışık olma" | **otoimmünizasyon** *(tanım eklenmez)* |
| significantly *(istatistik)* | önemli ölçüde | **anlamlı ölçüde / anlamlı olarak** |
| odds ratio | olasılık oranı | **odds oranı** |
| few … recognized by many | birçok … arasında | **az sayıdaki … birçok araştırmacının kabul ettiği** |

> **En sık anlam hatası kiplik düşürmedir.** Dokuz sayfada 25 yerde *may / likely / suggest* kaybolmuş ya da kesinleşmiş (*"katkıda bulunur", "seçicidir", "gösterilmiştir", "ortaya koymaktadır"*). §5/3 bu yüzden bu skill'in en önemli maddelerinden biridir; kitap bu noktada referans **değildir**.

### 6.5 Yazım tercihleri

| Kullan | Kullanma |
|---|---|
| diş eti · yan etki · risk faktörü | dişeti, yanetki |
| diş taşı | diştaşı |
| kolajen | kollajen |
| aminoasit | amino asit |
| enflamasyon · enflamatuar · proenflamatuar | inflamasyon, enflamatuvar, inflame |
| rezorpsiyon | rezorbsiyon |
| nekrotizan | nekrotize |
| yineleyen *(apse)* | tekrarlayan |
| erişkin *(payda 20–79 yaş ise)* | kişi |
| halitozis | fetor oris |
| aproksimal | approksimal |
| birçok | bir çok |
| florür | florid |
| **kuron** ★ | kron |
| diyagram | diagram |
| yanı sıra · fark etmek · göz ardı etmek | yanısıra, farketmek, gözardı etmek |

### 6.6 Kurum sapmaları

Bir kurumun kendi sabitlediği terim biçimleri varsa **§6.3 ve §6.5'in üstündedir**. Çeviriye başlamadan önce kullanıcının kurum listesi var mı diye bakılır; varsa ona uyulur, yoksa bu dosyanın varsayılanları geçerlidir.

> Bu skill'i `akademik-turkce-denetimi` ile birlikte kullananlarda kurum listesi o dosyanın **§10.1**'indedir. Liste burada tekrarlanmaz — iki nüsha tutulursa zamanla birbirinden ayrılır.

Kurum listesi yoksa ve çeviri sırasında yeni bir terim kararı alındıysa, karar `[ÇN]` ile bildirilir ve kullanıcının listesine yazılması önerilir; bu dosya kendi kendine değiştirilmez.

## 7. Yetki sınırı — tümce kurmak senin, cila denetimin

**Bu bölüm, §6.1 ile birlikte bu skill'in en kritik yeridir.** Hedef, çıktının profesyonel çevirmen elinden çıkmış gibi okunmasıdır. Bunu terim listesine bakmak vermez; **cümle mimarisi** verir — terim *kaydı* ise §6.1'in işidir.

**Yanlış varsayım:** *"İngilizce söz dizimini korumak anlamı korur."* Korumaz. Anlamı **§5** korur. Kaynağın diziliminde donmuş bir çeviri sadık değil, **bitmemiştir** — üstelik en zor işi, kaynağı göremeyen denetim geçişine yıkar.

### 7.0 Paragrafın kip çerçevesi — v11

> *"Türkçe akıcılığı, aynı zaman kiplerinin kullanılması ile gelen uyum daha fazlaydı. Native speaker bunu anlayabiliyor fakat kelimelerle ifadesi zor."* — alan uzmanı, kitabın üç pasajı neden kazandığı üzerine (29 Eylül 2026)

İngilizce paragraf cümleden cümleye kip değiştirir (present · past · present perfect · *could*). **Türkçe paragraf bir kip çerçevesi seçer ve onu korur.** İngilizcenin kipini cümle cümle aktarmak, her cümleyi tek başına doğru ama paragrafı yamalı yapar — kör işaretlemede basımın öne geçtiği yer tam burasıdır.

| Paragrafın işi | Çerçeve | Karışmayacaklar |
|---|---|---|
| **Araştırma bulgusu aktarmak** (*X et al. found / showed / compared*; *after 2 weeks … was seen*) | **-mıştır / -mışlardır** baştan sona | -mıştı, -dı, -ebilmiştir, geniş zaman |
| **Genel bilgi, tanım, mekanizma** | **geniş zaman** (varsayılan; ad cümlesi *-dır* ile gider). -maktadır vurgu için paragrafta en çok bir kez (§7.1; denetim A6) | geniş zamanla -mıştır'ın cümle cümle değişmesi |
| **Metin içi gönderme** (*is dealt with in Chapter 12; is briefly discussed here; see below*) | başka bölüm → **ele alınmıştır / anlatılmıştır**; bu bölüm → **değinilmektedir** | geniş zaman: "ele **alınır**", "değin**ilir**" · gelecek zaman: "değin**ilecektir**", "durul**acaktır**" *(uzman kararı, 26 Ekim 2026)* |
| **Öneri, klinik yönerge** | **-malıdır / -ilmelidir** | — |

Kurallar:
- **-mıştı (hikâye birleşik kipi) akademik düzyazıda kullanılmaz.** *was almost complete* → "neredeyse tamamlanmıştır".
- **Araştırmacı özne olur.** *In a further experiment in rat calvaria, Smith et al. compared…* → "**Smith ve ark. (2015)** sıçan kalvaryasında **yaptıkları** başka bir deneyde … karşılaştır**mışlardır**" (→ "Sıçan kalvaryasında yapılan başka bir deneyde Smith ve ark. … karşılaştırmıştır" değil). *(Uzman tercih anketi.)*
- **Deney zaman çizelgesi:** *after 1 week / 2 weeks* → "**birinci haftanın sonunda** / 2. haftanın sonunda" (→ "bir hafta sonra" da yanlış değildir, ama bulgu aktaran paragrafta sıralı çizelge böyle okunur).
- **Paragrafı bitirdikten sonra yalnız yüklemleri sırayla oku.** Kip değişiyorsa bir nedeni olmalı (bulgudan yoruma geçiş, öneriye geçiş); yoksa çerçeveye çek.

### 7.1 Yap — tümce düzeyinde Türkçe kur

- **Cümleyi böl veya birleştir.** Kaynaktaki nokta bağlayıcı değildir. 30 sözcüğü aşan İngilizce cümle genellikle iki Türkçe cümledir. **Ama paragraf sınırı bölünmez** (§5/10).
- **Ad önündeki ortaç öbeğini yükleme çevir.** Addan önce en çok bir sıfat-fiil öbeği kalır.
- **Adlaştırmayı fiile çevir.** *ilerlemesinin engellenmesinin önemi* → *ilerlemesini engellemek önemlidir*.
  - **Adlaşmış yüklemden kaçın.** "Bir başka özellik de X'in Y'nin Z nedeniyle maskelen**mesidir**" anlaşılmayı zorlaştırır → "Bir başka özellik de şudur: X ve Y, Z nedeniyle maskelen**ir**." İki nokta burada Türkçedir. *(Uzman: "A kötü değil, anlaşılması zorlaşmış.")*
- **İngilizce çoğulu genel adda korumak gerekmez.** Türkçe genel adı tekil söyler: *vascularized tissue structures (72.8%)* → "vaskülarize doku **yapısı** (%72,8)"; *the regeneration processes* → "rejenerasyon **süreci**". Sayılabilir, tek tek anılan nesnelerde çoğul kalır. *(Uzman tercih anketi.)*
- **`tarafından` ile kurma.** Eylemi doğrudan özneye bağla: *hekim tarafından değerlendirilir* → *hekim değerlendirir*.
- **Odağı yüklemin hemen önüne al.** Eski bilgi başta, yeni bilgi sonda.
- **Boş yüklem kurma:** `sahip olmak`, `gerçekleştirmek`, `teşkil etmek`, `bulunmaktadır`, `yer almaktadır`, `oluşturmaktadır`.
- **İlgi cümlesini `-DIK / -AcAK` ile kur**, `ki` ile değil.
- **Eksiz ad yığınını çöz:** *artmış sondlamada kanama* → *sondlamada kanama artışı*.
- **İlgi cümlesini ada sıkıştırırken bağı denetle.** *which / from which / in which* ortaca çevrilecekse, bağın hangi öğeye gittiği kontrol edilir. Şüphe varsa **böl**.
  > ✗ *hücre dışı boşluğa salınan tropokolajen molekülündeki fibroblast içerisinde gerçekleşir* → ✓ *fibroblastın içinde gerçekleşir; molekül oradan hücre dışı boşluğa salgılanır*
- **Zarf taşıyan ilgi cümlesi bölünür.** Ortaç öbeği zarf taşıyamaz; *subsequently, laterally, gradually, initially* gibi öğeler sıkıştırmada sessizce düşer.
- **Parantez içi açıklama, açıkladığı sözcüğün hemen ardına konur.**
- **`-maktadır / -mektedir` yoğunluğunu kır — yalnız işlem tarifinde değil, düzyazının tamamında.** Türkçe bildirim cümlesinin varsayılan yüklemi geniş zamandır: *gösterir, kapsar, değişir, verir, tanımlar*. `-maktadır` vurgu için ara ara kullanılır; her cümlede kullanılırsa metin rapor diline döner ve **en görünür çeviri imzası** hâline gelir. **Ölçüm:** B39 ≈11/sayfa, B29 ≈14/sayfa, B7 ≈10–12/sayfa; bu skill'in kör çevirilerinde ≈0,2–0,35/sayfa. *(§11, v5–v7.)*
- **Sıfatın hangi ada bağlandığını denetle.** *the bottom of the **deepened** pocket*, *multirooted **teeth** with FI* gibi öbeklerde niteleyici Türkçeye geçerken komşu ada kayabilir. Öbeği kurduktan sonra sıfatı yüksek sesle ada bağla; olmuyorsa **böl**. Aynı dikkat zarfa da gerekir: *Importantly, X shows Y* = "Önemli bir nokta: X, Y gösterir" — "X **önemli biçimde** Y gösterir" değil. *(§11 v6, v7.)*
- **Failin yönünü denetle — özellikle şekil altyazılarında.** *"X walling off Y"*, *"X lined by Y"*, *"X produced by Y"*, *"X regulated by Y"* kalıplarında edilgen yapı Türkçeye geçerken fail ile nesne yer değiştirebilir. Altyazılar kısa olduğu için hata gözden kaçar. *(§11 v2, v4.)*
  > ✗ *Cep epitelini duvar gibi ayıran cep içindeki biyofilm ve diş taşı* → ✓ *Cep epiteli, cepteki diş taşını ve biyofilmi çevreden ayırmaktadır*
- **Sayısal ilişkinin yönünü denetle.** *"A% of X account for B% of Y"* kalıbında hangi öğenin özne olduğu kaynakla karşılaştırılır (§5/12). Bu hata en çok **şekil altyazılarında ve gövdedeki tekrarında** çıkar. *(Basımda aynı ilişki iki kez ters çevrildi: §11 v7.)*
- **İlgeç yönünü denetle.** *penetrates apically **to** the bottom of the pocket* = cebin tabanına **kadar**. Yön ilgeçleri (to / from / beyond / along) tek harfle önermeyi ters çevirir. *(§11 v6.)*
- **Aynı bilgiyi iki kez yazma.** Fronted bir öbeği çevirip cümle sonunda yeniden çevirmek, uzun cümlelerde sessizce olur. *(Basımda ölçüldü: §11 v7.)*

### 7.2 Yapma — bunlar denetim geçişinin işi

- Ritim ve cümle uzunluğu çeşitliliği ayarı
- Bağlaç çeşitlendirme
- Paragraf içi cümle sırası değiştirme
- Kayıt düzeltmesi, yapay zekâ imzası temizliği
- Yazım, noktalama, başlık düzeni

**Sınır:** tümce düzeyinde kurma çevirinin, metin düzeyinde cila denetimin.

**Ve bir sınır daha — yeniden kurma yorum değildir.** "Daha akıcı", "daha anlaşılır" diye sıfat, zarf veya bağlaç eklemek §5/2'nin ihlalidir ve bu skill'in ölçülmüş iki hatası tam burada çıkmıştır (*concise* → "açık"; kurum adının çevrilip genişletilmesi). Sözcüğün anlamını genişletmek, söz dizimini Türkçeleştirmek değildir.

### 7.2b Motamot kalıplar

| İngilizce | Kurma | Kur |
|---|---|---|
| underlying | altında yatan | **altındaki** |
| Once …, | Bir kez … -dığında | **-DIktan sonra** |
| the latter / the former | ikincisi / birincisi | **adını söyle** *(belirsiz gönderme)* |
| overlapping by X% | %X'i ile örtüşür | **%X'i kadar** |
| differs … in that … | … noktasında | **şu noktada ayrılır: …** |
| rule of thumb | başparmak kuralı | **pratik kural** |
| tooth-based diagnosis | diş-ile-ilişkili-teşhis | **dişe dayalı teşhis** |
| disease-free group | hastalık-olmayan grup | **hastalıksız grup** |
| 14–31-year-old male laborers | 14-31-yaş-erkek işçiler | **14–31 yaşındaki erkek işçiler** |
| in this context | bu vesile ile | **bu bağlamda** |
| from a therapeutic point of view | tedavi edici bir bakış açısıyla | **tedavi açısından** |
| under investigation | inceleme altındaki | **incelenen** |
| of utmost importance | en büyük önemi taşır | **son derece önemlidir** |
| with advanced precision | ileri hassasiyetli | **hassasiyeti artmış** |
| less accidental damage | daha az kazara hasar içeren | **istenmeden verilen hasarı azalmış** *(uzman: "kazara hasar içeren Türkçe gibi durmuyor")* |
| in the wake of the trend toward | eğilimin ardından | **eğilimle birlikte** |
| could be observed *(bulgu)* | gözlenebilmiştir | **gözlenmiştir** (§5/3) |
| X et al. compared / showed | …yapılan çalışmada X ve ark. … karşılaştırmıştır | **X ve ark. … yaptıkları çalışmada … karşılaştırmışlardır** (§7.0) |
| is dealt with in Chapter N | Bölüm N'de ele alınır | **Bölüm N'de ele alınmıştır** (§7.0) |
| indicate(s) / point(s) to | … olduğuna işaret eder *(her cümlede)* | **gösterir**; *suggest* → **düşündürür** *(kiplik korunur)* |
| a brief discussion of X is given here | X'in kısa bir tartışması verilmiştir | **burada X'e kısaca değinilmektedir** (§7.0) |

> **`the former / the latter` özel uyarısı.** Gönderge **adla** açılır, ama **doğru adla**: kaynakta "erişkin çalışmaları / genç yaş çalışmaları" karşıtlığı varsa bu "eski / yeni çalışmalar" diye zaman karşıtlığına çevrilemez. Basım bunu bir sayfada doğru, bir sonraki sayfada yanlış çözmüştür (§11 v7). Adı yazmadan önce **geriye dönüp hangi iki öğe olduğunu göster**.

> **`işaret eder` uyarısı — v10.** B20'de v7 de v9 da 4.500 sözcükte bu kalıbı **on kez** kurdu; basılı çeviri aynı sayfalarda üç kez. Alan uzmanı kör işaretlemede "…pozitif bir ilişkiye tutarlı biçimde işaret eder" cümlesi için **"İngilizce kokuyor"** dedi ve o pasajda basımı birinci sıraya koydu. *indicate* düz bir bulgu bildirir → **gösterir**. *suggest* kiplik taşır → **düşündürür / akla getirir** (§5/2 — "gösterir" yazmak kipliği düşürür). *point to* bir metinde en çok bir kez "işaret eder" olabilir. Denetim betiği üç ve üzeri geçişte İNCELE verir. *(B20 öbek işaretlemesi, alan uzmanı, 28 Eylül 2026.)*

### 7.3 Karşı risk

Yeniden kurma yetkisi anlam kayması riskini yükseltir. Karşılığı üç kilittir:

1. **§5 dokunulmazdır.** Hiçbir yeniden kurma bir önermeyi, niceleyiciyi, olumsuzluğu veya kiplik derecesini değiştiremez.
2. **Vurguyu veya kapsamı değiştiren her yeniden kurma `[ÇN]` açar.** Özne ve odak korunur: *Streptococci are among the first organisms to colonize…* = "Streptokoklar, … ilk kolonize eden organizmalar **arasındadır**"; **asla** "ilk organizmalar arasında streptokoklar **da vardır**" — ikincisi öne çıkan bir türü sıradan bir üyeye indirir. *(Uzman öbek işaretlemesi, B12, 24 Eylül 2026.)*
3. **Denetim geçişi yine koşar.**

Emin değilsen kaynağa yakın bırak ve `[ÇN]` aç. Ama *"İngilizcesi böyleydi"* tek başına gerekçe değildir.

### 7.4 Teslim öncesi yirmi kontrol

Çıktıyı vermeden önce kendine sor — ilk altısı "hayır", kalanı "evet" olmalı:

1. Kaynaktaki **her noktayı** olduğu yerde mi bıraktım? *(Bıraktıysam muhtemelen bölmem gereken cümleler var.)*
2. Ardışık cümleler **aynı uzunlukta** mı?
3. Yüklemler **boş** mu (*oluşturmaktadır, sağlamaktadır, bulunmaktadır*)?
4. Cümleler İngilizcedeki gibi **özneyle mi** başlıyor?
5. Bir cümlede **ikiden çok adlaştırma** var mı?
6. Herhangi bir terimi **hatırlamak yerine kurdum mu** (§6.1)? *(İlk dört kör sınavı da bu kaybettirdi.)*
7. Kaynaktaki **olumsuzluk, niceleyici ve kiplik taşıyan her sözcüğü** (*not, only, all, largely, likely, possible, putative, some, may, can be postulated, remains to be, demonstrated*) çeviride bulabiliyor muyum?
8. **Bağlaçların türü korundu mu** (§5/13)? *since* zaman mı neden mi, *with* eşlik mi karşıtlık mı, *as well as* sıralama mı karşılaştırma mı, *i.e.* ≠ *e.g.*
9. Aynı külliyatta **daha önce karara bağladığım terimleri aynı biçimde mi yazdım** (§6.2)? *(Önceki çevirinin terim çiftleri tablosu elimde mi?)*
10. **Metin içi terim taraması yaptım mı?** Terim çiftleri tablosundaki her Türkçe karşılığın metindeki **bütün** geçişleri sayılır; bir İngilizce terim için ikiden çok karşılık çıkıyorsa tek karşılığa indirilir.
11. **Kısaltmaları ve özel adları kaynakla harf harf karşılaştırdım mı?** Kurum kısaltmaları (FDI, WHO, EFP, AAP, CDC), yayıncı ve veri bankası adları, yazar adları. **Ve hiçbirini çevirmedim, genişletmedim mi** (§5/7)? *(Basımda FDI → **FDA**, "John Wiley **ve** Sons", "Community Periodontal **İndeks**"; bu skill'de "DSÖ Küresel Ağız **Sağlığı** Veri Bankası".)*
12. **Sayı yazımını taradım mı** (§5/5)? Ondalık **virgül**, binlik nokta, `%` önde, aralık en dash, ve sayıya gelen ekte **kesme**: `29-1'de`, `104'ü`, `6 mm'yi`, `%8'ini`.
13. **Sayısal ilişkilerin yönünü kaynakla karşılaştırdım mı** (§5/12)? "X'in %a'sı Y'nin %b'sini oluşturur" biçimindeki her cümlede özne ile nesne.
14. **Kaynakta olmayan bir yorum kattım mı?** Özellikle sıfat ve zarflarda: yazdığım niteleyicinin karşılığı kaynakta **hangi sözcük**? *(Bu skill'in ölçülmüş iki hatası burada.)*
15. **Kaynağın paragraf sınırlarını koruduğum mu** (§5/10)? Tek paragrafı ikiye bölmedim, ikisini birleştirmedim.
16. **Terim tabanına baktım ve denetim betiğini çalıştırdım mı** (§6.0)? HATA sayısı sıfır mı; her İNCELE'ye bakıldı mı?
17. **Yeniden kurduğum cümlelerde özne ve vurgu kaynaktakiyle aynı mı** (§7.3/2)?
18. **Her niteleyici kaynaktaki başına mı bağlı ve hiçbiri düşmedi mi?** Tamlama başı (*the **interpretation** of data* → "verilerin **yorumu**", "veriler" değil) ve sıfatın bağlandığı ad (*a **high** inherited component* → "yüksek" **bileşeni** niteler; "yüksek oranda kalıtsal" ya da "yüksek risk" değildir). Uzun ad öbeğini yeniden kurarken her sıfatın ve *of*-tümlecinin hangi ada gittiğini tek tek eşle. *(v9'un B20'deki iki anlam hatasının ikisi de burada: biri düşen baş, biri kayan sıfat.)*
19. **Her paragrafın yüklemlerini sırayla okudum mu** (§7.0)? Bulgu paragrafı baştan sona -mıştır mı; genel bilgi paragrafı tek çerçevede mi; -mıştı, -ebilmiştir ya da metin içi göndermede geniş zaman kaldı mı?
20. **Eşgüdümlü terimler aynı kayıtta mı?** *cross-sectional and longitudinal* → "kesitsel ve boylamsal" ("kesitsel ve longitudinal" değil) — biri Türkçe öbürü Latince olursa "uyum bozulur" (uzman). Latince ile Türkçe karşılık arasında seçim çoğu zaman **fark etmez** (matür/olgunlaşmamış, formasyon/oluşum, vaka/olgu, oryantasyon/yönelim); karışık dizmek fark eder.

### 7.5 Ölçülmüş imzalar

Basılı Türkçe çevirinin **altı ayrı bölümü, altı ayrı çevirmenin elinden**, bu skill'in **kör** çevirisiyle karşılaştırıldı.

| İmza | El A | El B | El C | El D | El E | El F | Bu skill |
|---|---|---|---|---|---|---|---|
| `tarafından` | 4 | ≥9 | 3 | 5 | ≥4 | ≥3 | **0** |
| `sahip olmak / sahip` | 7 | ≥6 | 1 | 4 | var | ≥5 | **0–1** |
| Cansız çoğul özne + çoğul yüklem | 4 | 30+ | ~0 | 2 | var | var | **0** |
| `-maktadır / -mektedir` | — | orta | ≈11/s. | **≈14/s.** | yüksek | ≈10–12/s. | **≈0,3/s.** |
| Kiplik kaybı / kayması | 1 | 8 | 1 | **11** | var | var | — |
| Ondalık ayırıcı **virgül** | — | — | — | hiç | hiç | hiç | **her yerde** |

Bunlar üslup kusuru değildir. **El A'da** donmuş söz dizimi üç sayfada beş kez içeriği bozmuştur. **El B'de** hasar sözcük düzeyine kaymıştır. **El C'de** kiplik neredeyse kusursuz taşınmış, hasar bilgi düşmesine kaymıştır. **El D'de** hasar kiplikte yoğunlaşmıştır (yedi sayfada on bir kayıp; *FDI* → "(FDA)"). **El E'de** kutup tersleşmesi, fail yönü ve sistemli bir editör-listesi hatası. **El F'de** hasar **sayısal ilişkide** yoğunlaşmıştır: aynı istatistik iki kez ters çevrilmiş, *former/latter* yanlış göndergeye bağlanmış.

**Altı elin ortak zayıflığı yok.** Taklit edilecek tek bir üslup yok — ama **altısının ortak olduğu üç nokta** var ve üçü de bu skill'in lehine: `tarafından`, `-maktadır` yoğunluğu, ve §5/5'in sayı yazımı.

**Okuma:** §7 çalışıyor ve **tek başına yetmiyor**. Söz dizimi temizken bile tek bir terim metni ele verir (§6.1).

## 8. Çıktı biçimi

```
## ÇEVİRİ
<çevrilmiş metin>

## ÇEVİRİ NOTLARI
[ÇN-1] <belirsiz, çok anlamlı veya kaynakta hatalı görünen yer; vurgu değiştiren yeniden kurma>
(yoksa: yok)

## TERİM ÇİFTLERİ
| İngilizce | Türkçe karşılık | İlk geçiş | Kaynak (taban / karar / skill) |
```

**Çeviriye başlamadan önce:** kaynağın **bölüm künyesi** okunur. Çok yazarlı bir ders kitabının Türkçe basımıyla karşılaştırma yapılıyorsa, **her bölümü ayrı kişi çevirmiş olabilir** ve açılış sayfasında adı yazar. Çevirmenin adı ve kurumu kayda geçirilir; kalibrasyon ölçümlerinde tanıklar **ele göre** ayrılır, tek bir "basım kararı" gibi toplanmaz.

**Terim çiftleri tablosu saklanır.** Aynı külliyattan sonraki bir metin çevrilirken önceki tablo okunur ve kararlar taşınır (§6.2).

**Kör çeviri protokolü.**

1. Çeviri, basılı sayfalar **açılmadan önce** dosyaya yazılır ve kilitlenir (özet değeri kaydedilir).
2. **Kilitli dosya, basım açıldıktan sonra hiçbir gerekçeyle düzeltilmez** — kuralın kendi ihlalini içerse bile; ölçülen şey tam olarak odur. Yanlışlıkla düzeltilirse geri alınır ve olay kayda geçirilir. Basım **açılmadan önce** yapılan düzeltme serbesttir, ama iki özet değeri de kaydedilir.
3. **Sınav pasajları önceden ve rastgele çekilir.** Çeviriyi yapan taraf pasajı seçemez. Yöntem: sabit bir tohumla (sayfa, sütun, o sütunun *q*. tam paragrafı) üçlüler çekilir ve çekiliş **kilitli dosyanın başlığına** yazılır. *(Gerekçe: beşinci sınavda pasajları çeviren taraf seçmişti ve seçim yanlıydı — basımın söz diziminin en ağır olduğu yer seçilmişti. §11 v7.)*
4. **Çekilen pasaj elde yoksa sınav ertelenir; yerine başkası konmaz.** Eksik sayfa fotoğrafı sınavı böler, içeriğini belirlemez.
5. Pasajın sınırı **kaynağın** paragraf yapısına göre belirlenir (PDF'te satır dolgusundan doğrulanır), basımın dizgisine göre değil.

**`[ÇN]` açılacak durumlar:** kaynak cümle iki biçimde okunabiliyorsa; yerleşik karşılık yoksa ve karar verildiyse; §6.3 veya §6.4'teki bir karardan sapıldıysa; **yeniden kurma vurguyu veya kapsamı değiştirdiyse**; kaynakta olgusal hata veya iç tutarsızlık görülüyorsa; bir kısaltma açılmadan kullanılıyorsa; **iki İngilizce terim aynı Türkçe sözcüğe düşüyorsa ve ayrım sabitlendiyse** (§6.2). Karar verilemeyen yerde metinde yorum yapılmaz, `[ÇN]` ile bildirilir; **ancak** kaynaktaki kusur (yeri yanlış niteleyici, göndergesi kayan *which*) olduğu gibi aktarıldığında Türkçe cümle açıkça yanlış bir iddia kuruyorsa, en olası okuma yazılır ve `[ÇN]` ile bildirilir (Panel-1: yeri yanlış "such as" altı çevirinin üçünde taşındı; değerlendirici hata saydı). *(Ölçülmüş değer: bir bölümde `[ÇN]` ile açılan üç kaynak kusuru basılı çeviride de düzeltilmemiş olarak bulundu; başka bir bölümde CPITN skor aralığı kusurunu basım da fark etmemişti.)*

## 9. Denetime devir

Çeviri bittikten sonra dil denetimi **ayrı bir geçişte** koşar. Devir kuralı:

- Denetime **yalnız ÇEVİRİ bölümü** verilir; kaynak İngilizce metin ve çeviri gerekçeleri verilmez.
- `[ÇN]` notları kullanıcıya gider, **denetime gitmez**.
- Terim çiftleri tablosu denetime verilebilir; tutarlılık taramasında işe yarar.
- Aynı sohbette çalışılıyorsa denetim temiz bağlamda alt görev olarak koşturulur.

## 10. Yasaklar

- Kaynağı özetlemek, kısaltmak, "daha akıcı olsun" diye budamak.
- Kendi bilgisiyle kaynağı düzeltmek veya tamamlamak (görülen hata `[ÇN]` olur, düzeltme olmaz; tek istisna §8'deki anlamı bozan kaynak kusurudur).
- Terim çiftleri tablosunu tutmadan farklı yerlerde farklı karşılık kullanmak.
- Öğrenciye seslenen bir ton, retorik soru, motive edici cümle eklemek.
- Çıktıya çeviri dışında açıklama, özür veya değerlendirme yazmak.
- Denetim geçişini aynı yanıtta birleştirmek.
- §6.6'daki kurum kararını genel dil tercihiyle ezmek.
- **Söz dizimini İngilizceden kopyalayıp "sadık kaldım" demek** (§7).
- **Terimi İngilizce bileşiğin biçiminden türetip "kaynağa sadık kaldım" demek** (§6.1).
- **Sözcüğün anlamını genişletip "daha anlaşılır oldu" demek** (§5/2, §7.2).
- **Kurum, yayıncı veya veri bankası özel adını çevirmek ya da genişletmek** (§5/7).
- **Kaynağın paragrafını bölmek veya birleştirmek** (§5/10).
- **Türkçe cümlenin içinde İngilizce sözcük bırakmak** (*microarray, peripheral, resident, predominant, Table*) — karşılığı yoksa §6.2 uygulanır.
- **Akademik metne konuşma dili sokmak** (*kafa karıştırıcı, soru işareti, olmazsa olmaz, merak konusu*).
- **Düzyazıyı `-maktadır` ile doldurmak; işlem tarifini bu ekle yazmak** (§7.1).
- **Aynı külliyatta aynı terimi iki farklı biçimde yazmak** (§6.2).
- **Aynı metnin içinde aynı terimi iki farklı biçimde yazmak** — teslim öncesi taranmadan çıkmak (§7.4/#10).
- **Kurum kısaltmasını veya yazar adını kaynakla karşılaştırmadan yazmak** (§7.4/#11).
- **Kilitli kör çeviriyi basım açıldıktan sonra düzeltmek; sınav pasajını çeviren tarafın seçmesi** (§8).

## 11. Sürüm ve kanıt

Ayrıntılı sürüm geçmişi (v1–v7, kör sınavlar, basım karşılaştırmaları) geliştirme projesinde tutulur; kaynak kitaptan uzun alıntılar içerdiği için bu pakette yoktur. Buradaki `§11 vN` göndermeleri o kayda işaret eder. Ölçüm yöntemi: `yontem/kor-olcum-yontemi.md`.

| Sürüm | Kaynak | Ana değişiklik |
|---|---|---|
| v1–v2 | Dizin ve Bölüm 1 düzyazı karşılaştırması | §6.3 sözlüğü, §7 tümce kurma kuralları |
| v3–v4 | Kör sınav B1, B13 | §6.1 "hatırla, türetme" |
| v5–v6 | Kör sınav B39, B29 | Külliyat tutarlılığı, `-maktadır` imzası, öz-test |
| v7 | Kör sınav B46, B7 · 22 uzman kararı | Yön kuralı (kavram adı ↔ sıradan sözcük), özel ad, paragraf sınırı, sayısal ilişki yönü |
| **1.0** | Panel-1: üç dış değerlendirici, kör, 6 bölüt (akıcılık v11 10 · v10 7 · eşit 1; genel 8–8) · gürültü tabanı: v10 ×3, v11 ×3 — metin uzaklığı arası/içi 1,06; tarafsız kör anlam puanı altısında 0 | Geliştirme donduruldu. §8'de kaynak kusuru istisnası; denetimde üç İNCELE (*düşük kaliteli*, yalın *ilk on makale*, noktalı virgülden sonra *X da/de*) |
| **v11** | B53 kör yarışı: 4/4 koşul ✅, öbek sırası v11 1,0 · v10 1,67 · kitap 2,0 · Akıcılık analizi (5 yarış, 30 metin) · uzman tercih anketi (18 çift, 29 Eylül) | **§7.0 paragrafın kip çerçevesi**; §5/3 *indicates/suggests* ve *could be observed*; §7.1 adlaşmış yüklem, genel adda tekil; §7.2b yedi yeni kalıp; §7.4/#19–20 |
| **v10** | B48 kör yarışı: 4/4 koşul ✅ (öbek sırası payın sınırında) · B20 öbek işaretlemesi · v9'un B20 anlam hataları · B20 s. 382–388 gövde hasadı | §7.2b *indicate → gösterir*, *brief discussion → kısaca değinilir*; §7.4/#18 niteleyici bağlama; denetimde `işaret eder` yoğunluğu ve `tartışması verilmiştir` İNCELE'si |
| **v9** | B20 kör yarışı: 4/4 koşul ✅ · B38 + B42 ölçümleri · 129 sayfalık Cilt 2 + gövde taraması (29 çevirmen eli) · 26 Eylül ilkesi | §6.0 üç kademe (tercih / kabul / hata), Türkçesi yerleşikse yabancı kökenli seçilmez, taban `kabul` sütunu, denetimde TERCİH düzeyi ve olgu bilgisi sınıfı |
| **v8** | B12 ölçümü · dizin hizalaması · 9 sayfalık gövde taraması · 24 Eylül kararları | **§6.0** (kitap = terim referansı, hiyerarşi, taban + denetim), §6.4b (kitabın anlam hataları), *response → cevap*, *diagnosis → teşhis*, *attachment level → seviye*, *junctional → birleşim*, kiplik ve vurgu kuralları |

**Bakım kuralı (1.0'dan sonra):**
- Bu metin büyümez. Yeni bir kural ancak var olan bir kuralın yerini alırsa ya da onunla birleşirse girer.
- Tekil sözcük ve kalıp düzeltmeleri skill metnine değil, **terim tabanına** ve **denetim betiğine** (testiyle birlikte) gider.
- Skill metnine yalnız, gerçek kullanımda en az iki kez görülen ya da A düzeyinde anlam hatası üreten bir hata sınıfı girer; değişiklik kilitli bir bölümde eski metne karşı sınanır.
- Üslup ve akıcılık cilası bu skill'in değil, ikinci geçişin (`akademik-turkce-denetimi`) işidir.
- Geliştirme yeniden açılırsa, önce gürültü tabanı ölçülür: yeni sürümün farkı aynı sürümün iki çevirisi arasındaki farktan büyük değilse değişiklik kanıtlanmış sayılmaz.

**B12 ölçümü (v7 ve v7 + taban, kör puanlama):** kitapla terim uyumu %67–76; anlam hatası 3 ve 1 (6.300 sözcük); uzmanın kör sıralaması: bu skill 1,5 ve 2,0 — basım 2,5. Taban, kapsadığı terimlerde uyumu %76 → %81 çıkardı; genel uyumun tavanını kitabın kendi içindeki el farkı belirliyor → §6.0/3.
