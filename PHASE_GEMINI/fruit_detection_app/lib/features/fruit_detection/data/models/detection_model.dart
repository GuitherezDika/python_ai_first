import '../../domain/entities/detection_result.dart';

class DetectionModel extends DetectionResult {
  DetectionModel({
    required super.label,
    required super.confidence,
    required super.boundingBox,
  });

  factory DetectionModel.fromMap(Map<dynamic, dynamic> map) {
    return DetectionModel(
      label: map['label'] as String,
      confidence: (map['confidence'] as num).toDouble(),
      boundingBox: List<double>.from(
        (map['boundingBox'] as List).map((e) => (e as num).toDouble()),
      ),
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'label': label,
      'confidence': confidence,
      'boundingBox': boundingBox,
    };
  }
}
