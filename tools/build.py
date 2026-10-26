#!/usr/bin/env python3
"""Build motdang's plan documents into one site: docs/ (GitHub Pages, motdang/business-plan).

Each document keeps its own source folder; this copies the public build of each into docs/<slug>/,
renders the full plan from src/business-plan.md, renders The Wheels from its slide files, and writes
the index. Run it again after any source changes, then publish with pr-push.
"""
import html, json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ogcards  # noqa: E402
P = ROOT.parent
DOCS = ROOT / "docs"
BASE = "https://motdang.github.io/business-plan/"
CARD_V = 1

COPIES = {  # slug: public build folder of each document
    "red-ant": P / "red-ant-plan-motdang/docs",
    "the-plan": P / "the-plan/docs",
}
WHEELS = P / "motdang-roadmap/wheels/deck/project"

DOCS_LIST = [  # newest first
    ("plan/", "The business plan", "14 October 2026",
     "The full plan: what is built, who pays, sixteen lines of revenue, year-one targets and the ask — ฿35M in three draws for 10% of revenue until 3×."),
    ("red-ant/", "The Red Ant Plan", "14 October 2026",
     "The same plan as toys you tap, in English, Thai, Burmese, Chinese and Khmer."),
    ("wheels/", "The Wheels", "14 October 2026",
     "The plan as a 16-slide deck: wheels within wheels, full of eyes."),
    ("the-plan/", "The Plan · แผนมดแดง", "27 September 2026",
     "The 23-slide pitch deck: Indra's net, robots as the audience, a baht-billion goal."),
]

BACK = ('<a href="{href}" style="position:fixed;right:12px;bottom:12px;z-index:2147483647;'
        'background:#e8b84a;color:#000;font:600 13px/1 system-ui,sans-serif;padding:9px 12px;'
        'border-radius:999px;text-decoration:none;box-shadow:0 2px 8px rgba(0,0,0,.35)">'
        '&larr; all plan documents</a>')

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500'
         '&family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">')

CSS = """
:root{--paper:#f4ecdc;--ink:#1d1a16;--quiet:#6b6257;--rule:#d8ccb4;--red:#b8261b;--gold:#e8b84a;--card:#fbf6ec}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#14110e;--ink:#efe6d6;--quiet:#a99d8b;--rule:#3a332b;--red:#e0574a;--gold:#e8b84a;--card:#1d1915}}
:root[data-theme="dark"]{--paper:#14110e;--ink:#efe6d6;--quiet:#a99d8b;--rule:#3a332b;--red:#e0574a;--gold:#e8b84a;--card:#1d1915}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 'IBM Plex Sans',system-ui,sans-serif}
main{max-width:780px;margin:0 auto;padding:40px 16px 96px}
h1,h2,h3{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;line-height:1.1}
h1{font-size:clamp(38px,8vw,60px);margin:0 0 8px}
h2{font-size:32px;margin:48px 0 12px;padding-top:12px;border-top:1px solid var(--rule)}
a{color:var(--red)}
.by{color:var(--quiet);margin:0 0 28px}
.tw{overflow-x:auto;margin:16px 0}
table{border-collapse:collapse;width:100%;font-size:15px}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--rule)}
th{font-weight:600;border-bottom:2px solid var(--ink)}
ul{padding-left:22px}
li{margin:6px 0}
.ant{display:inline-block;cursor:pointer;transition:transform .3s}
.ant.go{animation:scurry .9s ease-in-out}
@keyframes scurry{0%{transform:none}20%{transform:translateX(14px) rotate(8deg)}45%{transform:translateX(-10px) rotate(-10deg)}70%{transform:translateX(6px) rotate(4deg)}100%{transform:none}}
@media (prefers-reduced-motion:reduce){.ant.go{animation:none}}
footer{color:var(--quiet);font-size:14px;margin-top:64px;border-top:1px solid var(--rule);padding-top:16px}
"""

ANT = ('<svg class="ant" width="44" height="44" viewBox="0 0 64 64" role="button" aria-label="the red ant" tabindex="0">'
       '<g fill="var(--red)"><ellipse cx="18" cy="34" rx="10" ry="8"/><ellipse cx="33" cy="32" rx="6" ry="5"/>'
       '<circle cx="46" cy="28" r="7"/></g><g stroke="var(--red)" stroke-width="2.5" fill="none" stroke-linecap="round">'
       '<path d="M30 36l-6 12M33 37l1 13M36 36l7 11M30 28l-7-11M34 27l2-12M37 28l8-9M50 22l6-9M52 26l9-4"/></g></svg>')

ANT_JS = """<script>document.querySelectorAll('.ant').forEach(a=>{const f=()=>{a.classList.remove('go');void a.offsetWidth;a.classList.add('go')};a.addEventListener('click',f);a.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' ')f()})})</script>"""


def head(title, desc, url, extra=""):
    card = f"{BASE}card.jpg?v={CARD_V}"
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:type" content="website"><meta property="og:site_name" content="motdang">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{card}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The red ant beside the words: motdang business plan">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{card}">
<link rel="icon" href="{BASE}icon.svg">
{FONTS}<style>{CSS}{extra}</style></head>"""


# ---------- markdown, the few shapes the plan uses ----------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m[2]}">{m[1]}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", s)
    return s


def md(text):
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
        elif ln.startswith("<"):
            out.append(ln); i += 1
        elif ln.startswith("## "):
            t = ln[3:].strip()
            out.append(f'<h2 id="{re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")}">{inline(t)}</h2>'); i += 1
        elif ln.startswith("# "):
            out.append(f"<h1>{inline(ln[2:])}</h1>"); i += 1
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            hdr, body = rows[0], rows[2:]
            t = ['<div class="tw"><table>']
            if any(hdr):
                t.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in hdr) + "</tr></thead>")
            t.append("<tbody>" + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table></div>")
            out.append("".join(t))
        elif ln.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{inline(lines[i][2:])}</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "|", "- ", "<")):
                para.append(lines[i]); i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


ROADMAP = [
    ("Ankles", "now to April 2027",
     ["Payment switched on", "Remittance via a partner", "20 cities on the map", "10 data and bot buyers", "Border counters open"],
     "Locals use motdang more than Google, with better results"),
    ("Knees", "to October 2027",
     ["100 cities, 5 countries", "100,000 senders home", "20,000 Gold pages", "Payment rail, 2,000 firms", "12 businesses sold"],
     "Our own payment vertical, offered to other businesses"),
    ("River", "to October 2031",
     ["Licences of our own", "Hosting in three countries", "Cities on every continent", "Bot billing everywhere", "Merch worn to look cool"],
     "A speaker’s seat at Davos"),
]
ROAD_CSS = """
.road{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:20px 0 8px}
@media (max-width:640px){.road{grid-template-columns:1fr}}
.road>div{border:1px solid var(--rule);border-radius:10px;padding:14px;background:var(--card)}
.road h3{margin:0;font-size:26px}.road .d{color:var(--quiet);font-size:13px;margin:0 0 8px}
.road ul{list-style:none;padding:0;margin:0 0 12px;font-size:15px}.road li{margin:4px 0}
.road .g{border:2px solid var(--red);border-radius:8px;padding:10px;font-weight:600;font-size:15px}
.road .g span{display:block;font-weight:400;color:var(--quiet);font-size:12px}
.road-t{font-weight:600;margin:16px 0 0}.road-s{color:var(--quiet);font-size:14px;margin:2px 0 0}
"""


def roadmap_html():
    cols = "".join(
        f'<div><h3>{n}</h3><p class="d">{d}</p><ul>' + "".join(f"<li>{s}</li>" for s in steps)
        + f'</ul><div class="g"><span>NaN’s card</span>{html.escape(g)}</div></div>'
        for n, d, steps, g in ROADMAP)
    return ('<p class="road-t">World domination, itemised: ฿35M takes the corridor in year one</p>'
            '<p class="road-s">Ezekiel 47: waters to the ankles, then the knees, then a river.</p>'
            f'<div class="road">{cols}</div>')


def public_plan(t):
    """The public copy: the same plan, less what stays inside the team."""
    t = t.replace("Oct 14, 2026 · @Nan", "14 October 2026 · NaN")
    t = t.replace("(https://claude.ai/artifact/7FuS9tESMtoELfMgDBcWbk)", "(../red-ant/)")
    # Running-cost table itemises one person's pay; the total stays in the lead sentence.
    t = re.sub(r"\*\*Running cost today, monthly, October 2026\*\*\n\n(\|.*\n)+\n", "", t)
    # Internal note on how the terms were set; the offer is public on the Red Ant Plan.
    t = re.sub(r"\*\*Settled, 14 October 2026\.\*\*.*\n", "", t)
    t = re.sub(r"&#91;embedded content: road map[^\n]*\n", roadmap_html() + "\n", t)
    assert "claude.ai" not in t and "40,000" not in t and "embedded content" not in t, "private line left in"
    return t


def build_plan():
    src = (ROOT / "src/business-plan.md").read_text()
    body = md(public_plan(src))
    body = body.replace("<h1>motdang — business plan</h1>",
                        f'<h1>{ANT} motdang — business plan</h1>', 1)
    body = re.sub(r"<p>14 October 2026 · NaN</p>", '<p class="by">14 October 2026 · NaN</p>', body, 1)
    desc = "motdang.net Co., Ltd., Chiang Rai: what is built, who pays, sixteen lines of revenue, year-one targets and the ask."
    page = (head("motdang — business plan", desc, BASE + "plan/", ROAD_CSS)
            + f"<body><main>{body}<footer><a href=\"../\">All plan documents</a> · nan@motdang.net</footer></main>"
            + ANT_JS + "</body></html>")
    (DOCS / "plan").mkdir(parents=True, exist_ok=True)
    (DOCS / "plan/index.html").write_text(page)


def build_wheels():
    deck = json.loads((WHEELS / "deck.json").read_text())
    starts = {v["start"]: v["description"] for v in deck["sections"].values()}
    fonts = "".join(f'<link href="{f["href"]}" rel="stylesheet">' for f in deck["faces"].values())
    slides = []
    for n, sid in enumerate(deck["order"], 1):
        if sid in starts:
            slides.append(f'<h2 class="sec">{html.escape(starts[sid])}</h2>')
        s = (WHEELS / "slides" / f"{sid}.html").read_text()
        slides.append(f'<div class="frame" id="s{n}"><div class="stage">{s}</div></div>')
    css = """
body{background:#0b0d12;color:#e9e1cf}
main{max-width:1200px}
.frame{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;border-radius:6px;margin:0 0 18px;background:#10141c}
.stage{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}
.stage *{margin:0}
.stage aside{display:none}
.stage{line-height:normal;font-size:16px}
.stage>section{position:relative;width:1920px;height:1080px;overflow:hidden;box-sizing:border-box}
.sec{font-size:26px;color:#c9a23f;border:0;margin:36px 0 12px}
a{color:#e8b84a}
"""
    js = """<script>
const fit=()=>document.querySelectorAll('.frame').forEach(f=>{f.firstElementChild.style.transform=`scale(${f.clientWidth/1920})`});
addEventListener('resize',fit);fit();
const fr=[...document.querySelectorAll('.frame')];
addEventListener('keydown',e=>{const k=e.key;if(!['ArrowRight','ArrowLeft','PageDown','PageUp',' '].includes(k))return;
const y=scrollY+innerHeight*0.3;let i=fr.findIndex(f=>f.offsetTop+f.offsetHeight>y);if(i<0)i=fr.length-1;
i+= (k==='ArrowLeft'||k==='PageUp')?-1:1;i=Math.max(0,Math.min(fr.length-1,i));e.preventDefault();fr[i].scrollIntoView({behavior:'smooth',block:'center'})});
</script>"""
    desc = "motdang's plan as a 16-slide deck: the vision, the problem, the eight wheels, the tolls and the number."
    page = (head("The Wheels", desc, BASE + "wheels/", css).replace("</head>", fonts + "</head>")
            + '<body><main><h1>The Wheels</h1><p class="by">motdang, 14 October 2026 · arrow keys step through the slides</p>'
            + "\n".join(slides)
            + '<footer><a href="../">All plan documents</a></footer></main>' + js + "</body></html>")
    (DOCS / "wheels").mkdir(parents=True, exist_ok=True)
    (DOCS / "wheels/index.html").write_text(page)


def copy_docs():
    for slug, src in COPIES.items():
        dst = DOCS / slug
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".*", "*.bak*"))
        for f in dst.rglob("*.html"):
            if f.name == "card.html":
                continue
            t = f.read_text()
            if "</body>" in t and "all plan documents" not in t:
                up = "../" * (len(f.relative_to(DOCS).parts) - 1)
                t = t.replace("</body>", BACK.format(href=up) + "</body>", 1)
                f.write_text(t)


def build_index():
    items = "".join(
        f'<li><a href="{href}"><span class="t">{html.escape(t)}</span><span class="d">{d}</span>'
        f'<span class="l">{html.escape(line)}</span></a></li>'
        for href, t, d, line in DOCS_LIST)
    css = """
.docs{list-style:none;padding:0;margin:28px 0 0}
.docs li{margin:0 0 12px}
.docs a{display:block;text-decoration:none;color:var(--ink);background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:16px 18px;transition:border-color .2s,transform .2s}
.docs a:hover,.docs a:focus-visible{border-color:var(--red);transform:translateY(-1px)}
.docs .t{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;font-size:28px;line-height:1.1;color:var(--red)}
.docs .d{display:block;color:var(--quiet);font-size:13px;margin:4px 0 6px}
.docs .l{display:block;font-size:16px}
"""
    desc = "Every version of motdang's business plan in one place: the full plan, the Red Ant Plan, The Wheels and The Plan."
    page = (head("motdang business plan", desc, BASE, css)
            + f'<body><main><h1>{ANT} motdang business plan</h1>'
            + '<p class="by">motdang.net Co., Ltd. · 48–49 Thai Wiwat Alley, Chiang Rai · every version, newest first</p>'
            + f'<ul class="docs">{items}</ul>'
            + '<footer>nan@motdang.net</footer></main>' + ANT_JS + "</body></html>")
    (DOCS / "index.html").write_text(page)


ICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#f4ecdc"/>'
        '<g fill="#b8261b"><ellipse cx="18" cy="34" rx="10" ry="8"/><ellipse cx="33" cy="32" rx="6" ry="5"/><circle cx="46" cy="28" r="7"/></g>'
        '<g stroke="#b8261b" stroke-width="2.5" fill="none" stroke-linecap="round"><path d="M30 36l-6 12M33 37l1 13M36 36l7 11M30 28l-7-11M34 27l2-12M37 28l8-9M50 22l6-9M52 26l9-4"/></g></svg>')

if __name__ == "__main__":
    DOCS.mkdir(exist_ok=True)
    copy_docs()
    build_plan()
    build_wheels()
    build_index()
    ogcards.copy(ROOT, DOCS)
    ogcards.apply_tree(DOCS, BASE)
    (DOCS / "icon.svg").write_text(ICON)
    (DOCS / ".nojekyll").write_text("")
    print("built", sorted(p.name for p in DOCS.iterdir()))
