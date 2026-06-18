package com.example.fruit_detection_app

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import androidx.annotation.NonNull
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import ai.onnxruntime.OrtEnvironment
import ai.onnxruntime.OrtSession
import ai.onnxruntime.OnnxTensor
import java.nio.FloatBuffer
import java.util.Collections

class MainActivity: FlutterActivity() {
    private val CHANNEL = "com.example.fruit_detection/yolov8"
    private var ortEnv: OrtEnvironment = OrtEnvironment.getEnvironment()
    private var ortSession: OrtSession? = null

    // Sesuai dengan urutan data.yaml di Colab kamu (Contoh isi 5 kelas dummy)
    private val labels = listOf( "Ripe", "Unripe", "Underripe", "Overripe", "Empty Bunch", "Damaged", "Abnormal", "Dirty/Long Stalk")

    override fun configureFlutterEngine(@NonNull flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        
        // Load model ONNX saat aplikasi pertama kali dinyalakan
        initOnnxRuntime()

        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler { call, result ->
            if (call.method == "predictImage") {
                val imageBytes = call.argument<ByteArray>("imageBytes")
                if (imageBytes != null) {
                    try {
                        val predictions = runInference(imageBytes)
                        result.success(predictions)
                    } catch (e: Exception) {
                        result.error("INFERENCE_ERROR", e.message, null)
                    }
                } else {
                    result.error("INVALID_ARGUMENT", "Bytes gambar kosong", null)
                }
            } else {
                result.notImplemented()
            }
        }
    }

    private fun initOnnxRuntime() {
        try {
            if (ortSession == null) {
                // 1. Pastikan nama file di sini sama persis dengan yang ada di folder assets!
                // Jika namanya masih "dummy_fruits.onnx", sesuaikan string di bawah ini.
                val inputStream = assets.open("dummy_fruits_opset19.onnx")
                val modelBytes = inputStream.readBytes()
                inputStream.close()
                
                ortSession = ortEnv.createSession(modelBytes)
                android.util.Log.d("YOLOv8_ONNX", "BERHASIL! Model ONNX sukses dimuat ke Session.")
            }
        } catch (e: Exception) {
            // Perbaikan: Print stack trace lengkap biar kelihatan baris mana yang bikin gagal
            android.util.Log.e("YOLOv8_ONNX", "Gagal total inisialisasi model ONNX!", e)
        }
    }

    private fun runInference(imageBytes: ByteArray): List<Map<String, Any>> {
        val bitmap = BitmapFactory.decodeByteArray(imageBytes, 0, imageBytes.size)

        if (bitmap == null) {
            android.util.Log.e("YOLO_ANDROID", "Gagal melakukan decode gambar. Byte data rusak atau tidak valid.")
            return emptyList()
        }
        
        val resizedBitmap = Bitmap.createScaledBitmap(bitmap, 640, 640, true)
        
        // Perbaikan 1: Alokasikan FloatBuffer dan isi secara berurutan agar pointer bergerak maju
        val imgData = FloatBuffer.allocate(1 * 3 * 640 * 640)
        val pixels = IntArray(640 * 640)
        resizedBitmap.getPixels(pixels, 0, 640, 0, 0, 640, 640)

        // Saluran R (Red)
        for (i in 0 until 640 * 640) {
            val pixel = pixels[i]
            imgData.put(((pixel shr 16) and 0xFF) / 255.0f)
        }
        // Saluran G (Green)
        for (i in 0 until 640 * 640) {
            val pixel = pixels[i]
            imgData.put(((pixel shr 8) and 0xFF) / 255.0f)
        }
        // Saluran B (Blue)
        for (i in 0 until 640 * 640) {
            val pixel = pixels[i]
            imgData.put((pixel and 0xFF) / 255.0f)
        }
        
        // Kembalikan posisi pointer buffer ke 0 sebelum dioper ke ONNX
        imgData.rewind()

        val inputShape = longArrayOf(1, 3, 640, 640)
        val inputTensor = OnnxTensor.createTensor(ortEnv, imgData, inputShape)
        
        val inputName = ortSession?.inputNames?.iterator()?.next() ?: return emptyList()
        val output = ortSession?.run(Collections.singletonMap(inputName, inputTensor))

        val outputTensor = output?.get(0) as? OnnxTensor ?: return emptyList()

        val info = outputTensor.info
        
        val numElements = 8400 
        val numClasses = labels.size
        val totalRows = 4 + numClasses // Berjumlah 12 baris

        val buffer = outputTensor.floatBuffer
        val floatArrayOutput = FloatArray(buffer.remaining())
        buffer.get(floatArrayOutput) 

        val shape = info.shape // Ini akan mengembalikan array dimensi, misal [1, 14, 8400] atau [1, 8400, 14]
        android.util.Log.d("YOLO_SHAPE", "Output Shape Model Anda: ${shape.joinToString(", ")}")
        android.util.Log.d("YOLO_SHAPE", "Total size buffer: ${floatArrayOutput.size}")

        val candidates = ArrayList<Map<String, Any>>()
        val confidenceThreshold = 0.40f 

        // Perbaikan 2: Struktur data YOLOv8 berbentuk [1, 12, 8400]
        // Setiap baris (kolom asli dari model) merepresentasikan 1 deteksi dari total 8400 kandidat
        for (i in 0 until numElements) {
            var maxClassScore = 0.0f
            var classId = -1

            for (c in 0 until numClasses) {
                // Rumus pemetaan flat-array ONNX yang benar untuk shape [1, dimensions, 8400]
                val indexInFlatArray = ((4 + c) * numElements) + i
                
                if (indexInFlatArray >= floatArrayOutput.size) continue

                val score = floatArrayOutput[indexInFlatArray]
                if (score > maxClassScore) {
                    maxClassScore = score
                    classId = c
                }
            }

            if (maxClassScore > confidenceThreshold && classId != -1) {
                // Mengambil nilai koordinat box dengan index array datar yang sudah diperbaiki
                val xCenter = floatArrayOutput[(0 * numElements) + i]
                val yCenter = floatArrayOutput[(1 * numElements) + i]
                val width   = floatArrayOutput[(2 * numElements) + i]
                val height  = floatArrayOutput[(3 * numElements) + i]

                val xMin = xCenter - (width / 2)
                val yMin = yCenter - (height / 2)
                val xMax = xCenter + (width / 2)
                val yMax = yCenter + (height / 2)

                val prediction = HashMap<String, Any>()
                prediction["label"] = labels[classId]
                prediction["confidence"] = maxClassScore.toDouble()
                // Menyimpan koordinat boks ke list
                prediction["boundingBox"] = listOf(xMin.toDouble(), yMin.toDouble(), xMax.toDouble(), yMax.toDouble())
                
                candidates.add(prediction)
            }
        }

        // Terapkan Non-Maximum Suppression (NMS)
        return applyNMS(candidates, iouThreshold = 0.45f)
    }

    // Fungsi tambahan NMS demi kestabilan UI Flutter
    private fun applyNMS(boxes: List<Map<String, Any>>, iouThreshold: Float): List<Map<String, Any>> {
        val sortedBoxes = boxes.sortedByDescending { it["confidence"] as Double }.toMutableList()
        val selectedBoxes = ArrayList<Map<String, Any>>()

        while (sortedBoxes.isNotEmpty()) {
            val current = sortedBoxes.removeAt(0)
            selectedBoxes.add(current)

            val currentBox = current["boundingBox"] as List<Double>
            val iterator = sortedBoxes.iterator()

            while (iterator.hasNext()) {
                val next = iterator.next()
                val nextBox = next["boundingBox"] as List<Double>

                // Hitung Intersection over Union (IoU)
                val xMinInter = Math.max(currentBox[0], nextBox[0])
                val yMinInter = Math.max(currentBox[1], nextBox[1])
                val xMaxInter = Math.min(currentBox[2], nextBox[2])
                val yMaxInter = Math.min(currentBox[3], nextBox[3])

                val interWidth = Math.max(0.0, xMaxInter - xMinInter)
                val interHeight = Math.max(0.0, yMaxInter - yMinInter)
                val interArea = interWidth * interHeight

                val currentArea = (currentBox[2] - currentBox[0]) * (currentBox[3] - currentBox[1])
                val nextArea = (nextBox[2] - nextBox[0]) * (nextBox[3] - nextBox[1])
                val unionArea = currentArea + nextArea - interArea

                val iou = if (unionArea > 0) interArea / unionArea else 0.0

                if (iou > iouThreshold) {
                    iterator.remove() // Hapus boks yang terlalu menumpuk
                }
            }
        }
        return selectedBoxes
    }
}