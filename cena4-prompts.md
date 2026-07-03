# prompts — cena 4 (o livro vira celular / o problema de hoje)

beat do roteiro: *"o livro vira uma tela de celular. o ritmo acelera. notificações, vídeos
curtos, cortes rápidos, dedos rolando a tela. as cores ficam mais frias e confusas. a
criança, antes desenhada com brilho nos olhos, começa a ficar parada diante da tela."*

plano combinado com o Iagho (2026-07-02, "vamos por partes"):
1. ✅ o livro reaparece NA TELA DA TV (fade in) e toca a animação inteira do grid
   (papel → vira livro → folheia) — JÁ NO AR no index.html.
2. ⏳ o livro **se transforma num smartphone** (grid abaixo — o código já espera
   `livro_vira_celular.png`, entra sozinho).
3. ⏳ transição: a moldura da TV some com um zoom no celular → o celular vira a tela
   principal.
4. ✅ conteúdo do celular NO AR: reels (like vermelho/share verde) + spam de mensagens
   com vibração por código (ver status abaixo).
5. 🔶 (decisão nova, substitui o "roda de lado") a MENINA entra ANDANDO dir→esq, o
   celular ENCOLHE suave até ficar bem menor que ela, ela PEGA e vira pra si —
   caminhada+encolhimento JÁ NO AR; falta o grid da pegada (prompt pronto na §3).
   narração da cena 4 (Marcela) + TÍTULO em destaque no fim: JÁ NO AR (QUOTES4/Q4SEQ
   no index.html; título com letras fervendo a 8fps — handWrite perLetter).
6. ⏳ a lampadazinha de ideia na cabeça dela **se racha** (§4).

## 1. o livro virando smartphone — grid 4×3 → `livro_vira_celular.png`

**anexar `livro_ref.png`** (o livro aberto do projeto). mesma receita do
`folhalivrogrid.png` que deu certo: 12 células, objeto centralizado, últimos 3 quadros
quase idênticos (= boil do celular parado).

> Attached is a hand-drawn open book from my ink animation. Create ONE image: a grid of
> 12 equal panels (4 columns × 3 rows), pure white background, no gaps, no borders, no
> numbers, no text. Each panel shows the same object centered, at the same scale, drawn
> in the same loose scribbled black India ink technique as the reference. The 12 panels
> are consecutive frames of an animation where the open book SLOWLY TRANSFORMS into a
> modern smartphone standing upright — and its color DRAINS AWAY during the
> transformation: panels 1–2, the open book from the reference starts to close, still
> with its aged-paper yellow watercolor wash; panels 3–4, it closes and tilts up into a
> vertical block, the yellow wash visibly fading, ink lines getting more scribbly;
> panels 5–6, the block slims down and stretches taller, its corners rounding, now
> almost completely BLACK AND WHITE, only a faint ghost of the paper color left;
> panels 7–9, all color is gone — a thin flat vertical rectangle drawn ONLY in black
> India ink on white: scribbled sketchy outline drawn with 2–3 overlapping tremulous
> strokes, a dark bezel filled with loose cross-hatching, the empty screen indicated
> only by light diagonal hatching marks, one small hand-drawn button dot at the bottom —
> a smartphone that looks doodled in pen, same scribbly cartoon language as the rest of
> my animation; panels 10–12, the SAME finished black-and-white smartphone redrawn three
> times almost identically (same pose, same size, only the sketchy line wobble changes —
> animation boil frames). The screen stays EMPTY. NO color anywhere in the final frames.
> Same ink technique as the attached reference drawing.

quando chegar (salvar como `livrocelgrid.png`), fatiar SEM alinhamento:

```
python slice_grid.py livrocelgrid.png livro_vira_celular.png 4 3 12 none
```

⚠️ conferir se o limiar não furou o celular (mesmo problema do folhalivrogrid — se furar,
me chamar que eu faço um fatiador com keying próprio). o código toca a 5fps
(`CEL_FPS`) a partir de `T3.celAt` e segura o boil dos frames 10–12 no fim.

## 2. o celular animado — DECISÃO NOVA (2026-07-02): CELULAR JÁ NA ARTE, minimalista p&b

❌ a 1ª tentativa (telas cheias de aquarela fria) foi REPROVADA pelo Iagho — carregada
demais. o que ele quer: **arte SIMPLES, preto e branco do projeto**, o celular incluso
na imagem (grids com MUITOS frames = o boil/arestas fervendo vem de graça), e só DOIS
acentos de cor: **coração VERMELHO** ao curtir (pop) e **compartilhar VERDE** ao apertar.
referência do nosso celular: **`celular_ref.png`** (gerado do strip; ANEXAR nos prompts).

### 2a. reels + curtir/compartilhar — grid 4×3 → `celreelsgrid.png`

> Attached is my hand-drawn ink smartphone (reference). Create ONE image: a grid of 12
> equal panels (4 columns × 3 rows), pure white background, no gaps, no borders, no
> numbers, no text. EVERY panel shows THE EXACT SAME smartphone as the reference — same
> design, same size, same centered position — with a very MINIMAL short-video app
> interface hand-drawn INSIDE its screen, all in simple scribbled black ink lines only:
> a thin vertical column of three small icons on the right side of the screen (a heart,
> a speech bubble, a share arrow), a thin scribbled progress line at the bottom, and a
> few loose sketchy strokes suggesting an abstract video in the middle (nothing
> detailed). Everything is black ink outline on white — EXCEPT the heart and the share
> arrow, which change state across the panels: panel 1: everything idle, heart and share
> arrow just white outlines; panel 2: the heart POPS — filled solid RED, drawn slightly
> bigger, with tiny burst dashes around it; panel 3: the heart stays solid red, normal
> size; panel 4: the heart is back to white outline (unliked); panel 5: the heart POPS
> red again (bigger + burst dashes); panel 6: heart solid red, normal size; panel 7:
> heart white outline again; panel 8: the SHARE ARROW pops — filled solid GREEN, slightly
> bigger, tiny burst dashes; panel 9: share arrow back to white outline; panel 10: heart
> POPS red (bigger + burst); panel 11: heart solid red; panel 12: share arrow POPS green.
> The red heart and the green share arrow are THE ONLY colored things in the whole image.
> In every panel the entire linework is redrawn slightly differently (tremulous sketchy
> lines, like hand-drawn animation frames — the edges must wobble). Same ink technique
> as the attached reference smartphone.

### 2b. spam de mensagens — grid 4×3 → `celspamgrid.png`

> Attached is my hand-drawn ink smartphone (reference). Create ONE image: a grid of 12
> equal panels (4 columns × 3 rows), pure white background, no gaps, no borders, no
> numbers. EVERY panel shows THE EXACT SAME smartphone as the reference — same design,
> same size, same centered position. Across the 12 panels, message notifications PILE UP
> progressively inside the screen, like spam arriving: panel 1: screen empty except one
> small rectangular message bubble sliding in at the top (rounded corners, two short
> scribbled lines of unreadable text and a tiny circle avatar); panel 2: two bubbles;
> panel 3: three bubbles; and so on, each panel adding one or two more message bubbles,
> stacking down and starting to overlap slightly crooked, until panel 12 where the
> screen is completely FLOODED with overlapping crooked message bubbles. Everything in
> simple scribbled black ink outlines on white — NO color at all in this grid, no
> legible text (only scribbled marks as text). In every panel the entire linework is
> redrawn slightly differently (tremulous sketchy lines, like hand-drawn animation
> frames — the edges must wobble). Same ink technique as the attached reference
> smartphone.

✅ **NO AR (2026-07-02, sessão 2)**: os dois grids fatiados (limiar 252 → `cel_reels.png`
338×338 e `cel_spam.png` 326×350, 12f cada), re-registrados pelo bbox do maior
componente conexo e ligados no `drawBook3`: reels em loop a 6fps a partir de
`T3.reelsAt` (e≈98) → spam empilhando a 6fps em `T3.spamAt` (e≈102) com o celular
vibrando por código e segurando o flood no fim. Escala = média geométrica dos bboxes
(`REELS_S:0.777`/`SPAM_S:0.842`). Verificado com screenshots (coração vermelho pop,
share verde com burst, emendas sem salto). Detalhes no bullet "✅ REELS + SPAM NO AR"
do `PROJETO.md`.

## 3. a menina PEGA o celular e vira pra ela — grid 4×3 → `menina_pega.png`

**decisão nova do Iagho (2026-07-02, sessão 2 — substitui o "celular roda de lado"):**
a menina do início entra andando da DIREITA pra ESQUERDA, o celular dá um zoom-out suave
(fica bem menor que ela) e ela PEGA o celular e VIRA ele pra si, ficando olhando.

**o que JÁ ESTÁ NO AR no index.html:** a caminhada dir→esq (`menina_anda` espelhado por
código, para diante do celular em `T3g.arrive`), o encolhimento do celular (~1/4 dela,
desce pra altura da mão, vibra cada vez menos — `CEL4_F/X/Y` + `T3.shrinkAt`) e a pose
parada (pose 11 do levanta + boil). o código já espera **`menina_pega.png`**
(carregamento especulativo): quando o strip existir, em `T3g.grabAt` (~0.8s depois de
ela parar) ela pega o celular e vira pra si (12f a `GRAB_FPS:5`, fim = boil f10–12).

⚠️ **gerar a menina DE PERFIL PRA DIREITA** (igual às refs) — o código ESPELHA o strip
(`scale(-1,1)`), como já faz com a caminhada. **anexar `menina_pe.png`** (a menina de
pé, perfil) **e `celular_ref.png`** (o nosso celular).

> Attached are two hand-drawn references from my ink animation: (1) a little girl
> standing in profile facing right — a solid black India ink silhouette with wild
> scribbly hair; (2) a hand-drawn scribbled smartphone. Create ONE image: a grid of 12
> equal panels (4 columns × 3 rows), pure white background, no gaps, no borders, no
> numbers, no text. EVERY panel shows THE SAME girl from reference 1 — same size, same
> position, standing in profile FACING RIGHT, her feet on the SAME ground line in every
> panel. Floating upright in the air in front of her chest is the smartphone from
> reference 2, drawn SMALL — about the size of her head — with its screen toward the
> viewer, completely FLOODED with tiny overlapping crooked message bubbles (scribbled
> marks only, no legible text). The 12 panels are consecutive frames of ONE animation
> of her picking up the phone and turning it toward herself:
> panel 1: she stands still, arms relaxed at her sides, looking at the floating phone;
> tiny vibration dashes around the phone;
> panel 2: she begins raising her near arm toward the phone (phone unchanged, still
> with vibration dashes);
> panel 3: her arm is extended, open hand almost touching the phone;
> panel 4: her hand GRASPS the phone by its edge — the vibration dashes disappear;
> panel 5: her elbow bends and she pulls the phone a little toward her chest; the
> phone starts to tilt in her hand;
> panel 6: the phone is HALF-TURNED — seen edge-on as a thin vertical sliver between
> her fingers;
> panel 7: the turn completes — now we see the BACK of the phone (a plain scribbled
> rounded rectangle, no screen visible), and her head starts to tilt down toward it;
> panel 8: final pose — she holds the phone up in front of her face at chest height,
> screen facing HER, head bowed, absorbed by the screen;
> panel 9: exactly the same final pose, with a tiny settling of her weight;
> panels 10–12: the SAME final pose redrawn three times almost identically (same
> silhouette, same phone position, only the sketchy line wobble changes — animation
> boil frames).
> The girl is always a solid black ink silhouette exactly like reference 1; the phone
> always in loose scribbled black outline exactly like reference 2. NO color anywhere.
> In every panel the entire linework is redrawn slightly differently (tremulous sketchy
> lines, like hand-drawn animation frames — the edges must wobble).

✅ **CHEGOU E ESTÁ NO AR (2026-07-02, sessão 2)** — grid ótimo (pegada em 4 frames,
vira em 3, absorvida nos últimos 5). ⚠️ neste grid os PÉS VAZAM das células (fatiar
por grade fixa decepava o pé — o Iagho pegou no ar): fatiado com o **`slice_pega.py`**
(recorte por componente conexo, igual ao slice_levanta; re-registro pelo corpo já
embutido). calibrado: `GRAB_GF:0.80, GRAB_X:0.635`; emenda do celular casada:
`CEL4_F:0.328, CEL4_X:0.542, CEL4_Y:0.464` — ele flutua na frente do ROSTO dela
(medido do f0). refatiar = só rodar `python slice_pega.py`. instruções originais
abaixo (referência):

```
python slice_grid.py meninapegagrid.png menina_pega.png 4 3 12 none 252
```

- **re-registro**: NÃO recentrar pelo bbox de tudo (braço/celular deslocam o centro) —
  centralizar x pelo **CENTROIDE do MAIOR componente conexo** (o corpo) e ancorar y
  pelo **fundo do bbox** (pés), + limpeza de vazamento de borda (padrão da sessão).
- **calibrar knobs** no index.html: `GRAB_GF` (fração da altura da célula que a menina
  ocupa — medir bbox), `GRAB_X` (x do centro da célula no palco), `GRAB_PAD` (pé).
- **emenda**: o celular do código (`CEL4_X/Y/F`) deve casar com o celular do frame 1
  do grid — medir bbox e ajustar, como foi feito no livro→celular.

## 4. lâmpada rachando — grid 4×3 → `lampada.png`

**a ponte cena 4→5 (decisão 2026-07-02, sessão 2):** ela absorvida no celular → a
lampadinha de ideia ACENDE sobre a cabeça (amarelo aquarela, único acento de cor) →
TREME → RACHA → apaga. quando ela racha, **o PAPEL da cena racha junto** (rachaduras
abrutas por código irradiando da lâmpada + escurecimento) e **a tela CONGELA** (o boil
de TUDO para — só o título continua fervendo). ✅ código JÁ NO AR (`T5` no index.html,
sincronizado com a narração: acende no "de criar…", treme no "e quando esquecemos…",
racha quando "…interrompida." termina). ✅ **GRID CHEGOU E ESTÁ NO AR** (2026-07-02,
sessão 2): mapeamento exato, fatiado com inset 12 (o grid veio com LINHAS DE GRADE —
o inset corta), re-registrado pelo bulbo, amarelo ok. Verificado com screenshots.

**anexar `celular_ref.png`** (âncora do traço). o amarelo sobrevive ao keying
(luminância ~226 < 252) — pedir amarelo RICO, não pálido.

> Attached is a hand-drawn scribbled smartphone from my ink animation (style
> reference). Create ONE image: a grid of 12 equal panels (4 columns × 3 rows), pure
> white background, no gaps, no borders, no numbers, no text. EVERY panel shows THE
> SAME small classic cartoon "idea" light bulb — round glass, a few scribbled filament
> lines inside, small screw base at the bottom — centered, same size and position in
> every panel, drawn in the same loose scribbled black India ink outline as the
> reference. The 12 panels are consecutive frames of ONE animation of the idea dying:
> panel 1: the bulb is only half-sketched, faint thin lines, not lit — it is just
> appearing;
> panel 2: the bulb complete and LIT: the glass filled with a RICH WARM YELLOW
> watercolor wash and short ink ray dashes radiating around it;
> panels 3–5: the SAME lit bulb redrawn three times almost identically (same pose,
> same rays, only the sketchy line wobble changes — animation boil frames);
> panel 6: the lit bulb TREMBLES — tilted slightly to the left, rays shaky and uneven;
> panel 7: trembling to the other side — tilted slightly right, rays more uneven;
> panel 8: still lit but weaker (only 2–3 short rays left) and ONE thin jagged CRACK
> LINE appears across the glass;
> panel 9: the cracks SPREAD — two or three jagged crack lines across the glass, the
> yellow wash visibly fading, almost no rays;
> panel 10: a big crack SPLITS the glass, the light goes OUT — no rays, no yellow at
> all, just the dark cracked bulb in black ink;
> panels 11–12: the SAME dead dark cracked bulb redrawn twice (boil frames), with a
> single tiny wisp of smoke curling up from it.
> The rich warm yellow inside the glass in panels 2–9 is THE ONLY color in the whole
> image. In every panel the entire linework is redrawn slightly differently (tremulous
> sketchy lines, like hand-drawn animation frames — the edges must wobble). Same ink
> technique as the attached reference.

quando chegar (salvar como **`lampadagrid.png`**):

```
python slice_grid.py lampadagrid.png lampada.png 4 3 12 none 252
```

- **re-registro** pelo bbox do MAIOR componente conexo (o bulbo — os raios são
  tracinhos soltos, não puxam o centro; padrão do reg_cel.py da sessão).
- conferir se o amarelo sobreviveu ao keying (se vier pálido demais ele some — o miolo
  fica transparente sobre o papel creme; aceitável, mas melhor regenerar mais rico).
- **calibrar** `LAMP_X/LAMP_Y/LAMP_H` no index.html (posição sobre a cabeça dela /
  altura) com screenshots. o mapeamento de frames já está no código:
  f0–f1 acende (0.2s cada) → loop f2–4 (acesa, boil 8fps) → f5/6 alternando (TREME,
  com jitter por código) → f7/f8/f9 (trinca → espalha → apaga, 0.35s cada, em
  `T5.crackAt`) → loop f10/11 (morta, boil).

## status (2026-07-02)
- ✅ parte 1 no ar (livro na tela da TV, fade in + transformação + folheia).
- ✅ `livrocelgrid.png` CHEGOU e está NO AR: fatiado com
  `python slice_grid.py livrocelgrid.png livro_vira_celular.png 4 3 12 none 252`
  (limiar 252 — o default 238 furava o miolo das páginas) + **limpeza de vazamento**
  por componente conexo (as células do grid quase se encostam; pedaços do livro vizinho
  grudados na borda lateral foram removidos por script — se refatiar, repetir a limpeza).
  **Emenda sem salto**: o frame 0 do strip nasce com a MESMA largura/posição do livro
  folheante (knobs `CEL_K/CEL_AX/CEL_AY/CEL_X/CEL_Y` no index.html, medidos do bbox).
  Transformação em `T3.celAt` (~e94 da cena 3), fim segura o boil dos frames 10–12.
- as falas da cena 3 (Marcela) já são escritas NA TELA da TV antes disso (QUOTES3 no
  index.html, knobs `Q3_PX`, agenda `Q3SEQ` auto-derivada ~0.05s/letra).
