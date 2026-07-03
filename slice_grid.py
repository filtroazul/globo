"""
fatiador de grid com REGISTRO FIXO + ALINHAMENTO pelo corpo (pra loops de boil).
- keya só o quase-branco (amarelo/preto ficam opacos).
- alinha cada quadro pelo CENTRO DE MASSA dos pixels escuros (o corpo),
  então o personagem trava no lugar e só o traço/braço mudam.

uso:  python slice_grid.py entrada.png saida.png COLS ROWS [inset] [align] [thresh]
ex :  python slice_grid.py meninagrid.png menina.png 4 2
      python slice_grid.py folhalivrogrid.png folha_vira_livro.png 3 4 6 none 252
thresh = luminância a partir da qual vira transparente (default 238; use 252 quando
o desenho tem páginas/áreas creme-claras que o default apagaria — fundo ~254).
"""
import sys
from PIL import Image
try:
    import numpy as np
    HAVE_NP = True
except Exception:
    HAVE_NP = False

src_path = sys.argv[1]
out_path = sys.argv[2]
COLS     = int(sys.argv[3])
ROWS     = int(sys.argv[4])
inset    = int(sys.argv[5]) if len(sys.argv) > 5 else 6
align    = sys.argv[6] if len(sys.argv) > 6 else "body"   # body (centro de massa) | bottom (pés) | none
thresh   = int(sys.argv[7]) if len(sys.argv) > 7 else 238 # >=thresh transparente (252 p/ páginas claras)
ramp     = 16 if thresh <= 240 else 6

im = Image.open(src_path).convert("RGB")
W, H = im.size

def alpha_of(cell):
    g = cell.convert("L")
    return g.point(lambda v: 0 if v >= thresh else (255 if v <= thresh - ramp else int((thresh - v) / ramp * 255)))

cells = []
for r in range(ROWS):
    for c in range(COLS):
        x0 = round(c * W / COLS) + inset; x1 = round((c + 1) * W / COLS) - inset
        y0 = round(r * H / ROWS) + inset; y1 = round((r + 1) * H / ROWS) - inset
        cell = im.crop((x0, y0, x1, y1))
        rgba = cell.convert("RGBA"); rgba.putalpha(alpha_of(cell))
        cells.append(rgba)

fw = min(c.width for c in cells); fh = min(c.height for c in cells)
cells = [c.crop((0, 0, fw, fh)) for c in cells]
N = len(cells)

def centroid(rgba):
    arr = np.asarray(rgba)
    a = arr[:, :, 3]; lum = arr[:, :, :3].mean(axis=2)
    mask = (a > 128) & (lum < 100)                 # pixels escuros = corpo
    if mask.sum() < 50:
        mask = a > 128                             # fallback: qualquer opaco
    ys, xs = np.nonzero(mask)
    return xs.mean(), ys.mean()

if align == "bottom":
    # ancora pelos PÉS: fundo do bbox no mesmo Y, centraliza X (bom p/ levantar/subir)
    boxes = [c.split()[3].getbbox() for c in cells]
    baseY = fh - 4; cx0 = fw / 2
    aligned = []
    for cell, b in zip(cells, boxes):
        bcx = (b[0] + b[2]) / 2
        off = (round(cx0 - bcx), round(baseY - b[3]))
        canv = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
        canv.paste(cell, off, cell)
        aligned.append(canv)
    cells = aligned
    print("alinhado pela base (pés)")
elif align == "body" and HAVE_NP:
    cents = [centroid(c) for c in cells]
    tx = sum(cx for cx, cy in cents) / N
    ty = sum(cy for cx, cy in cents) / N
    aligned = []
    for cell, (cx, cy) in zip(cells, cents):
        off = (round(tx - cx), round(ty - cy))
        canv = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
        canv.paste(cell, off, cell)
        aligned.append(canv)
    cells = aligned
    print(f"alinhado pelo corpo (alvo x={tx:.0f} y={ty:.0f})")
else:
    print("sem alinhamento")

strip = Image.new("RGBA", (fw * N, fh), (0, 0, 0, 0))
for i, cc in enumerate(cells):
    strip.paste(cc, (i * fw, 0), cc)
strip.save(out_path)
print(f"FRAMES={N} FW={fw} FH={fh} -> {out_path}")
