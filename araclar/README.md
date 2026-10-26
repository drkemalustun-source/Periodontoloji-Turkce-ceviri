# Denetim betiği

`denetim.py`, bir çeviriyi İngilizce aslıyla karşılaştırır ve daha önce gerçek çevirilerde ölçülmüş hata türlerini arar: düşürülen kiplik (*may* → kesin yargı), çevrilmiş özel adlar, yanlış ondalık ayırıcı, alanda olmayacak terim karşılıkları ve benzerleri.

Bulguların üç düzeyi var:

- **HATA:** neredeyse kesin kural ihlali, düzeltilmeli.
- **İNCELE:** bakılmalı; yanlış alarm olabilir.
- **TERCİH:** hata değil; kabul edilen bir eş anlamlı biçim kullanılmış, baskın biçim öneriliyor.

Karar her zaman insanındır. Betik, ilk kez karşılaşılan bir terimin yanlış karşılığını yakalayamaz.

## Kullanım

Python 3 yeterlidir; ek paket gerekmez.

```
python3 denetim.py --en kaynak.txt --tr ceviri.md --out rapor.md
```

- `kaynak.txt`: İngilizce asıl metin.
- `ceviri.md`: Türkçe çeviri. Çeviri skill'inin çıktısıysa yalnız `## ÇEVİRİ` bölümü denetlenir.
- `rapor.md`: bulguların yazılacağı dosya.

Raporun başında `Terim tabanı: … (N terim)` satırı görünmelidir. Betik, yanındaki `terim-listesi.tsv` dosyasını kendiliğinden kullanır. Bu liste çeviri skill'inin §6.3 sözlüğünden üretilmiştir. Kendi terim listeniz varsa aynı sütunlarla (`ingilizce`, `hedef`, `kabul`, `durum`) hazırlayıp `--taban liste.tsv` ile verin.

## Testler

```
python3 test_denetim.py
```

143 vakanın hepsi geçmelidir. Testler `testveri/` klasöründeki küçük örnek listeyle çalışır.
