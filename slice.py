"""
fatiador de grid -> tira horizontal transparente (branco vira transparente).
baseado no _slice.py do aquarela, mas com grade e nomes configuraveis.

uso:
    python slice.py entrada.png saida.png COLS ROWS
ex:
    python slice.py hand_grid_src.png hand.png 2 2
"""
import sys
from PIL import Image

src_path = sys.argv[1] if len(sys.argv) > 1 else "hand_grid_src.png"
out_path = sys.argv[2] if len(sys.argv) > 2 else "hand.png"
COLS     = int(sys.argv[3]) if len(sys.argv) > 3 else 2
ROWS     = int(sys.argv[4]) if len(sys.argv) > 4 else 2
N = COLS * ROWS

src = Image.open(src_path).convert("RGB")
W, H = src.size

def alpha_of(cell):
    g = cell.convert("L")
    # branco -> transparente; tinta preta -> opaca (corte do quase-branco)
    return g.point(lambda v: 0 if v > 228 else min(255, int((255 - v - 22) * 1.7)))

figs = []
for r in range(ROWS):
    for c in range(COLS):
        x0 = round(c * W / COLS); x1 = round((c + 1) * W / COLS)
        y0 = round(r * H / ROWS); y1 = round((r + 1) * H / ROWS)
        cell = src.crop((x0 + 4, y0 + 4, x1 - 4, y1 - 4))  # ignora 4px de borda
        a = alpha_of(cell)
        bbox = a.getbbox()
        if bbox is None:
            continue
        rgba = cell.convert("RGBA"); rgba.putalpha(a)
        figs.append(rgba.crop(bbox))

assert len(figs) == N, f"esperava {N} figuras, achei {len(figs)} (grade vazia demais?)"

maxW = max(f.width for f in figs)
maxH = max(f.height for f in figs)
padX, padTop, padBot = 16, 10, 3
fw = maxW + 2 * padX
fh = maxH + padTop + padBot

strip = Image.new("RGBA", (fw * N, fh), (0, 0, 0, 0))
for i, fig in enumerate(figs):
    x = i * fw + (fw - fig.width) // 2   # centraliza horizontal
    y = fh - padBot - fig.height         # alinha a base
    strip.paste(fig, (x, y), fig)

strip.save(out_path)
print(f"FRAMES={N} FW={fw} FH={fh}  (folha {strip.width}x{strip.height}) -> {out_path}")
