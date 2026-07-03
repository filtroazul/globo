# cena 1 — "era uma vez" (tela preta → folha amarelada → mão escrevendo)

mesma lógica do aquarela: **tinta preta sobre fundo branco**, traço solto/sketch, e animação via **grid de keyframes** fatiado pelo slicer.

## a cena em camadas (o que é IA, o que é código)
1. **tela preta + som de lápis** → código (só um `fillRect` preto + fade).
2. **folha amarelada** entra em fade → **1 imagem de IA** (fundo, PNG horizontal).
3. **mãozinha infantil escrevendo** → **1 grid de IA** (keyframes da mão, fundo BRANCO pra fatiar) + o **texto "Era uma vez…" é revelado por CÓDIGO** (fonte Caveat, que o aquarela já usa) sincronizado com a ponta do lápis. mão = keyframe animado; letra = código (mais confiável que a IA acertar texto).

---

## PROMPT 1 — a folha amarelada (fundo, gera 1 imagem só)
cole no ChatGPT (peça formato **16:9 horizontal**):

> Uma folha de papel envelhecida e amarelada preenchendo todo o quadro horizontal 16:9. Tom creme-âmbar quente, textura de papel suave com leve granulado e manchinhas de tempo, cantos levemente gastos. Sem linhas, sem texto, sem objetos. Vista de cima, plana. Estética de livro ilustrado antigo, feito à mão. Iluminação uniforme.

salva como `paper.png` na pasta.

## PROMPT 2 — a mãozinha (grid de keyframes, fundo BRANCO)
regras pro slicer funcionar: **fundo branco puro**, **só tinta preta** (sem cor/cinza chapado), células iguais, mão centralizada e do mesmo tamanho — **só a pose muda**, sem linhas de grade, sem legendas.

> Sprite sheet numa grade 2×2 (4 quadros), fundo branco puro. Em cada quadro: a mãozinha e o antebraço de uma criança segurando um lápis de madeira, vista de cima em ângulo, como quem escreve numa linha. Desenho a nanquim/lápis preto, traço solto e minimalista, silhueta simples, SEM cor. Entre os 4 quadros a mão se desloca levemente para a direita e sobe/desce de leve, como escrevendo. Mesmo tamanho e posição em todos, mão centralizada em cada célula. Sem linhas de grade, sem números, sem texto.

salva como `hand_grid_src.png` na pasta.

> **plano B (mais confiável):** se a IA não segurar a mão igual nos 4 quadros, gera **1 mão só** bem limpa no branco (`hand.png`) e o código faz o "bob"/tilt sozinho. funciona bem e é o que eu recomendo se o grid vier torto.

---

## fatiar o grid
com PIL (já tem aqui). do dir da pasta:

```bash
python slice.py hand_grid_src.png hand.png 2 2   # arquivo, saida, COLS, ROWS
```

gera `hand.png` (tira horizontal transparente) e imprime `FRAMES FW FH` — anota esses números, vão no canvas igual o aquarela (`const FRAMES=4, FW=..., FH=...`).

## depois disso
com `paper.png` + `hand.png` prontos, eu monto o `index.html` (canvas 16:9) que:
- entra do preto, fade da folha,
- toca os frames da mão a ~12fps deslizando da esquerda pra direita,
- revela "Era uma vez…" em Caveat conforme o lápis passa,
- pausa no reticências pro texto da Marcela entrar.
