/**
 * Particle background + pause control.
 * Particles: particleground by Jonathan Nicol (@mrjnicol), MIT.
 *
 * Colours are the originals. Motion is paused when the visitor prefers reduced
 * motion, when the tab is hidden, or when they press the pause button.
 */

document.addEventListener('DOMContentLoaded', function () {
  var container = document.getElementById('particles');
  var toggle = document.getElementById('motion-toggle');
  if (!container || typeof window.particleground !== 'function') return;

  var reduceMotion = window.matchMedia
    ? window.matchMedia('(prefers-reduced-motion: reduce)')
    : { matches: false };

  // Fewer particles on small screens: the line-drawing pass is O(n^2).
  var smallScreen = window.innerWidth < 640;

  var particles = particleground(container, {
    dotColor: '#e8dc39',
    lineColor: '#ffffff',
    density: smallScreen ? 16000 : 11000,
    particleRadius: 6,
    proximity: smallScreen ? 90 : 110
  });

  var userPaused = reduceMotion.matches;
  var running = true;

  function sync() {
    var shouldRun = !userPaused && !document.hidden;
    if (shouldRun && !running) particles.start();
    if (!shouldRun && running) particles.pause();
    running = shouldRun;
    if (toggle) toggle.setAttribute('aria-pressed', String(userPaused));
  }

  // The first frame is already drawn, so pausing leaves a static constellation.
  sync();

  if (toggle) {
    toggle.hidden = false;
    toggle.addEventListener('click', function () {
      userPaused = !userPaused;
      sync();
    });
  }

  document.addEventListener('visibilitychange', sync);

  var onMotionPrefChange = function (e) {
    userPaused = e.matches;
    sync();
  };
  if (reduceMotion.addEventListener) {
    reduceMotion.addEventListener('change', onMotionPrefChange);
  } else if (reduceMotion.addListener) {
    reduceMotion.addListener(onMotionPrefChange);
  }
});
