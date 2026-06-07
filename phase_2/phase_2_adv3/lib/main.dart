import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:tflite_flutter/tflite_flutter.dart';
import 'package:image/image.dart' as img;

void main() => runApp(const MaterialApp(home: AIClassifierApp()));

class AIClassifierApp extends StatefulWidget {
  const AIClassifierApp({super.key});
  @override
  State<AIClassifierApp> createState() => _AIClassifierAppState();
}

class _AIClassifierAppState extends State<AIClassifierApp> {
  late Interpreter _interpreter;
  List<String>? _labels;
  File? _image;
  String _result = 'Select an image to classify';

  @override
  void initState() {
    super.initState();
    _loadModel();
  }

  Future<void> _loadModel() async {
    try {
      _interpreter = await Interpreter.fromAsset(
          'assets/mobilenet_v1_1.0_224_quant.tflite');
      final labelData = await DefaultAssetBundle.of(context)
          .loadString('assets/labels_mobilenet_quant_v1_224.txt');
      print('== $labelData');
      _labels = labelData.split('\n').where((s) => s.isNotEmpty).toList();
      print('Model and labels loaded successfully');
    } catch (e) {
      print('Error loading model: $e');
    }
  }

  Future<void> _pickAndProcessImage() async {
    final picker = ImagePicker();
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);

    if (pickedFile == null) return;

    File imageFile = File(pickedFile.path);
    setState(() {
      _image = imageFile;
      _result = 'Processing image...';
    });

    _runInference(imageFile);
  }

  Future<void> _runInference(File imageFile) async {
    if (_interpreter == null || _labels == null) return;

    // read and resize
    final imageBytes = await imageFile.readAsBytes();
    final decodedImage = img.decodeImage(imageBytes);
    final resizedImage = img.copyResize(decodedImage!, width: 224, height: 224);

    // ubah gambar ke format UintList
    var input = List.generate(
        1,
        (i) => List.generate(
            224, (j) => List.generate(224, (k) => List.filled(3, 0))));

    for (var y = 0; y < 224; y++) {
      for (var x = 0; x < 224; x++) {
        final pixel = resizedImage.getPixel(x, y);
        input[0][y][x][0] = pixel.r.toInt();
        input[0][y][x][1] = pixel.g.toInt();
        input[0][y][x][2] = pixel.b.toInt();
      }
    }

    var output = List.filled(1 * 1001, 0).reshape([1, 1001]);

    _interpreter.run(input, output);

    List<int> results = List<int>.from(output[0]);
    int maxIdx = 0;
    int maxVal = -1;
    for (int i = 0; i < results.length; i++) {
      if (results[i] > maxVal) {
        maxVal = results[i];
        maxIdx = i;
      }
    }

    setState(() {
      _result =
          "Prediksi: ${_labels![maxIdx]} \nConfidence: ${(maxVal / 255 * 100).toStringAsFixed(2)}%";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("TFLite Image Classifier")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            _image != null
                ? Image.file(_image!, height: 300)
                : const Icon(Icons.image, size: 100, color: Colors.grey),
            const SizedBox(height: 20),
            Text(_result,
                textAlign: TextAlign.center,
                style:
                    const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _pickAndProcessImage,
        child: const Icon(Icons.add_a_photo),
      ),
    );
  }
}
