Fase 1: Data & Model Preparation (Python / Notebook)
[ ] Pengumpulan Dataset: Kumpulkan gambar tandan buah segar (TBS) sawit untuk 8 kategori: Ripe, Unripe, Underripe, Overripe, Empty Bunch, Damaged, Abnormal, Dirty/Long Stalk.

[ ] Pelabelan (Labelling): Gunakan tools seperti Roboflow atau LabelImg untuk membuat bounding box (Object Detection jika ingin menghitung jumlah buah sekaligus).

[ ] Training Model: Train model menggunakan arsitektur ringan seperti YOLOv8 Nano / Small.

[ ] Export ke Edge Format: Konversi model .pt (PyTorch) atau .onnx ke format ONNX Mobile atau TensorFlow Lite (LiteRT), lalu terapkan kuantisasi (INT8/FP16) agar ringan di HP.

Fase 2: Backend Development (FastAPI & Database)
[ ] Setup Database: Hubungkan FastAPI dengan PostgreSQL/MySQL untuk menyimpan data user dan riwayat scanning (hitung buah).

[ ] Autentikasi (OAuth2 / Google Auth): Buat endpoint untuk registrasi/login menggunakan Google Sign-In.

[ ] API Gateway & Sync: Buat endpoint untuk sinkronisasi data riwayat inspeksi dari HP ke cloud saat pekerja mendapatkan sinyal internet.

Fase 3: Frontend Foundation & Auth (Flutter)
[ ] Setup Arsitektur BLoC: Buat struktur folder sesuai blueprint (presentation, domain, data, native_ai).

[ ] Integrasi Google Sign-In: Implementasikan package google_sign_in di Flutter dan hubungkan ke backend FastAPI.

[ ] Local Database (Offline-First): Setup Isar atau ObjectBox di Flutter untuk menyimpan hasil scan kelapa sawit secara lokal di memori HP (karena di kebun tidak ada sinyal).

Fase 4: Integrasi Kamera & Edge AI (Flutter Native - Krusial)
[ ] Camera Stream Optimization: Setup camera package di Flutter untuk menangkap frame image stream (YUV ke RGB).

[ ] Dart Isolates: Bungkus proses pengolahan gambar di Background Thread (Isolate) agar UI kamera tidak patah-patah (No UI Freeze).

[ ] Native Bridge (MethodChannel/FFI): Hubungkan Flutter ke ONNX Runtime Mobile / MediaPipe di sisi Android (Kotlin/C++).

[ ] Counter Logic: Buat logika untuk menghitung (counting) jumlah masing-masing jenis buah yang terdeteksi di layar secara realtime.

Fase 5: UI & Finisihing ke Playstore
[ ] BLoC Stream State UI: Tampilkan hasil deteksi dan jumlah buah menggunakan StreamBuilder dengan efek typing atau bounding box yang responsif.

[ ] Fitur Sinkronisasi: Buat tombol "Sinkronisasi Data" yang akan aktif ketika HP mendeteksi adanya sinyal internet (mengirim data lokal ke FastAPI).

[ ] Publish: Setup Keystore Android, bundling APK/AAB, dan rilis ke Google Play Store (Internal/Closed Testing lalu Production).


FLOW APPLIKASI

1. Alur Autentikasi & Inisialisasi (Online/Office)
graph TD
    A[Buka Aplikasi] --> B{Apakah Sudah Login?}
    B -- Belum --> C[Halaman Login/Register]
    C --> D[Klik Register/Login dengan Gmail]
    D --> E[Firebase/Google Auth]
    E --> F[Kirim Token ke FastAPI Backend]
    F --> G[Simpan/Verifikasi User di DB]
    G --> H[Download/Update Model AI Terbaru ke HP]
    H --> I[Masuk ke Dashboard Utama]
    B -- Sudah --> I

2. Alur Inspeksi Lapangan (Full Offline di Kebun Sawit)
graph TD
    A[Dashboard Utama] --> B[Buka Fitur AI Kamera]
    B --> C[Kamera HP Aktif Stream Frame]
    C --> D[Dart Isolate / Background Thread]
    
    subgraph Edge AI Processing (No Internet)
    D --> E[Konversi Frame YUV ke RGB]
    E --> F[Inference via ONNX Runtime Mobile]
    F --> G[Model Deteksi 8 Kategori TBS Sawit]
    G --> H[Hitung Jumlah Per Kategori]
    end
    
    H --> I[Kirim Hasil via Stream ke UI]
    I --> J[UI Menampilkan Bounding Box & Total Counter]
    J --> K[Pekerja Klik 'Simpan Hasil Scan']
    K --> L[Data Tersimpan di Local DB HP Isar/ObjectBox]

3. Alur Sinkronisasi Data (Kembali ke Sinyal / Kantor)
graph TD
    A[Pekerja Kembali ke Kantor / Dapat Sinyal] --> B[Buka Riwayat Scan]
    B --> C{Apakah Ada Internet?}
    C -- Tidak --> D[Tampilkan Notifikasi 'Mode Offline']
    C -- Ya --> E[Klik Tombol 'Sinkronisasi']
    E --> F[Ambil Data dari Local DB Isar/ObjectBox]
    F --> G[Kirim JSON Data ke FastAPI Backend]
    G --> H[FastAPI Simpan ke Database Server]
    H --> I[Hapus/Tandai Data Lokal Sudah Tersinkron]
    I --> J[Dashboard Web Pusat Update Data Panen]

=============================== DUMMY MODEL DEVELOPMENT ================================
Bangun Arsitektur applikas:
FastAPI + Flutter + Native Bridge + Isolate
menggunakan model AI Tiruan atau dataset publik yang mirip

20 Juni retrain model