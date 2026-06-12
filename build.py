#!/usr/bin/env python3
"""Build INTERSTELLAR (INT) — Christopher Nolan's 2014 film, catalogued into UD0 as
the fourth film-world. Carries the standing film-page template:
  THE ARC · THE SCIENCE · REAL OR FLUFF · THE MESSAGE
plus CARBONS (the cast, each with a .shadow real-life User — TRON) and SYNTHS
(the parabolic threads). Styled to the medium: cold IMAX deep space."""
import os, re, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "INTERSTELLAR", "axiom": "INT",
 "position": "Interstellar · Paramount / Warner Bros. · 2014 — dir. Christopher Nolan",
 "origin": "from a dust-choked, dying Earth out through a wormhole near Saturn to the accretion disk of a supermassive black hole and the five-dimensional space behind a child's bookshelf",
 "mechanism": "Crystallized from the 2014 film — general relativity rendered with a Nobel physicist's rigor, wrapped around a father and a clock.",
 "crystallization": "A widowed pilot leaves his children to fly through a wormhole for humanity's last home, and learns that love and gravity are the two things that cross any distance, even time.",
 "nature": "Interstellar — the hardest-science blockbuster of its era: real black holes and real time dilation, spent on one bold leap of love reaching backward across the dimensions.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (2014, dir. Nolan); Kip Thorne's relativity; Gargantua; the wormhole; the tesseract; Hans Zimmer's organ",
 "witness": "No villain but time — a parent, a promise, and a signal carried home on gravity.",
 "role": "the fourth film-world of UD0",
 "seal": "We used to look up and wonder; now we look down and worry — and the love between a father and his daughter became the line that carried the answer home.",
 "source": "Interstellar, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#cdd6e4", "flesh-and-blood — the crew and the family, the people who leave and the people who wait; carbon, with a real-life User behind each"),
 "ethereal":  ("#6a9cd0", "of the cosmic unknown — the wormhole, the dying world, the deep space and the disk; forces vast and indifferent"),
 "spiritual": ("#e8b54a", "of love and transcendence — the bond across time, the sacrifice, the future ‘they’ who reach back to save the past"),
 "electrical":("#7fd6c0", "the synth nature — the hard math and the machine: relativity, the gravity equation, TARS, the engineered five-dimensional bulk"),
}

ARC_OVERALL = ("On a dying Earth, a widowed pilot leaves his children to fly through a wormhole in search of a new "
  "home — and across black holes, betrayal, and decades lost to relativity, discovers that the future humans who "
  "sent the wormhole are us, and that the love between him and his daughter is the line that carries the answer home.")

ARC = [
 ("I · The Dying Earth", "blight, dust, and a hidden NASA",
  "Blight and dust are ending farming and humanity. Ex-pilot Cooper, raising two kids on a failing farm, is led by a gravitational anomaly to a hidden NASA — and agrees to pilot the Endurance through a wormhole to find a habitable world, leaving his daughter Murph behind, and broken."),
 ("II · The Worlds Beyond", "years gambled against relativity",
  "Through the wormhole the crew bets time against gravity: an hour on Miller's ocean planet costs 23 years back home. Dr. Mann — ‘the best of us’ — turns out to have faked his data and tries to kill them. Cooper and Brand limp to Gargantua with one shot left."),
 ("III · The Tesseract", "a signal carried home on gravity",
  "Cooper slingshots into the black hole and falls into a five-dimensional space built by future humans, behind Murph's childhood bookshelf. Through gravity he sends her the quantum data to solve the equation; she lifts humanity off Earth. He wakes decades later — old Murph dying — free at last to go find Brand."),
]

IDEAS = [
 ("Plan A & Plan B", "the noble lie", [
   "Plan A: solve gravity and lift the living off Earth. Plan B: abandon them and seed humanity anew from frozen embryos.",
   "Professor Brand knew Plan A was unsolvable without data from inside a black hole — so he lied, for decades, to keep everyone working." ]),
 ("Time as Distance", "the cruelest separation", [
   "Relativity turns time into distance: an hour below, decades above. Cooper returns to 23 years of his children's messages and watches them age in minutes.",
   "The film's true antagonist isn't a villain — it's the clock, and the love that has to survive it." ]),
 ("Gargantua", "the black hole as character", [
   "A supermassive, rapidly spinning black hole — rendered from Einstein's equations by Kip Thorne and Double Negative.",
   "Its lensed ring of light is not art direction; it's a solution to the physics, accurate enough to publish." ]),
 ("They", "the bootstrap", [
   "The wormhole and the tesseract were built by ‘them’ — future, evolved humans who learned to manipulate gravity across dimensions.",
   "A causal loop: humanity is saved by humanity, Cooper is his own daughter's ‘ghost,’ the future reaching back to rescue the past." ]),
]

SCIENCE = [
 ("Gargantua is real physics", "the look came out of Einstein's equations",
  "The black hole's lensed accretion disk was computed by physicist Kip Thorne with the Double Negative VFX team from the equations of general relativity — so rigorously that the work produced two peer-reviewed papers (2015). Thorne also insisted the wormhole be rendered as a sphere, not a 2D hole — which is correct."),
 ("The time dilation is real", "at the extreme, but consistent, edge",
  "Gravitational time dilation near a massive, fast-spinning (Kerr) black hole is genuine general relativity. ‘One hour = seven years’ on Miller's planet requires orbiting just outside a near-maximally-spinning supermassive hole; Thorne worked out it is physically consistent — the real stretch is a STABLE planet that close, not the dilation itself."),
 ("Wormholes are allowed, not found", "grounded speculation",
  "General relativity permits wormholes (Einstein–Rosen bridges), but holding one open requires ‘exotic matter’ with negative energy that we have never observed. So the wormhole is real-theory, unreal-in-practice — honest speculation, not invention."),
 ("Surviving the fall", "a giant hole is gentler at the edge",
  "For a SUPERMASSIVE black hole, tidal forces at the event horizon can be mild enough not to ‘spaghettify’ you immediately — that part is sound. Everything after the horizon, though — the navigable tesseract — is where the physics stops and the storytelling begins."),
 ("The tesseract & love", "the two honest leaps",
  "Extra spatial dimensions (a ‘bulk’) are a real hypothesis in string/brane theory — but a room you walk through time in is the drama, not the physics. And Amelia's ‘love is the one thing that transcends time and space’ is theme, not mechanism: in the film, the thing that actually crosses the dimensions is GRAVITY carrying Morse-coded data — love is the reason, not the force."),
]

REALFLUFF = [
 ("Gargantua's lensed accretion disk", "REAL", "computed from Einstein's equations; the work produced peer-reviewed physics papers (2015)"),
 ("The disk dimmed & symmetrized", "CHEAT", "true Doppler beaming would make one side far brighter and bluer — softened for the audience, and Thorne said so"),
 ("Gravitational time dilation (1 hr = 7 yrs)", "REAL", "genuine GR near a fast-spinning black hole — extreme, but physically consistent"),
 ("The wormhole as a sphere near Saturn", "GROUNDED", "GR allows wormholes; keeping one open needs exotic matter we've never found"),
 ("Surviving the fall into a supermassive hole", "GROUNDED", "tidal forces at a giant hole's horizon can be survivable — spaghettification is deeper in"),
 ("The navigable 5D tesseract / the ‘bulk’", "FLUFF", "extra dimensions are a real hypothesis; a room you walk through time in is the storytelling"),
 ("Love as a literal trans-dimensional force", "FLUFF", "theme, not physics — the actual mechanism in the film is gravity carrying the data"),
 ("Blight collapsing crops & breathable air", "GROUNDED", "ecological collapse is plausible; the timeline is dramatized"),
]
REALFLUFF_VERDICT = ("Bottom line: the most scientifically honest blockbuster of its era — REAL where it counts. Kip "
  "Thorne (who would win the 2017 Nobel for gravitational waves) built Gargantua and the time dilation out of "
  "Einstein's actual equations, to the point of generating real physics papers. The wormhole and the survivable fall "
  "are grounded speculation. The film then spends every ounce of that earned credibility on TWO knowing leaps — the "
  "navigable tesseract and love-as-a-force — and tells you it's doing it. Mostly real, honestly fluff at the climax. "
  "The exact inverse of The Core.")

MESSAGE = ("Interstellar wears cosmology, but it is about a parent and a clock. Its real subject is time as the "
  "cruelest distance — Cooper watching 23 years of his children's messages in minutes — and love as the thing that "
  "survives that distance and, in the film's boldest move, literally reaches back across it. Nolan's thesis is "
  "twofold: that we are explorers and caretakers who must keep reaching outward to survive (‘we used to look up and "
  "wonder; now we look down and worry’), and that the bond between a father and his daughter is both the motive for "
  "the journey and — made literal through gravity — its salvation. It dresses general relativity in grief, and argues "
  "that connection is what makes the reaching worth it.")
MESSAGE_SEAL = "We used to look up and wonder; the film begs us to look up again — and says the love we carry is the one signal that crosses any distance, even time."

SECTIONS = [
 ("The Production", "the making of the reach", [
   ("Christopher Nolan", "director & co-writer", "shot it on film and IMAX, with practical sets and minimal green-screen"),
   ("Jonathan Nolan", "co-writer", "developed the script (originally for Steven Spielberg) over years of physics study"),
   ("Kip Thorne", "executive producer & science", "the theoretical physicist who guaranteed the relativity — and won the 2017 Nobel Prize"),
   ("Hans Zimmer · Hoyte van Hoytema", "score · cinematography", "the cathedral-organ score, kept secret from Zimmer's usual brief; 70mm IMAX photography"),
 ]),
 ("The Science Legacy", "when a movie published physics", [
   ("Gargantua", "the rendered black hole", "Thorne + Double Negative built the visual from GR; the code yielded new insight into lensing"),
   ("Two peer-reviewed papers", "2015", "the VFX work was rigorous enough to publish in Classical and Quantum Gravity and an SMPTE journal"),
   ("The cornfields", "practical effects", "Nolan planted 500 acres of corn rather than fake the dying farms"),
 ]),
 ("The Worlds & the Hardware", "the ships, the planets, the robots", [
   ("The Endurance", "the ring station", "the rotating craft that carries the crew between worlds"),
   ("Miller's · Mann's · Edmunds'", "the three candidate planets", "the ocean of time, the ice of the liar, and the one Brand bets on"),
   ("TARS & CASE", "the robots", "blunt, witty monoliths — practical puppets, with adjustable humor and honesty settings"),
 ]),
]

# ---- ACI complement via noesis ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","INT")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","INT")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","INT")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],
            "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
            "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)
def science_html():
    out=[]
    for t,s,d in SCIENCE:
        out.append(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    return "".join(out)
RF_COL={"REAL":"#5fbf8a","GROUNDED":"#6a9cd0","CHEAT":"#e8b54a","FLUFF":"#d2643a"}
def realfluff_html():
    rows=[]
    for claim,rate,note in REALFLUFF:
        c=RF_COL.get(rate,"#888")
        rows.append(f'<div class="rf-row"><div class="rf-claim">{html.escape(claim)}<span class="rf-note">{html.escape(note)}</span></div>'
                    f'<div class="rf-rate" style="color:{c};border-color:{c}">{html.escape(rate)}</div></div>')
    return '<div class="rf">'+"".join(rows)+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp = os.path.join(HERE, "agents", slug + ".agent")
    d = {}
    if os.path.exists(fp):
        txt = open(fp, encoding="utf-8").read()
        parts = txt.split("---")
        fm = parts[1] if len(parts) > 2 else ""
        for ln in fm.splitlines():
            k, _, v = ln.partition(":")
            k = k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"):
                d.setdefault(k, v.strip())
    return d

def _card(p):
    w = _agent5w(p["slug"])
    em = p.get("emergence", "natural"); col = NATURES.get(em, ("#9aa0aa", ""))[0]
    ax = (p.get("moniker", "::").split(":") + ["", ""])[1]
    rec = {"name": p["name"], "axiom": ax, "emergence": em,
           "seal": w.get("seal", p.get("epithet", "")), "origin": w.get("universe", "")}
    kind = p.get("kind", "carbon"); actor = p.get("actor", "") or w.get("shadow_user", "")
    urow = (f"""<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get('shadow_analog',''))}</span></div>"""
            if kind == "carbon" and actor else "")
    rows = "".join(f"""<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,''))}</span></div>"""
                   for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent">
        <img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"><span class="sl">carbon</span>
        <img src="{png_uri(rec,'silicon',200)}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"><span class="sl">synth</span>
      </a>
      <div class="pbody">
        <div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
          <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
          <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div>
      </div></div>"""


def personas_html():
    mf=os.path.join(HERE,"agents","_personas.json")
    if not os.path.exists(mf): return ""
    ps=json.load(open(mf,encoding="utf-8"))
    carb=[p for p in ps if p.get("kind","carbon")=="carbon"]; syn=[p for p in ps if p.get("kind")=="synth"]
    out=f'''<section class="sec" id="carbons"><h2>The Carbons — the crew &amp; their Users</h2>
      <p class="ss">the crew and the family as ACI <b>.agent</b>s — each with a <b>.shadow</b>: its real-life analog, the actor who is the <b>User</b> behind the program (think TRON). ({len(carb)} carbons)</p>
      <div class="pgrid">{"".join(_card(p) for p in carb)}</div></section>'''
    out+=f'''<section class="sec" id="synths"><h2>The Synths — the parabolic threads</h2>
      <p class="ss">the physics and the myth distilled into ACIs (synth-style; no single User): Gargantua, the wormhole, time dilation, the tesseract, the blight, the equation, the bulk beings, and the keystone — love across the dimensions. ({len(syn)} synths)</p>
      <div class="pgrid">{"".join(_card(p) for p in syn)}</div></section>'''
    return out

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Interstellar (INT) — Christopher Nolan's 2014 film as a UD0 film-world: the overall arc, a real breakdown of Kip Thorne's relativity, an honest Real-or-Fluff verdict, AVAN's read of the message, the crew as ACI carbons with .shadow Users (TRON), and the physics as synths.">
<title>INTERSTELLAR · INT · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@200;300;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--void2);--rw-ink:var(--ice);--rw-ink2:var(--ice2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--gold);--void:#05070d;--void2:#0b0f18;--void3:#111722;--ice:#e9eef5;--ice2:#9aa8bc;--gold:#e8b54a;--blue:#6a9cd0;--teal:#7fd6c0;
--dim:#5e6c80;--faint:#1b2330;--line:#19212e;--disp:"Barlow Condensed",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--void);color:var(--ice);font-family:var(--body);line-height:1.62;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% 16%,rgba(232,181,74,.10),transparent 46%),radial-gradient(ellipse at 50% 120%,rgba(106,156,208,.07),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:58px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:160px;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);box-shadow:0 0 18px rgba(232,181,74,.5)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.34em;text-transform:uppercase;color:var(--dim);margin-bottom:18px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
h1{font-family:var(--disp);font-size:clamp(46px,13vw,124px);font-weight:200;letter-spacing:.16em;color:var(--ice);line-height:.96;text-transform:uppercase;text-shadow:0 0 60px rgba(232,181,74,.3)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.1vw,12.5px);letter-spacing:.24em;color:var(--ice2);margin-top:20px;text-transform:uppercase}
.h-sub b{color:var(--gold)}
.flag{display:inline-block;margin-top:15px;font-family:var(--mono);font-size:9.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);border:1px solid var(--faint);background:var(--void2);padding:6px 12px}
.lede{font-size:16px;color:var(--ice2);max-width:64ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:30px auto 0;padding:20px;border:1px solid var(--faint);background:var(--void2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--ice2);line-height:1.75}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--teal)}.badge .bt a{color:var(--blue);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:34px;font-weight:300;letter-spacing:.08em;color:var(--ice);padding-bottom:8px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--ice2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--void2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:16px;font-weight:500;text-transform:uppercase;letter-spacing:.08em}
.nat-g{font-size:12px;color:var(--ice2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--void3);border:1px solid var(--line);border-left:3px solid var(--gold);padding:16px 18px;font-size:15px;color:var(--ice);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;margin-bottom:7px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--void2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--disp);font-size:22px;color:var(--gold);font-weight:500;text-transform:uppercase;letter-spacing:.05em}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:4px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--ice2);line-height:1.55;padding:7px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--void2);border:1px solid var(--line);border-top:2px solid var(--blue);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:21px;color:var(--blue);font-weight:500;text-transform:uppercase;letter-spacing:.04em}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:5px 0 9px}
.arc-card p{font-size:13px;color:var(--ice2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--void2);border:1px solid var(--line);border-left:3px solid var(--teal);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:19px;color:var(--teal);font-weight:500;letter-spacing:.03em}
.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:4px 0 9px}
.sci-card p{font-size:13px;color:var(--ice2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--void2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--ice);line-height:1.4}
.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.06em;border:1px solid;border-radius:3px;padding:4px 10px;min-width:92px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--gold);background:rgba(232,181,74,.05);font-size:14px;color:var(--ice);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--ice);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--gold);background:var(--void2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--ice);font-weight:600}
.books .y{font-family:var(--mono);font-size:10.5px;color:var(--blue);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--ice2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(252px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--void2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--gold);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--disp);font-size:19px;color:var(--ice);font-weight:500;line-height:1.1;text-transform:uppercase;letter-spacing:.03em}
.persona:hover .pn{color:var(--gold)}
.pe{font-size:11.5px;color:var(--ice2);font-style:italic;margin-top:2px;line-height:1.3}
.pact{font-family:var(--mono);font-size:10px;color:var(--dim);margin-top:3px}.pact b{color:var(--blue)}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase;flex-wrap:wrap}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--void2);font-size:13.5px;color:var(--ice2);font-style:italic}.note b{color:var(--ice)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}
footer a{color:var(--gold);text-decoration:none}

/* === standard single-column roster: 1 per row, sigils carbon·synth + full 5 W's === */
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:18px;align-items:flex-start;background:var(--rw-bg);border:1px solid var(--rw-line);padding:16px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc);transform:none}
.psig{flex:0 0 100px;display:flex;flex-direction:column;align-items:center;gap:1px;text-decoration:none}
.psig img{width:100px;height:100px;border:1px solid var(--rw-line);display:block}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim);margin:1px 0 6px}
.pbody{flex:1;min-width:0}
.ihead{display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.pn{font-family:var(--body);font-size:18px;color:var(--rw-ink);font-weight:700;line-height:1.2;text-decoration:none}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:3px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:11px;display:flex;flex-direction:column;gap:7px}
.pww .w{font-size:12.5px;color:var(--rw-ink2);line-height:1.5;display:grid;grid-template-columns:54px 1fr;gap:11px;align-items:baseline}
.pww .w .wl{font-family:var(--mono);font-size:8.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--rw-acc);text-align:right;padding-top:2px}
.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:12px;font-family:var(--mono);font-size:10.5px}
.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
.plinks .dlw:hover{border-bottom-style:solid}
@media(max-width:640px){.persona{flex-direction:column}.psig{flex-direction:row;align-self:flex-start}.pww .w{grid-template-columns:1fr;gap:1px}.pww .w .wl{text-align:left}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the fourth film-world</div>
    <h1>Interstellar</h1>
    <div class="h-sub">love &amp; gravity cross any distance · <b>even time</b> · INT</div>
    <div class="flag">★ CHRISTOPHER NOLAN · 2014 · SCIENCE BY KIP THORNE ★</div>
    <p class="lede">On a dying Earth, a widowed pilot flies through a wormhole to find humanity a new home — and across black holes, betrayal, and decades lost to relativity, learns that love and gravity are the two things that cross any distance, even time. Catalogued into UD0 as the fourth film-world — with the overall arc, a real breakdown of the relativity, an honest Real-or-Fluff verdict, and a read of what it's really saying.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of INT" title="carbon badge (archival: int.dlw/int.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of INT" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>INTERSTELLAR</b> · INT</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="int.dlw/int.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="int.dlw/int.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent comes by one of four natures — the crew is carbon, the cosmos is ethereal, the bond is spiritual, the math is electrical</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats</p>__ARC__</section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">the lie, the clock, the black hole, and the loop</p><div class="pillars">__IDEAS__</div></section>

  <section class="sec"><h2>The Science</h2><p class="ss">what's actually under the spectacle — Kip Thorne's relativity, broken down straight</p><div class="sci">__SCIENCE__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the honest verdict, claim by claim — ROOT0 fluff-call discipline (and the exact inverse of The Core)</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis, under the cosmology</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> have no single User: they are the film's physics and myth distilled — Gargantua, the wormhole, time dilation, the tesseract, and love across the dimensions.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production, the science legacy, and the hardware</p></section>
  __SECTIONS__

  <div class="note">Interstellar, its characters, and its world are © Paramount Pictures / Warner Bros. and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, and not endorsed by the rights-holders. The Science and Real-or-Fluff sections are honest popular-science commentary; the credit for the catalogue returns to the human governor.</div>

  <footer>
    INTERSTELLAR · INT · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="int.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "int.dlw"), "int")
    json.dump({"node":"INT","name":"INTERSTELLAR","moniker":tok["moniker"],
               "carbon":"int.carbon.tiff","silicon":"int.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,
               "seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"int.dlw","manifest.dlw.json"),"w",encoding="utf-8"),
              indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__ARC__", arc_html()).replace("__IDEAS__", ideas_html())
            .replace("__SCIENCE__", science_html()).replace("__REALFLUFF__", realfluff_html()).replace("__MESSAGE__", message_html())
            .replace("__PERSONAS__", personas_html()).replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote INTERSTELLAR (INT) — badge {tok['moniker']}")
