// ============================================================
// EXPORTA a peça em MP4 1080p60 de alta qualidade (frame a frame).
// Como a peça é 100% função pura do tempo, congelamos o relógio
// (performance.now + requestAnimationFrame) e avançamos 1/60s por
// quadro — todo frame é exato, boil a 8fps de verdade, zero drop.
// MUITO melhor que gravar a tela (sem compressão de captura).
//
// USO (validado 2026-07-04, ~30min de render):
//   1) numa pasta qualquer:  npm init -y && npm i puppeteer-core
//      e copie este arquivo pra lá (ou rode daqui com node_modules ao lado)
//   2) ajuste CHROME abaixo (qualquer Chrome/Chromium serve;
//      o do agent-browser fica em ~/.agent-browser/browsers/)
//   3) node render_mp4.mjs          (gera ./frames/ com ~11k PNGs, ~4GB)
//   4) ffmpeg -framerate 60 -i "frames/%06d.png" -c:v libx264 -preset slow
//      -crf 16 -pix_fmt yuv420p -movflags +faststart saida.mp4
//   5) apague ./frames/
//
// GOTCHAS: NÃO usar clip:{...} no page.screenshot (dava frame preto no
// headless — viewport já é 1920x1080). O ?nohud=1 esconde o player/hint.
// Pra 4K: viewport 3840x2160 (e o youtube trata uploads 1440p+ com codec
// melhor). O erro ERR_FILE_NOT_FOUND do estatica2000.png é esperado
// (fallback especulativo que não existe).
// ============================================================
import puppeteer from 'puppeteer-core';
import fs from 'node:fs';
import path from 'node:path';

const FPS = 60;
const CHROME = 'C:/Users/Iagho/.agent-browser/browsers/chrome-150.0.7871.24/chrome.exe';
const URL = 'file:///' + path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\//, '')), 'index.html').replace(/\\/g, '/') + '?nohud=1&export=1';
const OUT = path.resolve('frames');
fs.mkdirSync(OUT, { recursive: true });

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: true,
  args: ['--force-device-scale-factor=1', '--hide-scrollbars'],
});
const page = await browser.newPage();
await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });

// relógio virtual: precisa entrar ANTES de qualquer script da página
await page.evaluateOnNewDocument(() => {
  let vt = 0;
  const cbs = [];
  window.__vtStep = (ms) => {
    vt += ms;
    const list = cbs.splice(0, cbs.length);
    for (const cb of list) { try { cb(vt); } catch (e) {} }
  };
  performance.now = () => vt;
  window.requestAnimationFrame = (cb) => { cbs.push(cb); return cbs.length; };
  window.cancelAnimationFrame = () => {};
});

console.log('abrindo', URL);
await page.goto(URL, { waitUntil: 'networkidle0', timeout: 60000 });

// garante fonte manuscrita + imagens carregadas antes do frame 0
await page.evaluate(async () => {
  await document.fonts.load("600 40px 'Caveat'");
  await document.fonts.load("500 40px 'Caveat'");
  await document.fonts.ready;
});
await new Promise(r => setTimeout(r, 4000));   // folga pros Image() do script (file:// é rápido)

const dur = await page.evaluate(() => window.__dur);
const total = Math.ceil((dur + 0.6) * FPS);
console.log(`duracao ${dur.toFixed(1)}s -> ${total} frames a ${FPS}fps`);

const step = 1000 / FPS;
for (let f = 0; f < total; f++) {
  await page.evaluate(ms => window.__vtStep(ms), step);
  await page.screenshot({ path: path.join(OUT, String(f).padStart(6, '0') + '.png') });
  if (f % 300 === 0) console.log(`frame ${f}/${total} (${(100 * f / total).toFixed(1)}%)`);
}
console.log('FRAMES-OK');
await browser.close();
