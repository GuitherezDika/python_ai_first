# Phase RAG — AI Memory Systems (On-Device)

Lanjutan dari Phase Advanced (On-Device AI & Edge Computing).

Phase ini fokus pada memberi AI kemampuan "ingatan" — menyimpan, mencari, dan menggunakan pengetahuan secara lokal di HP tanpa upload ke cloud.

---

## Kenapa Phase Ini Penting?

Mayoritas AI app saat ini:
- semua data dikirim ke server
- tidak punya memory jangka panjang
- tidak bisa cari berdasarkan makna (hanya keyword)

Phase ini mengajarkan cara membangun AI yang:
- menyimpan data lokal & terenkripsi
- mencari berdasarkan makna semantik (bukan keyword)
- punya "ingatan" personal tanpa bocor ke cloud

---

## Target Akhir

```
User Notes
   ↓
Encrypted Locally
   ↓
Converted to Embeddings
   ↓
Stored in Vector Database
   ↓
Semantic Search
   ↓
AI Response with Context
```

Mirip Notion AI / Apple Intelligence memory — tapi local-first & privacy-first.

---

## Portfolio Project #3

**Privacy-First AI Journal & Knowledge Base**

Fitur:
- Tulis catatan → otomatis di-embed dan disimpan lokal
- Cari catatan dengan bahasa natural ("meeting kemarin")
- AI menjawab pertanyaan berdasarkan catatan yang relevan
- Semua data terenkripsi di device, tidak pernah ke server

---

## Roadmap — 8–10 Minggu

### RAG-1 | Fundamental RAG & Embeddings (1 minggu)

Konsep dasar sebelum implementasi:

**Apa itu Embedding?**

Teks diubah jadi vektor angka matematika:
```
"Saya suka Flutter" → [0.283, -0.114, 0.982, ...]
```

Tujuannya agar AI bisa memahami makna, bukan hanya mencocokkan kata.

Contoh: "Mobil merah" dan "Kendaraan warna merah" → secara embedding, keduanya dekat secara matematika.

Konsep kunci: **Cosine Similarity** — semakin dekat dua vektor, semakin relevan kontennya.

Output: Paham bagaimana AI memory dan semantic search bekerja.

---

### RAG-2 | Mini RAG Pipeline (1 minggu)

Implementasi flow RAG lengkap di Python:

```
Question
   ↓
Embedding Query
   ↓
Search Similar Notes (top-k)
   ↓
Build Context
   ↓
Send to LLM
   ↓
Generate Answer
```

Materi: chunking text, retrieval, top-k search, context injection

Mini Practice: 5 notes → cari note paling relevan berdasarkan pertanyaan.

Output: Paham bagaimana ChatGPT "memory" bekerja di balik layar.

---

### RAG-3 | Flutter Local Database (1 minggu)

Belajar database lokal Flutter yang cocok untuk AI:

Rekomendasi: **ObjectBox** — karena punya native vector search support.

Alternatif: **Isar** — lebih ringan, Flutter-centric.

Materi: CRUD (insert, update, delete note), local persistence architecture.

---

### RAG-4 | Vector Database on Mobile (1–2 minggu)

Menyimpan embeddings langsung di HP:

Schema note:
```
Note
- id
- content
- encryptedContent
- embedding (vector)
- createdAt
```

Materi: vector indexing, nearest neighbor search, semantic retrieval

Mini Project: Cari note "meeting minggu lalu" meski note aslinya "diskusi sprint project dengan tim" — dan berhasil ditemukan.

---

### RAG-5 | Embedding Model On-Device (1–2 minggu)

Generate embedding langsung di HP tanpa API:

Strategi:
- **Option A (lebih mudah)**: pakai API embedding dari server (FastAPI dari Phase 1)
- **Option B (lebih advanced)**: on-device embedding model

Rekomendasi: mulai hybrid (A), naik ke full offline (B) setelah paham.

Model yang bisa dipakai: MiniLM, all-MiniLM-L6-v2, MobileBERT

---

### RAG-6 | Encryption & Privacy Layer (1 minggu)

Enkripsi data user sebelum disimpan:

```
User Note
   ↓ AES Encryption
Save Local (encrypted)
   ↓
Generate Embedding (dari plaintext)
   ↓
Store Vector (tanpa plaintext)
```

Materi: AES encryption, secure storage, key management

Target: Data user tidak pernah plaintext di storage, aman meski HP hilang.

---

### RAG-7 | AI Context Injection (1 minggu)

Menghubungkan vector search dengan AI response:

```
User bertanya: "Apa hasil meeting kemarin?"
   ↓
Retrieve notes relevan dari vector DB
   ↓
Build prompt: "[CONTEXT: notes relevan] + [QUESTION: user]"
   ↓
Send to AI (Gemini / local LLM)
   ↓
AI menjawab dengan konteks yang tepat
```

Output: AI punya memory personal yang akurat dan relevan.

---

### RAG-8 | Flutter Architecture Integration (1 minggu)

Clean architecture untuk AI memory app:

```
presentation/
domain/
data/
  vector_service/
  embedding_service/
  ai_service/
  crypto_service/
```

Integrasi dengan BLoC + Stream + Isolates dari Phase 1 & Phase 2.

Output: Codebase scalable, testable, siap production.

---

## Final Skill Stack

Setelah phase ini selesai:

```
Phase 1:  FastAPI + AI Gateway + Streaming + WebSocket + Flutter BLoC
Phase 2:  TFLite + Computer Vision + Dart Isolates + Quantization
Phase 3:  RAG + Embeddings + Vector DB + Encryption + AI Memory
```

Profile yang terbentuk: **AI Memory Systems Engineer (Mobile)**

Ini niche yang sangat sedikit developernya dan sangat dicari untuk:
- Personal AI assistant
- Enterprise knowledge management
- Privacy-first AI product
- Edge AI with long-term memory
