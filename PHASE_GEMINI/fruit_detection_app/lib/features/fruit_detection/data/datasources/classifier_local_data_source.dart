import 'dart:ffi';

import 'package:flutter/services.dart';
import '../models/detection_model.dart';

class ClassifierLocalDataSource {
  static const _channel = MethodChannel("com.example.fruit_detection/yolov8");
  // = "com.example.fruit_detection/yolov8"
  Future<List<DetectionModel>> classifyImage(Uint8List imageBytes) async {
    print('++1+ $_channel'); // : +++ Instance of 'MethodChannel'
    print('++1+ ${_channel.name}'); // com.example.fruit_detection/yolov8
    print('CLASSIFIER 1');
    try {
      final List<dynamic>? result = await _channel.invokeMethod(
        'predictImage',
        {'imageBytes': imageBytes},
      );
      print("Hasil mentah dari Android: $result");
      //  Hasil mentah dari Android: []
      if (result == null) return [];

      return result.map((item) {
        return DetectionModel.fromMap(item as Map<dynamic, dynamic>);
      }).toList();
    } catch (e, st) {
      print("Error in classifyImage: $e");
      print("Stack trace: $st");
      return [];
    }
  }
}
