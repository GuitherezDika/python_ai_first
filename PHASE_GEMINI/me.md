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
success_model.export(format='onnx', imgsz=640, simplify=True, opset=19) // tambahan dari flutter harus opset 19
Run
Suksess
-> best.onnx tercreate
/content/runs/detect/train/weights/best.onnx

ukuran = 11.7mb
download dari web

letakin dalam folder project - rename = dummy_fruits_opset19.onnx
============
Tahap 5 = FLUTTER

flutter create fruit_detection_app
tambahkan direktori
    assets/models/dummy_fruits_opset19.onnx
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

issue flutter terkait dataset roboflow yang cocok dengan bridge native code saat ini yaiut Opset 19;
 web: https://colab.research.google.com/drive/1tSfeD6YHvnryv157oTy-yWXS0CbK69Kf#scrollTo=ZtuF5Oi35j9x

 run berurutan:
 code 1 = !pip install ultralytics roboflow

 code 2
 from roboflow import Roboflow

rf = Roboflow(api_key="42OUONhF0n4aZzSTe2fB")
project = rf.workspace("class-ntrex").project("fruits-detection-gh4it")
version = project.version(1)
dataset = version.download("yolov8")

code 3
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(
    data=f"{dataset.location}/data.yaml",
    epochs=15,
    imgsz=640,
    device='cuda'
)

code 4
success_model = YOLO('/content/runs/detect/train/weights/best.pt')
success_model.export(format='onnx', imgsz=640, simplify=True, opset=19)

dummy_fruits_opset19.onnx
download dan letakkan pada
1. android/app/src/main/assets/
2. assets/models/
3. pubspec.yaml 
    flutter:
        uses-material-design: true
        assets:
            - assets/models/dummy_fruits_opset19.onnx

DONE
=====

coba public oil palm fruits model datraset
https://universe.roboflow.com/data-fyp-1/oil-palm-fruit-zohnc/dataset/2/download
Oil Palm Fruit Dataset
klik = Train a model with this dataset
    Fork Dataset - KLIK INI => untuk kopi ke workspace
        PalmBunchesSortation
        Done
    Buka Project Workspace pribadi
        https://app.roboflow.com/palmbunchessortation/projects
        Klik Project yang tadi
        masuk ke detail page
        Tab Kiri:
            Dataset (4274 images)
            Versions --- KLIK INI
                version name = oil_palm_v1
                Preprocessing -> continue
                Augmentation -> Continue
                Create - 
                tunggu proses sampai selesai (beberapa menit)

                Abaikan anjuran Train Data Model
                Cukup klik:
                    Download Dataset
                
                Klik: Show Downloaded Code
                Selesai:
                    !pip install roboflow

                    from roboflow import Roboflow
                    rf = Roboflow(api_key="42OUONhF0n4aZzSTe2fB")
                    project = rf.workspace("palmbunchessortation").project("oil-palm-fruit-zohnc-w8eea")
                    version = project.version(1)
                    # dataset = version.download("folder")
                    dataset = version.download("yolov8")         

                Roboflow Colab
                https://colab.research.google.com/drive/1tSfeD6YHvnryv157oTy-yWXS0CbK69Kf#scrollTo=l5dcRQCtwh8E
                klik code;
                    !pip install ultralytics roboflow
                KLIK code:
                    from roboflow import Roboflow

                    rf = Roboflow(api_key="42OUONhF0n4aZzSTe2fB")
                    project = rf.workspace("palmbunchessortation").project("oil-palm-fruit-zohnc-w8eea")
                    version = project.version(1)

                    # Mengunduh dengan format terstruktur khusus YOLOv8
                    dataset = version.download("yolov8")

                    ATAU
                    from roboflow import Roboflow

                    rf = Roboflow(api_key="42OUONhF0n4aZzSTe2fB")
                    project = rf.workspace("palmbunchessortation").project("oil-palm-fruit-zohnc-w8eea")
                    version = project.version(1)

                    dataset = version.download("folder")


                    ================================

                    1. Jika Menggunakan "folder"Format "folder" adalah format paling dasar (mentah) di Roboflow. Format ini biasanya digunakan jika Anda ingin menyusun dataset secara manual atau ingin menggunakan visualisasi gambar yang menyatu dengan labelnya.Struktur: Biasanya memisahkan data ke dalam folder train, valid, dan test.Format Label: Format file labelnya sering kali berupa file XML (Pascal VOC), JSON, atau bahkan gambar yang sudah di-overlay (ditimpa) kotak pembatasnya, tergantung pada bagaimana dataset tersebut pertama kali diunggah.Tujuan: Cocok jika Anda ingin memproses ulang (preprocessing) gambar secara manual menggunakan script Python sendiri (misalnya dengan OpenCV) sebelum dimasukkan ke model visual.2. Jika Menggunakan "yolov8"Jika baris kode tersebut diubah menjadi version.download("yolov8"), Roboflow akan otomatis mengekspor dataset ke dalam struktur dan format yang siap pakai khusus untuk melatih model YOLOv8.Struktur: Mengikuti standar ketat arsitektur YOLO, yaitu memisahkan gambar (images) dan label (labels).Plaintextdataset/
                    ├── train/
                    │   ├── images/  (berisi file .jpg / .png)
                    │   └── labels/  (berisi file .txt)
                    ├── valid/
                    │   ├── images/
                    │   └── labels/
                    └── data.yaml    (file konfigurasi penting untuk YOLOv8)
                    Format Label: File anotasi otomatis diubah menjadi file teks (.txt). Setiap baris di dalam file teks tersebut berisi koordinat objek yang sudah dinormalisasi antara 0 sampai 1 dengan format:$$\text{class\_id} \quad x_{\text{center}} \quad y_{\text{center}} \quad \text{width} \quad \text{height}$$File Tambahan: Anda akan mendapatkan file data.yaml yang berisi informasi lokasi folder dan nama-nama kelas objek (misalnya untuk proyek kelapa sawit Anda: kelas buah matang, mentah, dll.).