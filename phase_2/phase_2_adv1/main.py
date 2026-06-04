import cv2
import numpy as np

#baca gambar # masukkan gambar foto.jpg setara dengan main.py
img = cv2.imread("foto.jpg")

#cek shape
print(f"Shape: {img.shape}")
print(f"Type: {img.dtype}")
print(f"Type: {img.size}")
# contoh:
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

# tampil
cv2.imshow("Image", img)
cv2.imshow("Resized 224x224", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()