import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'features/fruit_detection/data/datasources/classifier_local_data_source.dart';
import 'features/fruit_detection/domain/usecases/predict_image_usecase.dart';
import 'features/fruit_detection/presentation/bloc/detection_bloc.dart';
import 'features/fruit_detection/presentation/pages/home_detection_page.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    final dataSource = ClassifierLocalDataSource();
    final predictImageUseCase = PredictImageUseCase(dataSource);

    return MaterialApp(
      title: 'YOLOv8 Fruit Detection',
      theme: ThemeData(useMaterial3: true, primarySwatch: Colors.green),
      home: BlocProvider(
        create: (context) => DetectionBloc(predictImageUseCase),
        child: const HomeDetectionPage(),
      ),
    );
  }
}
