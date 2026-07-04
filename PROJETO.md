# O capítulo que falta — projeto de animação

> **Registro-mestre do projeto.** Qualquer sessão/assistente que abrir esta pasta deve ler
> este arquivo primeiro. É a fonte de verdade: conceito, arquitetura, assets, o que já está
> feito, as decisões tomadas e o que falta. Última atualização: 2026-07-03 (madrugada,
> sessão 3).
>
> ## ⭐ PRÓXIMA SESSÃO: COMECE EXATAMENTE AQUI
>
> **ONDE ESTAMOS (2026-07-03): CENAS 1–6 COMPLETAS.** A cena 6 (caça à frase no
> ecossistema Globo, 5 estações deslizando + fecho com a frase montada de
> pedacinhos) foi TODA construída na sessão 3 — detalhes nos bullets ✅ abaixo e
> no `cena6-prompts.md` (status frame a frame dos 6 sprites eco_*). A peça vai
> até ~5:14. **O PRÓXIMO TRABALHO, EM ORDEM:**
> 1. **narração da cena 6** (texto integral da Marcela no `roteiro.md` cena 6):
>    escrita à mão, agenda tipo CSEQ; DECIDIR COM O IAGHO onde vive (faixa fixa
>    no topo vs bloco por estação).
> 2. **polimento da cena 6** depois que o Iagho assistir inteiro (ele ainda NÃO
>    viu: pedir pra abrir com `?v=101` do ~4:23 em diante). Radar meu: moldura do
>    celular da estação 1 "limpa" demais, barras do ⏸ muito retas, dwell 7.5s.
> 3. **cenas 7–8**: páginas se preenchendo (REUSO dos `futuro_*.png` — nada de
>    asset novo a princípio) e a volta ao "Era uma vez…" (menina da cena 1
>    continua escrevendo; a frase vira várias histórias). Fecho do filme já
>    existe como beat na cena 5 — decidir se repete ou emenda.
> 4. **PACING: 5:14 → ~3:54 UNIFORME** (2026-07-03, sessão 4): ⚠️ a 1ª tentativa foi um
>    TIME-WARP por trechos (velocidade variável) — o Iagho REPROVOU ("uma hora rapidão,
>    outra normal, estranho") e foi TOTALMENTE REVERTIDO. NÃO reintroduzir velocidade
>    variável. O que ficou: **timeline apertada nos knobs, tudo a 1x** — agendas de texto
>    (QSEQ 0.055s/letra hold 1.4; Q3/Q4 0.04 hold 1.1; CSEQ 0.04 hold 1.4; leads 0.45–0.5,
>    fades 0.65–0.9, gaps 0.2), abertura/cena2 encurtadas (sceneAt 5.9, pushAt 12.6,
>    qHand 24.1 — offsets internos preservados), refs 1.15+0.15, T3 (livro refolheia em
>    3.3s — pedido; reels Q3_END+7.4), título/tear/tag levemente, respiro T6 1.8,
>    cena 6 dwell 5.4/slide 1.0 (STs internos re-sincronizados: scrapAts 3.6–4.2,
>    pauseAt 1.8, popAt 2.7, glowAt 2.6), DUR fecho +7. `window.__dur` exposto.
>    **TEXTO ENXUGADO (2026-07-03, na sequência): peça em ~3:22.** As 21 frases viram
>    18 (~880 letras): QUOTES 5→4 (frases 3+4 fundidas), QUOTES3 9→7, QUOTES4
>    encurtadas (frases 4 e 5 INTACTAS — sincronizam lâmpada/racha via Q4SEQ[3]/[4]),
>    CAMP compactada. Ideias todas preservadas; **texto integral da Marcela segue no
>    `roteiro.md`** (não mexer lá). ⚠️ A MARCELA precisa REVISAR a redação enxuta
>    (é trabalho dela). Pra chegar a 3:00 em ponto: ela enxugar mais um pouco, ou
>    aceitar 3:22, ou apertar escrita no limite (~3:12). Re-tunar quando 7–8 entrarem.
> **Jeito de trabalhar**: "de pouco em pouco" — um passo por vez no chat, prompt
> de GPT pronto pra colar quando precisar de asset (frame a frame, anexar
> `ultimo_frame.png`), fatiar/re-registrar/verificar com screenshot ANTES de
> avançar. Verificação: pausar (espaço via KeyboardEvent) antes de seek+screenshot.
>
> ✅ **reels + spam NO AR** (2026-07-02, sessão 2 — verificado com screenshots): os grids
> foram fatiados (limiar 252), re-registrados por bbox, e o celular agora toca
> `cel_reels.png` (2 voltas a 6fps, coração vermelho pop + share verde) e depois
> `cel_spam.png` (mensagens empilhando a 6fps, celular VIBRANDO por código, segura o
> flood no fim). Detalhes/knobs no bullet "✅ REELS + SPAM NO AR" logo abaixo.
>
> ✅ **CENA 4c NO AR** (mesma sessão, decisão nova do Iagho — SUBSTITUI o "celular roda
> de lado"): a menina entra ANDANDO dir→esq (`menina_anda`/`menina_levanta` ESPELHADOS
> por código), o celular ENCOLHE suave (~1/4 dela, desce pra altura da mão, vibra cada
> vez menos) e ela para diante dele. ✅ **NARRAÇÃO DA CENA 4 NO AR** (`QUOTES4`/`Q4SEQ`,
> 5 blocos na coluna esquerda do papel) + no fim **"por isso, existe" + o TÍTULO
> "O capítulo que falta" em DESTAQUE** (os dois FICAM; título com **letras fervendo a
> 8fps uma a uma** — `handWrite` ganhou modo `perLetter`, pedido do Iagho). Timeline
> termina ~3:58. Tudo verificado com screenshots.
>
> ✅ **`meninapegagrid.png` CHEGOU E ESTÁ NO AR** (mesma sessão): ⚠️ GOTCHA (o Iagho
> pegou: o pé dela saía CORTADO) — nesse grid os PÉS VAZAM da célula pra fileira de
> baixo (os "filetes" na borda superior das células eram os DEDOS da menina de cima!).
> Fatiar por grade fixa decepava o pé → **`slice_pega.py`** novo, recorte por
> **COMPONENTE CONEXO atribuído à célula do centroide** (igual ao `slice_levanta.py`),
> célula final 362×482 com folga vertical, re-registro pelo CORPO (centroide x, pés no
> fundo do bbox em fh-4). Calibração por bbox: `GRAB_GF:0.80` (corpo f0 370/482 casado
> com levanta f11 326/340 — altura idêntica à pose de pé), `GRAB_X:0.635`,
> `CEL4_F:0.328 / CEL4_X:0.542 / CEL4_Y:0.464` (o celular do código termina EXATAMENTE
> onde o celular flutuante do f0 do grid está — na frente do ROSTO dela; emenda
> verificada: (673,263)→(668,262), sem salto, pés inteiros nos 12 frames). Ela pega em
> `T3g.grabAt` (~e108), vira pra si e fica absorvida (boil f10–12).
>
> ✅ **CENA 5a/5b NO AR (código)** (mesma sessão — plano aprovado pelo Iagho): a
> lampadinha de ideia acende sobre a cabeça dela → treme → RACHA → apaga (grid
> especulativo **`lampada.png`**, mapeamento de frames pronto no código; **PROMPT
> FRAME A FRAME PRONTO em `cena4-prompts.md` §4** — anexar `celular_ref.png`; amarelo
> aquarela é o único acento, sobrevive ao keying). Quando ela racha, **o PAPEL racha
> junto**: rachaduras ANGULOSAS por código (zigue-zague seco + quebradas fortes +
> galhos, determinísticas por hash) irradiando da lâmpada em 3 degraus abruptos
> (0.35s) + **escurecimento** (`CRACK_DK` 0.06/0.11/0.17), e a tela **CONGELA**
> (`T5.freezeAt`: o `now`/`e` dos sprites travam — menina, celular e lâmpada viram
> desenho morto; **só o título continua fervendo**, letra a letra). Sincronia com a
> narração: acende no "de criar. de imaginar…", treme no "e quando esquecemos…",
> racha quando "…interrompida." termina de ser escrita. Knobs: `LAMP_X/Y/H`, `T5`,
> `CRACKS`. Verificado com screenshots (sem a lâmpada ainda — entra sozinha).
>
> ✅ **`lampadagrid.png` CHEGOU E ESTÁ NO AR** (mesma sessão): mapeamento veio EXATO
> (f0 esboço → f1–4 acesa amarela → f5/6 tremendo → f7 trinca → f8 espalha → f9 racha
> aberta → f10/11 morta com fumacinha). Fatiado `4 3 12 none 252` (o grid veio com
> LINHAS DE GRADE pretas — o inset 12 corta), limpeza 4 bordas + re-registro pelo
> bulbo (maior componente), amarelo sobreviveu (147.932 px). Bulbo ~150×237 de célula
> 338. Verificado com screenshots: acesa sobre a cabeça, tremendo, trincando com a
> rachadura nascendo DO BULBO, morta no mundo escuro congelado.
>
> ✅ **CENA 5 COMPLETA (5c/5d NO AR)** (mesma sessão — verificado com screenshots):
> depois do título escrito, as **rachaduras CRESCEM** (degraus 3/4 em `T5b.crack2At`,
> `CRACK_DK` até 0.30) → o **rasgo se desenha** (polilinha `TEAR` quase vertical perto
> da borda esquerda, fibra branca + traço escuro, `T5b.tearAt`) → a **página é
> ARRANCADA como folha de caderno**: o mundo velho INTEIRO (menina congelada, lâmpada,
> rachaduras, "por isso, existe") é desenhado dentro de um transform rígido clipado ao
> pedaço à direita do rasgo, que sai voando pra direita com rotação (`tearP²`,
> `T5b.tearDur:1.6`); sobra a **tirinha serrilhada** presa na "espiral" (papel velho
> escurecido) e atrás revela a **página NOVA mais clara** (`BG5`). **O TÍTULO NÃO SAI —
> fica vivo por cima** (decisão do Iagho: não reescreve, ele sobrevive à rachadura).
> Na página nova: **campanha** escrita à mão (`CAMP`/`CSEQ`, 2 blocos centrados) + o
> fecho **"Histórias começam com o saber."** destacado com perLetter (`TAG`, esquerda
> alinhada com a do título) — composição final = o fecho do roteiro. ❌ as "folhas dos
> futuros voando ao fundo" foram REMOVIDAS (Iagho não gostou — não repor). `DUR`
> auto-deriva do fecho (~4:26 total).
>
> ✅ **TRANSIÇÃO 5→6 NO AR** (2026-07-02, sessão 3 — verificado com screenshots,
> pausar antes de capturar!): depois do fecho respirar 3s (`T6.at`), a **tirinha
> serrilhada se ESVAI** (alpha `stripA`, 1.2s — a página nova toma o palco) e o
> **título + "Histórias começam com o saber." saem em fade** juntos (`fadeAt:T6.at`
> nos dois handWrite). Palco limpo pro início da cena 6. Texto integral das cenas
> 6–8 da Marcela CONFERIDO no `roteiro.md` (já estava salvo, bate palavra a palavra).
>
> ✅ **OS 5 PERSONAGENS DA CENA 6 ESTÃO PRONTOS** (2026-07-02, sessão 3 — todos
> gerados pelo Iagho no GPT, fatiados e re-registrados; detalhes frame a frame no
> "status" do `cena6-prompts.md`): `eco_pista.png` (16f 313×313, dupla acha a pista
> no chão, f10–15 espelhados p/ continuidade), `eco_jornal.png` (12f 362×362, pista
> cai do jornal, registrado pelos pés), `eco_sofa.png` (12f, casal DE COSTAS reage à
> pausa — telona é do código, registrado por bbox), `eco_influencer.png` (12f
> frontal, todos limpos) + `eco_influencer2.png` (12f perfil→frontal; USAR SÓ
> f0–5+f8–9, resto tem celular decepado), `eco_leitura.png` (12f, palavra acende em
> amarelo na folha). Pista amarela = callback da lâmpada, sobrevive ao keying.
> ✅ **ESQUELETO DA CENA 6 + ESTAÇÃO 1 NO AR** (mesma sessão — verificado com
> screenshots): `S6` (at=T6.at+fadeDur+0.8, dwell 7.5s, slide 1.3s), câmera por
> `s6off(e)` (pura função do tempo, sem estado), 5 estações lado a lado, letreiro
> manuscrito escrito NA CHEGADA de cada uma (viaja com a estação; logos =
> caligrafia). **Estação 1 (@globo/GloboPop)**: moldura de celular (sketchRect 2
> passadas) com "vídeo" de riscos fervendo + barra de progresso em loop, dupla
> `eco_pista` (p0–11 a 6fps → boil p12–15), pista voa em arco pro RODAPÉ
> (`drawScraps`, slots `SCRAP_X`, fixos na câmera) e a palavra **"Histórias"** se
> revela no pedacinho. `eco_pista` foi RE-REGISTRADO pelos pés (o chão subia entre
> fileiras do grid). Knobs: `S6`, `ST1`, `SCRAP_*`. `DUR` agora = 5 estações
> (~5:13).
> ✅ **CENA 6 COMPLETA — AS 5 ESTAÇÕES + O FECHO NO AR** (mesma sessão, tudo
> verificado com screenshots): **g1** (`drawSt2`: página de portal com manchete
> manuscrita "a educação de milhões de jovens / foi interrompida no meio" +
> colunas de risquinhos + foto hachurada; pista cai do jornal → "começam");
> **globoplay** (`drawSt3`: telona 16:9 com "novela" de riscos que **CONGELA na
> pausa** (desenho morto, só a moldura ferve), ⏸ pop rabiscado, casal eco_sofa
> reage, mini anúncio lower-third sobe com o pedacinho "com o" já escrito —
> `early:true` no S6SCRAP); **Viu** (`drawSt4`: 2 shorts verticais, eco_influencer2
> na A [f0–3 fala → f4 aponta → f5 varre → f8/9 braços abertos] e eco_influencer
> na B defasado 0.5s; **BOLHA rabiscada** em volta da A que **ESTOURA** em cacos +
> tracinhos radiais sincronizada com os braços abrindo; "Fora da bolha" manuscrito);
> **Movimento LED** (`drawSt5`: carta de linhas corridas com VÃO na linha 4 onde a
> palavra **"saber." se acende** em amarelo, sincronizada com a eco_leitura achando
> a dela; pista voa → rodapé). **FECHO** (`S6F`, at=fim do dwell da estação 5): véu
> BG5 cobre a estação e os 4 pedacinhos voam do rodapé pro CENTRO, crescem
> (`grow:0.32`) e se encaixam lado a lado — **"Histórias começam com o saber."**
> como bilhete de recortes (tgtX espaçados 0.135, encostados). `DUR`≈5:14.
> Knobs: `ST2..ST5`, `S6SCRAP`, `S6F`.
>
> **FALTA na cena 6 / próximos passos:**
> 1. **NARRAÇÃO da cena 6** (texto da Marcela no roteiro.md — "nas redes sociais,
>    queremos reacender…" etc.): escrita à mão, fixa na câmera (faixa de cima ou
>    por estação), agenda tipo CSEQ. Decidir posição com o Iagho.
> 2. **polimento** (o Iagho vai olhar): moldura do celular da estação 1 meio
>    "limpa", pause bars muito retas, timing dos dwells (7.5s por estação).
> 3. **cenas 7–8** (páginas se preenchendo — reuso dos futuro_*.png; volta ao "Era
>    uma vez…" com a menina escrevendo) + fecho do filme.
> 4. pacing geral: ~3:54 a 1x uniforme (knobs apertados; ver item 4 do bloco ⭐ —
>    warp de velocidade foi reprovado/revertido; 3:00 exige enxugar texto).
>
> O que vem agora:
>
> 1. **CENA 6 PLANEJADA (2026-07-02, sessão 3 — plano + prompts em `cena6-prompts.md`,
>    aguardando ok do Iagho)**: caça à frase em **5 estações deslizando** (GloboPop →
>    g1 → Globoplay → Viu → Movimento LED). Direção do Iagho: personagens = SILHUETAS
>    PRETAS (4–5, grids de boil 3×1 no GPT — prompts §1–5 prontos, anexar
>    `ultimo_frame.png`); logos Globo = **letreiros manuscritos POR CÓDIGO** (não pedir
>    logo ao GPT). Mecânica proposta: pista de cada estação = **pedacinho de papel
>    AMARELO** (callback da lâmpada) com a palavra ("Histórias"/"começam"/"com o"/—/
>    "saber."), acumulando no rodapé; no fecho os pedaços se ENCAIXAM formando a frase.
>    Telas/jornal/player pausado/bolha que estoura/texto do LED = tudo código.
>    Depois: cenas 7–8 (páginas se preenchendo, volta ao "Era uma vez…").
> 2. Pacing geral: a peça está em ~4:26 (pedido original ≤3min) — quando o conteúdo
>    fechar, apertar os knobs das agendas (QSEQ/Q3SEQ/Q4SEQ/CSEQ, holds e 0.05s/letra).
>
> Gotchas que valem sempre: cache do `file://` (abrir com `?v=N` + conferir com
> `eval "document.scripts[0].text.includes('<trecho novo>')"`), double-open, `node --check`
> no script extraído, `window.__s3(e)` pra pular na cena 3 (reels começa em e≈98,
> spam e≈102; pausar com espaço ANTES de capturar frame exato — o seek tem drift).
>
> ## O QUE FOI FEITO em 2026-07-02 (sessão longa — TUDO verificado com screenshots)
>
> - **CENA 2 COMPLETA, zero pendência**: 5 futuros no ar repetindo em ciclo (nenhuma
>   folha em branco, pintura por folha com tinta), carrossel acelerado (SCROLL_V 0.16,
>   PAGE_GAP 1.30), narração inteira da cena 2 escrita à mão (QSEQ, multilinha),
>   caminhada v3 com passos de verdade (andandogrid12 → WFN=12).
> - **PLAYER DE SCRUB**: barra embaixo do palco; espaço=pausa, ←/→=±5s, arrastar=seek
>   (funciona pausado). Clique-replay só no canvas. `window.__seek(s)` e
>   `window.__s3(e)` (e = tempo DENTRO da cena 3) pra testes.
> - **CENA 3 COMPLETA**: rebobinar exponencial com borrão → flash → a MESMA TV da cena 1
>   com estática 2000 BAKED (tvest1/2/3) → 8 refs curadas passando centradas com degradê
>   nas bordas + tinta (sítio, caverna do dragão, vila sésamo, cocoricó, pingu, bob
>   esponja, zoboomafoo, shaun) → estática sai → falas da Marcela escritas NO MEIO DA
>   TELA (QUOTES3, 9 frases) → livro reaparece com fade-in e folheia.
> - **CENA 4 (metade)**: livro→SMARTPHONE p&b rabiscado (livro_vira_celular.png fatiado
>   limiar 252 + limpo + re-registrado; emenda sem salto) + **zoom que empurra a TV pra
>   fora** (celular NÃO cresce, termina sozinho e centrado no palco).
> - **celular_ref.png** criada (ref do nosso celular pra prompts).
> - ✅ **REELS + SPAM NO AR** (2026-07-02, sessão 2): `celreelsgrid`/`celspamgrid` fatiados
>   (`slice_grid.py ... 4 3 12 none 252`; vermelho/verde sobrevivem ao keying — conferido:
>   3368 px vermelhos, 677 verdes), **re-registrados pelo bbox do MAIOR componente conexo**
>   (bursts/balões não puxam o centro; 1 filete de borda removido no spam f0). No
>   `drawBook3`: a partir de `T3.reelsAt` (=Q3_END+12, 0.2s depois do fim do zoom, e≈98)
>   toca `cel_reels.png` em loop a `REELS_FPS:6`; em `T3.spamAt` (=Q3_END+16, e≈102) troca
>   pro `cel_spam.png` empilhando a `SPAM_FPS:6` e SEGURA o último frame (flood); o celular
>   **vibra por código** no spam (`VIB_HZ:45`, `VIB_AMP:0.004·R.w`, amplitude cresce com a
>   pilha). **Escala = MÉDIA GEOMÉTRICA** dos ratios de largura/altura do bbox
>   (`REELS_S:0.777`, `SPAM_S:0.842` — os desenhos têm proporções diferentes: antigo
>   154×272, reels 211×329, spam 181×326; casar só largura dava pop de −12% na altura).
>   Carregamento especulativo (cel2/cel3). Emendas verificadas com screenshots (sem
>   salto; troca fica dentro do wobble do boil).
> - ✅ **CENA 4c NO AR** (2026-07-02, sessão 2): menina entra andando DIR→ESQ (sprites
>   espelhados — `G4_H:0.52, G4_FY:0.80, G4_X0:1.10→G4_X1:0.635, WALK4_V:0.16`; chegada
>   auto-derivada `T3g.arrive`, para na pose 11 do levanta + boil) enquanto o celular
>   ENCOLHE (`T3.shrinkAt=Q3_END+19`, 2.6s, fator `CEL4_F:0.35`, destino `CEL4_X:0.555 /
>   CEL4_Y:0.63` = altura da mão; a vibração escala junto). Asset especulativo
>   **`menina_pega.png`** já esperado no código (`T3g.grabAt=arrive+0.8`, o celular do
>   código some e o grid assume; knobs `GRAB_GF/GRAB_X/GRAB_PAD` a calibrar) — prompt
>   frame a frame pronto em `cena4-prompts.md` §3 (gerar de perfil pra DIREITA, o código
>   espelha).
> - ✅ **NARRAÇÃO DA CENA 4 + TÍTULO NO AR** (2026-07-02, sessão 2, texto do Iagho):
>   `QUOTES4` (5 blocos: "hoje, temos uma nova tecnologia…" → "…a nossa história é
>   interrompida."), agenda `Q4SEQ` auto-derivada (começa junto com os reels,
>   ~0.05s/letra), escrita à mão na COLUNA ESQUERDA do papel (`Q4_PX:0.042, Q4_CX:0.25,
>   Q4_Y:0.28` — o celular vive no centro/direita). No fim: **"por isso, existe"**
>   (`Q4_LEAD`) e o **TÍTULO "O capítulo que falta" em destaque** (`TITLE_PX:0.075`,
>   centro `TITLE_CX:0.30/TITLE_Y:0.40`) — os dois SEM fade (ficam). **`handWrite`
>   ganhou `perLetter:true`**: cada letra com jitter próprio quantizado a `BOIL_FPS` (as
>   letras fervem individualmente — usado no título, pedido explícito). `DUR` agora
>   auto-deriva do título (~3:58 total). Verificado com screenshots.
>
> **ONDE PAREI (resumo pra nova sessão):**
> - **Cena 1 = PRONTA** no `index.html` (abertura TV → menina escreve "Era uma vez…" → texto some). Abrir com F11.
> - **Cena 2 quase toda NO AR dentro do `index.html`** (ver 8.4): texto some → câmera empurra a TV pra fora → menina **levanta** → folha **vira livro** (no lugar da folha, cresce pouco) → livro **folheia** → **folhas saem do livro e viram um CARROSSEL BRANCO no fundo** (borda preta) → câmera afasta → mundo desliza como se ela andasse. Verificado com screenshots.
> - **DECISÃO NOVA:** o "caminho de páginas no chão + pan" virou **carrossel de folhas no fundo enquanto ela ANDA** (mais 2.5D). Os futuros aparecem PINTANDO-SE nas folhas do carrossel + mão escreve "toda história começa com uma possibilidade.".
> - **Menina ANDANDO = no ar** (`menina_anda.png`, 8 frames; variante de cabeça virada foi descartada). Pendente: **regenerar o grid de andar** com passos de verdade (`andandogrid12.png`, prompt v3 com tabela de poses).
> - **CÓDIGO DA CENA 2c = PRONTO** (ver 8.5): futuros **pintando-se nas folhas** (carregamento especulativo — quando os `futuro_*.png` chegarem, entram sozinhos) + **mão escrevendo "toda história começa com uma possibilidade."** fixa na câmera, à direita da menina. Verificado com screenshots usando refs como arte-teste.
> - **ARTES DOS FUTUROS: 5/5 NA PASTA** (2026-07-02): escola, professora, casa, invenção e
>   comunidade (coloridas — DECISÃO: aquarela lavada no entorno, personagens silhueta preta;
>   fundo ~253–255 = ok pro multiply). Prompts finais em `futuros-prompts.md`.
> - ✅ **CAMINHADA v3 NO AR** (2026-07-02): `andandogrid12.png` chegou (estava nos
>   Downloads), fatiado (12 frames 221×327) e `WFN=12` — agora tem passagem de pés juntos,
>   passos de verdade. Verificado com screenshots. **CENA 2 SEM PENDÊNCIA DE ASSET.**
> - **CENA 3 NO AR (2026-07-02, ver §10):** depois da última frase, a animação REBOBINA
>   (reverso exponencial + borrão) e corta pra **A MESMA TV da cena 1** no centro
>   (DECISÃO do Iagho: não tem TV nova — muda só o conteúdo da tela) com estática +
>   slideshow de refs (TV Cultura/Globinho). Verificado com screenshots. ✅ **ASSETS DA
>   CENA 3 CHEGARAM** (2026-07-02): `tvest1/2/3.png` (TV com estática baked) + 8 refs
>   curadas (`tvref_01..08`: sítio, caverna do dragão, vila sésamo, cocoricó, pingu, bob
>   esponja, zoboomafoo, shaun — várias são FRAMES REAIS dos programas, decisão do casal).
>   Refs passam CENTRADAS na tela com bordas em degradê + tinta ao entrar, slideshow
>   acelerado. Tem **player de scrub** pra ajustes (espaço/←→/barra).
> - **CENA 3b + INÍCIO DA CENA 4 NO AR (2026-07-02):** depois da volta das 8 refs, a
>   estática SAI (crossfade tvest→tv em 0.7s) e as **falas da Marcela são escritas com a
>   mão NO MEIO DA TELA da TV**, uma por vez (`QUOTES3`/`Q3SEQ`, 9 frases, blocos
>   multilinha centrados, ~0.05s/letra — termina ~e85 da cena 3). Depois (`T3.bookAt`)
>   o **LIVRO reaparece na tela com fade-in** e toca a transformação inteira
>   (papel→livro, 12f a 5fps) + folheia em loop. ✅ **`livro_vira_celular.png` NO AR**
>   (2026-07-02): o livro fecha, a cor escorre e vira um SMARTPHONE p&b rabiscado
>   (12f a 5fps em `T3.celAt`, fim = boil f10–12; emenda sem salto calibrada por bbox —
>   detalhes/gotchas do fatiamento em `cena4-prompts.md` §1). O strip foi RE-REGISTRADO
>   por bbox (o GPT deixava o objeto passear ±25px → celular "desviava").
> - **ZOOM DE SAÍDA DA TV NO AR** (2026-07-02, pedido do Iagho): durante a transformação
>   (`T3.zoomAt=celAt+0.8`, 3s, ease), a TV é AMPLIADA (×`Z4_MAX:2.6`, pivô no centro
>   visual da tela) até sumir dos arredores — **o celular NÃO cresce** (o zoom é só na
>   TV + janela de clip `Rz`); o celular deriva suave pro CENTRO DO PALCO e fica sozinho
>   no papel. Verificado com screenshots. **DECISÃO NOVA no conteúdo do celular**
>   (1ª arte reprovada — carregada demais): minimalista P&B com o CELULAR JÁ NA ARTE,
>   grids de muitos frames; só o coração VERMELHO (like, com pop) e o compartilhar
>   VERDE (no aperto). **Aguardando `celreelsgrid.png` (4×3, sequência like/share) e
>   `celspamgrid.png` (4×3, mensagens empilhando)** — prompts em `cena4-prompts.md`
>   §2a/§2b; ref do nosso celular gerada: **`celular_ref.png`**. Vibração = código.
>   `window.__s3(e)` pula pra um tempo DA CENA 3 (testes). Próximas partes da cena 4
>   (zoom/moldura some, reels, notificações, menina presa, lâmpada racha): ver
>   `cena4-prompts.md` §2–4 — "vamos por partes".
> - ⚠️ **GOTCHA NOVO (perdemos tempo):** o Chrome do agent-browser **cacheia o index.html via
>   `file://`** mesmo com `close --all` + double-open — screenshots podem ser de CÓDIGO VELHO.
>   Sempre abrir com query de cache-buster (`index.html?v=N`, incrementa o N) e conferir com
>   `eval "document.scripts[0].text.includes('<trecho novo>')"` antes de screenshot.
> - **PACING RESOLVIDO (2026-07-02):** `SCROLL_V` 0.10→**0.16** e `PAGE_GAP` 1.75→**1.30** —
>   folha nova a cada ~9.5s; os 5 futuros terminam ~55s (antes ~90s). Verificado com screenshots.
> - **CARROSSEL AGORA REPETE AS ARTES** (pedido do Iagho): depois das 5 primeiras folhas, os
>   futuros voltam em ciclo (`k % FUT_SRC.length` no `drawFut`) — nenhuma folha fica em branco.
>   `futStart[]` passou a ser POR FOLHA (não por arte): cada repetição também se pinta com o
>   efeito tinta ao entrar no quadro. `FUT_PAINT` 2.4→**3.0** (pintura mais perceptível).
> - **ZERO FOLHA EM BRANCO PARADA** (2026-07-02): `FUT_TRIG` 1.65→**2.00** (pinta assim que
>   aparece na borda; borda visível ~1.97), `FUT_STAGGER` 2.2→**1.1**, `futAt` 25.5→**24.0**.
>   Folha só fica branca enquanto VOA do livro (proposital — nasce página).
> - **NARRAÇÃO DA CENA 2 INTEIRA NO AR** (2026-07-02): as 4 falas da Marcela ("histórias
>   começam com mudanças." → "quando a gente aprende…" → "a gente aprende a sonhar…" →
>   "porque aprender também é descobrir…") entram em sequência depois do "toda história
>   começa com uma possibilidade.": mão escreve, frase segura 2.6s, fade 1.2s, próxima entra
>   no mesmo lugar. **`QSEQ`** (agenda auto-derivada do tamanho, ~0.07s/letra) + **`handWrite`
>   ganhou MULTILINHA** (`\n`, 1ª linha na baseline `QUOTE_Y`, bloco cresce pra baixo, mão
>   acompanha linha a linha). Frases em `QUOTES[]`. Última segura +4s. Sequência termina ~82s.
>   Verificado com screenshots (todas as 5, multilinha ok, mão acompanhando).

---

## 1. O que é

Animação de **até 3 minutos** para a **Marcela** (esposa do Iagho), trabalho para uma
campanha da **Globo** chamada **"O capítulo que falta"** — educação como o prólogo de toda
história ("Histórias começam com o saber."). Ver `roteiro.md` para o roteiro completo (8 cenas).

- **Estética pedida:** traço de **desenho antigo feito à mão**, "como se alguém tivesse
  desenhado essa animação". Silhueta preta a nanquim no estilo do projeto `../aquarela`.
- **Formato:** **horizontal 16:9** (pedido da Marcela).
- **Efeito-assinatura:** **line-boil a 8fps** — tudo "ferve"/tremula como cartoon desenhado à mão.
- **Feito por código** (canvas 2D, arquivo único `index.html`) + **imagens geradas por IA**
  (ChatGPT / GPT-image) no traço rabiscado, recortadas e animadas pelo código.

## 2. Como rodar / pré-visualizar

- Abrir `index.html` no navegador (duplo-clique) ou **F11** pra tela cheia. Clique/**R** repete; **D** = debug (mostra retângulo da tela).
- Preview via `agent-browser` (CLI). **Gotchas importantes do daemon** (perdemos tempo com isso):
  - O daemon **dessincroniza abas**: `eval`/`screenshot` às vezes batem numa aba `about:blank` velha. Sintoma: telas pretas falsas ou `getElementById('c')==false`.
  - Depois de `close --all`, o **primeiro `open` cai em about:blank**; o **segundo `open` navega**. Use double-open.
  - Para cronometrar capturas, exponha `window.__el=()=>((performance.now()-t0)/1000)` temporariamente e faça poll com `awk` (não tem `bc` no Windows). Faça **abrir + polar + screenshot no MESMO comando** (entre comandos separados o tempo dispara).
  - `getImageData` em canvas com imagens `file://` = **taint/erro**. O código evita getImageData de propósito.
- Checar sintaxe sem navegador: extrair o `<script>` e `node --check`.

## 3. Arquitetura do código (`index.html`)

Canvas 2D único, IIFE, `"use strict"`. Palco **16:9 "contain"** centralizado na janela (resto preto = letterbox), tudo **clipado** ao palco.

Peças reutilizáveis:
- **`makeField(fw,fh,...)`** → efeito **"tinta"** (reveal orgânico das bordas pra dentro): campo de limiar por ruído fbm; `.update(p)` preenche uma máscara; usada via `destination-in`.
- **`boil(now, ampPx, ampRot)`** → tremor de linha a **`BOIL_FPS=8`** (jitter quantizado por passo de 1/8s).
- **`hash/vnoise/fbm`** → ruído determinístico.
- **TV via blend `multiply`** sobre página creme (`BG=#f4efe3`): a TV é preto-sobre-branco; multiply deixa o branco "sumir" e a **tela branca deixa a estática passar** sem precisar recortar.
- **Estática** = canvas de ruído colorido `440x248` regenerado a `STATIC_FPS=12`, escalado pixelado + scanlines.
- **Câmera** = zoom que **centraliza a tela da TV no quadro** (`translate(Cx)→scale(s)→translate(-pvx)`, com `Cx` indo do centro-da-tela ao centro-do-palco). `FRAME_FILL` controla o quanto fecha.
- **Sprites boil** = ciclar N imagens quase-iguais (tv1/2/3; ou a grade da menina) a 8fps.

## 4. Assets na pasta

| arquivo | o que é |
|---|---|
| `tv1.png`,`tv2.png`,`tv3.png` | TV de madeira anos 60/70 rabiscada, 1672×941, fundo branco, **3 variações** (boil). Tela vazia. |
| `tvoff.png` | mesma TV com tela apagada (cinza). **Ainda não usada** (o "off" é feito por código). |
| `meninagrid.png` | grade **4×2 = 8 quadros** da silhueta da menina sentada escrevendo num papel amarelo (estilo aquarela). Fundo branco. 1774×887. |
| `menina.png` | a grade acima **fatiada** (tira 8×431×431, branco→transparente, amarelo/preto opacos, **registro fixo + alinhada pelo corpo**). É o que o código usa. |
| `mao.png` | mãozinha rabiscada segurando lápis, 1254×1254, RGBA, ponta embaixo-esq, antebraço some num degradê. |
| `slice.py` | fatiador que **recentra** cada quadro (bom pra ciclo de caminhada, tipo o `../aquarela`). |
| `slice_grid.py` | fatiador de **registro fixo + alinhamento pelo centro de massa do corpo** (pra loops de boil que não podem "escorregar"). Uso: `python slice_grid.py meninagrid.png menina.png 4 2` |
| `levantandogrid.png` → `menina_levanta.png` | menina se levantando, 12 frames 360×340 (fatiar: `slice_levanta.py`). |
| `folhalivrogrid.png` → `folha_vira_livro.png` | folha vira livro, 12 frames 470×259 (fatiar: `slice_folha.py`). |
| `folheando.png` → `livro_folheia.png` | livro folheando, 8 frames 431×431 (fatiar: `slice_livro.py`). |
| `folha_ref.png`, `livro_ref.png` | recortes-referência p/ prompts no GPT (folha da cena 1; livro aberto). |
| `meninapegagrid.png` → `menina_pega.png` | menina pega o celular e vira pra si, 12 frames 362×482 (perfil pra DIREITA — o código espelha). Fatiar com **`slice_pega.py`** (componente conexo — os PÉS vazam das células; grade fixa decepava o pé). |
| `lampadagrid.png` → `lampada.png` | lampadinha de ideia: acende → treme → racha → apaga, 12 frames 338×338, amarelo aquarela (único acento). `slice_grid ... 4 3 12 none 252` + re-registro pelo bulbo. |
| `closeup.html` | **backup obsoleto** (abordagem de close-up com papel, abandonada — pode apagar). |
| `roteiro.md` | roteiro completo (8 cenas). |
| `ferramentas-e-fluxo.md` | pesquisa de IAs de imagem→vídeo (preços jul/2026) e plano de produção. |
| `cena1-prompts.md`, `prompts.md` | prompts de geração usados. |
| `futuros-prompts.md` | prompts das 5 artes dos futuros (cena 2c) + regras (branco puro, retrato, refs). |
| `cena6-prompts.md` | plano visual da cena 6 (5 estações, caça à frase) + prompts dos 5 grids de silhuetas (boil 3×1). |
| ~~`papel.png`~~ | **DELETADO** (a Marcela pediu pra tirar). |

## 5. Cena 1 — o que está FEITO (dentro do `index.html`)

Linha do tempo no objeto **`T`** (segundos). Fluxo:

1. **preto** → a **TV é desenhada** com efeito tinta (`makeField`, `reveal` 2.0s).
2. TV **liga** (flash) em `onAt` → **estática colorida** + **boil** trocando tv1/2/3 a 8fps.
3. **zoom** (`zoomStart/zoomDur`) centraliza a tela → **vira uma moldura** (`FRAME_FILL=0.95`).
4. a estática **sintoniza** (crossfade, `sceneAt`) numa página creme e a **menina surge com tinta** e fica **escrevendo a 8fps** em loop, **centralizada e mais pra baixo** (`gh=R.h*0.78`, `gx` puxado ~`0.455`).
5. a **mão (`mao.png`) escreve "Era uma vez…"** letra a letra **no topo, sobre a menina** (`drawWriting`, `hStart/wStart`), com boil. A mão é grafite (recolorida) e o pulso some num degradê.
6. a **mão sai** (`hLift`) e o **texto some em fade ~2s depois** de terminar (`wFade`).

### Knobs de calibração (topo do arquivo / funções)
- `SCREEN={x,y,w,h,r}` — retângulo da tela dentro da TV (tecla **D** mostra).
- `FRAME_FILL` — quanto o zoom fecha na tela (↑ = fecha mais).
- `HAND_TIP_X/Y`, `FADE_*` — ponta do lápis e degradê do pulso da `mao.png`.
- Em `drawScreen`: `gh` (tamanho da menina), `gx`/`gy` (posição).
- Em `drawWriting`: `fontPx`, `textX`, `baseY` (posição do texto), `dh` (tamanho da mão).
- `T`: `hStart,hDur,wStart,wDur,hLift,hLiftDur,wFade,wFadeDur` (tempos da escrita/some).

## 6. Decisões (log)

- **Descartado** o beat "zoom no papelzinho → close-up do papel → papel voando com física" e o `papel.png`. Em vez disso, a mão escreve **direto sobre a menina dentro da telinha** e o texto some em fade. (Marcela)
- Silhueta = **preta rabiscada estilo aquarela**; TV = **madeira anos 60/70**; braço = **8fps** (grade 4×2).
- O boil "cartoon" veio da ideia da Marcela de **redesenhar** cada elemento em variações e trocar a 8fps.
- Câmera passou a **centralizar a tela no quadro** + **clip 16:9** (antes cortava torto pra esquerda e vazava preto no modo janela).
- `slice_grid.py` passou a **alinhar pelo corpo** (a IA desenhou a menina em alturas diferentes nos 8 quadros → ela balançava; alinhar pelo centro de massa travou).

## 7. Ferramentas de IA (resumo — detalhe em `ferramentas-e-fluxo.md`)

- **Imagens (traço):** ChatGPT/GPT-image; grátis: Adobe Firefly (estilos sketch), Gemini "Nano-Banana" (consistência).
- **Vídeo (se precisar):** testar grátis sem cartão = Dreamina (Seedance 2.0) + Kling; assinatura barata = Kling Standard ~US$10 ou Higgsfield Starter US$15; barato em escala = Seedance via fal.ai.
- Mas o **grosso é por código** (canvas) + desenhos rabiscados da IA.

## 8. Cena 2 — EM ANDAMENTO (livro / caminho de páginas em branco)

Beat: *"a folha vira um livro animado; uma criança olhando pra um caminho de páginas
em branco — cada página um futuro (escola, profissão, casa, invenção, comunidade)."*
Locução: *"toda história começa com uma possibilidade."*

**Decisões (confirmadas com a Marcela):**
- **Tudo por código + desenhos do GPT — NÃO usar Dreamina/vídeo** aqui (quebraria o boil/estilo e criaria costura; código = continuação sem seam da mesma timeline, não precisa exportar "último frame").
- Criança = **mesma silhueta preta** (coeso com a menina), de costas/lado olhando pra direita.
- Câmera = **pan horizontal esquerda→direita** (cara de "caminho").
- Código faz: o caminho de páginas em branco (creme, boil), a criança no início, o pan, e cada
  futuro **se desenha** (tinta + boil) ao entrar, na ordem escola→profissão→casa→invenção→comunidade.
- Virada 1→2: a telinha/menina abre suave e o caminho entra (mesma timeline).

**Decisão nova:** a "criança olhando o caminho" será a MESMA menina **se levantando** (sentada→de pé) enquanto a folha vira livro — animação por grid.

**Assets:**
- ✅ `levantandogrid.png` — grid 4×3 = 12 quadros da menina levantando (gerado no GPT a partir de `menina_sentada.png`). Ótimo, mantido.
- ✅ `menina_levanta.png` — a tira fatiada (12 frames, **360×340**, pés em y=336), refeita pelo
  **`slice_levanta.py`**: as figuras VAZAM das células no grid (cabelo da fileira de baixo invade
  a de cima), então o recorte é por **componente conexo** (scipy) atribuído à célula do centroide.
  ⚠️ NÃO usar mais o `slice_grid.py ... bottom` neste grid (cortava cabeça / borrões).
  O frame 0 tem o papel desenhado — o código **pula pro frame 1**.
- ✅ `menina_sentada.png` — silhueta sentada isolada (recorte da grade), usada como referência pro GPT.
- ✅ `ultimo_frame.png` — screenshot do último frame da cena 1 (referência).
- ⏳ `futuros_grid.png` — AGUARDANDO: grade (5×1 ou 3×2) com escola, profissão, casa, invenção, comunidade. Fatiar com `slice_grid.py` (align `body` ou `none`).

**`slice_grid.py` agora tem modos de alinhamento:** `body` (centro de massa, p/ loops), `bottom` (pés, p/ levantar/subir), `none`. 6º argumento.
Comando usado: `python slice_grid.py levantandogrid.png menina_levanta.png 4 3 6 bottom`.

### 8.1 A virada folha→livro (detalhada pela Marcela)
A folha da menina deve **virar um livro que FOLHEIA** (páginas passando), o livro **se abre**, e as
**páginas se dissipam/voam** e assentam formando o **caminho de páginas em branco** (que viram os futuros).
- Estilo do folhear escolhido: **livro de FRENTE, páginas virando na lombada** (riffle clássico) → depois soltam e voam.

### 8.2 O livro — abordagem por GRIDS do GPT (decisão 2026-07)
O protótipo por código (`cena2_test.html`) foi **REPROVADO** — ficou "vetorial" demais perto do traço
rabiscado da IA. Nova abordagem (igual à `levantandogrid`): **dois grids gerados no ChatGPT**, no mesmo
traço nanquim, fatiados com `slice_grid.py` modo `none` e tocados a 8fps pelo código:
1. ✅ **`folhalivrogrid.png`** — CHEGOU (veio **3×4**, não 4×3; nome sem "vira"). Sequência ótima:
   folha deitada → levanta → retângulo → engrossa em livro fechado → abre → aberto de frente.
   **Bônus: os quadros 10–12 são o livro aberto quase idêntico = boil do livro parado.**
   ✅ Fatiado → **`folha_vira_livro.png`** (12 frames, 470×259).
   ⚠️ **Limiar:** o default (238) apagava o miolo creme-claro das páginas abertas (fundo ~254,
   páginas na faixa 238–253) → páginas "furadas". O `slice_grid.py` aceita limiar como 7º arg,
   mas a tira final foi gerada pelo **`slice_folha.py`** (keya também a sombra acinzentada/halo
   e remove risquinhos soltos <300px; NÃO realinha — as âncoras por frame estão no index.html).
2. ✅ **`folheando.png`** — CHEGOU (4×2 = 8 quadros; nome sem "grid"). Livro idêntico nos 8,
   página fazendo o arco completo dir→esq. Toca **em loop** (código controla o ritmo).
   ✅ Fatiado → **`livro_folheia.png`** (8 frames, 431×431) com o **`slice_livro.py`** (fatiador
   especial): (a) keya também a **sombra acinzentada** do fundo (claro+sem saturação) que virava
   halo, e (b) **alinha pela base do livro** — as 2 fileiras vieram ~53px desalinhadas e o loop
   pulava. Base do livro consistente (385–388px de largura nos 8) — sem precisar de escala.

Refs de imagem criadas: **`folha_ref.png`** (recorte ampliado da folha da cena 1, p/ prompt do grid 1)
e **`livro_ref.png`** (último quadro do grid 1 = o livro aberto, p/ prompt do grid 2 e dos futuros).

Receita dos prompts que funcionou (p/ futuros grids, ex. `futuros_grid.png`): fundo branco puro,
células iguais, objeto centralizado/mesmo tamanho, sem grade/números/texto; âncora de estilo do
`prompts.md`; anexar ref de imagem (`livro_ref.png`/`ultimo_frame.png`) pra manter o traço/o mesmo objeto.

`cena2_test.html` está **obsoleto** (pode apagar; serve ainda de referência da timeline/palco 16:9).

### 8.3 Falta na cena 2 (próximos passos)
1. ✅ **`andandogrid.png`** CHEGOU (ciclo de 8 quadros, ótimo) → fatiado pelo **`slice_anda.py`**
   → **`menina_anda.png`** (8 frames, 233×410, pés no fundo-4px). **ELA JÁ ANDA no index.html.**
   ❌ A variante "andando olhando pro fundo" foi **DESCARTADA** pelo casal (arquivos
   `andandogrid_olhando.png`/`menina_anda_olha.png` apagados, código removido). Só caminhada normal.
   ⚠️ **PASSOS RUINS — REGENERAR o grid de andar:** medido: só 2/8 quadros têm pés juntos, o resto
   perna aberta (ela parece deslizar). Prompt v3 entregue com TABELA de pose por quadro (contato →
   apoio → **PASSAGEM pés juntos** → subida, 2x). Salvar como **`andandogrid12.png`** (4×3 = 12)
   → `python slice_anda.py andandogrid12.png menina_anda.png 4 3` → **atualizar `WFN` 8→12 no
   index.html** quando chegar.
2. Marcela gerar as **artes dos futuros** — 5 imagens separadas, retrato, tinta preta em **fundo
   branco PURO** (prompts prontos em **`futuros-prompts.md`**). Salvar como: `futuro_escola.png`,
   `futuro_professora.png`, `futuro_casa.png`, `futuro_invencao.png`, `futuro_comunidade.png`.
   ✅ **O código já espera por elas** (carregamento especulativo): basta salvar na pasta e dar
   replay — cada uma se pinta na sua folha, na ordem, via blend `multiply` (por isso o fundo
   precisa ser branco puro; fundo off-white aparece como retângulo claro, visto no teste com refs).
3. ✅ **FEITO** (2026-07, ver 8.5): futuros pintando-se nas folhas + mão escrevendo "toda história
   começa com uma possibilidade." (mecânica do drawWriting extraída pra `handWrite(el,o)` genérica).

### 8.4 O que JÁ ESTÁ no `index.html` (cena 2, primeira metade)
Sequência montada e verificada com screenshots (continuação sem costura da cena 1):
- **Timeline em `T`:** `pushAt:15.0/pushDur:2.8` (câmera dá zoom extra ×1.30 e a moldura da TV
  sai do quadro; `drawTV` para de desenhar quando completa), `standAt:15.4/standDur:1.4`
  (menina levanta, frames 1–11 a 8fps, segura o 11 com boil), `bookAt:15.4/bookDur:2.4`
  (folha vira livro a 5fps, **no lugar do papel mesmo, crescendo só um pouco** — Marcela pediu
  discreto: `BOOK_W:0.21` vs folha `0.145`),
  `riffleAt:18.6` (folheia em loop: vira 1s + vira 1s + pausa 1.5s; na pausa, boil f9–11 da
  tira da transformação).
- **`drawBook(el,R)`**: âncoras da BASE por frame hardcoded (`BT_AX/BT_AY`, medidas da tira);
  folhear usa âncora fixa (`BR_AX/AY`, base 386px) — os dois livros casam de tamanho por
  `BOOK_W`.
- **Knobs cena 2** (topo do script): `PAPER_X/Y/W` (onde a folha nasce = onde o papel estava),
  `BOOK_X/Y/W` (onde/tamanho o livro assenta), `GIRL_X0→X1` (deriva sutil da menina p/ esquerda
  enquanto levanta), `GIRL_H`, `GIRL_FY` (chão), `BOOK_FPS`.
- A troca sentada→levantando acontece em `standAt` (o papel some junto com o sprite sentado e a
  folha-sprite nasce no mesmo lugar, mesmo instante).
- **Cena 2b (folhas → carrossel):** `pagesAt:21.0` (6 folhas saem do livro voando em arco —
  bezier — pro fundo, 1 a cada 0.4s; no voo giram/flutuam). O **livro se dissolve** enquanto
  solta as folhas (`BOOK_FADE:3.0`, some até ~24.4s).
  **Visual final das folhas (várias iterações da Marcela):** RETRATOS gigantes colados no céu —
  papel na **COR DO FUNDO** (`PAGE_BG`, só o traço define), **contorno rabiscado imperfeito**
  (`sketchRect`: 4 arestas tortas com overshoot nas pontas, 2 passadas, fervendo a 8fps) e
  **fitas adesivas nos 2 cantos de cima** (`tapeAt`, aparecem quando a folha assenta). Saem do
  livro na cor dele e fazem fade pra cor do fundo. Ficam **ACIMA da menina, como horizontes**
  (`PAGE_Y:-0.78`, `PAGE_H:1.75`, `PAGE_GAP:1.75`).
  `zoutAt:21.2/zoutDur:6.0` (câmera afasta devagar ×0.50 — `ZOUT:0.50`, `ZOUT_DY:0.22`) +
  **2º afastamento forte quando ela anda** (`ZOUT2:0.45` suave em 5s + `ZOUT2_DY:0.10`) — ela
  fica minúscula embaixo dos retratos. `walkAt:24.5` (mundo desliza, parallax `PAR:0.85`;
  carrossel infinito pela direita; culling alargado ±1.8/2.8 R.w — câmera afastada vê mais mundo).
  Knobs: `PAGE_Y/H/AR/GAP/X0`, `PAGE_BG`, `SCROLL_V/RAMP`.
- **"Era uma vez…"** deslocado mais pra direita a pedido (`textX: R.w*0.18`, mesma altura).
- Quando a moldura da TV termina de sair (`pushAt+pushDur`), o **clip da telinha é liberado**
  (mundo aberto no palco inteiro) — o cream do palco cobre tudo, sem emenda visível.
- **`menina_anda.png` é carregado especulativamente** (onload/onerror): enquanto não existir, a
  menina fica de pé (pose 11 + boil) mesmo com o mundo andando; quando o arquivo aparecer na pasta,
  o código troca sozinho pro ciclo de caminhada a 8fps (`WFN=8` frames, pés no fundo-4px da célula).

### 8.5 Cena 2c no `index.html` — futuros + frase (FEITO 2026-07)
Implementado e verificado com screenshots (arte-teste = `livro_ref.png`/`folha_ref.png` no lugar
dos `futuro_*.png`; já revertido pros nomes finais):
- **Futuros pintando-se nas folhas** (`drawFut`, chamado dentro do loop do `drawPages` entre o
  fill e o `sketchRect`): futuro `k` vai na folha `k` do carrossel (0=escola … 4=comunidade).
  - **Carregamento especulativo** (mesmo padrão do `menina_anda.png`): `futImg[]` com
    onload/onerror; sem arquivo = folha fica em branco, com arquivo = entra sozinho.
  - **Gatilho por posição + ordem**: começa a pintar quando a folha entrou no quadro
    (`slotX < R.w*FUT_TRIG`, com `FUT_TRIG:1.65`; borda visível fica em ~1.97 com a câmera
    afastada) **e** o futuro anterior já começou há `FUT_STAGGER:2.2`s. Nunca pinta voando
    (`flying`/`wh<1` pulam). Estado em `futStart[]` (zerado no replay).
  - **Efeito de pintura**: `composeFut` preenche o buffer com a COR DO PAPEL (`PAGE_BG`),
    desenha a arte `<img>` por cima com **multiply DENTRO do buffer**, e mascara com
    `destination-in` do `futField` (makeField); o buffer já sai na cor final e vai pra tela
    com **source-over comum**. Arte completa (p≥1.1) = `<img>` direto com multiply no ctx.
    ⚠️ A 1ª versão (mascarar a arte crua e multiplicar o buffer na tela) dava um **clarão
    branco** no meio da pintura — não repetir. O branco da arte some no papel creme (por isso
    o fundo das artes precisa ser branco PURO). `FUT_PAINT:2.4`s, margem `FUT_M:0.84`.
    Como a arte tem margem branca, o começo da revelação (bordas) é invisível — o desenho
    "brota" de fora pra dentro no fim, mesma linguagem da menina/TV. Verificado limpo (2026-07-02).
- **Frase da narração**: a mecânica do `drawWriting` virou **`handWrite(el,o)` genérica**
  (texto, fonte, posição, tempos e tamanho da mão por parâmetro); o "Era uma vez…" é um wrapper.
  A frase `QUOTE` é escrita **FIXA NA CÂMERA** (depois do `restore()` do draw, em coordenadas do
  palco, com clip no 16:9) — na faixa de céu entre a base das folhas e a cabeça da menina,
  **à direita dela** (a possibilidade à frente; à esquerda colidia com a cabeça).
  Knobs: `QUOTE_PX:0.050, QUOTE_X:0.55, QUOTE_Y:0.745`; tempos em `T`:
  `futAt:25.5` (libera a pintura), `qHand:28.0, qStart:28.7, qDur:3.8, qLift:32.8`,
  `qFade:60` (a frase FICA — fade é knob pra quando a cena 3 existir).
- `window.__el` agora fica exposto permanente no index.html (cronômetro pras capturas).

## 9. Convenções de escrita/tom (do workspace)

Textos da peça e conversa: **minúsculo, informal, alusões poéticas sutis** (estilo da Marcela).
Ver também os outros projetos-presente do Iagho em `../` (aquarela, aniversario, viagenzinha, homenagem).

## 10. Cena 3 — "a animação volta no tempo" (rebobinar → TV de tubo)

Beat: *"a animação volta no tempo. uma televisão antiga surge no centro. dela saem luzes,
letras, números e personagens (refs TV Cultura / TV Globinho)."* Pedido do Iagho: reverso
começando na velocidade normal e acelerando MUITO, com borrão, e uma TV de tubo DIFERENTE
da TV de madeira da cena 1.

**Como funciona (tudo no `index.html`, 2026-07-02):**
- Toda a animação é função pura do tempo `el`, então o rebobinar é um **tempo virtual**:
  a partir de `T.rewAt` (auto-derivado: fim da última frase da QSEQ + 0.8s, ~83s),
  `el = rewAt − (e^(REW_A·t) − 1)/REW_A` — parte de 1x reverso e acelera exponencial
  (`REW_A:1.35`; zera em ~3.5s). Frases se desescrevem, artes se despintam, tudo volta.
- **Borrão** cresce com a velocidade: `cv.style.filter=blur()`, cap `REW_BLUR:14px`.
  No corte (`REW_END`, tempo virtual = 0) entra a cena 3 com flash branco (`S3_FLASH`)
  e o borrão termina de limpar em 0.9s enquanto a TV "assenta" (`S3_POP` scale 0.92→1).
- **`drawScene3(e,now)`**: papel creme + **A MESMA TV da cena 1** (tv1/2/3, multiply,
  boil 8fps — DECISÃO 2026-07-02: não tem TV nova; muda só o conteúdo da tela).
- **Tela**: knob **`SCREEN3`** (frações do palco; = SCREEN da cena 1, mesma TV).
  Conteúdo: **a estática vem BAKED na própria TV** — `tvest1/2/3.png` (a mesma TV com o
  chuvisco colorido JÁ NA TELA, 3 variações do GPT, esquema tv1/2/3) cicladas a **8fps**
  + scanlines. Quando uma ref está no ar, volta a TV de tela vazia (tv1/2/3) com a ref
  por cima; nos blips entre refs a estática pisca de volta. ✅ `tvest1/2/3.png` CHEGARAM
  (1672×941, fundo ~253). Fallbacks em cascata continuam no código: tira avulsa
  `estatica2000.png` (`EST_N:6`, `slice_estatica.py`) → estática de código.
  A partir de `REF_START:1.6`, as **8 refs curadas** (`TVREF_N:8`; `tvref_01..08` =
  sítio, caverna do dragão, vila sésamo, cocoricó, pingu, bob esponja, zoboomafoo,
  shaun — ✅ chegaram, várias são FRAMES REAIS dos programas, decisão do casal) em loop
  acelerado — `REF_DUR:1.7s` + blip `REF_BLIP:0.25s` (ref que não existe = estática).
  Cada ref aparece **CENTRADA na tela (contain `REF_FIT:0.86`), com degradê transparente
  nas 4 bordas (`REF_FEATHER:0.10`) e pintando-se com tinta a cada aparição
  (`REF_PAINT:0.7s`, `composeRef`)** — antes cobria a tela inteira e vazava da
  delimitação (pedido do Iagho).
- **`window.__seek(s)`** pula a timeline (testes; zera `futStart`). `window.__el` segue.
- **PLAYER DE SCRUB** (pedido do Iagho, 2026-07-02): barra embaixo do palco (translúcida,
  acende no hover) com play/pause + tempo. **Espaço** = pausar, **←/→** = ±5s, arrastar a
  barra = seek (funciona pausado = frame a frame). Clique-replay agora é SÓ no canvas
  (`e.target===cv`) pra não conflitar com o player. `DUR = REW_END+35` (fim nominal).
  Não faz parte da peça — é ferramenta de ajuste; na exportação final a gente esconde.
- **Fix de seek nos futuros:** a corrente `futStart[k-1]+FUT_STAGGER` travava depois de um
  seek (as folhas antecessoras, já fora do quadro, eram puladas pelo culling e a corrente
  nunca começava → folhas em branco pra sempre). Válvula `prevGone` no `drawFut`: se a
  antecessora já saiu do quadro (`slotX-PAGE_GAP < R.x-1.4·R.w`), pinta sem esperar.
- **Assets aguardados** (prompts prontos em **`cena3-prompts.md`**):
  `tvest1/2/3.png` (§2b — a TV com estática na tela, 3 variações) e `tvref_01..12.png`
  (§3 — cenas coloridas full-bleed 4:3, lista sugerida no md, Marcela curadora).
- **Falta nesta cena:** os elementos que SAEM da TV (luzes, letras, números, personagens
  voando pra fora) — a definir com o casal; e casar `REF_DUR`/ordem com a locução.
