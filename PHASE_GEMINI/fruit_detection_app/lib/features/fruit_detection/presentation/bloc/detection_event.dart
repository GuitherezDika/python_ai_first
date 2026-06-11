import 'dart:typed_data';

abstract class DetectionEvent {}

class PredictImageEvent extends DetectionEvent {
  final Uint8List imageBytes;

  PredictImageEvent(this.imageBytes);
}
