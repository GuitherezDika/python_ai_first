import 'package:flutter_bloc/flutter_bloc.dart';
import '../../domain/usecases/predict_image_usecase.dart';
import 'detection_event.dart';
import 'detection_state.dart';

class DetectionBloc extends Bloc<DetectionEvent, DetectionState> {
  final PredictImageUseCase _predictImageUseCase;

  DetectionBloc(this._predictImageUseCase) : super(DetectionInitial()) {
    on<PredictImageEvent>(_onPredictImage);
  }

  Future<void> _onPredictImage(
    PredictImageEvent event,
    Emitter<DetectionState> emit,
  ) async {
    emit(DetectionLoading());
    try {
      final results = await _predictImageUseCase.execute(event.imageBytes);
      if (results.isEmpty) {
        emit(DetectionSuccess(const []));
      } else {
        emit(DetectionSuccess(results));
      }
    } catch (e) {
      emit(DetectionError("Failed to detect fruits: $e"));
    }
  }
}
