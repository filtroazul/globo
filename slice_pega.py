"""
fatiador do meninapegagrid.png -> menina_pega.png (12 frames 4x3).
igual ao slice_levanta.py: as figuras VAZAM das células (os PÉS da menina invadem a
fileira de baixo — fatiar por grade fixa decepava o pé), então o recorte é por
COMPONENTE CONEXO atribuído à célula do centroide. depois re-registra pelo CORPO
(centroide x do maior componente no centro, pés = fundo do bbox do corpo em fh-4)
e mede o celular do f0 (pra calibração no index.html).

uso: python slice_pega.py [entrada] [saida]
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

SRC = sys.argv[1] if len(sys.argv) > 1 else "meninapegagrid.png"
OUT = sys.argv[2] if len(sys.argv) > 2 else "menina_pega.png"
COLS, ROWS = 4, 3
THRESH, RAMP = 252, 6
MARGIN = 60          # folga vertical (pé/cabelo vazam da célula)
PAD = 4              # pés em fh-4 (convenção do projeto)

im = Image.open(SRC).convert("RGB")
W, H = im.size
g = np.asarray(im.convert("L")).astype(np.int32)
a = np.clip((THRESH - g) * 255 // RAMP, 0, 255).astype(np.uint8)   # keying do branco
rgba = np.dstack([np.asarray(im), a])

lab, n = ndimage.label(a > 16)
sizes = ndimage.sum(a > 16, lab, range(1, n + 1))
cw, rh = W / COLS, H / ROWS
fw, fh = int(round(cw)), int(round(rh)) + 2 * MARGIN

cells = [np.zeros((fh, fw, 4), np.uint8) for _ in range(COLS * ROWS)]
for comp in range(1, n + 1):
    if sizes[comp - 1] < 25:                    # poeira
        continue
    ys, xs = np.nonzero(lab == comp)
    c = min(COLS - 1, int(xs.mean() // cw))
    r = min(ROWS - 1, int(ys.mean() // rh))
    ox, oy = int(round(c * cw)), int(round(r * rh)) - MARGIN
    for y, x in zip(ys, xs):
        yy, xx = y - oy, x - ox
        if 0 <= yy < fh and 0 <= xx < fw:
            cells[r * COLS + c][yy, xx] = rgba[y, x]

strip = Image.new("RGBA", (fw * COLS * ROWS, fh), (0, 0, 0, 0))
for i, cell in enumerate(cells):
    aa = cell[:, :, 3]
    lab2, n2 = ndimage.label(aa > 16)
    s2 = ndimage.sum(aa > 16, lab2, range(1, n2 + 1))
    main = 1 + int(np.argmax(s2))
    ys, xs = np.nonzero(lab2 == main)           # corpo
    ccx, bot, bh = xs.mean(), ys.max(), ys.max() - ys.min() + 1
    offx, offy = round(fw / 2 - ccx), round((fh - PAD) - bot)
    msg = f"f{i}: corpo h={bh} bottom={bot}->{fh-PAD}"
    if n2 > 1:                                   # celular separado (frames iniciais)
        order = np.argsort(s2)[::-1]
        if s2[order[1]] > 800:
            comp2 = 1 + int(order[1])
            ys2, xs2 = np.nonzero(lab2 == comp2)
            msg += (f"  celular: cx={(xs2.min()+xs2.max())/2+offx:.0f}"
                    f" cy={(ys2.min()+ys2.max())/2+offy:.0f}"
                    f" w={xs2.max()-xs2.min()+1} h={ys2.max()-ys2.min()+1}")
    print(msg)
    img = Image.fromarray(cell)
    canv = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
    canv.paste(img, (offx, offy), img)
    strip.paste(canv, (i * fw, 0), canv)

strip.save(OUT)
print(f"FRAMES={COLS*ROWS} FW={fw} FH={fh} -> {OUT}")
