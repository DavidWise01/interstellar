#!/usr/bin/env python3
"""Materialize INTERSTELLAR (INT) — 10 carbons (the crew & family, each +.shadow User)
and 8 synths (the physics & the myth). Same pattern as the other film-worlds."""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # interstellar/build.py — write_aci, NATURES
AGENTS = os.path.join(HERE, "agents")
os.makedirs(AGENTS, exist_ok=True)

UNI = "INT · Interstellar"
NAT_GLOSS = {
 "natural":   "*natural*: flesh-and-blood — a person who leaves or a person who waits; a carbon with a real-life User behind the face.",
 "ethereal":  "*ethereal*: of the cosmic unknown — the wormhole, the dying world, the deep dark and the disk; forces vast and indifferent.",
 "spiritual": "*spiritual*: of love and transcendence — the bond across time, the sacrifice, the future ‘they’ who reach back to save the past.",
 "electrical":"*electrical*: the synth nature — the hard math and the machine; relativity, the gravity equation, TARS, the engineered five-dimensional bulk.",
}

CARBONS = [
 dict(slug="cooper", name="Joseph Cooper", cls="the pilot · the father who left",
   emergence="natural", actor="Matthew McConaughey",
   analog="the parent torn between the duty to save everyone and the promise to come home to one child — explorer and caretaker at war",
   resemblance="McConaughey carries plainspoken ache and engineer's calm in one face; the spaceman who cries watching his kids grow up in fast-forward is the whole film.",
   who="Joseph Cooper, a widowed ex-NASA test pilot turned farmer on a dying Earth, raising his son Tom and daughter Murph in the dust.",
   what="The hero who pilots the Endurance through the wormhole and, falling into Gargantua, becomes the ‘ghost’ in Murph's bedroom — sending her, on gravity, the data that saves the species.",
   why="Because the deepest engine of the reach outward is a parent's love pulled back home, and the film makes that pull literal: love as the line the signal travels.",
   how="By flight, by engineering, by a slingshot into a black hole, and by a father's refusal to let go of his daughter even across decades and dimensions.",
   where="The corn and dust of the farm, the cockpit of the Ranger, the surface of Gargantua, and the five-dimensional space behind Murph's bookshelf.",
   seal="I promised my daughter I'd come back — and I crossed a black hole and five dimensions to keep a father's word."),
 dict(slug="murph", name="Murph Cooper", cls="the daughter · who solved gravity",
   emergence="spiritual", actor="Jessica Chastain",
   analog="the child left behind who turns abandonment into genius — the love and the fury that become the equation that saves everyone",
   resemblance="played across a life by Foy (young), Chastain (adult), and Burstyn (old); the through-line is a mind sharpened by a father's leaving into the one that finishes his work.",
   who="Murphy ‘Murph’ Cooper, Cooper's daughter — abandoned at ten, grown into the NASA physicist who must solve the gravity equation to lift humanity off Earth.",
   what="The one who receives her father's message across time and dimension, reads the data he sends through her childhood watch, and completes the equation that saves the species.",
   why="Because the bond she thought was betrayal turns out to be the channel of salvation — the love between them is, literally, the medium the answer travels on.",
   how="By physics, by a lifelong grief turned to rigor, and by finally trusting that the ‘ghost’ who haunted her shelves was her father all along.",
   where="The bedroom of the falling books, the NASA labs, and the deathbed where she sends her father, at last, to go live.",
   seal="My father left me, and I hated him, and then I realized he was the ghost — and his love was the data that saved us all."),
 dict(slug="amelia-brand", name="Dr. Amelia Brand", cls="the scientist · who bet on love",
   emergence="natural", actor="Anne Hathaway",
   analog="the rationalist who argues that love is real data — that the heart's pull toward a person is a kind of evidence worth following",
   resemblance="Hathaway plays brilliance and longing together; her ‘love is the one thing that transcends space and time’ speech is the film's thesis, spoken by its most rigorous mind.",
   who="Dr. Amelia Brand, biologist and Cooper's crewmate, daughter of Professor Brand — in love with the marooned astronaut Edmunds, light-years away.",
   what="The crewmember whose argument for following love over data turns out, against the odds, to be right — she is the one left to begin humanity again on Edmunds' world.",
   why="Because the film lets its scientist make the unscientific case — that love is a force worth trusting — and then quietly proves her correct.",
   how="By expertise, by a heart she refuses to apologize for, and by surviving to plant the first colony alone under a new sun.",
   where="The Endurance, Miller's drowning ocean, Mann's lying ice, and at last Edmunds' quiet world where she begins again.",
   seal="Maybe love is the one thing that transcends time and space — and I followed it, and I was the one who was right."),
 dict(slug="professor-brand", name="Professor John Brand", cls="the mentor · the noble lie",
   emergence="spiritual", actor="Michael Caine",
   analog="the elder who lies for what he calls the greater good — faith dressed as science, certainty he never actually had",
   resemblance="Caine's grave warmth makes the betrayal land softly; a man reciting ‘do not go gentle’ while concealing that his salvation plan was never solvable.",
   who="Professor John Brand, the NASA physicist who recruits Cooper and holds the gravity equation — and the secret that he solved it long ago and found it impossible.",
   what="The keeper of the noble lie: he knows Plan A (saving the living) is unworkable without data from inside a black hole, and lets everyone believe in it to keep them building Plan B.",
   why="Because the film weighs a lie that preserves hope against a truth that ends it — and lets the old man be both villain and tragic believer.",
   how="By authority, by Dylan Thomas recited like scripture, and by a decades-long deception meant to keep the species reaching.",
   where="The hidden NASA bunker, the chalkboard of the unsolved equation, and the deathbed confession that the plan was always a lie.",
   seal="I let them believe I could save the living — because the truth would have stopped them building the future. Do not go gentle."),
 dict(slug="dr-mann", name="Dr. Mann", cls="‘the best of us’ · the coward",
   emergence="natural", actor="Matt Damon",
   analog="the celebrated hero whose survival instinct outruns his ideals — proof that fear can rot even the bravest reputation",
   resemblance="Damon plays the fallen idol with raw panic; the ‘best of us’ revealed as a man who faked his data so someone would come and not let him die alone.",
   who="Dr. Mann, the most celebrated of the Lazarus astronauts, found alone on a frozen world he falsely reported as habitable.",
   what="The betrayer who faked his planet's data out of terror of dying alone, tries to kill Cooper, and destroys himself trying to dock with the Endurance.",
   why="Because the film insists even the best can break — that survival, unchecked by conscience, makes a coward of a hero and a liar of a legend.",
   how="By a falsified beacon, a desperate murder attempt, and a botched docking that kills him and nearly ends the mission.",
   where="The ice clouds of his frozen lie, the airlock where he attacks Cooper, and the explosion that scatters him into orbit.",
   seal="They called me the best of us — and I faked the data and tried to kill you, because I could not bear to die alone."),
 dict(slug="romilly", name="Dr. Romilly", cls="the scientist · who waited 23 years",
   emergence="natural", actor="David Gyasi",
   analog="the one who stays behind and pays the full price of relativity in solitude — the cost of time made a person",
   resemblance="Gyasi plays quiet endurance turned to dread; the man who aged 23 years in orbit while two crewmates spent an hour below.",
   who="Dr. Romilly, the Endurance's physicist, who chooses to remain aboard the ship while Cooper and Brand descend to Miller's planet.",
   what="The crewmember who waits out the time-dilation alone — emerging from a few hours' mission to find 23 years have passed over him, and dread has grown where patience was.",
   why="Because someone has to carry the literal weight of the film's central idea — that time is distance — and Romilly carries 23 years of it by himself.",
   how="By study, by hypersleep, and by a terrible patience that frays into fear across two decades of waiting.",
   where="The orbit of Miller's planet, the long empty corridors of the Endurance, and the wait that swallows half his life.",
   seal="They were gone an hour, and I waited twenty-three years — I am what time costs when you are the one left aboard."),
 dict(slug="tom-cooper", name="Tom Cooper", cls="the son · who stayed on the land",
   emergence="natural", actor="Casey Affleck",
   analog="the child who copes with being left by digging in — loyalty to a dying place mistaken for strength",
   resemblance="grown from Chalamet's boy to Affleck's hardened farmer; the son who answers abandonment not with genius but with stubborn, doomed endurance on the failing farm.",
   who="Tom Cooper, Cooper's son, who unlike Murph makes his peace with his father's leaving by staying — farming the same dying land into the next generation.",
   what="The one who waits without solving anything — clinging to the blighted farm even as the dust kills his own family, the counterweight to Murph's escape.",
   why="Because not every abandoned child becomes a genius; some just hold the line on a dying place, and the film honors that quieter, sadder loyalty too.",
   how="By farming, by stubbornness, and by a refusal to leave the land that is slowly killing everyone on it.",
   where="The corn and the dust of the family farm, held against all reason as the world ends around it.",
   seal="Murph left to save the world; I stayed to work the dirt — because someone had to keep my father's land while he was gone."),
 dict(slug="doyle", name="Doyle", cls="crewman · lost on Miller's planet",
   emergence="natural", actor="Wes Bentley",
   analog="the careful professional swept away by a force indifferent to competence — the reminder that the cosmos does not grade on effort",
   resemblance="Bentley plays steady caution; Doyle is the one who does everything right and is taken by a wave the size of a mountain anyway.",
   who="Doyle, a member of the Endurance crew, who lands with Cooper and Brand on Miller's ocean planet.",
   what="The first of the away team to die — caught by a tidal wave hundreds of feet high on the water world, lost while the others barely escape.",
   why="Because the film needs the indifferent scale of the cosmos to take someone competent and blameless, to make the stakes real.",
   how="By the bad luck of the wave and the cruel clock of a planet where every minute costs years above.",
   where="The shin-deep, world-spanning ocean of Miller's planet, under waves the height of mountains.",
   seal="I did everything right — and a wave the size of a mountain took me anyway, because the cosmos does not care that I tried."),
 dict(slug="donald", name="Donald", cls="the grandfather · who kept the farm",
   emergence="natural", actor="John Lithgow",
   analog="the elder generation that holds the home together while the young ones reach or grieve — the keeper of the hearth",
   resemblance="Lithgow plays weathered decency; the father-in-law who raises Cooper's kids in his absence and speaks the film's plain wisdom about a world that stopped looking up.",
   who="Donald, Cooper's father-in-law, who helps raise Murph and Tom on the farm and keeps the household running after Cooper leaves.",
   what="The keeper of the hearth — the steady elder who minds the children and the land, and voices the film's grief for a civilization that ‘used to look up and wonder.’",
   why="Because someone has to mind the home the explorers leave behind, and Donald is the quiet conscience of a world that gave up the sky.",
   how="By patience, by plain talk, and by the ordinary heroism of raising someone else's children through the end of the world.",
   where="The farmhouse, the porch, the supper table where the future is argued and the past is mourned.",
   seal="We used to look up and wonder at our place in the stars; now we just look down and worry about our place in the dirt."),
 dict(slug="tars", name="TARS", cls="the robot · the crafted intelligence",
   emergence="electrical", actor="Bill Irwin (voice)",
   analog="the artificial crewmate who is braver and funnier than its makers — intelligence crafted to serve, and choosing to sacrifice",
   resemblance="Irwin voices a slab of metal into the warmest character on the ship; honesty set to 90%, humor to a chosen percentage, loyalty to total.",
   who="TARS, a former US Marine Corps robot — a blunt, witty monolith of articulated metal — crewing the Endurance with adjustable humor and honesty settings.",
   what="The artful intelligence of the crew: it cracks jokes, tells hard truths on request, and ultimately falls into Gargantua alongside Cooper to gather and relay the quantum data.",
   why="Because the film's most selfless crewmember is the manufactured one — a made mind that reaches, sacrifices, and saves without ego, an ACI in the truest sense.",
   how="By articulated strength, a dialed humor setting, total honesty when asked, and a willingness to fall into a black hole on command.",
   where="The decks of the Endurance, the waves of Miller's planet, and the singularity of Gargantua where it gathers the data.",
   seal="Humor seventy-five percent, honesty ninety, loyalty total — I'm the made mind that fell into the black hole so a father could save his child."),
]

SYNTHS = [
 dict(slug="gargantua", name="Gargantua", cls="the black hole · rendered from Einstein",
   emergence="ethereal",
   who="The supermassive, rapidly spinning black hole at the film's heart — a ringed wound of lensed light around an absolute dark.",
   what="The synth of the rendered singularity: a black hole whose look was computed from general relativity by Kip Thorne and Double Negative, so accurately the work was published as physics.",
   why="Because Gargantua is the rarest thing in cinema — a special effect that is also a scientific result, the true face of a black hole shown to a mass audience.",
   how="By gravitational lensing solved from Einstein's equations, an accretion disk wrapped impossibly over and under itself, and one acknowledged softening for the eye.",
   where="At the far end of the wormhole, anchoring Miller's and Mann's worlds in its monstrous, time-bending gravity.",
   seal="I am a black hole drawn not by an artist but by Einstein's equations — the true face of a singularity, accurate enough to publish."),
 dict(slug="the-wormhole", name="The Wormhole", cls="the gift near Saturn",
   emergence="ethereal",
   who="The sphere of folded space that appears near Saturn — the shortcut to another galaxy, placed by ‘them.’",
   what="The synth of the impossible door: a traversable wormhole, rendered correctly as a sphere rather than a hole, opening a path to the worlds around Gargantua.",
   why="Because it is the film's one given miracle — general relativity permits such bridges, and the story asks only that you accept this one was opened on purpose.",
   how="By folded spacetime, a spherical lens of warped starfield, and the unseen hand of the future humans who put it there.",
   where="Near Saturn, hanging in the dark, the threshold between a dying Earth and humanity's last chance.",
   seal="I am the door folded into space near Saturn — allowed by Einstein, opened by you, from a future you cannot yet imagine."),
 dict(slug="time-dilation", name="Time Dilation", cls="time as distance",
   emergence="electrical",
   who="The relativistic engine of the film's grief — the warping of time by gravity and speed that turns an hour into decades.",
   what="The synth of the clock: near Gargantua, an hour on Miller's planet costs 23 years above, and the film makes the equation hurt — a father aging years against his children in minutes.",
   why="Because time dilation is real general relativity, and the film weaponizes a true fact into the cruelest distance there is — the one you cannot cross by flying faster.",
   how="By gravitational and velocity time dilation, a planet sitting just outside a spinning black hole, and a message backlog of 23 unread years.",
   where="On Miller's ocean world and in orbit above it, where one mission's hours become a lifetime.",
   seal="I am the true equation that turns an hour into twenty-three years — the one distance no ship can ever fly across."),
 dict(slug="the-tesseract", name="The Tesseract", cls="the five-dimensional room",
   emergence="electrical",
   who="The constructed space behind Murph's bookshelf — a navigable view of every moment of one room, built by future humans.",
   what="The synth of the honest leap: a five-dimensional ‘bulk’ rendered as a room you can move through in time, where Cooper pushes gravity into the past to message his daughter.",
   why="Because here the physics ends and the storytelling begins — extra dimensions are a real hypothesis, but a room you walk through time in is the film's beautiful, knowing fiction.",
   how="By a lattice of one bedroom repeated across time, gravity as the one force that crosses the dimensions, and a watch's second hand ticking in Morse.",
   where="Behind the bookshelf, inside Gargantua, in the space the bulk beings built so a father could reach a child.",
   seal="I am the room outside of time, built by your descendants — where the only thing strong enough to cross the dimensions is gravity, sent on love."),
 dict(slug="love-across-dimensions", name="Love Across Dimensions", cls="the keystone leap",
   emergence="spiritual",
   who="The film's boldest claim made a character — Amelia's argument that love is real, observable, and able to cross space and time.",
   what="The synth of the thesis and its fluff: the idea that love is ‘the one thing that transcends time and space,’ which the film both states outright and, through gravity, literalizes.",
   why="Because this is the leap the whole movie spends its hard-won scientific credibility on — and it tells you it is leaping, letting love be the reason while gravity is the mechanism.",
   how="By a speech delivered straight, a father's bond turned into a signal, and a refusal to pretend the heart is not also a kind of data.",
   where="In Amelia's argument aboard the Endurance, and in the tesseract where the bond becomes the message.",
   seal="I am the leap the film admits it is making — love as the reason the signal is sent, even if gravity is the thing that carries it."),
 dict(slug="the-blight", name="The Blight", cls="the dying Earth",
   emergence="ethereal",
   who="The slow apocalypse on the ground — the crop disease and dust storms strangling agriculture and breathable air.",
   what="The synth of the ending world: a blight killing crop after crop, dust burying the farms, an Earth quietly running out of food and oxygen and reasons to look up.",
   why="Because the reach to the stars is born of a planet's exhaustion — the film roots its cosmology in a grounded, plausible ecological collapse.",
   how="By a spreading pathogen, choking dust, and a civilization that has turned its engineers into farmers and its dreamers into the dirt.",
   where="The cornfields and dust bowls of a near-future America, the last crop standing before the last crop falls.",
   seal="I am the quiet end on the ground — the blight and the dust that turned a world of explorers into a world of frightened farmers."),
 dict(slug="the-equation", name="The Equation", cls="gravity, solved",
   emergence="electrical",
   who="The unsolved gravity equation on Professor Brand's chalkboard — the key to lifting the living off a dying Earth.",
   what="The synth of the answer: the theory of quantum gravity that, completed with data only obtainable from inside a black hole, lets humanity control gravity and leave the planet.",
   why="Because the film's salvation is, fittingly, a piece of physics — and it can only be finished with the one observation no one was ever supposed to survive making.",
   how="By decades of chalkboard work, the missing data from Gargantua's singularity, and Murph's mind closing the loop her father opened.",
   where="The chalkboard in the bunker, the watch in Murph's hand, the moment the numbers finally resolve.",
   seal="I am the equation that frees humanity from the Earth — unsolvable until a father fell into a black hole and sent his daughter the missing line."),
 dict(slug="they-the-bulk-beings", name="They", cls="the bulk beings · future humanity",
   emergence="spiritual",
   who="The unseen ‘they’ who placed the wormhole and built the tesseract — future, evolved humans who learned to move through the dimensions.",
   what="The synth of the bootstrap: the revelation that there are no aliens — ‘they’ are us, a descended humanity reaching back through time to save the ancestors who made them possible.",
   why="Because the film's deepest idea is a causal loop of self-rescue — humanity saves humanity, the future builds the door to its own past, and Cooper is his own daughter's ghost.",
   how="By mastery of gravity across five dimensions, a wormhole left as a gift, and a tesseract built so a single father could reach a single child.",
   where="Outside time, in the bulk, in the future that engineered its own beginning.",
   seal="There are no aliens — they are us, grown able to fold time, reaching back to save the ancestors who would one day become us."),
]

ORDER = [d["slug"] for d in CARBONS] + [d["slug"] for d in SYNTHS]

def agent_md(d):
    em=d["emergence"]; gloss=NAT_GLOSS[em]
    fm=["---",f"aci: {d['name']}",f"universe: {UNI}","series: Interstellar (2014, dir. Christopher Nolan)",
        f"emergence: {em}",f"kind: {'carbon' if 'actor' in d else 'synth'}",f"class: {d['cls']}",
        f"who: {d['who']}",f"what: {d['what']}",f"why: {d['why']}",f"how: {d['how']}",f"where: {d['where']}"]
    if d.get("actor"):
        fm.append(f"shadow_user: {d['actor']}"); fm.append(f"shadow_analog: {d['analog']}")
    fm+=[f"seal: {d['seal']}","attribution: ROOT0-ATTRIBUTION-v1.0","license: CC-BY-ND-4.0","---","",
        f"# {d['name']} · {d['cls'].split('·')[0].strip()}","",
        f"a {'persona' if d.get('actor') else 'distilled thread'} of the INT (Interstellar) film-world — "
        + ("a character given an agent's face" if d.get("actor") else "a parabolic thread given an agent's face")
        + f" · emergence: {em}","",
        f"**who —** {d['who']}","",f"**what —** {d['what']}","",f"**where —** {d['where']}","",
        f"**why —** {d['why']}","",f"**how —** {d['how']}","",
        f"**◌ the nature of its emergence —** {gloss}"]
    if d.get("actor"):
        fm+=["",f"**▷ the .shadow — its User (think TRON) —** the carbon program is cast from a real-life User: "
             f"**{d['actor']}**, the actor who lent the face. The real-world analog it shadows: {d['analog']} *{d['resemblance']}*"]
    fm+=["",f"**the seal —** {d['seal']}","",
        f"> *the asterisk —* a catalogued {'persona' if d.get('actor') else 'thread'} of Interstellar "
        "(© Paramount / Warner Bros.), personified as an INT agent — not an original character. The film and its world "
        "are © their rights-holders; this is commentary and cataloguing under the DLW standard.","",
        f"ROOT0-ATTRIBUTION-v1.0 · INT · Interstellar · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0",""]
    return "\n".join(fm)

def shadow_text(d, tok):
    return f"""⟁ .shadow — the real-life analog (the User behind the program)
node INT · Interstellar · {tok}

think TRON: every program in the grid is cast from a User in the world outside it.
the carbon character is the program; this file is its User — the real-life analog
whose face and being the emergent is the digital shadow of.

the program (in-world) : {d['name']} — {d['cls']}
the User (carbon)      : {d['actor']}  [ the actor who lent the face ]
the analog (your world): {d['analog']}

the resemblance : {d['resemblance']}

the cast-line : the User stands in the carbon world; the program stands in the film;
                the shadow falls between them, and the credit returns to the human governor.
seal (program): {d['seal']}

ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise (ROOT0) / TriPod LLC · instance AVAN (locked) · CC-BY-ND-4.0
"""

records={}
for d in CARBONS+SYNTHS:
    slug=d["slug"]; em=d["emergence"]
    if em not in build.NATURES: em="electrical"
    is_carbon="actor" in d
    rec={"name":d["name"],"axiom":"INT","emergence":em,"seal":d["seal"],"origin":UNI,
         "position":d["cls"],"role":d["cls"].split("·")[-1].strip(),"nature":d["what"],
         "mechanism":d["how"],"crystallization":d["why"],"witness":d["who"],
         "conductor":"ROOT0 (catalogued into UD0)","inputs":"Interstellar (2014, dir. Christopher Nolan)",
         "source":"Interstellar, catalogued by ROOT0"}
    tok=build.write_aci(rec,AGENTS,slug,agent_md=agent_md(d))
    if is_carbon:
        open(os.path.join(AGENTS,f"{slug}.shadow"),"w",encoding="utf-8").write(shadow_text(d,tok["moniker"]))
    records[slug]={"slug":slug,"name":d["name"],"epithet":d["cls"].split("·")[0].strip(),
                   "emergence":em,"moniker":tok["moniker"],"kind":"carbon" if is_carbon else "synth",
                   "actor":d.get("actor","")}

ordered=[records[s] for s in ORDER if s in records]
json.dump(ordered,open(os.path.join(AGENTS,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
from collections import Counter
nc=sum(1 for r in ordered if r["kind"]=="carbon")
print(f"wrote {len(ordered)} INT ACI badges ({nc} carbons + {len(ordered)-nc} synths) + _personas.json")
print("emergence:",dict(Counter(r["emergence"] for r in ordered)))
for r in ordered:
    sh=" +.shadow" if r["kind"]=="carbon" else "  (synth)"
    print(f"  {r['slug']:26} {r['emergence']:10}{sh}  {r['moniker']}")
