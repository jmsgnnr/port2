"use strict";
(() => {
  const viewport = document.getElementById("experience-scroll");
  const first = viewport?.querySelector(".job");
  const hint = document.querySelector(".timeline-scroll__hint");
  if (!viewport || !first) return;

  // Size the scroll area to one complete entry, regardless of viewport width.
  const measure = () => {
    const height = Math.ceil(first.getBoundingClientRect().height);
    if (height > 0) viewport.style.height = height + "px";
    if (hint) hint.hidden = viewport.scrollHeight <= viewport.clientHeight + 2;
  };
  if (typeof ResizeObserver !== "undefined") {
    const observer = new ResizeObserver(measure);
    observer.observe(first);
  }
  window.addEventListener("resize", measure, { passive: true });
  measure();
})();
