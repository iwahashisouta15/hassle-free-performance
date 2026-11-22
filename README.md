# Hassle-Free Performance (H-F-P)

Panduan teknis optimasi Unreal Engine 5.4 untuk open-world FPS, berbasis data aktual dan verifikasi visual A/B. Tujuan benchmark: 60 FPS pada 1440p, 1% low >= 50 FPS, dan frame-time target <=16.6 ms.

## Konfigurasi Referensi

- Engine: Unreal Engine 5.4
- Platform: PC, Windows 11
- CPU: AMD Ryzen 7 7800X3D
- GPU: NVIDIA RTX 4070, 12 GB VRAM
- RAM: 32 GB
- Resolusi: 2560x1440, borderless
- Build: Shipping
- RHI: DX12
- Baseline: TSR Quality
- Gejala: traversal hitch di open-world outdoor; indikasi awal GPU 98%

Data baseline belum cukup untuk menyimpulkan optimasi spesifik. Semua nilai performa harus diukur, bukan diperkirakan.

## Metrik Wajib

- Average FPS
- 1% low dan 0.1% low
- Frame-time average, variance, dan p99
- Hitch per menit
- Peak GPU/CPU utilization
- Peak VRAM dan RAM
- GPU, Game Thread, Render Thread, dan Frame time
- Input-to-photon latency bila frame generation digunakan

## Struktur Repositori

```text
/docs/benchmarking.md
/docs/troubleshooting.md
/tools/run_ue5_benchmark.ps1
/tools/analyze_presentmon.py
/validation/scene-checklist.md
/config/UE5.4/PerformanceBaseline.ini
```

## Mulai Cepat

1. Jalankan target route selama 90 detik pada scene **Outdoor Settlement**.
2. Gunakan build Shipping yang sama untuk semua run.
3. Aktifkan Unreal Insights dan PresentMon.
4. Jalankan minimal tiga kali untuk cold cache dan tiga kali untuk warm cache.
5. Catat semua frame-time dan hitch metrics.
6. Jangan mengubah resolusi output atau preset grafis sebagai baseline gratis.

## Membaca Bottleneck

- `stat unit`: Frame, Game, Draw, dan GPU.
- Jika GPU mendekati 98% dan GPU time mendominasi, fokus pada pass rendering.
- Jika Render Thread mendominasi, profil draw submit dan scene setup.
- Jika Game Thread mendominasi, profil tick, event, Blueprint, AI, dan physics.
- Jika hitch berulang di posisi traversal yang sama, korelasikan dengan streaming dan memory trace.

## Kontrol Perubahan

Setiap perubahan wajib memiliki:

- Kamera dan route identik.
- Build dan driver identik.
- Side-by-side pada zoom 100%.
- SSIM/FLIP atau image diff.
- Video gerakan untuk pop-in, shimmer, ghosting, dan disocclusion.
- Delta frame time dan hitch count.

## Referensi Profiling UE5.4

- Unreal Insights
- GPU Visualizer / `ProfileGPU`
- `stat unit`
- `stat unitgraph`
- `stat game`
- `stat streaming`
- `stat streamingoverview`
- `stat hitches` dan `t.HitchThresholdMilliseconds` bila tersedia pada branch/proyek
- RenderDoc atau vendor GPU capture

Nama CVar/API spesifik yang belum terverifikasi pada UE 5.4 project harus dikonfirmasi sebelum digunakan.
