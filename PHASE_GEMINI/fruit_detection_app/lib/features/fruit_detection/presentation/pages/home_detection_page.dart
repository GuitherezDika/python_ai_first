import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:image_picker/image_picker.dart';
import '../bloc/detection_bloc.dart';
import '../bloc/detection_event.dart';
import '../bloc/detection_state.dart';

class HomeDetectionPage extends StatefulWidget {
  const HomeDetectionPage({super.key});

  @override
  State<HomeDetectionPage> createState() => _HomeDetectionPageState();
}

class _HomeDetectionPageState extends State<HomeDetectionPage> {
  File? _image;
  final ImagePicker _picker = ImagePicker();

  Future<void> _pickImage(ImageSource source) async {
    try {
      final XFile? pickedFile = await _picker.pickImage(
        source: source,
        maxWidth: 1024, // Membatasi resolusi agar tidak memakan RAM besar
        maxHeight:
            1024, // YOLO hanya butuh 640x640, jadi 1024 sudah sangat aman
        imageQuality:
            85, // Kompresi sedikit agar proses transfer byte via MethodChannel lebih ringan
      );

      if (pickedFile != null) {
        final File file = File(pickedFile.path);

        if (!await file.exists()) {
          debugPrint("File gambar tidak ditemukan di path: ${pickedFile.path}");
          return;
        }

        setState(() {
          _image = file;
        });

        await Future.delayed(const Duration(milliseconds: 50));

        final bytes = await file.readAsBytes();
        print('++= $bytes');

        if (bytes.isEmpty) {
          debugPrint("Gagal membaca bytes: Array kosong.");
          return;
        }

        if (mounted) {
          print('++ MOUNTED ++');
          context.read<DetectionBloc>().add(PredictImageEvent(bytes));
        }
      }
    } catch (e, st) {
      debugPrint("Error saat memilih gambar: $e");
      debugPrint("Stack trace: $st");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('YOLOv8 Fruit Detection'),
        backgroundColor: Colors.green,
        foregroundColor: Colors.white,
      ),
      body: BlocBuilder<DetectionBloc, DetectionState>(
        builder: (context, state) {
          return Column(
            children: [
              const SizedBox(height: 20),

              Expanded(
                child: Center(
                  child: _image == null
                      ? const Text('Silakan pilih gambar buah terlebih dahulu')
                      : Stack(
                          children: [
                            Container(
                              width: 300,
                              height: 300,
                              decoration: BoxDecoration(
                                border: Border.all(color: Colors.grey),
                              ),
                              child: Image.file(_image!, fit: BoxFit.fill),
                            ),
                            if (state is DetectionSuccess)
                              ...state.results.map((result) {
                                final double scaleX = 300 / 640;
                                final double scaleY = 300 / 640;

                                final left = result.boundingBox[0] * scaleX;
                                final top = result.boundingBox[1] * scaleY;
                                final width =
                                    (result.boundingBox[2] -
                                        result.boundingBox[0]) *
                                    scaleX;
                                final height =
                                    (result.boundingBox[3] -
                                        result.boundingBox[1]) *
                                    scaleY;

                                return Positioned(
                                  left: left,
                                  top: top,
                                  width: width,
                                  height: height,
                                  child: Container(
                                    decoration: BoxDecoration(
                                      border: Border.all(
                                        color: Colors.redAccent,
                                        width: 3.0,
                                      ),
                                    ),
                                    child: Align(
                                      alignment: Alignment.topLeft,
                                      child: Container(
                                        color: Colors.redAccent,
                                        padding: const EdgeInsets.symmetric(
                                          horizontal: 4,
                                          vertical: 2,
                                        ),
                                        child: Text(
                                          '${result.label} ${(result.confidence * 100).toStringAsFixed(0)}%',
                                          style: const TextStyle(
                                            color: Colors.white,
                                            fontSize: 10,
                                            fontWeight: FontWeight.bold,
                                          ),
                                        ),
                                      ),
                                    ),
                                  ),
                                );
                              }),
                            if (state is DetectionLoading)
                              Positioned.fill(
                                child: Container(
                                  color: Colors.black45,
                                  child: const Center(
                                    child: CircularProgressIndicator(
                                      color: Colors.white,
                                    ),
                                  ),
                                ),
                              ),
                          ],
                        ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(16.0),
                child: _buildStatusWidget(state),
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _pickImage(ImageSource.camera),
                    icon: const Icon(Icons.camera_alt),
                    label: const Text('Kamera'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.green,
                      foregroundColor: Colors.white,
                    ),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _pickImage(ImageSource.gallery),
                    icon: const Icon(Icons.photo_library),
                    label: const Text('Galeri'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.orange,
                      foregroundColor: Colors.white,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 40),
            ],
          );
        },
      ),
    );
  }

  Widget _buildStatusWidget(DetectionState state) {
    if (state is DetectionSuccess) {
      return Text(
        'Terdeteksi: ${state.results.length} objek buah.',
        style: const TextStyle(
          fontSize: 16,
          fontWeight: FontWeight.bold,
          color: Colors.green,
        ),
      );
    } else if (state is DetectionError) {
      return Text(
        state.message,
        style: const TextStyle(
          fontSize: 14,
          color: Colors.red,
          fontWeight: FontWeight.bold,
        ),
        textAlign: TextAlign.center,
      );
    } else if (state is DetectionLoading) {
      return const Text(
        'YOLOv8 sedang menganalisis...',
        style: TextStyle(fontSize: 14, fontStyle: FontStyle.italic),
      );
    }
    return const Text(
      'Menunggu input gambar...',
      style: TextStyle(fontSize: 14, color: Colors.grey),
    );
  }
}
