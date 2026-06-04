# Phase 4 — Build Real Project

Lanjutan dari Phase 1–3. Semua skill digabungkan jadi satu produk nyata yang bisa dipakai dan dipresentasikan.

---

## Tujuan Phase Ini

Phase 1–3 adalah belajar component per component. Phase 4 adalah menyatukan semuanya menjadi produk yang:
- bisa dipakai user sungguhan
- punya backend yang production-ready
- punya mobile app yang smooth dan offline-capable
- bisa dipresentasikan ke klien atau interviewer

---

## Pilihan Real Project

Pilih salah satu yang paling relevan dengan background dan target karir kamu.

---

### Option A — AI-Powered Attendance System

Use case industri yang langsung bisa dijual ke perusahaan.

**Flow:**
```
Karyawan buka app
   ↓
Kamera scan wajah (on-device Face Recognition)
   ↓
Match dengan database karyawan
   ↓
Kirim ke backend FastAPI
   ↓
Simpan ke PostgreSQL
   ↓
Generate laporan attendance
```

**Tech stack:**
- Flutter: camera, TFLite face recognition, BLoC, offline queue
- FastAPI: auth JWT, employee CRUD, attendance API, report export
- PostgreSQL: data karyawan dan attendance
- Redis: session cache
- Docker: deployment

**Nilai jual:** Sangat relevan untuk industri, bisa langsung di-demo ke klien.

---

### Option B — Internal AI Chatbot Enterprise

Chatbot yang "tahu" tentang dokumen perusahaan.

**Flow:**
```
Admin upload dokumen SOP / manual
   ↓
Backend proses → chunk → embed → simpan ke vector DB
   ↓
Karyawan tanya via mobile app
   ↓
RAG pipeline cari dokumen relevan
   ↓
Gemini jawab berdasarkan konteks dokumen
   ↓
Response streaming ke Flutter
```

**Tech stack:**
- Flutter: chat UI, BLoC, WebSocket streaming
- FastAPI: document upload, embedding pipeline, RAG API
- Vector DB: pgvector (PostgreSQL extension)
- Gemini: LLM response
- Docker: deployment

**Nilai jual:** Enterprise AI yang privacy-first, dokumen tidak bocor ke cloud publik.

---

### Option C — Smart Field Inspector App

App untuk inspeksi lapangan dengan AI vision + laporan otomatis.

**Flow:**
```
Inspector di lapangan (bisa offline)
   ↓
Foto objek → on-device AI deteksi kondisi
   ↓
Data disimpan lokal (offline mode)
   ↓
Saat online → sync ke backend
   ↓
AI generate laporan inspeksi otomatis
   ↓
Export PDF / kirim ke supervisor
```

**Tech stack:**
- Flutter: camera, TFLite object detection, offline sync, BLoC
- FastAPI: sync API, report generation, PDF export
- PostgreSQL: data inspeksi
- Gemini: auto-generate laporan dari temuan

**Nilai jual:** Sangat cocok untuk industri perkebunan, konstruksi, warehouse.

---

## Checklist Build Real Project

### Fase Perencanaan
- [ ] Pilih use case project
- [ ] Definisikan user story & fitur utama
- [ ] Buat wireframe / mockup sederhana
- [ ] Tentukan tech stack final
- [ ] Setup repository dan struktur folder

### Fase Backend
- [ ] Setup PostgreSQL + SQLAlchemy ORM
- [ ] Implement auth JWT (register, login, refresh token)
- [ ] Buat semua API endpoint yang dibutuhkan
- [ ] Implement business logic di service layer
- [ ] Setup Redis untuk caching
- [ ] Rate limiting dan security middleware
- [ ] Unit test untuk service layer
- [ ] Docker + docker-compose

### Fase Mobile
- [ ] Setup Flutter project dengan clean architecture
- [ ] Implement BLoC untuk semua feature
- [ ] Build semua screen (berdasarkan wireframe)
- [ ] Integrasi dengan backend API
- [ ] Implement offline mode (kalau relevan)
- [ ] Implement on-device AI (kalau relevan)
- [ ] Handle error state dan loading state
- [ ] Test di device Android & iOS

### Fase AI Integration
- [ ] Integrasi AI sesuai use case (vision / RAG / streaming)
- [ ] Optimasi performa AI
- [ ] Handle fallback kalau AI gagal

### Fase Production
- [ ] Deploy backend ke VPS
- [ ] Setup Nginx reverse proxy
- [ ] SSL certificate
- [ ] Environment variables management
- [ ] Monitoring dasar (log, uptime)
- [ ] Build APK / IPA untuk demo

### Fase Portfolio
- [ ] README project yang jelas
- [ ] Demo video (screen recording)
- [ ] Architecture diagram
- [ ] Dokumentasi API (Swagger sudah otomatis)
- [ ] Siap dipresentasikan

---

## Timeline Estimasi

```
Perencanaan:      1 minggu
Backend:          2–3 minggu
Mobile:           2–3 minggu
AI Integration:   1–2 minggu
Production:       1 minggu
Polish & Demo:    1 minggu
─────────────────────────────
Total:            8–11 minggu
```
