# Prosedur Benchmark UE5.4

## Persiapan

1. Tutup aplikasi nonesensial.
2. Aktifkan Windows High Performance/GPU performance mode untuk game dan launcher.
3. Pastikan temperature normal dan batas daya GPU tidak berubah selama run.
4. Matikan dan catat semua aplikasi overlay kecuali PresentMon.
5. Gunakan satu build, satu driver, dan satu resolusi:
   - Build: Shipping
   - RHI: DX12
   - Resolusi: 2560x1440 borderless
   - Upscaler: TSR Quality

## Route Wajib

Gunakan route **Outdoor Settlement** sebanyak 90 detik.

- Durasi: 90 detik.
- Mulai dan berhenti pada lokasi yang sama.
- Gunakan input yang identik atau rekam script traversal.
- Gunakan kamera identik dan tidak ubah FOV antar run.
- Catat waktu first shader/PSO cold load.

## Skenario

### Baseline

- Tidak mengubah kualitas visual.
- Catat Unreal Insights dan PresentMon.

### Cold Cache

- Restart aplikasi dan Windows shader cache sesuai kebijakan proyek.
- Jalankan route sekali sebagai pengenalan shader.
- Ambil 3 run terukur.

### Warm Cache

- Jalankan route sebelumnya, lalu ambil 3 run terukur.
- Bandingkan jumlah hitch dan lokasi histogram.

### GPU Profiling

- Jalankan `stat unit` selama scene outdoor.
- Jalankan `ProfileGPU` pada timestamp yang sama untuk lokasi dominasi.
- Jika suspect pass tidak jelas, gunakan GPU Visualizer dan vendor capture.

## Red Flags

- 1% low <50 FPS.
- P99 frame time >16.6 ms jika target 60 FPS tidak tercapai.
- VRAM mendekati atau melampaui batas kartu.
- Hitch muncul saat asset baru masuk frame.
- Perubahan visual muncul pada shadow, foliage, shimmer, atau tekstur.
- 1 run sangat jauh dari dua run lainnya.
- Cold run lebih buruk secara signifikan daripada warm run; investigasi shader/PSO.

## Output Minimum

```text
average_fps
1_percent_low_fps
0.1_percent_low_fps
frame_time_p99_ms
frame_time_variance
hitch_count
hitches_per_minute
peak_vram_mb
peak_ram_mb
peak_gpu_percent
peak_cpu_percent
```
