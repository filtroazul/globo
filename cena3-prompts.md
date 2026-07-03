# prompts — cena 3 (TV de tubo anos 2000)

beat do roteiro: *"a animação volta no tempo. uma televisão antiga surge no centro. dela
saem luzes, letras, números e personagens (referência aos desenhos emblemáticos da TV
Cultura / TV Globinho)."*

**o código já espera por tudo** (carregamento especulativo, igual aos futuros): é só
salvar na pasta com os nomes exatos e dar replay (R). enquanto os arquivos não existem,
o código usa a TV da cena 1 como stand-in e uma estática de código.

## regras de ouro

- **anexar referência de estilo** (`ultimo_frame.png` ou `tv1.png`) em todo prompt.
- gerar cada família na MESMA conversa do ChatGPT ("same exact technique").
- refs da tela (tvref): **full-bleed** — a cena preenche o quadro ATÉ A BORDA (vai
  esticada/cortada dentro da tela da TV, não pode ter margem branca nem moldura).

---

## 1. a TV — DECIDIDO: é a MESMA da cena 1 (tv1/2/3)

✅ **não precisa gerar TV nova.** decisão do Iagho (2026-07-02): a cena 3 usa a mesma TV
de madeira da cena 1 (o boil tv1/tv2/tv3 já existente) — o que muda é o CONTEÚDO da tela:
a estática colorida anos 2000 e as referências. `SCREEN3` = `SCREEN` (mesma calibração).

⚠️ depois que chegar: recalibrar `SCREEN3` no index.html (tecla **D** mostra o retângulo
vermelho da tela; hoje está com os valores da TV stand-in).

## 2. a estática colorida DESENHADA — grid 3×2 → `estatica2000.png`

DECISÃO (Iagho, 2026-07-02): a estática também é **desenhada à mão, em GRID de variações**
(igual aos outros grids do projeto), pra ferver a 8fps com contorno cartunesco — não é
uma imagem só chacoalhada. **anexar `tv1.png` como referência de estilo.**

> Attached is a reference of my hand-drawn ink animation style. Create ONE image that is
> a grid of 6 equal panels (3 columns × 2 rows, no gaps, no borders, no numbers). Every
> panel shows THE SAME subject: colorful analog TV static — the "snow" of a CRT television
> with no signal in the early 2000s — but HAND-DRAWN in the same loose, scribbled,
> imperfect ink technique as the reference: a dense chaos of small scribbly dashes, dots
> and short strokes of white, black, red, green, blue and magenta, with a few faint
> horizontal interference lines, looking like ink and gouache marks made by hand, NOT
> digital noise. Each panel is completely filled edge to edge (full-bleed). The 6 panels
> are slightly different from each other — same density, same colors, same technique,
> only the random strokes change — like 6 frames of a hand-drawn animation. Landscape
> panels. No text, no TV, no frame lines.

quando chegar (salvar como `estaticagrid.png`):

```
python slice_estatica.py estaticagrid.png estatica2000.png 3 2
```

(fatiador SEM keying — os outros furariam os pontinhos brancos do chuvisco; ele corta as
células com um inset de 5% pra descartar calhas e cola a tira. o código toca a tira a
**8fps** (`EST_N:6`) + chacoalho leve + scanlines. se o grid vier 4×2=8, fatiar `4 2` e
mudar `EST_N` pra 8 no index.html.)

## 2b. ⭐ DECISÃO FINAL: a TV COM a estática — `tvest1/2/3.png` (substitui o §2)

o Iagho quer a **TV já com a estática colorida NA TELA, pronta do GPT** — a mesma TV da
cena 1, em **3 variações** (mesmo esquema tv1/tv2/tv3: imagens 16:9 inteiras, boil 8fps).
o §2 acima fica só como fallback (o código ainda aceita a tira avulsa se existir).
**anexar `tv1.png`** e colar:

> Attached is a hand-drawn ink television from my animation. Redraw THE SAME image — the
> exact same television, same design, same position, same size, same framing, same loose
> scribbled black India ink technique, same PURE WHITE background — but now the TV is
> TURNED ON: its screen is completely filled, edge to edge, with colorful analog TV
> static — the "snow" of an early-2000s CRT with no signal — HAND-DRAWN in the same
> scribbly imperfect technique: a dense chaos of small dashes, dots and short strokes of
> white, black, red, green, blue and magenta ink, with a few faint horizontal
> interference lines, like ink and gouache marks made by hand, NOT digital noise.
> Everything outside the screen stays exactly like the reference. Landscape 16:9.
> No text, no logos.

quando a primeira vier boa, pedir 2x na mesma conversa:

> now redraw the exact same image slightly differently — same TV, but the static strokes
> redrawn randomly, like the next frame of a hand-drawn animation. Same density, same
> colors.

salvar como **`tvest1.png`, `tvest2.png`, `tvest3.png`** — o código troca sozinho:
cicla as 3 a 8fps + scanlines enquanto está "sem sinal"; quando uma ref entra, volta a
TV de tela vazia com a ref por cima; nos blips entre refs, a estática pisca de volta.

## 3. as 12 referências que passam na tela — `tvref_01.png` … `tvref_12.png`

cenas COLORIDAS (nanquim + aquarela lavada do projeto), inspiradas nos programas
educativos/infantis da TV Cultura e da TV Globinho. **paisagem ~4:3, full-bleed** (a
aquarela cobre o quadro todo — vai dentro da tela da TV). passam na ordem do número do
arquivo, com um blip de estática entre uma e outra.

âncora pra colar no começo de cada prompt:

> A hand-drawn children's TV show scene in black India ink with soft muted watercolor
> washes filling the WHOLE frame edge to edge (full-bleed, no white margins, no border,
> no text). Loose sketchy tremulous linework, washed-out faded colors like a Brazilian
> educational kids' TV show from the 1990s/2000s. Landscape 4:3. Same technique as the
> attached reference drawing.

sugestão de cenas (Marcela é a curadora — trocar à vontade, só manter os nomes/ordem):

| arquivo | cena (inspiração) |
|---|---|
| `tvref_01.png` | um castelo mágico e colorido com três crianças curiosas na porta (Castelo Rá-Tim-Bum) |
| `tvref_02.png` | um robô simpático feito de sucata ensinando algo apontando uma plaquinha (X-Tudo) |
| `tvref_03.png` | peixinhos coloridos conversando num aquário azul (Glub Glub) |
| `tvref_04.png` | uma fazendinha com um galo cantando no telhado e um bezerro sorridente (Cocoricó) |
| `tvref_05.png` | um menino olhando a lua por uma luneta no quarto (Mundo da Lua) |
| `tvref_06.png` | um passarinho azul GIGANTE e gentil cercado de crianças (Vila Sésamo) |
| `tvref_07.png` | uma boneca de pano ruiva de chapéu falando com um sabugo de milho de cartola (Sítio do Picapau Amarelo) |
| `tvref_08.png` | um estúdio de TV tocado por cachorros apresentadores (TV Colosso) |
| `tvref_09.png` | letras e números coloridos flutuando e dançando num céu de aquarela |
| `tvref_10.png` | crianças construindo um foguete de papelão no quintal |
| `tvref_11.png` | uma sala de aula alegre dentro da TV, lousa verde e mãos levantadas |
| `tvref_12.png` | uma família reunida no sofá vendo TV numa sala dos anos 2000, luz da tela iluminando os rostos |

## status (2026-07-02) — ✅ TUDO CHEGOU
- ✅ `tvest1/2/3.png` no ar (TV com estática baked, boil 8fps).
- ✅ refs: lista REDUZIDA PRA 8, curada pelo casal (`TVREF_N=8`): 01 sítio, 02 caverna
  do dragão, 03 vila sésamo, 04 cocoricó, 05 pingu, 06 bob esponja, 07 zoboomafoo,
  08 shaun. várias são FRAMES REAIS dos programas (não ilustração) — decisão do casal.
  a tabela de 12 sugestões acima ficou como histórico.
- refs passam CENTRADAS na tela (não full-bleed), com degradê transparente nas bordas
  e tinta ao entrar; slideshow acelerado (1.7s + 0.25s de blip).
- próximo beat depois das refs: "da TV saem luzes, letras, números e personagens"
  voando PRA FORA da tela — a definir com o casal.
