# fatiador do grid da ESTÁTICA (cena 3) -> tira horizontal.
# diferente dos outros fatiadores: SEM keying e SEM alinhamento — a estática é full-bleed
# (keiar o branco furaria os pontinhos brancos do chuvisco). só corta as células com um
# inset pra descartar eventuais calhas/bordas brancas do grid, e cola lado a lado.
#
# uso: python slice_estatica.py estaticagrid.png estatica2000.png 3 2 [inset]
#      (inset = fração da célula cortada em cada borda; default 0.05)
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
cols, rows = int(sys.argv[3]), int(sys.argv[4])
inset = float(sys.argv[5]) if len(sys.argv) > 5 else 0.05

im = Image.open(src).convert('RGB')
W, H = im.size
cw, ch = W / cols, H / rows
ix, iy = int(cw * inset), int(ch * inset)
fw, fh = int(cw) - 2 * ix, int(ch) - 2 * iy

frames = []
for r in range(rows):
    for c in range(cols):
        x0, y0 = int(c * cw) + ix, int(r * ch) + iy
        frames.append(im.crop((x0, y0, x0 + fw, y0 + fh)))

strip = Image.new('RGB', (fw * len(frames), fh))
for i, f in enumerate(frames):
    strip.paste(f, (i * fw, 0))
strip.save(dst)
print(f'{dst}: {len(frames)} frames de {fw}x{fh}')
