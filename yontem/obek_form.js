// obek_form.js — kör yarış öbek işaretleme formu (.docx). Her yarışta kopyalanan obek.js'lerin yerini alır.
//
// Kullanım:
//   node obek_form.js obek.json cikti.docx "B53" "Bölüm 53, Restoratif Diş Hekimliğinde İmplantlar"
//
// obek.json: { "1": {"en": "...", "surumler": [["X", "<gizli kim>", "metin"], ["Y", ...], ["Z", ...]]}, "2": {...} }
// Sürümlerin kime ait olduğu (ikinci alan) forma yazılmaz; anahtar ayrı dosyada tutulur.
const fs = require('fs');
const {Document, Packer, Paragraph, TextRun, HeadingLevel, BorderStyle} = require('docx');

const [girdi, cikti, kod, bolum] = process.argv.slice(2);
if (!girdi || !cikti || !kod || !bolum) {
  console.error('kullanım: node obek_form.js obek.json cikti.docx <B53> "<Bölüm 53, başlık>"');
  process.exit(1);
}
const d = JSON.parse(fs.readFileSync(girdi, 'utf8'));
const n = Object.keys(d).length;
const SAYI = ['sıfır', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı'];
const P = (t, o = {}) => new Paragraph({spacing: {after: 120, line: 300}, ...o.p,
  children: [new TextRun({text: t, font: 'Calibri', size: 22, ...o.r})]});

const kids = [
  new Paragraph({heading: HeadingLevel.TITLE, children: [new TextRun({text: `${kod} — Öbek işaretleme`, font: 'Calibri'})]}),
  P(`${bolum}. Aşağıda ${SAYI[n] || n} pasaj var. Pasajlar çeviri yapılmadan önce rastgele seçildi. Her pasajın üç Türkçe sürümü X, Y ve Z olarak verildi; hangisinin kime ait olduğu bu belgede yazmıyor.`),
  P('Her sürümde şunları yapın:', {r: {bold: true}}),
  P('1. Çeviri kokan, Türkçede doğal durmayan öbekleri SARI ile vurgulayın. Tek sözcük de olabilir, kalıp da.'),
  P('2. İngilizceye göre anlamı yanlış olan öbekleri KIRMIZI ile vurgulayın.'),
  P('3. Her pasajın sonundaki satıra sürümleri en iyiden en zayıfa sıralayın (1–3). İsterseniz kısa bir not ekleyin.'),
  P('Paragraf bölmesine ve biçime bakmayın; yalnız dile bakın.', {r: {italics: true}}),
];
for (const k of Object.keys(d)) {
  kids.push(new Paragraph({heading: HeadingLevel.HEADING_1, pageBreakBefore: k !== Object.keys(d)[0],
    children: [new TextRun({text: `Pasaj ${k}`, font: 'Calibri'})]}));
  kids.push(P('İngilizce kaynak', {r: {bold: true, color: '555555'}}));
  kids.push(P(d[k].en, {r: {color: '555555', size: 20}}));
  for (const [harf, , metin] of d[k].surumler) {
    kids.push(new Paragraph({heading: HeadingLevel.HEADING_2, children: [new TextRun({text: `Sürüm ${harf}`, font: 'Calibri'})]}));
    kids.push(P(metin));
  }
  kids.push(new Paragraph({spacing: {before: 240}, border: {top: {style: BorderStyle.SINGLE, size: 6, color: '999999', space: 4}},
    children: [new TextRun({text: 'Sıralama (1 = en iyi):   X: ___   Y: ___   Z: ___          Not: ', font: 'Calibri', size: 22, bold: true})]}));
}
const doc = new Document({sections: [{properties: {page: {margin: {top: 1134, bottom: 1134, left: 1134, right: 1134}}}, children: kids}]});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(cikti, b); console.log(cikti); });
