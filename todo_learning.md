# Learning Todo List

Roadmap belajar dari Phase 1 sampai Phase 3.
Centang setiap item setelah selesai.

---

## Phase 1 — FastAPI + Flutter AI Gateway

### 1_3 | FastAPI Architecture
- [x] Clean architecture: model → repository → service → router
- [x] Todo CRUD API
- [x] Auth register & login
- [x] Middleware logger
- [x] Config dari .env

### 1_4 | AI Gateway
- [x] Gemini SDK integration
- [x] Provider abstraction pattern
- [x] API key security via .env

### 1_5 | Streaming Response (SSE)
- [x] StreamingResponse FastAPI
- [x] Async generator
- [x] Thread-safe Gemini streaming
- [x] SSE format (data: chunk\n\n)

### 1_6 | WebSocket
- [x] WebSocket endpoint FastAPI
- [x] Persistent connection
- [x] Realtime streaming per chunk
- [x] Disconnect handling

### 1_7 | Flutter Streaming Client
- [x] WebSocket connection dari Flutter
- [x] BLoC state management
- [x] StreamBuilder UI
- [x] Typing effect (chunk append)

### 1_8 | Production Ready
- [x] Redis cache (hemat quota AI)
- [x] Rate limiting per IP
- [x] Docker + docker-compose
- [ ] Nginx reverse proxy
- [ ] Deploy ke VPS
- [ ] Retry/fallback AI provider
- [ ] Monitoring

---

## Phase 2 — On-Device AI & Edge Computing

### ADV-1 | Dasar AI & Computer Vision
- [ ] Memahami image classification, object detection, OCR
- [ ] Konsep: Tensor, RGB, Bounding box, FPS
- [ ] Setup Python + OpenCV + Jupyter

### ADV-2 | TensorFlow Lite Foundation
- [ ] Memahami TFLite inference pipeline
- [ ] Eksperimen model.tflite + labels.txt
- [ ] Run image classification sederhana

### ADV-3 | Flutter + TFLite Integration
- [ ] Install tflite_flutter / google_mlkit
- [ ] Load model di Flutter
- [ ] Run inference dari image file
- [ ] Mini project: offline image classifier

### ADV-4 | Realtime Camera AI
- [ ] Setup camera + image stream
- [ ] YUV/RGB conversion
- [ ] Frame throttling
- [ ] Mini project: realtime object detector

### ADV-5 | Dart Isolates
- [ ] Paham konsep isolate vs main thread
- [ ] Implementasi compute()
- [ ] SendPort + ReceivePort
- [ ] Pindahkan inference ke isolate
- [ ] Target: UI 60 FPS saat inference jalan

### ADV-6 | Model Optimization & Quantization
- [ ] Dynamic quantization
- [ ] Full integer quantization (int8)
- [ ] Float16 quantization
- [ ] Ukur perbandingan sebelum/sesudah

### ADV-7 | Architecture AI Mobile
- [ ] Struktur folder: ai_service, camera_service, isolate_service
- [ ] Integrasi BLoC + Stream

### ADV-8 | Portfolio Project #2
- [ ] Pilih use case (PPE / OCR / Face / Palm Oil)
- [ ] Implementasi full dengan semua requirement
- [ ] Demo ready

---

## Phase 3 — AI Memory Systems (RAG)

### RAG-1 | Fundamental RAG & Embeddings
- [ ] Paham konsep embedding
- [ ] Paham cosine similarity
- [ ] Eksperimen vektor sederhana di Python

### RAG-2 | Mini RAG Pipeline
- [ ] Implementasi chunking text
- [ ] Top-k search sederhana
- [ ] Context injection ke prompt AI

### RAG-3 | Flutter Local Database
- [ ] Setup ObjectBox di Flutter
- [ ] CRUD note lokal
- [ ] Local persistence architecture

### RAG-4 | Vector Database on Mobile
- [ ] Schema note dengan embedding field
- [ ] Vector indexing di ObjectBox
- [ ] Semantic retrieval test

### RAG-5 | Embedding Model On-Device
- [ ] Option A: API embedding dari FastAPI backend
- [ ] Option B: on-device MiniLM / MobileBERT
- [ ] Bandingkan performa keduanya

### RAG-6 | Encryption & Privacy Layer
- [ ] AES encryption untuk note content
- [ ] Secure storage key management
- [ ] Data tidak pernah plaintext di storage

### RAG-7 | AI Context Injection
- [ ] Retrieve notes relevan dari vector DB
- [ ] Build prompt dengan context
- [ ] Test akurasi jawaban AI

### RAG-8 | Flutter Architecture Integration
- [ ] Clean architecture: vector_service, embedding_service, crypto_service
- [ ] BLoC + Stream + Isolates terintegrasi
- [ ] Portfolio project #3 ready

---

## Phase 4 — Build Real Project

### Perencanaan
- [ ] Pilih use case (Attendance / Enterprise Chatbot / Field Inspector)
- [ ] Definisikan user story & fitur utama
- [ ] Buat wireframe / mockup sederhana
- [ ] Tentukan tech stack final
- [ ] Setup repository dan struktur folder

### Backend
- [ ] Setup PostgreSQL + SQLAlchemy ORM
- [ ] Auth JWT (register, login, refresh token)
- [ ] Semua API endpoint sesuai use case
- [ ] Business logic di service layer
- [ ] Redis caching
- [ ] Rate limiting dan security middleware
- [ ] Unit test service layer
- [ ] Docker + docker-compose

### Mobile
- [ ] Flutter project dengan clean architecture
- [ ] BLoC untuk semua feature
- [ ] Semua screen sesuai wireframe
- [ ] Integrasi dengan backend API
- [ ] Offline mode (kalau relevan)
- [ ] On-device AI (kalau relevan)
- [ ] Error state dan loading state
- [ ] Test di Android & iOS

### AI Integration
- [ ] Integrasi AI sesuai use case (vision / RAG / streaming)
- [ ] Optimasi performa AI
- [ ] Fallback handling

### Production & Portfolio
- [ ] Deploy backend ke VPS
- [ ] Nginx reverse proxy + SSL
- [ ] Monitoring dasar
- [ ] Build APK untuk demo
- [ ] README project yang jelas
- [ ] Demo video (screen recording)
- [ ] Architecture diagram

---

## Status Keseluruhan

```
Phase 1:  ████████████░░  Hampir selesai (tinggal deploy/nginx)
Phase 2:  ░░░░░░░░░░░░░░  Belum mulai
Phase 3:  ░░░░░░░░░░░░░░  Belum mulai
Phase 4:  ░░░░░░░░░░░░░░  Belum mulai
```
