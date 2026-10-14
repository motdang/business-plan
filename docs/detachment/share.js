/* Sharing for the page: a bar of places to send it, passage sharing on text selection, links to each plan sheet. */
(function () {
  "use strict";
  var page = location.origin + location.pathname;
  var title = document.querySelector('meta[property="og:title"]').content;
  var blurb = document.querySelector('meta[name="share-text"]').content;

  function enc(s) { return encodeURIComponent(s); }
  function frag(s) { return enc(s).replace(/-/g, "%2D"); }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  function targets(text, url) {
    var both = text + " " + url;
    var inst = (store("mastodon-instance") || "mastodon.social").replace(/^https?:\/\//, "").replace(/\/.*$/, "");
    return [
      ["Bluesky", "https://bsky.app/intent/compose?text=" + enc(both)],
      ["Mastodon", "https://" + inst + "/share?text=" + enc(both)],
      ["Threads", "https://www.threads.net/intent/post?text=" + enc(both)],
      ["X", "https://x.com/intent/post?text=" + enc(text) + "&url=" + enc(url)],
      ["Facebook", "https://www.facebook.com/sharer/sharer.php?u=" + enc(url)],
      ["LINE", "https://social-plugins.line.me/lineit/share?url=" + enc(url) + "&text=" + enc(text)],
      ["WhatsApp", "https://wa.me/?text=" + enc(both)],
      ["Telegram", "https://t.me/share/url?url=" + enc(url) + "&text=" + enc(text)],
      ["Reddit", "https://www.reddit.com/submit?url=" + enc(url) + "&title=" + enc(title)],
      ["LinkedIn", "https://www.linkedin.com/sharing/share-offsite/?url=" + enc(url)],
      ["Email", "mailto:?subject=" + enc(title) + "&body=" + enc(both)]
    ];
  }

  function copy(text, btn) {
    var done = function () { var t = btn.textContent; btn.textContent = "Copied"; setTimeout(function () { btn.textContent = t; }, 1600); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { fallback(text); done(); });
    } else { fallback(text); done(); }
  }
  function fallback(text) {
    var ta = document.createElement("textarea"); ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.opacity = "0";
    document.body.appendChild(ta); ta.select(); try { document.execCommand("copy"); } catch (e) {} ta.remove();
  }

  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt) e.textContent = txt; return e; }

  function buildRow(box, text, url, withExtras) {
    var row = el("div", "share-row");
    if (navigator.share) {
      var native = el("button", "share-btn share-main", "Share…");
      native.type = "button";
      native.onclick = function () { navigator.share({ title: title, text: text, url: url }).catch(function () {}); };
      row.appendChild(native);
    }
    var cp = el("button", "share-btn", "Copy link"); cp.type = "button";
    cp.onclick = function () { copy(url, cp); }; row.appendChild(cp);
    targets(text, url).forEach(function (t) {
      var a = el("a", "share-btn", t[0]); a.href = t[1];
      if (t[0] !== "Email") { a.target = "_blank"; a.rel = "noopener"; }
      if (t[0] === "Mastodon") a.addEventListener("click", function () { a.href = targets(text, url)[1][1]; });
      row.appendChild(a);
    });
    box.appendChild(row);
    if (!withExtras) return;
    var extra = el("div", "share-extra");
    var lab = el("label", "share-inst"); lab.htmlFor = box.id + "-inst"; lab.textContent = "Your Mastodon server";
    var inp = el("input"); inp.id = box.id + "-inst"; inp.placeholder = "mastodon.social"; inp.value = store("mastodon-instance") || "";
    inp.autocomplete = "off"; inp.spellcheck = false;
    inp.oninput = function () { store("mastodon-instance", inp.value.trim()); };
    lab.appendChild(inp); extra.appendChild(lab);
    var qrb = el("button", "share-btn", "QR code"); qrb.type = "button"; qrb.setAttribute("aria-expanded", "false");
    var qr = el("img", "share-qr"); qr.alt = "QR code for this page"; qr.hidden = true; qr.loading = "lazy"; qr.src = box.getAttribute("data-qr") || "qr.svg";
    qrb.onclick = function () { qr.hidden = !qr.hidden; qrb.setAttribute("aria-expanded", String(!qr.hidden)); };
    var card = el("a", "share-btn", "Download the card"); card.href = box.getAttribute("data-card") || "card.jpg"; card.download = card.href.split("/").pop();
    extra.appendChild(qrb); extra.appendChild(card); box.appendChild(extra); box.appendChild(qr);
  }

  document.querySelectorAll("[data-share]").forEach(function (box, i) {
    if (!box.id) box.id = "share-" + i;
    buildRow(box, blurb, page, box.hasAttribute("data-share-extras"));
  });

  /* A link button on every plan sheet, copying the address of that sheet. */
  document.querySelectorAll(".doc[id]").forEach(function (sheet) {
    var b = el("button", "sheet-link", "Copy link to this sheet"); b.type = "button";
    b.onclick = function () { copy(page + "#" + sheet.id, b); };
    sheet.appendChild(b);
  });

  /* Passage sharing: select words in the story and a small panel offers to send them, with a link that lands on them. */
  var main = document.querySelector("main");
  var pop = el("div", "passage"); pop.hidden = true; pop.setAttribute("role", "dialog"); pop.setAttribute("aria-label", "Share this passage");
  document.body.appendChild(pop);
  function hide() { pop.hidden = true; pop.innerHTML = ""; }
  function show() {
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed || sel.rangeCount === 0) return hide();
    var range = sel.getRangeAt(0);
    if (!main.contains(range.commonAncestorContainer) || pop.contains(range.commonAncestorContainer)) return;
    var words = sel.toString().replace(/\s+/g, " ").trim();
    if (words.length < 12) return hide();
    if (words.length > 260) words = words.slice(0, 257).replace(/\s\S*$/, "") + "…";
    var plain = words.replace(/…$/, "");
    var hit = plain.length > 80 ? frag(plain.slice(0, 40).replace(/\s\S*$/, "")) + "," + frag(plain.slice(-40).replace(/^\S*\s/, "")) : frag(plain);
    var url = page + "#:~:text=" + hit;
    var text = "“" + words + "” — " + title;
    pop.innerHTML = "";
    pop.appendChild(el("p", "passage-head", "Share this passage"));
    buildRow(pop, text, url, false);
    var cq = el("button", "share-btn", "Copy quote"); cq.type = "button";
    cq.onclick = function () { copy(text + "\n" + url, cq); };
    pop.querySelector(".share-row").appendChild(cq);
    var r = range.getBoundingClientRect();
    pop.hidden = false;
    var top = window.scrollY + r.bottom + 10, left = Math.max(12, Math.min(window.scrollX + r.left, window.scrollX + document.documentElement.clientWidth - pop.offsetWidth - 12));
    pop.style.top = top + "px"; pop.style.left = left + "px";
  }
  var t;
  document.addEventListener("selectionchange", function () { clearTimeout(t); t = setTimeout(show, 350); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") hide(); });
})();
