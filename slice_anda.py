"""
fatiador do grid da menina andando (andandogrid.png -> menina_anda.png).
mesma tecnica do slice_levanta.py (componentes conexos, ancora pelos pes),
mas celula de saida dimensionada pela maior figura do proprio grid.
serve tambem pra variantes: python slice_anda.py [entrada.png] [saida.png] [COLS] [ROWS]
ex 12 quadros:  python slice_anda.py andandogrid_olhando.png menina_anda_olha.png 4 3
"""
import sys
from PIL import Image
import numpy as np
import scipy.ndimage as ndi

SRC = sys.argv[1] if len(sys.argv) > 1 else "andandogrid.png"
OUT = sys.argv[2] if len(sys.argv) > 2 else "menina_anda.png"
COLS = int(sys.argv[3]) if len(sys.argv) > 3 else 4
ROWS = int(sys.argv[4]) if len(sys.argv) > 4 else 2
MIN_PX = 500

im = Image.open(SRC).convert("RGB")
W, H = im.size
arr = np.asarray(im).astype(int)
lum = arr.mean(axis=2)
mask = lum < 238
lab, n = ndi.label(mask)
sizes = ndi.sum(mask, lab, range(1, n + 1))
alpha = np.clip((238 - lum) / 16 * 255, 0, 255)

cells = [[] for _ in range(COLS * ROWS)]
for i in range(1, n + 1):
    if sizes[i - 1] < MIN_PX: continue
    ys, xs = np.nonzero(lab == i)
    r = min(ROWS - 1, int(ys.mean() * ROWS / H))
    c = min(COLS - 1, int(xs.mean() * COLS / W))
    cells[r * COLS + c].append(i)

figs = []
for comps in cells:
    m = ndi.binary_dilation(np.isin(lab, comps), iterations=4)
    a = np.where(m, alpha, 0).astype("uint8")
    ys, xs = np.nonzero(a > 16)
    figs.append((a, ys.min(), ys.max(), xs.min(), xs.max()))
fw = max(f[4] - f[3] for f in figs) + 24
fh = max(f[2] - f[1] for f in figs) + 12

strip = Image.new("RGBA", (fw * len(figs), fh), (0, 0, 0, 0))
for k, (a, y0, y1, x0, x1) in enumerate(figs):
    rgba = np.dstack([arr[y0:y1 + 1, x0:x1 + 1], a[y0:y1 + 1, x0:x1 + 1]]).astype("uint8")
    fig = Image.fromarray(rgba)
    canv = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
    canv.paste(fig, (round(fw / 2 - fig.width / 2), fh - 4 - fig.height), fig)
    strip.paste(canv, (k * fw, 0), canv)
strip.save(OUT)
print(f"FRAMES={len(figs)} FW={fw} FH={fh} -> {OUT}")
