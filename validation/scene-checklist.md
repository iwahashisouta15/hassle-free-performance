# Visual Validation Checklist

Gunakan scene, camera, timestamp, dan input yang identik untuk baseline dan perubahan.

## Static Frame

- Pastikan zoom 100%.
- Bandingkan side-by-side.
- Gunakan FLIP atau SSIM diff.
- Periksa foliage, geometry edge, shadows, LOD, texture mip, dan distance detail.

## Motion

- Rekam 10–30 detik kamera bergerak cepat.
- Periksa shimmer pada foliage.
- Periksa ghosting pada moving object.
- Periksa disocclusion dan temporal artifacts.
- Periksa pop-in saat masuk/lewati area.

## UI and Text

- Periksa teks, minimap, crosshair, reticle, dan damage indicator.
- Catat latensi input-to-photon.
- Jika frame generation digunakan, cek HUD duplication, stutter, dan moving particles.

## Minimum Pass Condition

Perubahan visual harus dianggap gagal jika muncul penurunan signifikan pada:

- Edge atau surface detail pada jarak pandang normal.
- Shadow dan indirect lighting continuity.
- Foliage atau vegetation shimmer.
- Pop-in dan streaming blur.
- Noise/artefak baru pada motion.
- Input latency atau frame pacing yang melampaui baseline.
