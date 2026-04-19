# sop-en-013-udara-tekan

**Status:**   
**Kategori:**   
**Exported:** 2026-04-19 06:54

---

# SOP/EBI/EN-013 — Pengoperasian dan Perawatan Sistem Udara Tekan
**Summary**: Source summary untuk SOP pengoperasian dan perawatan sistem udara tekan (compressed air) di PT Etana Biotechnologies Indonesia.
**Sources**:
- `SOP-EBI-EN-013 Pengoperasian Dan Perawatan Terhadap Sistem Udara Tekan.DOC` (versi lama, tanpa nomor revisi)
- `SOP-EBI-EN-013 Pengoperasian Dan Perawatan Terhadap Sistem Udara Tekan.pdf` (**Rev.04**, 37 halaman — sumber utama)
**Last updated**: 2026-04-14
---
## Identitas Dokumen
| Field | Value |
|---|---|
| SOP No. | SOP/EBI/EN-013 |
| Revision | **04** (sumber: PDF Rev.04) |
| Total halaman | 26 halaman prosedur + lampiran |
| Signatories | Riki Depano (Engineering Supervisor) · Purno Budi Kiswanto (Engineering Manager) · Happy Monda Pintauli (QA Manager) |
## Tujuan
Petunjuk pengoperasian dan perawatan sistem udara tekan berikut peralatan pendukungnya agar sesuai standar PT EBI: Ingersoll Rand IRN37 OF-A10, Atlas Copco ZT37KW, Refrigerator Dryer, Desiccant Dryer, dan Atlas Copco Dryer CD 130+ - 70.
(source: SOP-EBI-EN-013 ...pdf Rev.04)
## Peralatan yang Dicakup
| Peralatan | Keterangan |
|---|---|
| Ingersoll Rand IRN37 OF-A10 | Compressor variable speed (Unit 1 & 2) |
| Atlas Copco ZT37KW | Compressor variable speed (Unit 3) |
| Refrigerator Dryer D780IN-A | 2 unit, dijalankan bergantian tiap 1 hari |
| Heatless Desiccant Dryer D500IL | Unit utama |
| Atlas Copco Dryer CD 130+ - 70 | Heatless desiccant dryer — sebagai **cadangan** (backup); digunakan jika D500IL mengalami kendala |
## Klasifikasi Udara Tekan
| Tipe | Penggunaan | Standar |
|---|---|---|
| **Kontak Produk** | Kontak langsung dengan produk steril (mis. proses autoclave) | ISO 14644:1 (partikel); ISO 8573-1:2010 (uap air & oli) |
| **Non-Kontak Produk** | Tidak kontak langsung dengan produk (mis. pneumatik) | ISO 8573-1:2010 |
Klasifikasi lengkap sesuai Point of Use (POU) lihat lampiran `SOP/EBI/EN-004-L01` dan `SOP/EBI/EN-004-L02`.
## Operasional
- 3 unit compressor: **Udara Tekan 1** (IR IRN37), **Udara Tekan 2** (IR IRN37), **Udara Tekan 3** (Atlas Copco ZT37KW).
- Compressor dan Refrigerator Dryer dijalankan **bergantian setiap 1 hari**.
- **Akses setting/parameter mesin** hanya bisa dilakukan oleh **Supervisor**; Operator/Teknisi hanya bisa memantau dan melaporkan penyimpangan ke formulir.
### Prosedur Start-Up Compressor (IR37-OF / Atlas Copco ZT37KW)
1. Pastikan katup-katup pada jalur pipa udara tekan telah **terbuka**.
2. Pastikan kompressor dalam keadaan **Unloading**.
3. Cek semua parameter dan indikator pada display — pastikan sesuai standar.
4. Jika display menampilkan "**Ready To Start**" → tekan tombol **Start** (hijau).
### Prosedur Shut-Down Compressor
- Normal: tekan **Unloaded Stop** hingga Sump Pressure < **2,9 bar** → tekan **Stop** (merah).
- Darurat: tekan **Emergency Stop**.
### Prosedur Start-Up Refrigerant Air Dryer D780IN-A
1. Pastikan katup inlet dan outlet terbuka.
2. Putar saklar main power ke posisi **On**.
3. Cek semua parameter dan indikator.
4. Tekan tombol **Start/Stop** (merah) satu kali pada panel P&ID.
### Prosedur Start-Up Heatless Desiccant Dryer (D500IL / Atlas Copco CD 130+ - 70)
1. Pastikan katup inlet dan outlet terbuka.
2. Putar saklar utama ke posisi **I (ON)**.
3. Cek semua parameter dan indikator.
4. Tekan tombol **nomor 1 (ON)** pada panel display. Untuk mematikan, tekan **nomor 7 (OFF)**.
## Parameter Pemantauan Harian
### IR37-OF — Monitoring Parameters
| Parameter | Standar / Limit |
|---|---|
| Package discharge pressure | 7–10 bar |
| Inlet vacuum pressure | alert ≤ 0,05 bar; action ≤ 0,07 bar |
| 1st discharge temperature | 105–250 °C |
| 2nd stage inlet pressure | alert ≤ 3,0 bar; action ≤ 3,2 bar |
| 2nd stage discharge pressure | 7–10 bar |
| 2nd stage discharge temperature | 105–280 °C |
| Oil Filter Drop pressure | alert ≤ 3,0 bar; action ≤ 3,2 bar |
| Oil level | terlihat pada sight glass (tambah jika tidak terlihat) |
| Tank non-contact product pressure | 7–9 bar |
| Tank contact product pressure | 7–9 bar |
### Atlas Copco ZT37KW — Monitoring Parameters
| Parameter | Standar / Limit |
|---|---|
| Oil level | terlihat pada sight glass |
| Tank non-contact product pressure | 7–9 bar |