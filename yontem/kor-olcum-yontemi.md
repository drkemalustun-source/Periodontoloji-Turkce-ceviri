# Kör ölçüm yöntemi

Bir çeviri talimatının (skill) yeni sürümü gerçekten daha iyi mi, yoksa öyle mi görünüyor? Bu belge, bu soruyu yanlılığa düşmeden yanıtlamak için kullandığımız yöntemi anlatır. Yöntem herhangi bir kitap ya da makaleyle uygulanabilir; burada örnek metin yoktur.

## Temel fikir

İki sürüm aynı İngilizce metni çevirir. Değerlendirici hangi çevirinin hangi sürüme ait olduğunu bilmez. Neyin "kazanmak" sayılacağı, çeviriler yapılmadan önce yazılır ve sonradan değiştirilmez.

## Adımlar

**1. Ön kayıt.** Çeviriye başlamadan önce kısa bir metin dosyasına şunlar yazılır:

- Neyin karşılaştırıldığı (örneğin yayındaki sürüm ile yeni taslak).
- Hangi metnin çevrileceği ve nasıl seçildiği.
- Hangi ölçülerin kullanılacağı.
- Yeni sürümün hangi koşullarda kabul edileceği (aşağıdaki "yayın kararı").

**2. Metin kurayla seçilir.** Çeviriyi yapan taraf metni seçemez. Bölüm ya da pasaj, sabit bir sayıyla (tohum) çalışan rastgele çekilişle belirlenir ve tohum ön kayda yazılır. Gerekçe: bir denemede pasajları çeviren taraf kendisi seçmiş ve farkında olmadan karşılaştırmayı kendi lehine çevirmişti. Çekilen pasaj elde yoksa deneme ertelenir; yerine başka pasaj konmaz.

**3. Karşılaştırma metni çeviriden sonra açılır.** Elinizde aynı metnin basılı bir Türkçe çevirisi varsa, o sayfalar çeviriler bitip kilitlenene kadar açılmaz.

**4. Çeviriler ayrı ayrı yapılır.** Her sürüm, öbürünü görmeyen temiz bir oturumda çalışır. Aynı terim listesini ve aynı İngilizce dosyayı kullanırlar; fark yalnız talimat metnindedir.

**5. Kilit.** Çeviriler bitince her dosyanın parmak izi (MD5 özeti) bir kilit dosyasına yazılır. Kilitli çeviri sonradan hiçbir gerekçeyle düzeltilmez. Ölçülen şey tam olarak odur.

**6. Kör puanlama.** Üç ölçü kullandık:

- **Anlam hatası.** Çeviriler harf etiketiyle (A, B, …) bir puanlayıcıya verilir. Hatalar ağırlıklandırılır: klinik ya da bilimsel olarak yanıltan hata (A) 3 puan, önermenin anlamını açıkça değiştiren hata (B) 2 puan, küçük kayma (C) 1 puan.
- **Terim uyumu.** Çevirideki terimler bir referans terim listesiyle karşılaştırılır. Farklı ama kabul edilebilir eş anlamlı biçim hata sayılmaz; alanda olmayacak bir sözcük hata sayılır.
- **Öbek işaretlemesi.** Bir alan uzmanı, kurayla seçilmiş iki ya da üç pasajın sürümlerini X, Y, Z etiketleriyle okur. Çeviri kokan öbekleri sarıya, anlamı yanlış öbekleri kırmızıya boyar ve sürümleri en iyiden en zayıfa sıralar. Etiketler her pasajda ayrı karıştırılır. Form `obek_form.js` ile üretilir; anahtar ayrı dosyada tutulur ve işaretleme bitene kadar açılmaz.

**7. Yayın kararı.** Önceden yazılmış koşullar uygulanır. Bizim kullandığımız dört koşul şunlardı. Yeni sürüm ancak dördü birden sağlanırsa yayınlandı:

1. Ağırlıklı anlam puanı eski sürümden en fazla 1 puan kötü.
2. Terim uyumu eski sürümden en fazla 2 yüzde puanı düşük.
3. Uzmanın ortalama sıralaması eski sürümden en fazla 0,5 kötü.
4. Olmayacak terim hatası eski sürümden fazla değil.

## Gürültü tabanı: geliştirmeyi ne zaman durdurmalı?

Aynı talimat aynı metni iki kez çevirince bile iki farklı metin çıkar. Bu "çevirmen gürültüsü"dür. Sürümler arasındaki fark bu gürültüden büyük değilse, yeni sürümün daha iyi olduğu kanıtlanmış sayılmaz.

Ölçmek için her sürüm aynı metni üç kez çevirir. Sonra şu karşılaştırılır:

- **Sürüm içi fark:** aynı sürümün çevirileri birbirinden ne kadar farklı?
- **Sürümler arası fark:** iki sürümün çevirileri birbirinden ne kadar farklı?

Arası/içi oranı 1,15'in altında kaldıysa sürümler metin düzeyinde birbirinden ayırt edilemiyor demektir. Bizde bu oran 1,06 çıktı ve geliştirme durduruldu. Bir değişiklik bu sınamayı geçti: paragrafın tek kip çerçevesinde yazılması (çeviri skill'i §7.0). Yeni sürümün üç çevirisinde de geçmiş zamanlı (-dı) cümle sonu sıfırdı; eski sürümünkilerde 5, 5 ve 2.

## Dış okur paneli

Tek bir uzmanın yargısı yetmeyebilir. Panelde üç dış okura, hangisinin yeni olduğu söylenmeden "aynı metnin iki farklı Türkçe çevirisi" verildi. Form iki bölümden oluşur:

1. Yalnız Türkçe: "Hangisi daha doğal, akıcı Türkçe?" (X / Y / Eşit) ve kısa bir gerekçe.
2. İngilizce aslıyla birlikte: anlam ya da terim hatası var mı, genel tercih hangisi?

Gerekçeler, anahtar açılmadan önce kodlanır (kip uyumu, söz dizimi, sözcük seçimi, terim, anlam, noktalama…). Üç okur ve altı bölütle istatistiksel gücün düşük olduğu raporda açıkça yazılır.

## Öğrendiklerimiz

- **Yapay zekâ puanlayıcısı insanın yerini tutmuyor.** Puanlama talimatındaki örnekler değişince aynı çeviride bulunan anlam hatası sayısı 3'ten 0'a düştü. Kör puanlayıcı kullanılacaksa talimatı tarafsız tutun ve sonucu bir insan okuruyla doğrulayın.
- **Terim sorunu kuralla değil veriyle çözülür.** Kayıpların çoğu ilk kez karşılaşılan terimlerdeydi. Kitabın kendi gövde metninden çıkarılmış bir terim tabanı uyumu belirgin biçimde artırdı.
- **Basılı çeviri altın standart değildir.** Profesyonel çevirilerde de bölüm başına birkaç anlam hatası ve kiplik düşürme ölçtük. Terimi basımdan alın, anlamı her zaman İngilizceden.
