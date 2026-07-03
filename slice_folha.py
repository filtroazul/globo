"""
fatiador ESPECIAL do grid folha->livro (folhalivrogrid.png -> folha_vira_livro.png).
igual ao slice_livro.py: keya o quase-branco E a sombra acinzentada (halo), mas SEM
realinhar (as ancoras por frame estao hardcoded no index.html — nao mover pixels!).
tambem remove componentes soltos <300px (risquinhos que o GPT deixou no fundo).

uso:  python slice_folha.py    (le folhalivrogrid.png, escreve folha_vira_livro.png)
"""
from PIL import Image
import numpy as np
import scipy.ndimage as ndi

SRC, OUT = "folhalivrogrid.png", "folha_vira_livro.png"
COLS, ROWS, inset = 3, 4, 6

im = Image.open(SRC).convert("RGB")
W, H = im.size
cells = []
for r in range(ROWS):
    for c in range(COLS):
        x0 = round(c * W / COLS) + inset; x1 = round((c + 1) * W / COLS) - inset
        y0 = round(r * H / ROWS) + inset; y1 = round((r + 1) * H / ROWS) - inset
        cells.append(im.crop((x0, y0, x1, y1)))
fw = min(c.width for c in cells); fh = min(c.height for c in cells)
cells = [c.crop((0, 0, fw, fh)) for c in cells]

strip = Image.new("RGBA", (fw * len(cells), fh), (0, 0, 0, 0))
for i, cell in enumerate(cells):
    arr = np.asarray(cell).astype(int)
    lum = arr.mean(axis=2)
    sat = arr.max(axis=2) - arr.min(axis=2)
    alpha = np.full(lum.shape, 255)
    alpha[lum >= 252] = 0
    alpha[(lum >= 205) & (sat < 28)] = 0                  # halo/sombra acinzentada
    ramp = (lum >= 246) & (lum < 252) & (sat >= 28)
    alpha[ramp] = ((252 - lum[ramp]) / 6 * 255).astype(int)
    lab, n = ndi.label(alpha > 16)                        # tira risquinhos soltos
    sizes = ndi.sum(alpha > 16, lab, range(1, n + 1))
    for j in range(1, n + 1):
        if sizes[j - 1] < 300: alpha[lab == j] = 0
    rgba = np.dstack([arr, alpha]).astype("uint8")
    strip.paste(Image.fromarray(rgba), (i * fw, 0))
strip.save(OUT)
print(f"FRAMES={len(cells)} FW={fw} FH={fh} -> {OUT}")
