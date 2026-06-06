import numpy as np 
from PIL import Image # Python Imaging Library
from ai_edge_litert.interpreter import Interpreter 

# load model ke memori
interpreter = Interpreter(model_path="models/mobilenet_v1_1.0_224_quant.tflite")
# siapkan wadah input dan output
interpreter.allocate_tensors()
print("✅ Model loaded")

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(f"Input shape: {input_details[0]['shape']}")
print(f"Input shape: {input_details[0]['dtype']}")
print(f"Output shape: {output_details[0]['shape']}")

img = Image.open("foto.jpg").convert("RGB")
img = img.resize((224, 224))    
# siapkan array berdasar tipe data uint8 0-255
img_array = np.array(img, dtype=np.uint8) # [[[255, 0, 0], [0, 255, 0], ...]] shape: (224, 224, 3)
# (224, 224, 3) = 1 gambar 
img_array = np.expand_dims(img_array, axis=0) # tambah 1 dimensi di depan karena model TFLite butuh input bentuk batch
# (1, 224, 224, 3)
# function ini akan proses banyak gambar sekaligus
print(f"Tensor shape: {img_array.shape}")

# run inference = AI buat prediksi bukan training
# masukkan gambar ke wadar input model
# input_details[0]['index'] = alamat memori
interpreter.set_tensor(input_details[0]['index'], img_array)
interpreter.invoke() # execute

# baca hasil dr prediksi
output = interpreter.get_tensor(output_details[0]['index'])[0]
# baca file label dan simpan sebagai list
with open("models/labels_mobilenet_quant_v1_224.txt", "r") as f:
    # line.strip() = hapus spasi/ newline tiap baris
    # f.readline = baca semua baris jadi list
    labels = [line.strip() for line in f.readlines()]

# output = [12, 0, 255, 8, 180, ...]
# argsort = urut index dari kecil ke besar
# [::-1] balik urutan dari besar ke kecil 
#[:3] = 3 index di awal
top3 = np.argsort(output)[::-1][:3]
print("\n🔍 Top 3 Predictions:")

# enumerate = loop
for i, idx in enumerate(top3):
    confidence = output[idx] / 255.0
    print(f" {i+1}. {labels[idx]} - {confidence:.1%}")

# => GAMBAR TERKLASIFIKASI KUPU-KUPU MONARCH
# 🔍 Top 3 Predictions:
#  1. monarch - 98.0% = kupu-kupu monarch orange hitam
#  2. admiral - 1.6% = kupu2 admiral merah hitam
#  3. lacewing - 0.8% = kupu2 lacewing sayap transparan