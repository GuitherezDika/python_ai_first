🛠️ Apa yang Harus Dilakukan Sekarang? (Pre-Onsite)
1. Buat "Dummy Model" Menggunakan Dataset Publik
Jangan tunggu model sawit jadi untuk mulai coding Flutter.

Pergi ke Roboflow Universe atau Kaggle.

Cari dataset deteksi objek yang ringan dan gratis, misalnya "Fruit Detection" (apel, pisang, jeruk) atau "General Objects".

Lakukan training singkat menggunakan YOLOv8, lalu export ke format ONNX Mobile atau TFLite.

Tujuannya: Menggunakan model buah tiruan ini untuk mengetes apakah MethodChannel, Dart Isolate, dan StreamBuilder di Flutter-mu sudah bekerja mentransfer data kamera ke native runtime tanpa bikin UI freeze. Jika deteksi buah apel sudah lancar dan lancar 60 FPS, nanti diganti model sawit pun jalannya akan sama.

2. Cicil Backend FastAPI (Phase 1_4 sampai 1_6)
Kamu bisa menyelesaikan seluruh urusan backend server dan database:

Setup database untuk menyimpan data user (registrasi via Google Mail).

Buat skema tabel database untuk menampung data hasil panen (contoh kolom: id, user_id, ripe_count, unripe_count, location_gps, timestamp).

Buat endpoint FastAPI untuk menerima sinkronisasi data JSON dari Flutter.

3. Setup Arsitektur Flutter BLoC & Local DB (Isar/ObjectBox)
Setup boilerplate project Flutter dengan clean architecture yang sudah direncanakan.

Buat fitur Auth (Login/Register menggunakan Google Sign-In) yang menembak ke FastAPI.

Setup database lokal (Isar atau ObjectBox) di HP untuk menyimpan data scan lokal secara offline.

📸 Panduan Penting Pengambilan Data (Saat Onsite - 20 Juni)
Mengambil dataset untuk Industrial AI di kebun sawit tidak bisa sembarangan foto. Biar kerja kerasmu di tanggal 20 Juni tidak sia-sia, ikuti aturan main pengambilan dataset ini:

Variasi Pencahayaan (Crucial!): Ambil foto kelapa sawit di pagi hari (cahaya lembut), siang hari (cahaya terik/kontras tinggi), dan sore/mendung. AI sering bingung kalau ditraining hanya pakai foto siang hari, lalu dipakai bekerja saat mendung.

Variasi Sudut (Angle): Foto Tandan Buah Segar (TBS) dari arah depan, agak ke bawah, bawah pohon, dan saat sudah dipotong di Tempat Pengumpulan Hasil (TPH).

Gunakan Kamera HP yang Sama: Ambil data menggunakan HP yang nantinya kira-kira setara dengan spesifikasi HP pekerja di lapangan agar karakteristik sensor gambarnya mirip.

Minimal Jumlah Foto: Targetkan minimal 100–150 foto per kategori. Jadi untuk 8 kategori, usahakan total mendapat sekitar 1.000 - 1.200 foto. Jika waktu mepet, ambil video durasi 10–20 detik per buah, nanti di komputer video tersebut bisa kita potong-potong per frame menjadi puluhan foto (menggunakan OpenCV).

🎯 Target Minimum Minggu Ini
Saran saya: Minggu ini fokus ke ADV-3 (Flutter + Native AI Integration) menggunakan model tiruan (misal: model pendeteksi objek umum/buah biasa).

Selesaikan urusan "jembatan" antara kamera Flutter, Dart Isolate, dan ONNX Runtime. Dengan begitu, tanggal 20 Juni nanti kamu ke lapangan murni hanya fokus berburu foto berkualitas!

Mau saya bantu buatkan code template sederhana untuk interogasi ONNX Runtime di sisi Android (Kotlin) atau setup Dart Isolate untuk camera stream-nya terlebih dahulu?