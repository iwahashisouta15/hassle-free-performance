# UE5.4 Troubleshooting

## Jika GPU Mendominasi

1. Jalankan `stat unit` dan pastikan GPU time benar-benar lebih besar dari Frame, Game, dan Draw.
2. Jalankan `ProfileGPU` pada frame dengan hitch atau route yang representative.
3. Identifikasi pass GPU termahal.
4. Cari biaya per mesh, shadow, translucency, particle, post-process, atau Lumen/VSM bila digunakan.
5. Lakukan satu perubahan pada satu waktu.

**Jangan** menurunkan resolusi output atau preset grafis sebagai solusi sebelum bottleneck teridentifikasi.

## Jika Render Thread Mendominasi

1. Jalankan Unreal Insights dan sort Render Thread.
2. Periksa scene update, draw submission, dan shadow setup.
3. Pastikan bounds/culling valid.
4. Periksa jumlah visible mesh dan draw call.
5. Terapkan instancing/batching hanya pada workload yang terbukti cocok.

## Jika Game Thread Mendominasi

1. Jalankan `stat game` dan Unreal Insights trace.
2. Cari tick count, C++/Blueprint hotspot, AI, physics, dan actor spawning.
3. Hapus tick berulang atau beri interval update.
4. Jangan melakukan nativisasi massal tanpa hotspot yang terukur.

## Jika Hitch Berkorelasi dengan Streaming

1. Jalankan `stat streaming` dan Unreal Insights memory/I/O trace.
2. Tandai timestamp hitch pada route.
3. Cocokkan area/world partition dan asset loading.
4. Audit critical texture/mesh residency.
5. Tambah preload hanya untuk asset krusial.
6. Jangan menaikkan texture streaming pool tanpa bukti eviction dan VRAM budget.

## Jika Hitch Berkorelasi Cold Shader/PSO

1. Bandingkan cold dan warm runs.
2. Gunakan Unreal Insights untuk mencari compile/PSO hit.
3. Verifikasi nama workflow PSO warmup yang tersedia pada UE 5.4 dan project branch.
4. Jangan mengubah nama CVar/API yang belum ada di project Anda.

## Jika Frame Pacing Buruk Tetapi FPS Rata-Rata Baik

1. Ambil p99, variance, 1% low, 0.1% low dan hitch count.
2. Cocokkan PresentMon capture dengan Unreal Insights.
3. Pertimbangkan frame limiting VRR/Reflex/Anti-Lag di level system hanya setelah base frame rate stabil.
4. Jangan mengaktifkan frame generation tanpa mengukur latency dan artefak HUD.
