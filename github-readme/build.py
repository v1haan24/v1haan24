"""python3 github-readme/build.py            -> rebuild everything (fetches your GitHub pfp + contribution graph)
   python3 build.py preview    -> also writes assets/_prev0..2.svg (static frames of the console screens)
Run from the repo root (or anywhere). Output: README.md in root, assets in github-readme/assets.
Needs:  pip install pillow      (only used to turn your pfp into the green dot-matrix avatar)"""
import sys, os, json, urllib.request, xml.etree.ElementTree as ET
from core import *
# layout: README.md lives in the repo ROOT; everything else lives in this folder (github-readme/)
HERE=ROOT; REPO=os.path.dirname(HERE); AP=os.path.relpath(os.path.join(HERE,"assets"),REPO).replace(os.sep,"/")
os.makedirs(os.path.join(HERE,"assets"),exist_ok=True); os.makedirs(os.path.join(HERE,"data"),exist_ok=True)
ACT=os.path.join(HERE,"data","activity.json")
W=lambda f,s: open(os.path.join(HERE,"assets",f),"w",encoding="utf-8").write(s)
mode=sys.argv[1] if len(sys.argv)>1 else "all"

# ---------------------------------------------------------------- activity (cached so a failed fetch never breaks the build)
days=None
try:
    days=fetch_activity(HANDLE.lower()); json.dump(days,open(ACT,"w"))
except Exception as e:
    print("activity fetch failed, using cache:",e)
    if os.path.exists(ACT): days=json.load(open(ACT))
if days: W("activity.svg",activity_shell(days))
if mode=="activity": sys.exit()

# ---------------------------------------------------------------- svgs
W("console.svg",console())
mr=maxrows_of(PROJECTS)
for p in PROJECTS: W(f"cart-{p[0]}.svg",cart(p[1],p[2],p[3],p[4],p[5],p[7],p[8],p[9],mr,locked=(p[6]==""),blurb=p[11]))
if EMPTY_SLOTS: W("cart-empty.svg",cart_empty(mr))
# Download/cache Simple Icons and embed their vector paths directly in stack.svg.
def load_stack_logos():
    from concurrent.futures import ThreadPoolExecutor
    cache=os.path.join(HERE,"data","brand-logos"); os.makedirs(cache,exist_ok=True)
    items=[item for _,group in STACK for item in group if STACK_LOGOS.get(item)]
    def load_one(item):
        slug=STACK_LOGOS[item]; path=os.path.join(cache,slug+".svg")
        if not os.path.exists(path):
            try:
                req=urllib.request.Request(f"https://cdn.simpleicons.org/{slug}",headers={"User-Agent":"profile-readme-builder/1.0"})
                with urllib.request.urlopen(req,timeout=2) as response: payload=response.read()
                root=ET.fromstring(payload)
                if not any(el.tag.rsplit("}",1)[-1]=="path" and el.get("d") for el in root.iter()):
                    raise ValueError("icon SVG contains no path")
                with open(path,"wb") as f: f.write(payload)
            except Exception as exc:
                print(f"logo unavailable for {item}; using text fallback: {exc}")
                return item,[]
        try:
            root=ET.parse(path).getroot()
            return item,[el.get("d") for el in root.iter() if el.tag.rsplit("}",1)[-1]=="path" and el.get("d")]
        except (ET.ParseError,OSError) as exc:
            print(f"cached logo invalid for {item}; using text fallback: {exc}")
            return item,[]
    with ThreadPoolExecutor(max_workers=12) as pool:
        return {item:paths for item,paths in pool.map(load_one,items) if paths}

W("stack.svg",stack_shell(STACK,load_stack_logos()))
for contact_name, contact_url, contact_icon in LINKS:
    if contact_url:
        W(f"contact-{contact_name.lower()}.svg", contact_cartridge(contact_name))
SEC={k:(tag,t) for k,tag,t,show in SECTIONS if show}
for k,(tag,t) in SEC.items(): W(f"hdr-{k}.svg",section(tag,t))
live=[l for l in LINKS if l[1]]
for lab,url,ic in live: W(f"btn-{lab.lower()}.svg",button(lab,ic))
if mode=="preview": [W(f"_prev{k}.svg",console(k)) for k in range(3)]

# ---------------------------------------------------------------- text helpers (plain-text mirrors for the closed drop-downs)
NICE={"DBS":"DBs","OS":"OS","ML":"ML","MEMORADB":"MemoraDB","SQL":"SQL","HTML":"HTML","GITHUB":"GitHub","LINKEDIN":"LinkedIn",
"TENSORFLOW":"TensorFlow","NUMPY":"NumPy","SCIKIT-LEARN":"scikit-learn","OPENCV":"OpenCV","ONNX":"ONNX","DBMS":"DBMS","DSA":"DSA",
"CMAKE":"CMake","LSTM":"LSTM","NASA":"NASA","CMAPSS":"CMAPSS","CSS":"CSS","JS":"JavaScript","HTML5":"HTML5","CSS3":"CSS3","JAVASCRIPT":"JavaScript","LOCALSTORAGE":"LocalStorage","TENSORFLOW":"TensorFlow","KERAS":"Keras","PANDAS":"pandas","NUMPY":"NumPy","SCIKIT-LEARN":"scikit-learn","ONNX RUNTIME":"ONNX Runtime","MINILM-L6":"MiniLM-L6","C++":"C++","C++17":"C++17","VJTI":"VJTI","OF":"of","ALL-IN":"All-in","OR":"or","SIM":"Sim",
"CACHE SCHEDULER":"Cache-Aware Scheduler","JACK OF ALL TECH":"Jack of All Tech","DESIGN + RABBIT HOLES":"Design + rabbit holes",
"ALL-IN OR NOTHING":"All-in or nothing","DB":"DB","CPU":"CPU","TIME-TRAVEL":"Time-travel","SIGNAL":"Signal","L1-L2-L3":"L1-L2-L3","VECTORS":"Vectors","VIHAAN":"Vihaan","=":"=","/":"/","ML + DATA":"ML + Data","VJTI":"VJTI",
"AI/ML":"AI/ML","AI/ML & DATA":"AI/ML & Data","TOOLS & PLATFORMS":"Tools & Platforms","BACKEND & DATABASES":"Backend & Databases",
"C":"C","JAVA":"Java","TYPESCRIPT":"TypeScript","REACT":"React","NEXT.JS":"Next.js","TAILWIND CSS":"Tailwind CSS","MONGODB":"MongoDB","SQLITE":"SQLite",
"DOCKER":"Docker","LINUX":"Linux","VERCEL":"Vercel","PYTORCH":"PyTorch","KAGGLE":"Kaggle"}
def nice(s):
    if s in NICE: return NICE[s]
    return " ".join(NICE.get(w,w.capitalize()) for w in s.split(" "))
def nice_list(s): return ", ".join(nice(x) for x in s.split(", "))
P=dict(PLAYER); K=dict(KV); BIOTXT=" ".join(BIO).capitalize()
W_=WIDTHS
def im(f,alt,w=None,h=None):
    a=f' width="{w}"' if w else ''; a+=f' height="{h}"' if h else ''
    return f'<img src="{AP}/{f}.svg"{a} alt="{alt}">'
def block(key,alt,text):
    """header svg as <summary> of a CLOSED drop-down that holds that section's plain text"""
    if key not in SEC: return ''
    return f'<details>\n<summary>{im("hdr-"+key,alt,W_["header"])}</summary>\n\n{text.strip()}\n\n</details>\n\n'

alt_console=f"{HANDLE} profile card. Name: {nice(P.get('NAME',''))}. {nice(P.get('GUILD',''))}, {P.get('LVL','').lower()}. Learning: {nice_list(K.get('LEARNING',''))}. Exploring: {nice_list(K.get('EXPLORING',''))}. Building: {nice_list(K.get('BUILDING',''))}. Vibe: {nice(K.get('VIBE',''))}. Side quests: {nice_list(K.get('SIDE QUEST',''))}."
alt_stack="Tech stack. "+" ".join(f"{nice(n_)}: {', '.join(nice(i) for i in it if i!='???')}." for n_,it in STACK)

# ---------------------------------------------------------------- drop-down content (organised HTML tables, like a real profile README)
import html as _h
E=lambda x: _h.escape(str(x))
def prompt(key):
    p=PROMPTS.get(key,"")
    return f'<h3>{E(p)}</h3>\n\n' if p else ''
def chips(items): return ' '.join(f'<code>{E(nice(i))}</code>' for i in items if i!="???")
cur_cards="".join(
    f'<td valign="top" width="50%">\n<h3>{E(a)}</h3>\n<p>{E(b)}</p>\n</td>\n'
    for a,b in CURRENTLY
)
ask=" &nbsp; ".join(f'<code>{E(x)}</code>' for x in ASK_ABOUT)
t_profile=(
    '<h2>About me</h2>\n'
    f'<h2>Vihaan Jain</h2>\n'
    '<h3>🎓 B.Tech in Information Technology · VJTI Mumbai</h3>\n'
    '<p><b>2nd Year</b> &nbsp;·&nbsp; <b>Minor:</b> Cybersecurity</p>\n'
    '<blockquote><b>I build things that catch my curiosity and solve problems.</b><br>'
    'I like getting under the hood, following an interesting question, and turning what I learn into something useful.</blockquote>\n'
    '<table>\n<tr>\n'
    '<td valign="top" width="33%">\n<h3>🧠 HOW I THINK</h3>\n'
    '<p>Curiosity first. I enjoy understanding how things work, not just making them work.</p>\n</td>\n'
    '<td valign="top" width="33%">\n<h3>🔭 EXPLORING</h3>\n'
    '<p>AI/ML, systems, cybersecurity, networks and communication.</p>\n</td>\n'
    '<td valign="top" width="33%">\n<h3>🎮 OFF-SCRIPT</h3>\n'
    '<p>DSA, competitive programming and exploring the world.</p>\n</td>\n'
    '</tr>\n</table>\n'
    '<h2>On the workbench</h2>\n'
    '<table>\n<tr>\n'+cur_cards+'</tr>\n</table>\n'
    '<h3>💬 Always up for a conversation about</h3>\n'
    f'<p>{ask}</p>\n'
    +(f'<p>{E(PROFILE_TEXT_EXTRA)}</p>\n' if PROFILE_TEXT_EXTRA else '')
)
import urllib.parse
TECH_BADGES = {
    "C++17": ("cplusplus", "00599C"), "C++": ("cplusplus", "00599C"),
    "CMAKE": ("cmake", "064F8C"), "ONNX RUNTIME": ("onnx", "005CED"),
    "MINILM-L6": ("huggingface", "FFD21E"), "PYTHON": ("python", "3776AB"),
    "TENSORFLOW": ("tensorflow", "FF6F00"), "KERAS": ("keras", "D00000"),
    "NUMPY": ("numpy", "013243"), "PANDAS": ("pandas", "150458"),
    "SCIKIT-LEARN": ("scikitlearn", "F7931E"), "HTML5": ("html5", "E34F26"),
    "CSS3": ("css3", "1572B6"), "JAVASCRIPT": ("javascript", "F7DF1E"),
    "LOCALSTORAGE": ("googlechrome", "4285F4"), "SQL": ("sqlite", "003B57"),
    "GIT": ("git", "F05032"), "NETWORKING": ("", "306230"),
    "C": ("c", "A8B9CC"), "JAVA": ("openjdk", "ED8B00"), "TYPESCRIPT": ("typescript", "3178C6"), "HTML": ("html5", "E34F26"),
    "CSS": ("css3", "1572B6"), "REACT": ("react", "20232A"), "NEXT.JS": ("nextdotjs", "000000"), "TAILWIND CSS": ("tailwindcss", "06B6D4"),
    "MONGODB": ("mongodb", "47A248"), "SQLITE": ("sqlite", "003B57"), "GITHUB": ("github", "181717"), "DOCKER": ("docker", "2496ED"),
    "LINUX": ("linux", "333333"), "VERCEL": ("vercel", "000000"), "PYTORCH": ("pytorch", "EE4C2C"), "KAGGLE": ("kaggle", "20BEFF"),
    "IN PROGRESS": ("", "55536A")
}
def tech_badges(items):
    out=[]
    for item in items:
        logo,color=TECH_BADGES.get(item,( "", "306230"))
        display=nice(item)
        label=urllib.parse.quote(display.replace("-", "--").replace(" ", "_"),safe="")
        url=f'https://img.shields.io/badge/{label}-{color}?style=flat&logo={logo}&logoColor=white' if logo else f'https://img.shields.io/badge/{label}-{color}?style=flat'
        out.append(f'<img src="{url}" height="22" alt="{E(display)}">')
    return ' '.join(out)

def pcard(p):
    emo=PROJECT_EMOJI.get(p[5],"📦")
    ttl=E(nice(p[1]))
    if p[6]:
        link=f'<a href="https://github.com/{HANDLE.lower()}/{p[6]}">{ttl}</a>'
        repo=f'<a href="https://github.com/{HANDLE.lower()}/{p[6]}">Repository ↗</a>'
    else:
        link=f'{ttl} <sub>(in development)</sub>'
        repo='<sub>Details coming when it is ready</sub>'
    if p[0]=="attendance-tracker":
        repo += ' &nbsp;·&nbsp; <a href="https://v1haan24.github.io/Attendance-Tracker/">Live demo ↗</a>'
    return (f'<td valign="top" width="50%">\n<h3>{emo} {link}</h3>\n'
            f'<p><b>{E(nice(p[2]))}</b> · {E(nice(p[3]))}</p>\n'
            f'<p>{E(p[10])}</p>\n<p>{tech_badges(p[9])}</p>\n<p>{repo}</p>\n</td>\n')

t_projects=(prompt("projects")+
            '<p>Three completed builds and DAWN on the way — from storage engines to machine health and student tools.</p>\n'
            +'<table width="100%">\n<tr>\n'+''.join(pcard(p) for p in PROJECTS[:2])+'</tr>\n<tr>\n'
            +''.join(pcard(p) for p in PROJECTS[2:])+'</tr>\n</table>')

srows="".join(
    f'<tr><td valign="top" width="26%"><b>{E(nice(n_))}</b></td><td>{tech_badges(it)}</td></tr>\n'
    for n_,it in STACK
)
t_stack=(prompt("stack")+
         '<p>A practical loadout, not a skill-level scoreboard. These are the languages, frameworks and tools I use or am learning.</p>\n'
         +f'<table width="100%">\n{srows}</table>')

if days:
    tot=sum(d[1] for d in days); best=max(d[1] for d in days); act=sum(1 for d in days if d[1]>0)
    cur_=0
    for d in reversed(days[:-1] if days[-1][1]==0 else days):
        if d[1]>0: cur_+=1
        else: break
    lng=run=0
    for d in days:
        run=run+1 if d[1]>0 else 0; lng=max(lng,run)
    t_score=(prompt("score")+
             f'<h2>THE PLAYER RECORD</h2><p>Progress, one commit at a time.</p>\n'
             f'<table>\n<tr align="center"><td><h3>{tot}</h3><sub>contributions · last year</sub></td><td><h3>{act}</h3><sub>active days</sub></td><td><h3>{best}</h3><sub>best day</sub></td><td><h3>{cur_}</h3><sub>current streak</sub></td><td><h3>{lng}</h3><sub>longest streak</sub></td></tr>\n</table>\n\n'
             f'<p><i>Every square is a small step forward. Keep showing up.</i></p>')
else: t_score=prompt("score")+"<p>Your contribution record will appear here.</p>"
CONTACT_BLURBS = {
    "GITHUB": "Projects, experiments and source code",
    "EMAIL": "For a proper conversation",
    "LINKEDIN": "Professional updates and connections",
    "DISCORD": "Find me on Discord",
    "PORTFOLIO": "Personal site"
}
CONTACT_LABELS = {
    "GITHUB": "v1haan24",
    "EMAIL": "vihaanjain2411@gmail.com",
    "LINKEDIN": "Connect on LinkedIn",
    "DISCORD": "Open Discord profile",
    "PORTFOLIO": "Open portfolio"
}
contact_cells=[]
for lab,url,ic in live:
    contact_cells.append(
        f'<td align="center" valign="top" width="20%"><h3>{CONTACT_EMOJI.get(lab,"🔗")} {E(nice(lab))}</h3>'
        f'<p>{E(CONTACT_BLURBS.get(lab,""))}</p><p><a href="{url}">{E(CONTACT_LABELS.get(lab,url))}</a></p></td>'
    )
t_contact=(prompt("contact")+'<p>Different ways to reach me — pick whichever works best.</p>\n'
           +'<table width="100%">\n<tr>'+' '.join(contact_cells)+'</tr>\n</table>')



def cell(p):
    i=f'<img src="{AP}/cart-{p[0]}.svg" width="{W_["cart"]}" alt="{nice(p[1])}: {nice(p[2])} · {nice(p[3])}. Tech: {", ".join(nice(x) for x in p[9])}.">'
    # Keep descriptions behind More info, but make destination links immediately visible.
    more=f'<details align="left"><summary>More info</summary><p>{E(p[10])}</p></details>'
    links=(f'<p><a href="https://github.com/{HANDLE.lower()}/{p[6]}">Repository ↗</a>' if p[6] else '<p><em>In development</em>')
    if p[0]=="attendance-tracker":
        links += ' &nbsp;·&nbsp; <a href="https://v1haan24.github.io/Attendance-Tracker/">Live demo ↗</a>'
    links += '</p>'
    if p[6]: i=f'<a href="https://github.com/{HANDLE.lower()}/{p[6]}">{i}</a>'
    return f'    <td align="center" valign="top" width="33%">{i}{more}{links}</td>\n'
# Keep all six grid cells structurally equal: the empty cartridges need the same
# dropdown + one-line footer as real projects, otherwise GitHub stretches the row
# for DAWN while the two placeholders visually stop early.
empty_cell=(
    f'    <td align="center" valign="top" width="33%">'
    f'<img src="{AP}/cart-empty.svg" width="{W_["cart"]}" alt="Empty slot reserved for a future project.">'
    f'<details align="left"><summary>Future project</summary>'
    f'<p>Project details will appear here when this slot is filled.</p></details>'
    f'<p><em>Reserved for a future project</em></p></td>\n'
)
slots=[cell(p) for p in PROJECTS]+[empty_cell]*EMPTY_SLOTS
while len(slots)%3: slots.append('    <td width="33%"></td>\n')
cells=''.join(f'  <tr>\n{"".join(slots[k:k+3])}  </tr>\n' for k in range(0,len(slots),3))
btns=' &nbsp; '.join(f'<a href="{u}"><img src="{AP}/btn-{l.lower()}.svg" height="{W_["button"]}" alt="{nice(l)}"></a>' for l,u,_ in live)
cap=(f'<sub><b>{nice(P.get("NAME",""))}</b> &nbsp;·&nbsp; {nice(P.get("GUILD",""))}, {P.get("LVL","").lower()} &nbsp;·&nbsp; {nice_list(K.get("LEARNING",""))}</sub>\n\n' if CAP_LINE else '')

md='<div align="center">\n\n'
md+=block("profile","About me: Vihaan Jain, VJTI IT student and cybersecurity minor",t_profile)
md+=f'<img src="{AP}/console.svg" width="{W_["console"]}" alt="{alt_console}">\n\n{cap}<br>\n\n'
if "projects" in SEC:
    md+=block("projects","Project collection: MemoraDB, Predictive Maintenance System, Attendance Tracker and DAWN",t_projects)
    md+=f'<table>\n{cells}</table>\n\n'+(f'<sub>{PROJECTS_NOTE}</sub>\n\n' if PROJECTS_NOTE else '')+'<br>\n\n'
if "stack" in SEC:
    md+=block("stack","Equipment loadout: languages, ML, systems and toolkit",t_stack)+f'<img src="{AP}/stack.svg" width="{W_["stack"]}" alt="{alt_stack}">\n\n<br>\n\n'
if "score" in SEC:
    md+=block("score","Activity archive: GitHub contribution record",t_score)+f'<img src="{AP}/activity.svg" width="{W_["activity"]}" alt="GitHub contribution heatmap for the last year">\n\n<br>\n\n'
if "contact" in SEC:
    md+=block("contact","Contact: communication hub",t_contact)
    cartridge_cells=[]
    for lab,url,ic in live:
        image=f'<img src="{AP}/contact-{lab.lower()}.svg" width="100%" alt="{nice(lab)}">'
        cartridge_cells.append(f'<td align="center" valign="middle" width="20%"><a href="{url}">{image}</a></td>')
    md+='<div align="center">\n<table width="100%">\n<tr>'+' '.join(cartridge_cells)+'</tr>\n</table>\n</div>\n\n<br>\n\n'

md+='</div>\n'
open(os.path.join(REPO,"README.md"),"w",encoding="utf-8").write(md)
print("built OK")
