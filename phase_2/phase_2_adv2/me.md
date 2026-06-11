onnxruntime
numpy
pillow
opencv-python

buat file dulu requirement.txt
pip freeze > requirements.txt

pip install -r requirements.txt

======
Input (image/audio/text)
        ↓
Preprocessing (resize, normalize)
        ↓
Tensor conversion
        ↓
Model inference (ONNX / TFLite / MediaPipe)
        ↓
Output (prediction)

=======

Palm Bunches Qualification:
Ripe
Unripe
Underripe
Overripe
Empty Bunches

Damaged/Diseased
Abnormal
Long Stalk

dan Jumlah masing2 dari Jenis Kualifikasi Bunches, misalkan:
Ripe: 100
Unrip: 2
Underripe: 0
Overripe : 5
Damaged/Diseased: 0
Abnormal: 0
Long Stalk: 0

========
🧠 PHASE 1 — Problem Definition (WAJIB DONE FIRST)
✅ Task 1.1 — Definisikan label AI
 Ripe
 Unripe
 Underripe
 Overripe
 Empty Bunch
 Damaged / Diseased
 Abnormal
 Dirty / Long Stalk

👉 Output: Label schema final JSON

✅ Task 1.2 — Tentukan jenis AI problem

Ini penting:

Kamu bukan classification single object ❌
Tapi:

👉 Object Detection + Multi-Class Counting

Artinya:

1 gambar → banyak objek
tiap objek punya label
hasil → count aggregation
🧠 PHASE 2 — Data Preparation (PALING KRUSIAL)
✅ Task 2.1 — Dataset gambar sawit
 kumpulkan foto dari kebun
 minimal:
500–2000 images awal (prototype)
 variasi:
cahaya pagi / siang / hujan
jarak kamera
background kebun
✅ Task 2.2 — Labeling

Tools:

CVAT
Roboflow
Label Studio

Output format:

bounding box + class label

Contoh:

[ Ripe ] -> box (x,y,w,h)
[ Unripe ] -> box (x,y,w,h)
✅ Task 2.3 — Dataset structure
dataset/
  images/
  labels/
  train/
  val/
  test/
🧠 PHASE 3 — MODEL TRAINING
✅ Task 3.1 — Pilih model (IMPORTANT)

Untuk mobile AI sawit:

🔥 Recommended:
YOLOv8n (nano)
YOLOv5n
EfficientDet-lite

Kenapa:

ringan
bisa real-time
cocok edge device
✅ Task 3.2 — Training

Output:

.pt (PyTorch)
convert → ONNX
✅ Task 3.3 — Export model
PyTorch → ONNX → (Mobile Runtime)
📱 PHASE 4 — MOBILE AI RUNTIME (Flutter / Native)
Kamu punya 2 jalur:
🔥 OPTION A (RECOMMENDED) — MediaPipe + ONNX hybrid
Task 4.1
 convert YOLO → ONNX
Task 4.2
 run ONNX inference (native Android/iOS)
Task 4.3
 Flutter UI camera preview
Task 4.4
 stream frame → native inference
🔥 OPTION B — Full Native MediaPipe (lebih simple tapi terbatas)
cocok kalau pakai prebuilt model
kurang fleksibel untuk custom sawit class
📷 PHASE 5 — CAMERA PIPELINE
✅ Task 5.1 — Camera stream

Flutter:

camera plugin
frame streaming
✅ Task 5.2 — Frame preprocessing
resize (e.g 640x640)
normalize
convert to tensor
✅ Task 5.3 — inference loop
frame → model → output boxes → postprocess
🧠 PHASE 6 — POST PROCESSING
✅ Task 6.1 — NMS (Non-Max Suppression)
hapus duplicate detection
✅ Task 6.2 — counting logic

Pseudo:

countMap = {}

for detection in results:
   label = detection.class
   countMap[label]++

Output:

Ripe: 100
Unripe: 2
...
📊 PHASE 7 — OUTPUT SYSTEM (EPMS STYLE)
✅ Task 7.1 — JSON result
{
  "Ripe": 100,
  "Unripe": 2,
  "Overripe": 5
}
✅ Task 7.2 — integrate ke backend (optional)
send hasil ke API EPMS
simpan per OPH / TPH
🚀 PHASE 8 — REAL FIELD DEPLOYMENT
✅ Task 8.1
test di HP low-end (real estate condition)
✅ Task 8.2
test di kebun:
sunlight
blur
motion
🧠 FINAL ARCHITECTURE (YOU TARGET)
📷 Camera
   ↓
Flutter UI
   ↓
Native AI runtime (ONNX / MediaPipe)
   ↓
YOLO Model inference
   ↓
Postprocessing (NMS + counting)
   ↓
JSON result
   ↓
EPMS / Dashboard

======
💬 Kalau kamu mau next step

Aku bisa bantu kamu lanjut ke:

🔥 STEP NEXT (pilih aja)
🧠 desain dataset + labeling guideline sawit (biar AI akurat)
🔥 pilih model YOLO yang paling cocok + setup training
📱 Flutter camera + real-time frame pipeline
🏗️ full architecture EPMS + AI integration design
🚀 langsung bikin prototype inference dummy dulu (no training)