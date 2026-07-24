(() => {
  'use strict';

  const photo = (id, alt, className = '') => `<img class="${className}" src="https://images.unsplash.com/${id}?auto=format&amp;fit=crop&amp;w=1800&amp;q=86" alt="${alt}" loading="eager" decoding="async">`;
  const image = {
    team: ['photo-1521737711867-e3b97375f902', 'A team collaborating around a desk'],
    workshop: ['photo-1556761175-b413da4baf72', 'People working together in a workshop'],
    speaker: ['photo-1505373877841-8d25f7d46678', 'Speaker addressing an audience'],
    desk: ['photo-1499750310107-5fef28a66643', 'Notebook and desk materials'],
    planning: ['photo-1542744173-8e7e53415bb0', 'People discussing work around a table'],
  };
  const img = (key, className = '') => photo(...image[key], className);
  const eyebrow = label => `<p class="bench-eyebrow">${label}</p>`;
  const footer = (section, page) => `<footer class="bench-footer"><span>PRADASLIDES / HTML BENCHMARK</span><i></i><span>${section}</span><b>${String(page).padStart(2, '0')} / 07</b></footer>`;
  const tag = text => `<span class="bench-tag">${text}</span>`;

  const slides = [
    {
      id: 'P01', role: 'cover', topology: 'stage', layout: 'hero-evidence', tone: 'dark', density: 'air', transition: 'fade',
      classes: ['benchmark-slide', 'cover-slide'],
      title: 'A prompt is not<br>the presentation.',
      html: `<section class="cover-layout"><figure class="cover-photo">${img('team')}</figure><div class="cover-scrim"></div><div class="cover-copy">${eyebrow('PRADASLIDES / BENCHMARK')}<h1>A prompt is not<br>the <em>presentation.</em></h1><p>PradaSlides turns intent, evidence, and visual direction into an audience-ready story—with a delivery route that fits the available tools.</p><div class="cover-proof"><strong>07</strong><span>slides showing brief → narrative → art direction → stage QA</span></div></div>${footer('OPENING', 1)}</section>`,
      notes: 'Open with the central premise: a slide deck must make a decision or change visible, not simply decorate supplied words.',
      source: 'Benchmark-only content. Remote Unsplash photo; see example README for source links.',
      furniture: { kicker: false, pageNumber: false, progress: false, sourceLine: false }
    },
    {
      id: 'P02', role: 'content', topology: 'split', layout: 'brief-to-briefing', tone: 'light', density: 'air', transition: 'fade',
      classes: ['benchmark-slide', 'brief-slide'],
      title: 'Start with the communication job.',
      html: `<section class="brief-layout"><div class="brief-copy">${eyebrow('01 / COMMUNICATION BRIEF')}<h2>Start with the<br><em>communication job.</em></h2><p class="bench-lede">Before layout, establish what the audience should understand, decide, or do after this presentation.</p><div class="brief-list"><article><b>Audience</b><span>Who needs to act?</span></article><article><b>Outcome</b><span>What should become clearer?</span></article><article><b>Evidence</b><span>What can prove it?</span></article></div></div><figure class="brief-photo">${img('workshop')}<figcaption>Research is not a styling phase. It is the material for a credible story.</figcaption></figure>${footer('BRIEF', 2)}</section>`,
      notes: 'Explain the brief as a filter: it decides what to omit, which proof matters, and how the deck will earn attention.',
      source: 'Benchmark-only content. Remote Unsplash photo; see example README for source links.',
      furniture: { kicker: false, pageNumber: false, progress: false, sourceLine: false }
    },
    {
      id: 'P03', role: 'content', topology: 'spine', layout: 'narrative-arc', tone: 'accent', density: 'standard', transition: 'slide',
      classes: ['benchmark-slide', 'narrative-slide'],
      title: 'A deck moves, not just accumulates.',
      html: `<section class="narrative-layout"><div class="narrative-head">${eyebrow('02 / NARRATIVE ARCHITECTURE')}<h2>A deck moves,<br>not just <em>accumulates.</em></h2><p>A good outline uses contrast and consequence so every slide has a distinct reason to exist.</p></div><ol class="narrative-flow"><li><b>01</b><strong>Frame</strong><span>Name the change.</span></li><li><b>02</b><strong>Reveal</strong><span>Make the tension concrete.</span></li><li><b>03</b><strong>Prove</strong><span>Bring in the evidence.</span></li><li><b>04</b><strong>Decide</strong><span>Land the next move.</span></li></ol><figure class="narrative-photo">${img('speaker')}<figcaption>Every section needs one job.</figcaption></figure>${footer('NARRATIVE', 3)}</section>`,
      notes: 'Emphasize that a strong presentation is a sequence of decisions, not a holding area for all available content.',
      source: 'Benchmark-only content. Remote Unsplash photo; see example README for source links.',
      furniture: { kicker: false, pageNumber: false, progress: false, sourceLine: false }
    },
    {
      id: 'P04', role: 'content', topology: 'matrix', layout: 'capability-routes', tone: 'dark', density: 'standard', transition: 'fade',
      classes: ['benchmark-slide', 'capability-slide'],
      title: 'The output route adapts. The quality bar does not.',
      html: `<section class="capability-layout"><div class="capability-copy">${eyebrow('03 / CAPABILITY-AWARE')}<h2>The output route adapts.<br>The <em>quality bar</em> does not.</h2><p>PradaSlides plans for the runtime available today without pretending every system can inspect, generate, or render in the same way.</p></div><div class="route-grid"><article><span>Text-only</span><strong>Brief, copy, outline, production spec</strong><small>Image retrieval is delegated or held as an explicit request.</small></article><article><span>Vision + image gen</span><strong>Asset-aware visual plan and original visual direction</strong><small>Generated visuals remain distinguishable from supplied evidence.</small></article><article><span>Full production</span><strong>HTML or PPTX with visual QA and delivery checks</strong><small>Verify legibility, crops, density, and the actual output.</small></article></div><div class="capability-mark">NO SILENT<br>ASSUMPTIONS</div>${footer('ROUTING', 4)}</section>`,
      notes: 'This is the capability-aware promise. The agent should describe gaps and switch routes, rather than silently creating fake evidence.',
      source: 'Benchmark-only content.',
      furniture: { kicker: false, pageNumber: false, progress: false, sourceLine: false }
    },
    {
      id: 'P05', role: 'content', topology: 'mosaic', layout: 'media-roles', tone: 'light', density: 'air', transition: 'slide',
      classes: ['benchmark-slide', 'media-slide'],
      title: 'Every image needs a job.',
      html: `<section class="media-layout"><div class="media-copy">${eyebrow('04 / MEDIA INTELLIGENCE')}<h2>Every image<br>needs a <em>job.</em></h2><p>Images are selected and cropped according to the message they carry—not repeated as surface decoration.</p><div class="media-rules"><span>Subject protected</span><span>Frame follows evidence</span><span>Contrast checked in context</span></div></div><div class="media-mosaic"><figure class="mosaic-main">${img('planning')}<figcaption><b>Hero evidence</b><span>Sets the focal point</span></figcaption></figure><figure class="mosaic-tall">${img('speaker')}<figcaption><b>Moment</b><span>Raises stakes</span></figcaption></figure><figure class="mosaic-wide">${img('desk')}<figcaption><b>Texture</b><span>Supports craft</span></figcaption></figure></div>${footer('VISUALS', 5)}</section>`,
      notes: 'Use this visual hierarchy to explain the difference between meaningful media composition and a generic gallery of equally weighted photos.',
      source: 'Benchmark-only content. Remote Unsplash photos; see example README for source links.',
      furniture: { kicker: false, pageNumber: false, progress: false, sourceLine: false }
    },
    {
      id: 'P06', role: 'content', topology: 'frame', layout: 'stage-system', tone: 'light', density: 'standard', transition: 'fade',
      classes: ['benchmark-slide', 'system-slide'],
      title: 'Design for the room, not the canvas alone.',
      html: `<section class="system-layout"><div class="system-title">${eyebrow('05 / STAGE QUALITY')}<h2>Design for the room,<br>not the <em>canvas alone.</em></h2><p>Typography and spacing scale from the visual hierarchy first. Details stay quiet until they are needed.</p></div><div class="system-spec"><article><b>01</b><strong>Contrast is deliberate.</strong><span>Primary copy must be readable against the actual rendered background—not its intended background.</span></article><article><b>02</b><strong>Type earns the space.</strong><span>Large slides use large, product-specific display type instead of treating every idea as a small UI label.</span></article><article><b>03</b><strong>Decor must carry meaning.</strong><span>Lines, frames, and cards guide hierarchy; they never hide a crop or compensate for missing content.</span></article></div><div class="system-scale"><span class="scale-1">A</span><span class="scale-2">Aa</span><span class="scale-3">Aa</span><i></i><em>Display / Body / Utility</em></div>${footer('SYSTEM', 6)}</section>`,
      notes: 'The benchmark deliberately avoids ambiguous masks and low-contrast labels. Explain that these rules protect quality during implementation.',
      source: 'Benchmark-only content.',
      furniture: { kicker: false, pageNumber: false, progress: false, sourceLine: false }
    },
    {
      id: 'P07', role: 'closing', topology: 'stage', layout: 'call-to-action', tone: 'dark', density: 'air', transition: 'fade',
      classes: ['benchmark-slide', 'closing-slide'],
      title: 'From intent<br>to an audience-ready<br>presentation.',
      html: `<section class="closing-layout"><figure class="closing-photo">${img('team')}</figure><div class="closing-shade"></div><div class="closing-copy">${eyebrow('PRADASLIDES / AGENT SKILL')}<h1>From intent<br>to an <em>audience-ready</em><br>presentation.</h1><p>Research the message. Shape the journey. Direct the visuals. Verify the delivery.</p><div class="closing-actions">${tag('HTML')} ${tag('PPTX')} ${tag('PDF')} ${tag('PLANNING')}</div></div>${footer('CLOSING', 7)}</section>`,
      notes: 'Close by reinforcing the full workflow: communicate clearly, use evidence honestly, make deliberate visual choices, then verify the production result.',
      source: 'Benchmark-only content. Remote Unsplash photo; see example README for source links.',
      furniture: { kicker: false, pageNumber: false, progress: false, sourceLine: false }
    },
  ];

  window.PRADA_DECK = {
    meta: { title: 'PradaSlides · Tuned benchmark', status: 'final', storageKey: 'pradaslides:tuned-html-benchmark', transition: 'fade' },
    design: {
      canvas: { width_px: 1600, height_px: 900 },
      typography: { display_family: 'Trebuchet MS, Aptos Display, Arial, sans-serif', body_family: 'Aptos, Segoe UI, Arial, sans-serif', mono_family: 'Aptos Mono, Consolas, monospace' },
      color: { accent: '#f25549', positive: '#22a88a', warning: '#f0ad32', negative: '#d8465d', tones: {
        light: { background: '#fbf5e9', surface: '#fffdf7', text: '#18213a', muted: '#536076', line: '#d9d4c8' },
        dark: { background: '#17223b', surface: '#22304e', text: '#fffdf7', muted: '#d9e1ef', line: '#4e607d' },
        accent: { background: '#f3c84b', surface: '#fff2b2', text: '#18213a', muted: '#5c4c1e', line: '#c9971c' },
      } },
    },
    slides,
  };
})();
