python3 -m venv venv
source venv/bin/activate
pip install tflite-runtime numpy Pillow

tflite-runtime or
pip install tensorflow (500mb)
pip install tensorflow-cpu (agak ringan)
pip install ai-edge-litert (ringan) <---

pip install "numpy<2"
ai-litert tidak support dengan python 3 harus di downgrade ke 2

===
persiapan model
Download MobileNetV1 dari TensorFlow Hub  (ini udah jadi tidak perlu training)
Download 1:
curl -L "https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224_quant.tgz" -o /tmp/mobilenet.tgz
or
https://github.com/tflite-soc/tensorflow-models/blob/master/mobilenet-v1/mobilenet_v1_1.0_224_quant.tflite
klik download

Download 2:
curl -o phase_2/phase_2_adv2/models/labels.txt "https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/java/demo/app/src/main/assets/labels_mobilenet_quant_v1_224.txt"
atau
https://github.com/SNXJ/TensorFlowLiteDemo/blob/master/app/src/main/assets/labels_mobilenet_quant_v1_224.txt

hasil download semua diletakin dalam folder models

=====

cek ai litert
pip show ai-edge-litert

lanjut main.py

