# Diş hekimliği metinleri için Türkçe çeviri ve dil denetimi

Bu paket, İngilizce diş hekimliği metinlerinin yapay zekâ (Claude) ile daha iyi Türkçeye çevrilmesi için hazırlandı. Amaç basit: çeviri, yapay zekâ çevirisi gibi değil, alanı bilen bir çevirmenin elinden çıkmış gibi okunsun.

Kurallar, 2026 Eylül–Ekim aylarında bir periodontoloji ders kitabının bölümleri üzerinde yapılan kör karşılaştırmalarla sınandı. Hangi kuralın gerçekten işe yaradığı ölçüldü; işe yaramayanlar çıkarıldı.

## İçindekiler

| Klasör | Ne işe yarar |
|---|---|
| `skills/dis-hekimligi-ceviri-tr/` | **Çeviri talimatı.** İngilizceden Türkçeye çevirir: anlam ve kesinlik derecesi korunur, cümle Türkçe söz dizimiyle kurulur, terimler alanın yerleşik karşılıklarıyla verilir. 300'ü aşkın satırlık bir alan sözlüğü ve sık yapılan yanlış anlam tuzakları içinde. |
| `skills/akademik-turkce-denetimi/` | **Dil denetimi talimatı.** Bitmiş Türkçe metni yalnız dil bakımından denetler: söz dizimi, anlatım bozuklukları, yapay zekâ izleri, yazım ve noktalama. Her düzeltmeyi gerekçesiyle bildirir. |
| `araclar/` | **Denetim betiği** (`denetim.py`). Çeviriyi İngilizce aslıyla karşılaştırır ve ölçülmüş hata türlerini otomatik arar. İsteğe bağlıdır. |
| `yontem/` | **Kör ölçüm yöntemi.** Bir çeviri talimatının yeni sürümünün gerçekten daha iyi olup olmadığını yanlılığa düşmeden nasıl ölçtüğümüzün anlatımı. |

## Nasıl kullanılır

**En kolay yol: Claude'a skill olarak eklemek.**

1. `dis-hekimligi-ceviri-tr.zip` ve `akademik-turkce-denetimi.zip` dosyalarını indirin.
2. Claude'da (claude.ai) **Ayarlar → Yetenekler (Capabilities) → Skills** bölümünden her birini yükleyin.
3. Bundan sonra Claude'a "Bu metni Türkçeye çevir" demeniz yeterli. Claude çeviri talimatını kendiliğinden kullanır.

**İki aşamayı ayrı tutun.** En iyi sonuç için önce çeviriyi yaptırın. Sonra **yeni bir sohbette**, İngilizce aslını vermeden, "Bu Türkçe metni dil bakımından denetle" deyin. Aynı sohbette hem çevirip hem denetlettiğinizde model kendi hatalarını göremiyor.

**Skill kullanamıyorsanız:** `SKILL.md` dosyasının içeriğini kopyalayıp sohbetin başına yapıştırabilirsiniz. Sonuç biraz daha zayıf olur, ama kurallar yine uygulanır.

## Denetim betiği (isteğe bağlı)

Bilgisayarında Python kurulu olanlar için. Kullanım `araclar/README.md` dosyasında.

## Bilinmesi gerekenler

- **Bu bir yardımcıdır, uzmanın yerini tutmaz.** Klinik ya da yayın amaçlı her çeviri bir alan uzmanınca okunmalıdır.
- **Terim kararları bir kurumun tercihlerini yansıtır.** Örneğin *diagnosis* için "teşhis", *response* için "cevap" seçildi. "Tanı" ve "yanıt" hata sayılmaz. Kendi kurumunuzun tercihleri farklıysa denetim talimatının §10.1 bölümünü değiştirin.
- **Kitap metni pakette yoktur.** Ölçümlerde kullanılan kaynak kitap ve onun Türkçe çevirisi telifle korunduğu için paylaşılmamıştır. Talimatlarda ve testlerde yalnız tek tek terimler ve kısa örnek ifadeler bulunur. Basılı çeviriden ölçülen hatalar çevirmen adı verilmeden, "El A, El B…" diye anılır.
- **Sürüm:** 1.0 (Ekim 2026). Geliştirme bu sürümde donduruldu. Ölçümler, sonraki değişikliklerin farkının çevirmen gürültüsü içinde kaldığını gösterdi.

## Lisans

`LISANS.md` dosyasına bakın.
