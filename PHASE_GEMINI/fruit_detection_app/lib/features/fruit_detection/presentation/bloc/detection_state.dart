import '../../domain/entities/detection_result.dart';

abstract class DetectionState {}

class DetectionInitial extends DetectionState {}

class DetectionLoading extends DetectionState {}

class DetectionSuccess extends DetectionState {
  final List<DetectionResult> results;

  DetectionSuccess(this.results);
}

class DetectionError extends DetectionState {
  final String message;

  DetectionError(this.message);
}
