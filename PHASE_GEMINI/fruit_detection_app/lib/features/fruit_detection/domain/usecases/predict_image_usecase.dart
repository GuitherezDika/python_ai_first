import 'dart:typed_data';
import '../../data/datasources/classifier_local_data_source.dart';
import '../entities/detection_result.dart';

class PredictImageUseCase {
  final ClassifierLocalDataSource localDataSource;

  PredictImageUseCase(this.localDataSource);

  Future<List<DetectionResult>> execute(Uint8List imageBytes) async {
    return await localDataSource.classifyImage(imageBytes);
  }
}
