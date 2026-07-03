"""
fatiador ESPECIAL do grid do livro folheando (folheando.png -> livro_folheia.png).
diferente do slice_grid.py generico:
- keya tambem a SOMBRA acinzentada que o GPT pos no fundo (claro + sem saturacao),
  nao so o quase-branco -- senao fica um halo esbranquicado ao redor do livro.
- alinha cada frame pela BASE do livro (fundo do tinta-escuro + centro x da base):
  as duas fileiras do grid vieram com o livro em alturas diferentes (~53px) e o
  loop a 8fps "pulava".

uso:  python slice_livro.py            (le folheando.png, escreve livro_folheia.png)
"""
from PIL import Image
import numpy as np

SRC, OUT = "folheando.png", "livro_folheia.png"
COLS, ROWS, inset = 4, 2, 6
TY = 399  # y alvo da base do livro em cada frame

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

out, anchors = [], []
for cell in cells:
    arr = np.asarray(cell).astype(int)
    lum = arr.mean(axis=2)
    sat = arr.max(axis=2) - arr.min(axis=2)
    alpha = np.full(lum.shape, 255)
    alpha[lum >= 252] = 0
    alpha[(lum >= 205) & (sat < 28)] = 0          # halo/sombra acinzentada
    ramp = (lum >= 246) & (lum < 252) & (sat >= 28)
    alpha[ramp] = ((252 - lum[ramp]) / 6 * 255).astype(int)
    rgba = np.dstack([arr, alpha]).astype("uint8")
    dark = (alpha > 128) & (lum < 100)
    ys, xs = np.nonzero(dark)
    ymax = ys.max(); base = ys > ymax - 15
    anchors.append((ymax, xs[base].mean()))
    out.append(rgba)

strip = Image.new("RGBA", (fw * len(out), fh), (0, 0, 0, 0))
for i, (rgba, (ay, ax)) in enumerate(zip(out, anchors)):
    img = Image.fromarray(rgba)
    canv = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
    canv.paste(img, (round(fw / 2 - ax), round(TY - ay)), img)
    strip.paste(canv, (i * fw, 0), canv)
strip.save(OUT)
print(f"FRAMES={len(out)} FW={fw} FH={fh} -> {OUT}")
