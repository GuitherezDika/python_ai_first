import cv2
import numpy as np
import time

#baca gambar # masukkan gambar foto.jpg setara dengan main.py
img = cv2.imread("foto.jpg")

#cek shape
print(f"Shape: {img.shape}")
print(f"Type: {img.dtype}")
print(f"Type: {img.size}")
# Shape: (2848, 4288, 3)
# Type: uint8
# Type: 36636672

# tampilkan info per channel
print(f"Blue channel max: {img[:,:,0].max()}")
print(f"Green channel max: {img[:,:,1].max()}")
print(f"Red channel max: {img[:,:,2].max()}")
# contoh
# Blue channel max: 255
# Green channel max: 255
# Red channel max: 255

# resized -. masuk ke AI model
resized = cv2.resize(img, (224, 224))
print(f"after resize: {resized.shape}")
# after resize: (224, 224, 3)
# OLDShape: (2848, 4288, 3)

# normalized = ubah 0-255 -> 0.0-1.0
normalized = resized / 255.0
print(f"Pixel range: {normalized.min():.2f} - {normalized.max():.2f}")
# Pixel range: 0.00 - 1.00

# convert BGR ke RGB (OPenCV default: BGR, model AI butuh RGB)
rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

tensor = np.expand_dims(normalized, axis=0)
print(f"Tensor shape: {tensor.shape}")   # (1, 224, 224, 3)
print(f"Tensor dtype: {tensor.dtype}")   # float64
# Tensor shape: (1, 224, 224, 3)
# Tensor dtype: float64

tensor = tensor.astype(np.float32)
print(f"Final tensor dtype: {tensor.dtype}")  # float32
# Final tensor dtype: float32

# posisi kotak objek yang terdeteksi format [y min, x min, ymax, xmax] nilai 0.0 - 1.0
bounding_boxes = [
    [0.1, 0.2, 0.5, 0.6], # start 10% atas gambar y1, 20% kiri gambar x1, end 50% dari atas gambar y2, 60% dari kiri gambar x2
    [0.6, 0.1, 0.9, 0.4] # start 60% atas gambar, 10% kiri gambar, end 90% dari atas gambar, 40% dari kiri
]

# ┌──────────────────┐
# │    ┌────────┐    │  ← box 1 (helmet)
# │    │        │    │    dari (45,22) sampai (112,134)
# │    └────────┘    │
# │  ┌──────┐        │  ← box 2 (vest)
# │  │      │        │    dari (134,22) sampai (201,90)
# │  └──────┘        │
# └──────────────────┘

confidence_scores = [0.95, 0.72] # minimum tingkat keyakinan helmet, minimum tingkat keyakinan vest
labels = ["helmet", "vest"] # index 0 = helmet, index 1 = vest

img_draw = resized.copy() # salinan gambar bersih untuk digambarkan bounding box
# (224, 224, 3)
h, w = img_draw.shape[:2] # ambil height dan width; [:2] hanya akan ambail 2 nilai pertama (224, 224) -> h = 224; w = 224

for i, box in enumerate(bounding_boxes):
    y1, x1, y2, x2 = box
    # konversi dari 0-1 ke pixel
    pt1 = (int(x1 * w), int(y1 * h)) # titik kiri atas kotak (x1, y1)
    pt2 = (int(x2 * w), int(y2 * h)) # titik kanan bawah kotak (x2, y2)

    cv2.rectangle(img_draw, pt1, pt2, (0, 255, 0), 2) # (0, 255, 0) = warna hijau (BGR: Blue=0, Green=255, Red=0) ; 2 = ketebalan garis pixel
    cv2.putText(img_draw, f"{labels[i]}: {confidence_scores[i]:.0%}", pt1, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    # perintah untuk tulis label dan konfidens level di atas kotak

start = time.time() # catat waktu mulai
_ = tensor * 1.0 # SIMULASI proses nanti nya akan di invoke ke tf lite; tapi data tidak di simpan, untuk run simulasi di belakang
end = time.time() # catat waktu selesai
print(f"Inference time: {(end-start)*1000:.2f} ms") # tampilan waku milidetik proses


# tampil
cv2.imshow("Image", img)
cv2.imshow("Resized 224x224", resized)
cv2.imshow("Bounding Box Demo", img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()