# ferramentas de IA + fluxo de produção

pesquisa feita em **julho/2026**. preços/trials mudam rápido — sempre confere na página oficial antes de assinar.
objetivo: animação ~3min, **traço de desenho antigo feito à mão**, **horizontal (16:9)**.

---

## resumo rápido (o que eu faria)

1. **imagens (o traço / estilo):** ChatGPT (GPT-image) pra fechar o "look" e manter consistência num mesmo chat. grátis de reforço: **Adobe Firefly** (tem estilos Line Drawing / Ink / Sketch / Doodle) e **Gemini (Nano-Banana)** pra editar mantendo o personagem.
2. **testar animação de graça, sem cartão:** **Dreamina** (Seedance 2.0) + **Kling grátis** — ganham créditos diários. dá pra fazer MUITO teste sem pagar nada.
3. **uma assinatura barata pra fechar com qualidade:** **Kling Standard ~US$10/mês** (melhor custo-benefício isolado) OU **Higgsfield Starter US$15/mês** se quiser testar vários modelos (Sora 2, Veo, Kling, Seedance) num lugar só.
4. **mais barato em escala (via API):** Seedance pelo **fal.ai** (~US$0,022/s → ~US$0,22 por clipe de 10s).
5. **a espinha dorsal:** fazer a **composição/tempo/câmera por código** (horizontal, controle total) e usar a IA só pros **desenhos** e uns momentos "mágicos" de movimento. detalhe na seção "abordagem híbrida".

---

## imagens (gerar os desenhos)

| ferramenta | grátis? | força | preço |
|---|---|---|---|
| **ChatGPT / GPT-image** | limitado no free | segue prompt complexo, mantém estilo num chat, ótimo pra iterar | Plus US$20/mês |
| **Adobe Firefly** | sim (créditos diários) | estilos **Line Drawing, Ink, Sketch, Stippling, Doodle** — direto no lápis/nanquim | free + planos baratos |
| **Gemini (Nano-Banana)** | sim, generoso | edição mantendo o mesmo personagem/cena (consistência) | free |
| **Leonardo / OpenArt** | sim | "character reference": salva um personagem e reusa igual | free + pago |

**dica de consistência:** cria UM "prompt de estilo" (papel amarelado, lápis grafite, traço tremido, sem cor ou cor lavada, sombreado por hachura) e cola em TODA geração. gera os elementos em **PNG com fundo transparente** pra montar/animar depois.

## vídeo (animar os desenhos)

| ferramenta | grátis | pago | observação |
|---|---|---|---|
| **Dreamina (Seedance 2.0)** | ~225 tokens/dia, **sem cartão** | Basic US$15/mês | melhor porta de entrada grátis. Seedance 2.5 saindo início jul/2026 |
| **Kling** | **66 créditos/dia** | Standard **US$10**/mês (660 créd) | ótima consistência e movimento, barato |
| **Higgsfield** | 10 créд/dia (com marca d'água) | Starter US$15/mês | agrega Sora 2, Veo 3.1, Kling 3.0, Seedance num só lugar — bom pra **testar modelos** |
| **Pika** | trial | pago | tem modos **hand-drawn anime / claymation** — bom pro estilo |
| **Runway Gen-4.5** | trial curto | mais caro | melhor movimento, mas tende a "realistar" demais o 2D |
| **Kaiber** | trial | pago | mantém estilo artístico (ink-wash, aquarela) na animação |
| **Seedance via fal.ai (API)** | — | **~US$0,022/s** | mais barato em escala; precisa mexer em API |

**cuidado:** image-to-video que "realista" demais quebra a vibe de desenho à mão. Kling e Seedance costumam segurar melhor o traço 2D; teste com prompts do tipo *"2D hand-drawn animation, subtle line boil, no 3D, flat"*.

---

## abordagem híbrida (recomendada) — código + IA

ela quer **horizontal** e "como se alguém tivesse desenhado". o mais controlável (e a tua praia) é:

- **espinha:** uma página HTML 1920×1080, animação coreografada com **GSAP** (timeline: entradas, câmera, cortes).
- **look de papel:** textura de papel amarelado + grão por cima, tom âmbar quente.
- **linhas que se desenham sozinhas:** SVG com `stroke-dasharray`/`stroke-dashoffset` animado → dá o efeito "alguém está desenhando agora" (perfeito pro "Era uma vez…" e pras linhas surgindo).
- **traço tremido ("boiling line"):** filtro SVG `feTurbulence` + `feDisplacementMap` animado, OU trocar 2–3 frames quase iguais do desenho a ~8fps → aquele tremor de animação antiga.
- **câmera horizontal:** um container largo (o "livro") que desliza/zoom entre as páginas.
- **assets da IA:** os desenhos (criança, TV antiga, celular, páginas, comunidade) em PNG transparente, mesmo estilo.
- **exportar:** grava o canvas com `MediaRecorder`/CCapture.js → junta no **ffmpeg** (já instalado aqui). ou grava tela em 1080p.
- **áudio (lápis, trilha, voz da Marcela):** montar o mix final num editor (CapCut/Premiere) por cima dos clipes renderizados. 3min com muita locução → fechar o VO no editor é mais tranquilo.

> divisão de trabalho: **código** faz composição, tempo e câmera (barato, controlável, horizontal certinho). **IA** faz os desenhos e uns momentos de movimento orgânico que dão trabalho na mão.

---

## plano de ataque sugerido

1. **fase teste (grátis):** fecha o ESTILO no ChatGPT/Firefly (1 personagem + 1 cenário). anima o mesmo frame no Dreamina e no Kling grátis, compara qual segura o traço.
2. escolhe **1 assinatura** (Kling $10 ou Higgsfield $15) e gera os clipes das 8 cenas.
3. monta a **espinha em código** (horizontal, câmera, papel, texto que se escreve).
4. **junta** clipes de IA + animação de código no editor, adiciona VO + som de lápis + trilha.
5. exporta 16:9 1080p, ≤3min.

## fontes
- Seedance: https://www.seedance.tv/blog/seedance-2-0-free · https://www.atlascloud.ai/blog/case-studies/seedance-2.0-pricing-full-cost-breakdown-2026
- Higgsfield: https://higgsfield.ai/pricing · https://flowith.io/blog/higgsfield-pricing-2026-free-vs-creator-vs-studio/
- Kling: https://kling.ai/app/membership/membership-plan · https://aiimagetovideo.pro/blog/free-kling-ai-video-generator/
- estilo desenhado: https://www.argil.ai/blog/sketch-to-video-ai-the-6-best-tools-for-turning-drawings-into-videos-in-2026 · https://www.adobe.com/products/firefly/features/ai-drawing-generator.html
