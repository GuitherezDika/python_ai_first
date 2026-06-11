### CLOUD AI
contoh:
    Android - OpenAI API
    Android - Gemini AI

Foto - upload server - AI process - server kirim hasil - UI tampil hasil

Kelelbihan : model sangat besar misal : GPT - 5; Cloude. Gemini
UKuran Model: 10GB, 100GB, TB
dan tidak bisa di taruh di android

======
Update Mudah: Model V1 - Model V2
Akurasi Tinggi
Privacy: Data Keluar device - server:
    Dokumen
    KTP
    Invoice
    Foto Wajah

=======
### ON-DEVICE AI / EDGE AI / LOCAL AI
Arsitektur:
Android app - AI Runtime - Model

Flow:
Camera - Tensor - Model - Result


no internet
Realtime OCR; Object Detection; Face Detection; Gesture Recognition
Offline tetap jalan

Kelebihan: Privacy
Kurangan: RAM, CPU, Battrai, Storage

Model Harus Kecil:
YOLOv8n
MobileNet
Gemma 2B
Qwen 1.5B

Optimisasi lebih Sulit
    FPS
    Battery
    Memory
    Thermal

Real Case yang DONE: 
    Apple Intterligence (Offline)
    Gemini Nano
    Samsung Galaxy AI
    Google ML Kit

========
### HYBRID AI
Arsitektur:
Android
   ↓
Local AI
   ↓
Jika perlu
   ↓
Cloud AI

Contoh:
Camera
↓
OCR Lokal
↓
Extract Data Lokal
↓
Ringkasan Cloud
↓
Result

Analisis AI:
Jika Ringan:
    LOCAL LLM
Jika Kompleks:
    CLOUD LLM

Kelebihan
Gabungan dua dunia.
Cepat
Karena sebagian proses lokal.
Akurat
Karena cloud tersedia saat diperlukan.
Hemat biaya
Tidak semua request ke server

Kekurangan
Arsitektur lebih kompleks.

Real Case yang HYBRID: 
    Apple Intterligence (Offline)
    Gemini Nano
    Samsung Galaxy AI

========= mobile development =================
Cloud AI: DONE
Flutter
↓
FastAPI
↓
LLM API

== on device AI ===
START PROGRESS
Flutter
↓
ONNX Runtime

== Tahap 3 hybrid ==
Offlline Dulu 
    GAGAL:
Cloud


========

Exercise #1 (disarankan sebelum lanjut)

Ambil 3 fitur berikut dan coba klasifikasikan apakah lebih cocok:

Scanner KTP offline untuk petugas lapangan.
Chatbot customer service dengan pengetahuan perusahaan yang selalu berubah.
Deteksi cacat produk di pabrik menggunakan kamera Android realtime.

Jawab dengan format:

1. Cloud / On-device / Hybrid
Alasan:

2. Cloud / On-device / Hybrid
Alasan:

3. Cloud / On-device / Hybrid
Alasan:

Nanti saya review seperti mentor Edge AI engineer dan kita lanjut ke topik berikutnya: CPU vs GPU vs NPU Inference di Android.

======