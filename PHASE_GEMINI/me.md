https://universe.roboflow.com/

Looking: Fruit Detection
https://universe.roboflow.com/class-ntrex/fruits-detection-gh4it/dataset/1
Download Dataset:
    Format: YOLOv8
        Show Download Code

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="42OUONhF0n4aZzSTe2fB")
project = rf.workspace("class-ntrex").project("fruits-detection-gh4it")
version = project.version(1)
dataset = version.download("yolov8")

Langkah 1 DONE

==============================================

step 2
Buka https://colab.research.google.com/      atau
https://colab.research.google.com/?pli=1

new notebook
rename notebook = YOLOv8_Fruit_Detection.ipynb
aktifkan GPU:
    runtime - change runtime type
        Python 3
        Hardware accelerator: T4 GPU
        Save

Terminal 1:
!pip install ultralytics roboflow

terminal 2:
from roboflow import Roboflow

rf = Roboflow(api_key="42OUONhF0n4aZzSTe2fB")
project = rf.workspace("class-ntrex").project("fruits-detection-gh4it")
version = project.version(1)
dataset = version.download("yolov8")

Done -> Drawwer Kiri sudah munculin folder baru: fruits-detection-1
=====

3. Proses Training Singkat (Hanya untuk Dummy Model)
Karena ini hanya untuk dummy, kita tidak butuh akurasi 100%. Kita hanya butuh strukturnya jadi. Set epochs=10 atau epochs=20 saja agar cepat.

Code Python di web: #  YOLOv8 Nano (yolov8n.pt) = untuk android 
### start here ###
from ultralytics import YOLO

model = YOLO('yolov8n.pt') 

results = model.train(
    data=f"{dataset.location}/data.yaml", 
    epochs=15, 
    imgsz=640, 
    device='cuda'
)

akan create folder baru "runs"
https://colab.research.google.com/drive/1tSfeD6YHvnryv157oTy-yWXS0CbK69Kf#scrollTo=JncW_eU1yZCe

tujuannya: hasil training untuk Android "best.pt" akan tersimpan pada:
runs/detect/train/weights/best.pt
DONE

======

Tahap 4
web Yolo kembali ke project
klik code

success_model = YOLO('/content/runs/detect/train/weights/best.pt')
success_model.export(format='onnx', imgsz=640, simplify=True)
Run
Suksess
-> best.onnx tercreate
/content/runs/detect/train/weights/best.onnx

ukuran = 11.7mb
download dari web

letakin dalam folder project - rename = dummy_fruits.onnx
============
Tahap 5 = FLUTTER

flutter create fruit_detection_app
tambahkan direktori
    assets/models/dummy_fruits.onnx
daftarkan asset di pubspec.yaml
flutter pub get

struktur project:

lib/
├── features/
│   ├── fruit_detection/             <-- 🍏 Fitur 1: Deteksi Buah
│   │   ├── data/
        │   ├── datasources/
        │   │   └── classifier_local_data_source.dart ✨
        │   └── models/
        │       └── detection_model.dart
        ├── domain/
        │   ├── entities/
        │   │   └── detection_result.dart
        │   └── usecases/
        │       └── predict_image_usecase.dart ✨
│   │   └── presentation/
│   │       ├── bloc/                <-- Hanya berisi BLoC khusus deteksi buah
│   │       │   ├── detection_bloc.dart
│   │       │   ├── detection_event.dart
│   │       │   └── detection_state.dart
│   │       └── pages/
│   │
│   ├── detection_history/           <-- 📜 Fitur 2: Riwayat Deteksi (Banyak BLoC baru di sini)
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   │       └── bloc/                <-- BLoC khusus untuk riwayat & pagination
│   │
│   └── auth/                        <-- 🔑 Fitur 3: Login & Register
│       ├── data/
│       ├── domain/
│       └── presentation/
│           └── bloc/                <-- BLoC khusus untuk login/logout
│
├── core/                            <-- Tempat komponen yang dipakai bersama (Shared)
│   ├── theme/
│   └── utils/
└── main.dart

==============

=====
