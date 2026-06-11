# Phase Advanced — Edge AI Mobile Engineering

Lanjutan dari Phase 1 (FastAPI + Flutter Streaming AI).

Phase ini fokus pada membangun AI yang berjalan langsung di device mobile secara realtime, offline, dan production-ready menggunakan modern edge AI runtime.

---

## Kenapa Phase Ini Penting?

Mayoritas mobile developer:

* hanya consume AI API dari cloud
* tidak memahami realtime inference
* tidak memahami mobile AI optimization
* bergantung pada package AI Flutter yang tidak stabil

Padahal industri AI modern bergerak ke:

```text
Private AI + Offline AI + Edge Computing
```

Contoh production:

* Apple Intelligence
* Gemini Nano
* Samsung Galaxy AI
* Realtime mobile OCR
* Industrial mobile AI inspection

---

## Target Akhir

```text
Flutter App
   ↓
Native AI Runtime
   ↓
Realtime Inference
   ↓
Offline Processing
   ↓
No UI Freeze
   ↓
Production-ready Edge AI
```

---

# Portfolio Project #2

## Palm Oil Field AI

Offline AI Mobile App untuk:

* deteksi kematangan tandan sawit
* realtime grading
* field inspection AI

Output:

* ripe
* under-ripe
* over-ripe
* invalid / blur

Target:
plantation industry, agritech, industrial inspection.

---

# Roadmap — 10–14 Minggu

## ADV-1 | Computer Vision & AI Foundation

Materi:

* image classification
* object detection
* segmentation
* embedding
* inference pipeline

Tools:

* Python
* OpenCV
* Jupyter Notebook

Output:
Memahami alur AI vision dari input gambar hingga prediction.

---

## ADV-2 | Edge AI Runtime Foundation

Belajar runtime modern untuk mobile AI:

* ONNX Runtime Mobile
* MediaPipe Tasks
* LiteRT concept
* Native AI inference

Materi:

* model loading
* tensor input/output
* preprocessing pipeline
* inference lifecycle

Output:
Paham cara AI berjalan di mobile tanpa cloud.

---

## ADV-3 | Flutter + Native AI Integration

Integrasi Flutter dengan native AI runtime.

Architecture:

```text
Flutter UI
   ↓
MethodChannel / FFI
   ↓
Native Android AI Layer
   ↓
ONNX Runtime / MediaPipe
```

Materi:

* MethodChannel
* native Kotlin bridge
* image preprocessing
* result parsing

Output:
Flutter dapat menjalankan AI inference secara stabil dan production-ready.

---

## ADV-4 | Realtime Camera Processing

Materi:

* realtime frame processing
* camera image stream
* YUV → RGB conversion
* frame throttling
* FPS optimization

Mini Project:
Realtime palm oil classification dari kamera HP.

---

## ADV-5 | Dart Isolates & Multithreading

Materi:

* isolate
* compute()
* SendPort / ReceivePort
* background processing

Target:
UI tetap smooth meski inference realtime berjalan.

---

## ADV-6 | Model Optimization

Materi:

* quantization
* float16
* int8 optimization
* latency optimization
* memory optimization

Output:
Model kecil, inference cepat, battery efficient.

---

## ADV-7 | AI Mobile Architecture

Structure:

```text
presentation/
domain/
data/
native_ai/
camera_service/
stream_service/
isolate_service/
```

Integrasi:

* BLoC
* Stream architecture
* realtime rendering

---

## ADV-8 | Final Portfolio Project

Build:
Palm Oil Field AI Production App

Requirement:

* offline AI inference
* realtime camera AI
* native AI runtime
* isolate processing
* smooth FPS
* BLoC stream architecture

---

# Final Skill Stack

```text
Flutter
FastAPI
Streaming Architecture
ONNX Runtime Mobile
MediaPipe
Computer Vision
Realtime Camera Processing
Dart Isolates
Edge AI Optimization
Native Mobile AI Integration
```

Profile:
Edge AI Mobile Engineer
Realtime AI Engineer
Industrial AI Mobile Engineer
