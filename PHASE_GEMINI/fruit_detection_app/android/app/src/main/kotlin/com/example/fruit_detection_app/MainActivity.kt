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
                // Memastikan pembacaan aset aman dari crash
                val inputStream = assets.open("dummy_fruits.onnx")
                val modelBytes = inputStream.readBytes()
                inputStream.close()
                
                ortSession = ortEnv.createSession(modelBytes)
            }
        } catch (e: Exception) {
            // Jika gagal load, cetak error ke log system Android agar tidak langsung crash buntu
            android.util.Log.e("YOLOv8_ONNX", "Gagal inisialisasi model ONNX: ${e.message}")
        }
    }

    private fun runInference(imageBytes: ByteArray): List<Map<String, Any>> {
        // 1. Konversi byte array dari Flutter menjadi Bitmap Android
        val bitmap = BitmapFactory.decodeByteArray(imageBytes, 0, imageBytes.size)
        
        // 2. PRE-PROCESSING: Resize gambar menjadi 640x640 sesuai requirement YOLOv8 kamu
        val resizedBitmap = Bitmap.createScaledBitmap(bitmap, 640, 640, true)
        
        // 3. Alokasikan buffer data Float untuk gambar (Format BCHW: 1 * 3 * 640 * 640)
        val imgData = FloatBuffer.allocate(1 * 3 * 640 * 640)
        imgData.rewind()

        val pixels = IntArray(640 * 640)
        resizedBitmap.getPixels(pixels, 0, 640, 0, 0, 640, 640)

        // 4. Normalisasi pixel RGB dari 0-255 menjadi 0.0 - 1.0 (Standard YOLOv8)
        // Pola planar: Semua R dulu, lalu semua G, lalu semua B
        for (i in 0 until 640 * 640) {
            val pixel = pixels[i]
            imgData.put(i, ((pixel shr 16 and 0xFF) / 255.0f)) // Red
            imgData.put(640 * 640 + i, ((pixel shr 8 and 0xFF) / 255.0f)) // Green
            imgData.put(2 * 640 * 640 + i, ((pixel and 0xFF) / 255.0f)) // Blue
        }

        // 5. Buat Tensor Input ONNX
        val inputShape = longArrayOf(1, 3, 640, 640)
        val inputTensor = OnnxTensor.createTensor(ortEnv, imgData, inputShape)
        
        // 6. Jalankan Evaluasi Model
        val inputName = ortSession?.inputNames?.iterator()?.next() ?: return emptyList()
        val output = ortSession?.run(Collections.singletonMap(inputName, inputTensor))

        // 7. POST-PROCESSING: Parsing array output (1, 9, 8400)
        val outputTensor = output?.get(0) as? OnnxTensor ?: return emptyList()
        val outputArray = outputTensor.value as Array<Array<FloatArray>> // [1][9][8400]
        
        val results = ArrayList<Map<String, Any>>()
        val numElements = 8400 // Jumlah kandidat boks dari YOLOv8
        val numClasses = labels.size

        // Threshold untuk menyaring deteksi hantu/kurang yakin
        val confidenceThreshold = 0.40f 

        for (i in 0 until numElements) {
            // Cari skor kelas tertinggi untuk boks index ke-i
            var maxClassScore = 0.0f
            var classId = -1

            for (c in 0 until numClasses) {
                // Elemen 0,1,2,3 adalah bounding box (x, y, w, h). Kelas dimulai dari index ke-4
                val score = outputArray[0][4 + c][i]
                if (score > maxClassScore) {
                    maxClassScore = score
                    classId = c
                }
            }

            // Jika skor di atas threshold, ambil boksnya
            if (maxClassScore > confidenceThreshold && classId != -1) {
                val xCenter = outputArray[0][0][i]
                val yCenter = outputArray[0][1][i]
                val width = outputArray[0][2][i]
                val height = outputArray[0][3][i]

                // Ubah format YOLO (Center X, Center Y, W, H) menjadi format pojok boks (Min X, Min Y, Max X, Max Y)
                val xMin = xCenter - (width / 2)
                val yMin = yCenter - (height / 2)
                val xMax = xCenter + (width / 2)
                val yMax = yCenter + (height / 2)

                val prediction = HashMap<String, Any>()
                prediction["label"] = labels[classId]
                prediction["confidence"] = maxClassScore.toDouble()
                prediction["boundingBox"] = listOf(xMin.toDouble(), yMin.toDouble(), xMax.toDouble(), yMax.toDouble())
                
                results.add(prediction)
            }
        }

        // Catatan: Untuk simplifikasi dummy model, kita belum menambahkan algoritma NMS (Non-Maximum Suppression)
        // Jadi jika ada boks menumpuk, itu wajar untuk tahap awal ini.
        return results
    }
}