Track 1 — Fundamental Edge AI
Week 1 — Mobile AI Architecture
Todo
 Pelajari perbedaan:
Cloud AI
vs
On-device AI
vs
Hybrid AI

 Pelajari:
CPU Inference
GPU Inference
NPU Inference
 Pelajari Android:
Thread
Isolate
Background Worker
Foreground Service
 Pelajari memory constraint mobile
RAM
Heap
Tensor Memory
Model Size
Mini Project

Buat diagram:

Flutter
   ↓
Platform Channel
   ↓
Native Kotlin
   ↓
AI Runtime

===========================

ack 2 — ONNX Runtime Mobile

ONNX adalah skill yang paling banyak dipakai lintas vendor.

Week 2
Todo
 Install:
Android Studio
Flutter
ADB
 Pelajari:
ONNX
Tensor
Input Shape
Output Shape
Quantization
 Setup:
ONNX Runtime Mobile
Project

Load model:

MobileNetV2

Target:

Image
↓
Classification
↓
Result

Offline 100%.

===========================
Track 3 — TensorFlow Lite

Masih banyak digunakan di Android.

Week 3
Todo
 Pelajari:
TFLite
Interpreter
Delegate
 Pelajari:
FP32
FP16
INT8
Project

Bangun:

Realtime Object Detection

menggunakan:

YOLOv8n TFLite

Target:

kamera realtime
bounding box
fps monitor

[================================]

Track 4 — Mobile OCR

Skill yang sangat dicari.

Week 4
Todo

Pelajari:

Image preprocessing
Thresholding
Resize
Crop
Project

Realtime OCR Scanner

Input:

Camera

Output:

Invoice Number
Serial Number
License Plate

Offline.

========================================
Track 5 — Realtime Camera Pipeline

Ini yang membedakan engineer biasa dan edge AI engineer.

Week 5
Todo

Pelajari pipeline:

Camera Frame
↓
YUV
↓
RGB
↓
Tensor
↓
Inference
↓
Overlay
Project

Bangun:

Realtime Inspection Camera

Contoh:

Bottle
Box
Component
Document

Deteksi realtime.

Track 6 — LLM on Android

Ini fase yang mulai "serius".

Week 6-7
Todo

Pelajari:

GGUF
Quantization
Context Window
Tokenization

Runtime:

llama.cpp

atau

MLC LLM
Project

Local Chat AI

Model:

Qwen 2.5 1.5B

atau

Gemma 2B

Target:

Offline Chat

langsung di Android.

Track 7 — Voice AI Offline
Week 8
Todo

Pelajari:

Speech To Text
Text To Speech
Streaming Audio
Project

Bangun:

Offline Voice Assistant

Komponen:

Whisper Tiny
+
Local LLM
+
Android TTS

Flow:

Mic
↓
STT
↓
LLM
↓
TTS
↓
Speaker
Track 8 — Mobile RAG
Week 9
Todo

Pelajari:

Embedding
Vector Search
Chunking
Project

Offline Knowledge Assistant

Data:

PDF
Manual
SOP

Flow:

PDF
↓
Embedding
↓
Vector DB
↓
Local LLM
↓
Answer

Semua offline.

Track 9 — Production Optimization

Ini yang biasanya tidak dipelajari tutorial.

Week 10
Todo

Pelajari:

Quantization
Model Pruning
Memory Mapping
Batching
Caching

Benchmark:

Startup Time
RAM Usage
FPS
Latency
Battery Usage
Target

Android mid-range:

RAM < 500 MB

Inference:

< 100 ms
Track 10 — Capstone Project (Portfolio)

Pilih salah satu.

Option A — Offline Smart OCR
Camera
↓
OCR
↓
Extract Data
↓
Export JSON

Use case:

invoice
receipt
warehouse
Option B — Field Inspection AI
Camera
↓
Object Detection
↓
Damage Detection
↓
Report

Use case:

manufaktur
konstruksi
QA/QC
Option C — Offline AI Assistant
Voice
↓
STT
↓
LLM
↓
RAG
↓
TTS

Use case:

teknisi lapangan
maintenance
SOP assistant

============
