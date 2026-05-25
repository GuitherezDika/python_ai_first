struktur
three_basic
    day08_oop.py
    

===== ASDICT ========
key pada object di mapping dan key diubah bentuk string 
from dataclasses import dataclass, asdict

@dataclass
class T:
    x: int
    y: str

t = T(1, 'dika')
print(asdict(t))
# {'x': 1, 'y': 'dika'}

beli 
==============================
BELI TANAH
Pengecekan Umum Checked:
1. Sertifikat Ganda
2. Tanah Sengketa Warisan
3. Tanah masuk dalam kawasan terlarang/ jalur hijau

Cek Arsip:
1. Nama Pemilik Tanah yang tertera dalam sertifikat == nama di KTP Penjual
2.  Jenis Sertifikat Tanah: apakah
    SHM (Sertifikat Hak Milik) = yang paling kuat
    HGB (Hak Guna Bangunan) = perpanjang / 30 tahun
3.  Apakah tanah sedang diagunkan ke bank? 
    Cek di BPN atau nanya ke notaris
4.  Status Hukum Tanah - 
    Tidak dalam sengketa, tidak dijaminkan, bukan tanah warisan yang belum di bagi secara sah
5. Cek Sertifikat manual ke Kantor BPN / Layanan Online BPN dan peta bidang (Biaya cek mulai 50.000)
6. Legalitas aman => Survei & Pengukuran Ulang

Cek Kondisi Ril Lapangan:
1. batas tanah harus jelas sesuai arsip
2. ada / tidak ada bangunan lain berdiri di atas tanah
3. tumpang tindih dengan tanah tetangga?
4. harus mengajak RT/RW dan tetangga sekitar sebagai saksi batas
5. Pengajuan Pengukuran Ulang ke BPN (biaya mulai Rp. 1jt)
6. Biaya pasang patok. pagar batas tanah

PROSES AGREEMENT
1. Pernjanjian dan Booking Fee (Tanda Jadi ke Penjual misal Rp. 10jt)
2. PPJB (Perjanjian Pengikatan Jual Beli via Notaris start Rp. 1jt ) secara sah sebelum AJB (Akta Jual Beli) dilakukan.
3. Pembuatan AJB di depan PPAT (Pejabat Pembuat Akta Tanah) bukan notaris
4. PPAT akan mengecek ulang legalitas 

LAMPIRAN DOKUMEN di PPAT:
1. Sertifikat Tanah Asli
2. KTP & NPWP penjual dan pembeli
3. SPPT (Surat Pemberitahuan Pajak Terutang dasar Penagihan hutang pajak) dan bukti bayar PBB
4. Bukti Bayar DP atau pelunasan
5. Biaya AJB di kantor PPAT = > Rp. 2.5jt
6. Pajak Jual Beli Tanah:
    * Pajak Penjual - PPh = 2.5% dari transaksi atau NJOP (Nilai Jual Objek Pajak) Tertinggi:
        misal Tanah = Rp. 500jt -> PPh = 2.5% * 500jt = Rp. 12.5jt
        Biasanya ini dibayarkan oleh Penjual tapi bs dinegosiasikan
    * Pajak Pembeli - BPHTB (Bea Perolehan Hak atas Tanah dan Bangunan):
        Besarnya 5% (Harga Tanah - NJOPTKP ' Nilai Jual Objek Pajak Tidak Kena Pajak' yang ditetapkan pemerintah)
        Misal Tanah = Rp. 500jt - Rp. 60jt => 5% * 440jt = Rp. 22jt
    * PPH dan BPHTB sebelum balik nama
7.  Proses Balik Nama Sertifikat ke kantor BPN (2 - 4 minggu) > Rp.750,000

====
