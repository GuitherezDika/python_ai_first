# Phase Advanced — On-Device AI & Edge Computing

Lanjutan dari Phase 1 (FastAPI + Flutter Streaming AI).

Phase ini fokus pada menjalankan AI langsung di dalam HP pengguna — tanpa koneksi internet, tanpa server, tanpa biaya API.

---

## Kenapa Phase Ini Penting?

Mayoritas mobile developer hanya:
- consume API AI dari cloud
- pakai ChatGPT wrapper
- tidak memahami on-device inference

Padahal trend besar AI sekarang bergerak ke:

```
Private AI + Offline AI + Edge Computing
```

Contoh nyata yang sudah production:
- Apple Intelligence
- Gemini Nano di Android
- Samsung Galaxy AI
- Offline OCR, realtime translation, face recognition

---

## Target Akhir

```
Flutter App
   ↓
On-device AI inference
   ↓
Offline AI processing
   ↓
Fast performance (60–120 FPS)
   ↓
No UI freeze
```

---

## Portfolio Project #2

**Smart Vision AI Mobile App**

Pilihan use case (pilih salah satu):
- PPE Safety Detector (deteksi helmet, vest, mask)
- Palm Oil Fruit Detection (relevan industri perkebunan)
- Offline Attendance Face Recognition
- Document OCR Scanner

Target market: industri, manufacturing, plantation, warehouse, enterprise.

---

## Roadmap — 10–14 Minggu

### ADV-1 | Dasar AI & Computer Vision (1 minggu)

Memahami konsep dasar sebelum coding:

- Image classification, object detection, segmentation, OCR, face recognition
- Alur: Image → Preprocessing → AI Model → Inference → Prediction
- Istilah: Tensor, RGB image, Bounding box, Confidence score, FPS, Inference time

Tools: Python, OpenCV, Jupyter Notebook

Output: Paham bagaimana AI vision bekerja dari input gambar sampai prediksi.

---

### ADV-2 | TensorFlow Lite Foundation (1 minggu)

Memahami TFLite sebagai engine AI untuk mobile:

- Alur: Training Model → Export `.tflite` → Run di Mobile
- Konsep: model.tflite, labels.txt, input tensor, output tensor

Mini Practice: Run image classification sederhana dari file gambar.

---

### ADV-3 | Flutter + TFLite Integration (1–2 minggu)

Integrasi model AI ke Flutter app:

Package yang dipakai:
- `tflite_flutter`
- `google_mlkit_flutter`

Materi: load model, run inference, image input, parse output

Mini Project: Offline image classifier (classify PPE / cat / dog)

Output: AI bisa jalan offline di Flutter.

---

### ADV-4 | Computer Vision Real-Time Camera (1–2 minggu)

Jalankan AI dari input kamera secara realtime:

Package: `camera`, `image stream`

Materi:
- Camera frame processing
- YUV/RGB conversion
- Realtime inference
- Frame throttling (agar tidak drop FPS)

Tantangan: Kalau salah implementasi → UI freeze, FPS drop, memory leak.

Mini Project: Realtime object detector dari kamera HP.

---

### ADV-5 | Dart Isolates — KRUSIAL (2 minggu)

**Phase paling penting** di seluruh roadmap ini.

Kenapa? Karena AI inference berat. Kalau jalan di main thread:
- UI patah-patah
- ANR di Android
- Freeze di iOS

Solusinya: pindahkan inference ke thread terpisah menggunakan Dart Isolates.

```
Main UI Thread
   ↓
AI Isolate Thread → Run Inference → Return Result
   ↓
UI update smooth
```

Materi: `isolate`, `compute()`, `SendPort`, `ReceivePort`

Target: UI tetap 60 FPS meski AI inference berjalan di background.

---

### ADV-6 | Model Optimization & Quantization (1 minggu)

Ini yang membedakan engineer biasa dengan senior:

Quantization = memperkecil model tanpa banyak kehilangan akurasi:

```
Before: 250 MB, 2 sec inference
After:   18 MB, 200 ms inference
```

Jenis quantization:
- Dynamic quantization
- Full integer quantization (int8)
- Float16 quantization

Output: Paham tradeoff antara ukuran model, kecepatan, dan akurasi.

---

### ADV-7 | Architecture AI Mobile (1 minggu)

Membuat structure Flutter yang scalable untuk AI app:

```
presentation/
domain/
data/
  ai_service/
  camera_service/
  isolate_service/
```

Integrasi dengan BLoC + Stream architecture dari Phase 1.

Output: Codebase clean, testable, dan scalable.

---

### ADV-8 | Portfolio Project #2 (2–3 minggu)

Build final project dengan semua yang sudah dipelajari.

Requirement wajib:
- Offline AI inference (TFLite + quantized model)
- Realtime camera processing
- Dart Isolates (no UI freeze)
- BLoC + Stream architecture
- Smooth FPS (target 60+)

---

## Final Skill Stack

Setelah phase ini selesai, skill kamu:

```
Flutter
FastAPI (dari Phase 1)
AI Gateway + Streaming (dari Phase 1)
On-device AI (TFLite)
Computer Vision (OpenCV)
Realtime Camera Processing
Mobile Optimization
Multithreading (Dart Isolates)
```

Profile yang terbentuk: **Senior AI Mobile Engineer**

Market yang terbuka: AI startup, enterprise AI, industrial AI, smart factory, edge AI.
