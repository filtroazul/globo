"""
fatiador ESPECIAL do grid da menina levantando (levantandogrid.png -> menina_levanta.png).
o GPT desenhou as figuras VAZANDO das celulas (pes da fileira do meio encostam na divisa,
cabelo da fileira de baixo atravessa pra cima), entao recorte por celula corta cabeca/junta
borrao. aqui cada menina e separada por COMPONENTE CONEXO de tinta (scipy.ndimage.label) e
atribuida a celula do seu centroide; depois ancora pelos pes (base do bbox) + centro x.

uso:  python slice_levanta.py     (le levantandogrid.png, escreve menina_levanta.png)
"""
from PIL import Image
import numpy as np
import scipy.ndimage as ndi

SRC, OUT = "levantandogrid.png", "menina_levanta.png"
COLS, ROWS = 4, 3
FW, FH = 360, 340          # celula de saida (maior figura ~305px de altura)
MIN_PX = 500               # descarta poeira

im = Image.open(SRC).convert("RGB")
W, H = im.size
arr = np.asarray(im).astype(int)
lum = arr.mean(axis=2)

mask = lum < 238
lab, n = ndi.label(mask)
sizes = ndi.sum(mask, lab, range(1, n + 1))

# alpha global (rampa no quase-branco, como o slice_grid)
alpha = np.clip((238 - lum) / 16 * 255, 0, 255)

cells = [[] for _ in range(COLS * ROWS)]      # comps por celula (via centroide)
for i in range(1, n + 1):
    if sizes[i - 1] < MIN_PX: continue
    ys, xs = np.nonzero(lab == i)
    r = min(ROWS - 1, int(ys.mean() * ROWS / H))
    c = min(COLS - 1, int(xs.mean() * COLS / W))
    cells[r * COLS + c].append(i)

strip = Image.new("RGBA", (FW * COLS * ROWS, FH), (0, 0, 0, 0))
for k, comps in enumerate(cells):
    m = np.isin(lab, comps)
    m = ndi.binary_dilation(m, iterations=4)  # inclui a franja suave do traco
    a = np.where(m, alpha, 0).astype("uint8")
    ys, xs = np.nonzero(a > 16)
    y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    rgba = np.dstack([arr[y0:y1 + 1, x0:x1 + 1], a[y0:y1 + 1, x0:x1 + 1]]).astype("uint8")
    fig = Image.fromarray(rgba)
    canv = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    canv.paste(fig, (round(FW / 2 - fig.width / 2), FH - 4 - fig.height), fig)
    strip.paste(canv, (k * FW, 0), canv)
    print(f"frame {k}: fig {fig.width}x{fig.height} ({len(comps)} comp)")
strip.save(OUT)
print(f"FRAMES={COLS*ROWS} FW={FW} FH={FH} -> {OUT}")
