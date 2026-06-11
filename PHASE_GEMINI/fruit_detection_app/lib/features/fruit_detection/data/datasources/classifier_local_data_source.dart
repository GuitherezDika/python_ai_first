import 'dart:developer';
import 'package:flutter/services.dart';
import '../models/detection_model.dart';

class ClassifierLocalDataSource {
  static const _channel = MethodChannel("com.example.fruit_detection/yolov8");

  Future<List<DetectionModel>> classifyImage(Uint8List imageBytes) async {
    try {
      final List<dynamic>? result = await _channel.invokeMethod(
        'predictImage',
        {'imageBytes': imageBytes},
      );
      if (result == null) return [];

      return result.map((item) {
        return DetectionModel.fromMap(item as Map<dynamic, dynamic>);
      }).toList();
    } catch (e) {
      log("Error in classifyImage: $e");
      return [];
    }
  }
}
