# prompts — cena 6 (o ecossistema Globo / a caça à frase)

beat do roteiro (texto da Marcela, 2026-07-02): *"a campanha acontecendo dentro do
ecossistema Globo: @globo/GloboPop (personagens encontrando a primeira pista) → g1
(notícias e dados) → Globoplay (programa pausado, mini anúncio com a pista "com o") →
Viu (influenciadores, quadro "Fora da bolha") → Movimento LED (relatos reais, última
palavra escondida). a frase nunca aparece inteira — só se completa na cabeça de quem
junta os pedaços."*

## o plano visual (proposto 2026-07-02, sessão 3 — aguardando ok do Iagho)

**a mecânica: uma caça ao tesouro em 5 estações, deslizando pra direita.**

- depois do fecho da cena 5 (título + "Histórias começam com o saber." na página nova),
  a campanha some em fade e o palco **desliza** pra direita por 5 estações (reuso da
  linguagem do carrossel da cena 2 — "a imagem desliza", literal do texto dela).
- cada estação = **letreiro manuscrito** em cima (handWrite: "@globo", "g1",
  "globoplay", "Viu", "Movimento LED") + **moldura/tela rabiscada por código**
  (sketchRect) + **personagens em silhueta preta** (grids do GPT, boil 8fps) +
  o conteúdo específico por código.
- **os LOGOS são LETREIROS ESCRITOS À MÃO por código** (Caveat, como todo texto da
  peça) — não pedir logo pro GPT (ele erra marca registrada e quebra o traço; a peça
  inteira já é manuscrita, letreiro é a tradução natural).
- **a PISTA de cada estação é um pedacinho de papel AMARELO aquarela** (callback: o
  mesmo amarelo da lampadinha que rachou — a ideia reacendendo aos pedaços) com a
  palavra manuscrita. cada pedacinho "pinga" da estação e fica **guardado no rodapé**,
  acumulando: quem assiste vê a coleção crescer.
- distribuição das palavras: GloboPop = **"Histórias"** (a primeira pista) → g1 =
  **"começam"** → Globoplay = **"com o"** (especificado pela Marcela) → Viu = **sem
  palavra** (os influenciadores convidam a BUSCAR — a bolha estoura) → LED =
  **"saber."** (a última, escondida no relato).
- **fecho da cena**: os pedacinhos voam do rodapé pro centro e se ENCAIXAM formando
  "Histórias começam com o saber." — "ela só se completa na cabeça de quem junta os
  pedaços". emenda com a cena 7 (páginas se preenchendo).

**as 5 estações, beat a beat:**

1. **@globo / GloboPop** — moldura de celular (temos a linguagem do `celular_ref`),
   dentro dela uns traços de vídeo rolando (código); ao lado, DUPLA de silhuetas
   achando a primeira pista (grid §1). o pedacinho "Histórias" sai de dentro da tela.
2. **g1** — uma página de jornal/portal rabiscada por código (colunas de risquinhos
   ilegíveis + um título manuscrito real, ex. "a educação de milhões foi interrompida
   no meio"); silhueta lendo jornal (grid §2). pedacinho "começam" cai de entre as
   colunas.
3. **Globoplay** — TELONA pausada por código: barra de progresso, botão ⏸ gigante
   rabiscado, e o **mini anúncio** que desliza por baixo com "com o" no amarelo.
   casal de costas no sofá assistindo (grid §3).
4. **Viu** — 2–3 molduras verticais (shorts) com a silhueta do influenciador falando
   (grid §4); uma BOLHA rabiscada por código envolve a moldura e **ESTOURA** (quadro
   "Fora da bolha" — o estouro é a punchline visual). sem pedacinho: sai um bilhetinho
   manuscrito "procura a frase" (ou só a bolha estourando, a decidir no ar).
5. **Movimento LED** — uma carta/relato: bloco de linhas manuscritas ilegíveis
   (código) e UMA palavra que se acende em amarelo no meio do texto: "saber." —
   quem lê de verdade encontra. silhueta sentada lendo (grid §5).

**o que é código (zero asset):** letreiros, molduras/telas, jornal, player pausado,
mini anúncio, bolha + estouro, bloco de texto do LED, pedacinhos amarelos, o slide,
a montagem final da frase. **o que é GPT:** só os personagens (5 grids abaixo).

## regras de ouro (mesmas dos futuros)

- **anexar `ultimo_frame.png`** (a menina + o traço do projeto) em TODO prompt; se o
  traço desandar, "same technique as the attached reference".
- gerar os 5 grids **na mesma conversa** (a primeira boa vira âncora).
- **fundo branco PURO**, sem cor nenhuma (silhuetas p&b — o amarelo das pistas é do
  código), sem texto, sem moldura, sem chão até a borda.
- cada grid = **3 painéis (3 colunas × 1 linha) da MESMA pose redesenhada** = frames
  de boil (padrão tv1/2/3). fatiar:
  `python slice_grid.py <grid>.png <saida>.png 3 1 3 none 252`
- se a figura "escorregar" entre painéis, me chamar — re-registro por bbox (padrão).

## âncora de estilo (cola no começo de TODO prompt)

> Attached is a hand-drawn scribbled ink drawing from my animation (style reference).
> Create ONE image: a grid of 3 equal panels (3 columns × 1 row), pure white
> background, no gaps, no borders, no numbers, no text. EVERY panel shows THE SAME
> figure, centered, same size and position in every panel, drawn as a solid black
> scribbled India ink silhouette in the same loose tremulous technique as the
> reference. The 3 panels are animation boil frames: the entire linework is redrawn
> slightly differently in each panel (sketchy hand-drawn lines, the edges must
> wobble). NO color, NO text, NO frame, NO background scenery.

## os 5 prompts (âncora + isto)

### 1. `ecopistagrid.png` → `eco_pista.png` (GloboPop — a dupla ACHA a pista no chão)

⚠️ **v2 (pedido do Iagho 2026-07-02, sessão 3): virou SEQUÊNCIA de 16 quadros (4×4)**
— a dupla vê o papelzinho amarelado no chão, se abaixa, pega e comemora. o papelzinho
é **amarelo aquarela = a ÚNICA cor** (callback da lâmpada; sobrevive ao keying).
NÃO usa a âncora de 3 painéis — o prompt abaixo é completo e independente:

> Attached is a hand-drawn scribbled ink drawing from my animation (style reference).
> Create ONE image: a grid of 16 equal panels (4 columns × 4 rows), pure white
> background, no gaps, no borders, no numbers, no text. Every panel shows THE SAME
> TWO characters — a pair of young people drawn as solid black scribbled India ink
> silhouettes, in the same loose tremulous hand-drawn technique as the reference —
> at the same scale and position in every panel. The 16 panels are consecutive
> frames of ONE animation of them finding a small piece of paper on the ground:
> panel 1: the two stand side by side, one looking at a smartphone (small white
> outlined rectangle in their hand), the other looking around, bored;
> panel 2: a SMALL SCRAP OF PAPER appears lying on the ground near their feet,
> washed in WARM YELLOW watercolor — the second character notices it, head tilted
> down;
> panel 3: the second character POINTS down at the yellow scrap, the first one
> lowers the phone and looks down too;
> panel 4: both lean forward staring at the scrap on the ground, curious;
> panels 5–6: the second character crouches down toward the scrap (panel 5 half-way
> bending knees, panel 6 fully crouched close to the ground), the first one leans
> over their shoulder;
> panel 7: the crouched one reaches out and touches the yellow scrap;
> panel 8: the crouched one holds the scrap in their hand, still crouched, looking
> at it;
> panel 9: they rise back up, halfway standing, holding the scrap;
> panel 10: both standing again, heads close together, looking at the little yellow
> paper held between them;
> panel 11: one lifts the scrap UP high like a trophy, the other throws both arms up,
> excited — they FOUND the first clue;
> panel 12: same celebration pose, tiny variation, even more joyful;
> panels 13–16: the SAME final pose (one holding the scrap up, the other with arms
> raised) redrawn four times almost identically — animation boil frames, only the
> sketchy line wobble changes.
> The small paper scrap with its warm yellow watercolor wash is THE ONLY color in
> the whole image, in every panel where it appears; everything else is black India
> ink on pure white. The scrap is blank (no writing on it). In every panel the
> entire linework is redrawn slightly differently (tremulous sketchy lines, edges
> must wobble). Same ink technique as the attached reference drawing.

quando chegar, fatiar: `python slice_grid.py ecopistagrid.png eco_pista.png 4 4 16 none 252`
(se as figuras escorregarem entre células ou os pés vazarem, me chamar — re-registro
por componente conexo, padrão `slice_pega.py`). o código vai tocar p1–12 a ~6fps e
segurar o boil p13–16 no fim; conferir se o amarelo sobreviveu ao keying.

### 2. `ecojornalgrid.png` → `eco_jornal.png` (g1 — a pista cai de dentro do jornal)

**v2 (sequência, padrão do §1): 12 quadros (4×3)** — ele lê o jornal, o papelzinho
amarelo escorrega de dentro e cai, ele pega no ar. prompt completo e independente:

> Attached is a hand-drawn scribbled ink drawing from my animation (style reference).
> Create ONE image: a grid of 12 equal panels (4 columns × 3 rows), pure white
> background, no gaps, no borders, no numbers, no text. Every panel shows THE SAME
> character — a person drawn as a solid black scribbled India ink silhouette, in the
> same loose tremulous hand-drawn technique as the reference — at the same scale and
> position in every panel, standing and holding a LARGE open newspaper with both
> hands. The newspaper is white with only a few faint loose scribbled lines
> suggesting columns of text (absolutely nothing legible). The 12 panels are
> consecutive frames of ONE animation:
> panels 1–2: the person reads the open newspaper, head slightly bent, absorbed
> (panel 2 is the same pose redrawn, tiny variation);
> panel 3: they turn a page of the newspaper;
> panel 4: as the page turns, a SMALL SCRAP OF PAPER washed in WARM YELLOW
> watercolor slips out from between the newspaper pages, visible mid-air beside the
> newspaper;
> panel 5: the yellow scrap falls further down, the person's head starts turning
> toward it;
> panel 6: the scrap is near the ground, the person lowers the newspaper with one
> hand and reaches for the scrap with the other;
> panel 7: they CATCH the scrap mid-air, newspaper now folded under one arm;
> panel 8: they hold the yellow scrap up close to their face, examining it,
> newspaper under the arm;
> panel 9: they hold the scrap a bit higher, head tilted, intrigued and delighted;
> panels 10–12: the SAME final pose (scrap held up in one hand, newspaper folded
> under the other arm) redrawn three times almost identically — animation boil
> frames, only the sketchy line wobble changes.
> The small paper scrap with its warm yellow watercolor wash is THE ONLY color in
> the whole image; everything else is black India ink on pure white. The scrap is
> blank (no writing on it). In every panel the entire linework is redrawn slightly
> differently (tremulous sketchy lines, edges must wobble). Same ink technique as
> the attached reference drawing.

fatiar: `python slice_grid.py ecojornalgrid.png eco_jornal.png 4 3 0 none 252`
(⚠️ inset 0 — o 5º argumento é INSET, não contagem de frames; com 16 no §1 decepava
o papelzinho erguido).

### 3. `ecosofagrid.png` → `eco_sofa.png` (Globoplay — o casal no sofá, DE COSTAS)
> The figure is a simple couch seen FROM BEHIND, drawn in loose black ink outline,
> with two people sitting side by side on it, visible only as solid black scribbled
> silhouettes of their backs, heads and shoulders above the backrest — one head
> gently leaning on the other's shoulder. They are watching something in front of
> them (the space in front of the couch is EMPTY white — my code will draw the screen
> there). Cozy, quiet pose.

### 4. `ecoinfluencergrid.png` → `eco_influencer.png` (Viu — o influenciador)

**v2 (sequência 12 quadros, 4×3):** ele vloga → aponta pro espectador → ABRE os
braços (sincroniza com a BOLHA do código estourando — "Fora da bolha") → boil:

> Attached is a hand-drawn scribbled ink drawing from my animation (style reference).
> Create ONE image: a grid of 12 equal panels (4 columns × 3 rows), pure white
> background, no gaps, no borders, no numbers, no text. Every panel shows THE SAME
> character — a young influencer drawn as a solid black scribbled India ink
> silhouette, in the same loose tremulous hand-drawn technique as the reference —
> at the same scale and position in every panel, standing, holding a smartphone UP
> at arm's length in one hand as if filming themselves (vlog selfie pose). The
> phone is a small white outlined rectangle. The 12 panels are consecutive frames
> of ONE animation:
> panels 1–3: they talk to the phone with energy, free hand gesturing mid-speech —
> the same pose redrawn three times almost identically (animation boil frames);
> panel 4: they lean slightly closer to the phone, free hand rising;
> panel 5: they POINT straight out at the viewer with the free hand, confident;
> panel 6: the pointing arm sweeps outward, chest opening up;
> panels 7–8: they throw the free arm WIDE OPEN and tilt the phone arm outward too,
> chest proud, head high — a big open "break free" pose (panel 8 same pose, tiny
> variation);
> panels 9–12: the SAME final wide-open pose redrawn four times almost identically
> — animation boil frames, only the sketchy line wobble changes.
> Everything is black India ink on pure white — NO color anywhere in this image. In
> every panel the entire linework is redrawn slightly differently (tremulous
> sketchy lines, edges must wobble). Same ink technique as the attached reference
> drawing.

fatiar: `python slice_grid.py ecoinfluencergrid.png eco_influencer.png 4 3 0 none 252`
(+ re-registro pelos pés se escorregar, padrão §2).

### 5. `ecoleituragrid.png` → `eco_leitura.png` (Movimento LED — quem lê de verdade)

**v2 (sequência 12 quadros, 4×3):** ele lê o relato → se aproxima → a palavra
escondida SE ACENDE em amarelo na página → ele toca nela → levanta a cabeça (achou):

> Attached is a hand-drawn scribbled ink drawing from my animation (style reference).
> Create ONE image: a grid of 12 equal panels (4 columns × 3 rows), pure white
> background, no gaps, no borders, no numbers, no text. Every panel shows THE SAME
> character — a person drawn as a solid black scribbled India ink silhouette, in
> the same loose tremulous hand-drawn technique as the reference — at the same
> scale and position in every panel, sitting cross-legged on the floor, holding a
> single large sheet of paper with both hands. The sheet is white with only faint
> loose scribbled lines suggesting a handwritten letter (absolutely nothing
> legible). The 12 panels are consecutive frames of ONE animation:
> panels 1–3: they read the sheet quietly, head bent down over it, absorbed — the
> same pose redrawn three times almost identically (animation boil frames);
> panel 4: their head tilts, leaning a little closer to the sheet — something
> caught their eye;
> panel 5: they bring the sheet closer to their face, shoulders curling in;
> panel 6: on the sheet, ONE small word-sized smudge of WARM YELLOW watercolor
> appears among the faint scribbled lines — the hidden word revealing itself;
> panel 7: they touch the yellow smudge on the sheet with one finger, head still
> close;
> panel 8: they LIFT their head up from the sheet, back straightening, one finger
> still on the yellow smudge — they FOUND it;
> panels 9–12: the SAME final pose (sitting, sheet in the lap, head up, finger on
> the yellow smudge) redrawn four times almost identically — animation boil
> frames, only the sketchy line wobble changes.
> The small warm yellow watercolor smudge on the sheet (panels 6–12) is THE ONLY
> color in the whole image; everything else is black India ink on pure white. In
> every panel the entire linework is redrawn slightly differently (tremulous
> sketchy lines, edges must wobble). Same ink technique as the attached reference
> drawing.

fatiar: `python slice_grid.py ecoleituragrid.png eco_leitura.png 4 3 0 none 252`
(+ re-registro se escorregar; figura sentada — registrar por bbox base+centro).

## status (2026-07-02, sessão 3)

- ✅ **`ecopistagrid.png` CHEGOU e foi fatiado** → `eco_pista.png` (16 frames
  313×313, inset 0, thresh 252; amarelo sobreviveu: 5.151 px). Sequência veio EXATA
  (entediados → papelzinho no chão → aponta → agacha → pega → examinam → comemoram;
  f12–15 = boil da pose final). ⚠️ **frames 10–15 foram ESPELHADOS no strip** (no
  grid original a dupla trocava de lado na comemoração — menina do cabelo comprido
  agora fica na DIREITA o tempo todo). Mapeamento pro código: p0–9 a ~6fps, p10–11
  chegada da comemoração, loop de boil p12–15.
- ✅ **`ecojornalgrid.png` CHEGOU e foi fatiado** → `eco_jornal.png` (12 frames
  362×362, inset 0, thresh 252; fundo veio 253–255, ok; amarelo: 4.453 px).
  Sequência: lê (f0–1) → vira página (f2) → pista escorrega (f3) → cai (f4) →
  abaixa pra pegar (f5) → segura/examina (f6–7) → boil da pose final (f8–11).
  ⚠️ **RE-REGISTRADO PELOS PÉS** (centroide x da faixa de 30px do fundo do corpo,
  base em fh-8): o GPT deixou ele escorregar ~55px entre células — boil f8–11
  agora trava (bbox 61–63/92–95). O miolo branco do jornal É KEYADO de propósito
  (fica só o traço sobre o papel creme, linguagem das folhas).
- ✅ **`ecosofagrid.png` CHEGOU e foi fatiado** → `eco_sofa.png` (12 frames 362×362,
  inset 0, thresh 252, 100% p&b como pedido). Sequência: aconchegados (f0–2, boil) →
  cabeça levanta (f3) → braço sobe (f4) → APONTA (f5–6) → os dois atentos (f7) →
  pose final inclinados (f8) → boil (f9–11). ⚠️ **RE-REGISTRADO por bbox** (base +
  centro x): o sofá "subia" ~110px entre as fileiras do grid. Sofá agora cravado
  (base 353±1). O espaço na frente do sofá veio VAZIO — a telona do Globoplay é do
  código, casar quando montar a estação.
- ✅ **DOIS grids de influenciador CHEGARAM** (Iagho: "dá pra usar os dois" — e a
  Marcela escreveu "influenciadorES": um por moldura de vídeo curto no Viu).
  `ecoinfluencergrid.png` → `eco_influencer.png` (12f 362×362, FRONTAL, todos
  limpos) e `ecoinfluencergrid2.png` → `eco_influencer2.png` (12f, perfil→frontal,
  MELHOR narrativa: fala f0–3 → APONTA pro espectador com mãozinha branca f4 →
  varre f5 → braços abertos f8–9). Ambos re-registrados pelos pés. ⚠️ No grid 2 os
  braços abertos VAZARAM das células: intrusos desconectados removidos por
  componente (f6: 179px, f10: 8px), mas f6/f7/f10/f11 têm o celular DECEPADO na
  borda — **usar só f0–5 + f8–9** (boil final = f8↔f9). Grid 1 usa os 12.
- ✅ **`ecoleituragrid.png` CHEGOU e foi fatiado** → `eco_leitura.png` (12 frames
  362×362, re-registrado pela base sentada, amarelo: 1.182 px). Sequência: lê
  (f0–2, boil) → inclina (f3) → aproxima a folha (f4) → a palavra SE ACENDE em
  amarelo (f5) → toca com o dedo (f6) → levanta a cabeça (f7) → boil da pose
  final (f8–11).
- 🏁 **TODOS OS 5 GRIDS PRONTOS E FATIADOS (2026-07-02, sessão 3)**: `eco_pista`
  (16f), `eco_jornal` (12f), `eco_sofa` (12f), `eco_influencer` + `eco_influencer2`
  (12f cada — 2 molduras no Viu), `eco_leitura` (12f). Todos 362×362 exceto pista
  (313×313), todos re-registrados. **PRÓXIMO: o código das 5 estações** (plano no
  topo deste arquivo; fazer estação por estação com screenshots).

## depois de gerar

1. conferir: fundo branco puro? 3 painéis? traço parecido com a menina? silhueta
   sólida (não contorno)?
2. salvar os grids na pasta `video-animado/` com os nomes EXATOS acima e me chamar —
   eu fatio, registro e calibro posição/escala nas estações.
3. o código da cena 6 entra depois do plano aprovado (carregamento especulativo,
   padrão do projeto: os grids entram sozinhos quando existirem).
