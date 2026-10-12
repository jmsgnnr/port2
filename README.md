# James G. Potee: Portfolio (2026 refresh)

My personal site. It's a static, single-page portfolio: black background, neon yellow and hotpink,
a particle constellation behind everything, and roughly the design sensibilities of a 1999 homepage.
It's retro on purpose. There are no trackers on it, also on purpose.

## What's in it

- **About / experience / stack / projects / contact**, all in one `index.html`, using semantic
  sections and a real heading outline.
- **Particle background**: [particleground](https://github.com/jnicol/particleground) (MIT), kept
  from v1 with its original colours.
- **No build step, no framework, no analytics, no cookies, no third-party requests.** Icons are
  inline SVG and fonts are system fonts.

## Files

| Path | Purpose |
| --- | --- |
| `index.html` | All page content |
| `css/style.css` | Styles, including the responsive, reduced-motion and print rules |
| `js/demo.js` | Starts the particles and handles pausing (button, reduced motion, hidden tab) |
| `js/jquery.particleground.js` | Vendored particleground 1.1.0 with small local patches (marked `Local patch`) |
| `assets/favicon.svg` | Favicon (PNG fallback: `assets/favicon11.png`) |

`js/jquery-1.11.1.min.js` and `js/jquery.particleground.min.js` are left over from v1. The page
doesn't load either of them.

## Accessibility

- Skip link, visible focus styles, and a keyboard-reachable nav.
- `prefers-reduced-motion` is respected: the particles freeze into a static frame and the CSS
  blinking stops. The **pause particles** button (`aria-pressed`) lets anyone stop the motion.
- The particles also pause while the tab is hidden.
- All content sits on solid or near-solid black panels, so text contrast doesn't depend on
  where the particles happen to drift.
- The layout reflows to a single column on small screens.
- The page works without JavaScript; you just don't get particles.

## Running locally

Open `index.html` in a browser, or serve the folder:

```sh
python -m http.server 8000
# then visit http://localhost:8000
```

## Credits

- Particle effect: [particleground](https://github.com/jnicol/particleground) by Jonathan Nicol.
- Original template inspiration: [Particle Jekyll Template](https://github.com/nrandecker/particle).

Licensed under the terms in [LICENSE](LICENSE).
