class DetectionResult {
  final String label;
  final double confidence;
  final List<double> boundingBox;

  DetectionResult({
    required this.label,
    required this.confidence,
    required this.boundingBox,
  });
}
