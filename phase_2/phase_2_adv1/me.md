terminal;
python3 -m venv venv (kalau belum install)
source venv/bin/activate
pip install opencv-python jupyter numpy matplotlib

ADV 1
belajar image di komputer
Gambar = array 3D
shape = height, width, channels
Channels = R, G, B (0-255 per pixel)

===
Gambar/Kamera
    ↓
Preprocessing (resize, normalize)
    ↓
AI Model (TFLite / OpenCV)
    ↓
Inference (proses prediksi)
    ↓
Output: label + confidence score

=====
Istilah	Artinya
Tensor = Array multidimensi (input/output model)
Bounding box = Kotak yang mengelilingi objek terdeteksi
Confidence score = Seberapa yakin AI (0.0–1.0)
FPS = Frame per second (60 = smooth)
Inference time = Waktu model memproses 1 gambar

===

Gambar asli (2848×4288×3)
    ↓ cv2.resize()
Resize (224×224×3)
    ↓ / 255.0
Normalize (0.0 - 1.0)
    ↓ cv2.cvtColor()
BGR → RGB
    ↓ np.expand_dims()
Tensor (1×224×224×3) float64
    ↓ .astype(np.float32)
Final Tensor float32  ← siap masuk TFLite

DONE 

====
terminal: 
source venv/bin/activate
python3 main.py
