import sys, os
from config import *
ROOT=os.path.dirname(os.path.abspath(__file__))
# ------------------------------------------------------------------ PIXEL FONT 5x7
F = {}
def g(ch, s): F[ch] = s.split('/')
g('A','.###./#...#/#...#/#####/#...#/#...#/#...#'); g('B','####./#...#/#...#/####./#...#/#...#/####.')
g('C','.###./#...#/#..../#..../#..../#...#/.###.'); g('D','####./#...#/#...#/#...#/#...#/#...#/####.')
g('E','#####/#..../#..../####./#..../#..../#####'); g('F','#####/#..../#..../####./#..../#..../#....')
g('G','.###./#...#/#..../#.###/#...#/#...#/.###.'); g('H','#...#/#...#/#...#/#####/#...#/#...#/#...#')
g('I','.###./..#../..#../..#../..#../..#../.###.'); g('J','..###/...#./...#./...#./...#./#..#./.##..')
g('K','#...#/#..#./#.#../##.../#.#../#..#./#...#'); g('L','#..../#..../#..../#..../#..../#..../#####')
g('M','#...#/##.##/#.#.#/#.#.#/#...#/#...#/#...#'); g('N','#...#/##..#/#.#.#/#..##/#...#/#...#/#...#')
g('O','.###./#...#/#...#/#...#/#...#/#...#/.###.'); g('P','####./#...#/#...#/####./#..../#..../#....')
g('Q','.###./#...#/#...#/#...#/#.#.#/#..#./.##.#'); g('R','####./#...#/#...#/####./#.#../#..#./#...#')
g('S','.####/#..../#..../.###./....#/....#/####.'); g('T','#####/..#../..#../..#../..#../..#../..#..')
g('U','#...#/#...#/#...#/#...#/#...#/#...#/.###.'); g('V','#...#/#...#/#...#/#...#/#...#/.#.#./..#..')
g('W','#...#/#...#/#...#/#.#.#/#.#.#/##.##/#...#'); g('X','#...#/#...#/.#.#./..#../.#.#./#...#/#...#')
g('Y','#...#/#...#/.#.#./..#../..#../..#../..#..'); g('Z','#####/....#/...#./..#../.#.../#..../#####')
g('0','.###./#...#/#..##/#.#.#/##..#/#...#/.###.'); g('1','..#../.##../..#../..#../..#../..#../.###.')
g('2','.###./#...#/....#/...#./..#../.#.../#####'); g('3','####./....#/....#/.###./....#/....#/####.')
g('4','#...#/#...#/#...#/#####/....#/....#/....#'); g('5','#####/#..../####./....#/....#/#...#/.###.')
g('6','.###./#..../#..../####./#...#/#...#/.###.'); g('7','#####/....#/...#./..#../.#.../.#.../.#...')
g('8','.###./#...#/#...#/.###./#...#/#...#/.###.'); g('9','.###./#...#/#...#/.####/....#/....#/.###.')
g(' ','...../...../...../...../...../...../.....'); g('.','...../...../...../...../...../.##../.##..')
g(',','...../...../...../...../.##../..#../.#...'); g('-','...../...../...../#####/...../...../.....')
g(':','...../.##../.##../...../.##../.##../.....'); g('/','....#/....#/...#./..#../.#.../#..../#....')
g('+','...../..#../..#../#####/..#../..#../.....'); g('>','#..../.#.../..#../...#./..#../.#.../#....')
g('<','....#/...#./..#../.#.../..#../...#./....#'); g('!','..#../..#../..#../..#../..#../...../..#..')
g('?','.###./#...#/....#/...#./..#../...../..#..'); g('(','...#./..#../.#.../.#.../.#.../..#../...#.')
g(')','.#.../..#../...#./...#./...#./..#../.#...'); g('=','...../...../#####/...../#####/...../.....')
g('*','...../#.#.#/.###./#####/.###./#.#.#/.....'); g('%','##..#/##..#/...#./..#../.#.../#..##/#..##')
g('#','.#.#./#####/.#.#./.#.#./#####/.#.#./.....'); g('_','...../...../...../...../...../...../#####'); g('[','.###./.#.../.#.../.#.../.#.../.#.../.###.'); g(']','.###./...#./...#./...#./...#./...#./.###.'); g('@','.###./#...#/#.###/#.#.#/#.##./#..../.####')
def n(v): return ('%f'%v).rstrip('0').rstrip('.') if v!=int(v) else str(int(v))
def tw(s,sc): return len(s)*6*sc-sc
def tpath(s,x,y,sc=1):
    d=[]; cx=x
    for ch in s.upper():
        rows=F.get(ch,F['?'])
        for r,row in enumerate(rows):
            c=0
            while c<5:
                if row[c]=='#':
                    k=c
                    while k<5 and row[k]=='#': k+=1
                    d.append(f"M{n(cx+c*sc)} {n(y+r*sc)}h{n((k-c)*sc)}v{n(sc)}h{n(-(k-c)*sc)}z"); c=k
                else: c+=1
        cx+=6*sc
    return ''.join(d)
def T(s,x,y,fill,sc=1,center=None,extra=''):
    if center is not None: x=center-tw(s,sc)/2
    x=round(x); return f'<path d="{tpath(s,x,y,sc)}" fill="{fill}" {extra}/>'
def bmp(rows,x,y,sc,fill,extra=''):
    d=''
    for r,row in enumerate(rows):
        for c,ch in enumerate(row):
            if ch=='#': d+=f"M{n(x+c*sc)} {n(y+r*sc)}h{n(sc)}v{n(sc)}h{n(-sc)}z"
    return f'<path d="{d}" fill="{fill}" {extra}/>'
L0,L1,L2,L3=THEME
CE='shape-rendering="crispEdges"'
def svg(w,h,body,defs='',title='',desc=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" {CE}>'
            f'<title>{title}</title><desc>{desc}</desc><defs>{defs}</defs>{body}</svg>')
def blink(dur=1.0,v="1;0"):
    return f'<animate attributeName="opacity" values="{v}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/>'
GRID=f'<pattern id="grid" width="1" height="1" patternUnits="userSpaceOnUse"><path d="M1 0V1H0" stroke="{L3}" stroke-opacity=".10" stroke-width=".14" fill="none"/></pattern>'
# ------------------------------------------------------------------ AVATAR (github pfp -> green dot matrix)
import json, io
BAYER=[[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]]
def _prep(img):
    from PIL import Image, ImageOps, ImageEnhance
    if img.mode in ("RGBA","LA","P"):
        img=img.convert("RGBA"); bg=Image.new("RGBA",img.size,(255,255,255,255)); bg.alpha_composite(img); img=bg
    img=img.convert("L"); w,h=img.size; m=min(w,h)/max(1.0,AVATAR_ZOOM)
    l,t=(w-m)/2,(h-m)/2; img=img.crop((int(l),int(t),int(l+m),int(t+m)))
    img=ImageOps.autocontrast(img,cutoff=2)
    img=ImageEnhance.Contrast(img).enhance(AVATAR_CONTRAST); img=ImageEnhance.Brightness(img).enhance(AVATAR_BRIGHT)
    return img
def to_rows(img,px):
    """PIL image -> list of strings, digits 0..3 (0 = lightest LCD shade, 3 = darkest)"""
    from PIL import Image
    g=_prep(img).resize((px,px),Image.LANCZOS); v=list(g.getdata()); out=[]
    mode=AVATAR_DITHER
    if mode=="floyd":
        a=[float(x) for x in v]; lv=[0]*(px*px)
        for y in range(px):
            for x in range(px):
                i=y*px+x; old=a[i]; q=min(3,max(0,round(old/255*3))); lv[i]=q; err=old-q*255/3
                if x+1<px: a[i+1]+=err*7/16
                if y+1<px:
                    if x>0: a[i+px-1]+=err*3/16
                    a[i+px]+=err*5/16
                    if x+1<px: a[i+px+1]+=err/16
    else:
        lv=[]
        for y in range(px):
            for x in range(px):
                t=v[y*px+x]/255*3; b=int(t); fr=t-b
                if mode=="bayer": b+= 1 if fr>(BAYER[y%4][x%4]+.5)/16 else 0
                else: b=int(round(t))
                lv.append(min(3,b))
    for y in range(px):
        out.append(''.join(str(3-lv[y*px+x] if not AVATAR_INVERT else lv[y*px+x]) for x in range(px)))
    return out
def load_avatar():
    """fetch pfp (or use local file / cached copy) -> {'big':rows,'small':rows}. Returns None = use sprite."""
    if not AVATAR_SOURCE: return None
    from PIL import Image
    os.makedirs(os.path.join(ROOT,"data"),exist_ok=True); cache=os.path.join(ROOT,"data","avatar-src.png"); img=None
    try:
        if AVATAR_SOURCE=="github":
            raw=urllib.request.urlopen(urllib.request.Request(f"https://github.com/{HANDLE.lower()}.png?size=400",headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
            img=Image.open(io.BytesIO(raw)); img.load(); r=img.copy(); r.thumbnail((256,256)); r.convert("RGBA").save(cache)
        else:
            img=Image.open(os.path.join(ROOT,AVATAR_SOURCE)); img.load()
    except Exception as e:
        print("avatar fetch failed, using cached copy:",e)
        if os.path.exists(cache): img=Image.open(cache); img.load()
    if img is None: print("WARNING: no avatar available, using sprite"); return None
    return {"big":to_rows(img,AVATAR_BIG_PX),"small":to_rows(img,AVATAR_SMALL_PX)}
_AV=[False,None]
def avatar():
    if not _AV[0]: _AV[0]=True; _AV[1]=load_avatar()
    return _AV[1]
SPRITE=["..####..","########","##.##.##","########","########",".######.","..#..#..","..#..#.."]
def avatar_art(rows,x,y,sc):
    """draw rows of shade digits as LCD pixels at (x,y) with scale sc. returns (svg, width, height)"""
    cols=[L0,L1,L2,L3]; px=len(rows); wd=len(rows[0])*sc; ht=px*sc
    b=f'<rect x="{x}" y="{y}" width="{wd}" height="{ht}" fill="{L0}"/>'
    for sh in (1,2,3):
        d=''
        for r,row in enumerate(rows):
            c=0
            while c<len(row):
                if row[c]==str(sh):
                    k=c
                    while k<len(row) and row[k]==str(sh) and not AVATAR_DOTS: k+=1
                    if AVATAR_DOTS: k=c+1; d+=f"M{n(x+c*sc+sc*.12)} {n(y+r*sc+sc*.12)}h{n(sc*.76)}v{n(sc*.76)}h{n(-sc*.76)}z"
                    else: d+=f"M{n(x+c*sc)} {n(y+r*sc)}h{n((k-c)*sc)}v{n(sc)}h{n(-(k-c)*sc)}z"
                    c=k
                else: c+=1
        if d: b+=f'<path d="{d}" fill="{cols[sh]}"/>'
    return b,wd,ht
def avatar_framed(kind,x,y,box):
    """avatar inside a framed box of size `box` at (x,y). kind = 'big'|'small'. falls back to the sprite."""
    av=avatar(); rows=av[kind] if av else None
    if rows is None: rows=[r.replace('#','3').replace('.','0') for r in SPRITE]
    px=len(rows); sc=max(1,box//px); real=px*sc; ox=x+(box-real)//2; oy=y+(box-real)//2
    art,_,_=avatar_art(rows,ox,oy,sc)
    return f'<rect x="{x-1.5}" y="{y-1.5}" width="{box+3}" height="{box+3}" fill="{L0}" stroke="{L3}" stroke-width="1.5"/>'+art

# ------------------------------------------------------------------ CONSOLE
LW,LH=320,176; SC=640/LW       # LCD logical size. 320 -> SC is exactly 2.0 = every pixel is a perfect 2x2 square (no distortion)
VX=76   # wider label/value gap keeps longer labels from crowding the values
def spinner(x,y):
    """Three compact pixel dots pulse from left to right."""
    out=''
    for k in range(3):
        f=''
        for j in range(3):
            col=L3 if j==k else L2
            f+=f'<rect x="{x+j*4}" y="{y+2}" width="2" height="2" fill="{col}"/>'
        out+=f'<g opacity="0">{seq(k,3,0.75)}{f}</g>'
    return out
def profile_screen():
    s=f'<rect width="{LW}" height="11" fill="{L3}"/>'+T(TXT["detail_title"],4,2,L0)
    s+=f'<g>{T(TXT["detail_status"],LW-4-tw(TXT["detail_status"],1),2,L0)}{blink(1.4,"1;0.25")}</g>'
    y=17
    for a,b in PLAYER:
        if b:
            if len(b)>18: print("WARNING: PLAYER value too long:",b)
            s+=T(a,6,y,L2)+T(b,VX,y,L3); y+=10
    box=44; ax=LW-10-box; ay=18
    s+=avatar_framed("small",ax,ay,box)
    if AVATAR_CAPTION: s+=T(AVATAR_CAPTION,0,ay+box+5,L3,center=ax+box/2)
    y=max(y+2,ay+box+17)
    # A compact identity tagline uses the gap below LVL without crowding the avatar.
    s+=T("BUILD / BREAK / LEARN",6,ay+box-3,L2)
    s+=f'<rect x="6" y="{y-3}" width="{LW-12}" height="1" fill="{L2}"/>'
    for line in BIO: s+=T(line,6,y+1,L3); y+=10
    y+=1; s+=f'<rect x="6" y="{y}" width="{LW-12}" height="1" fill="{L2}"/>'; y+=6
    last=y
    for a,b in KV:
        if not b: continue
        s+=T(a,6,y,L2)
        s+=T(b,VX,y,L3); last=y; y+=11
    s+=f'<g>{T("_",VX+tw(KV_LAST_VALUE(),1)+6,last,L3)}{blink(.7)}</g>'
    s+=f'<g>{T(TXT["detail_hint"],0,LH-9,L2,center=LW/2)}{blink(.9,"1;0.2")}</g>'
    if y>LH-12: print("WARNING: LCD content too long, shorten BIO/KV/PLAYER rows (y=%d, max %d)"%(y,LH-12))
    return s

def KV_LAST_VALUE():
    v=[b for a,b in KV if b]; return v[-1] if v else ""
# ---------------------------------------------------------------- animated boot sequence
D=30.0   # loop length in seconds (profile page holds ~21s)
def anim(wins,dur=D):
    """discrete opacity animation: visible during each (start,end) window (seconds)."""
    times=[0.0]; vals=[1 if any(s==0 for s,e in wins) else 0]
    for s,e in wins:
        if s>0: times.append(s); vals.append(1)
        if e<dur: times.append(e); vals.append(0)
    return (f'<animate attributeName="opacity" values="{";".join(map(str,vals))}" '
            f'keyTimes="{";".join(n(round(t/dur,5)) for t in times)}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/>')
def lcd_head(t,r=""):
    s=f'<rect width="{LW}" height="11" fill="{L3}"/>'+T(t,4,2,L0)
    if r: s+=T(r,LW-4-tw(r,1),2,L0)
    return s
SPR_A=["..####..","##.##.##","########",".######.","..#..#..",".##..##."]
SPR_B=["..####..","##.##.##","########",".######.","..####..","..#..#.."]
TILE_ICONS={
'cart':[".######.","#......#","#.####.#","#.#..#.#","#.####.#","#......#","########","#.#.#.#."],
'chest':["..####..",".#....#.","########","#......#","#..##..#","#..##..#","#......#","########"],
'trophy':["########","#.####.#","#.####.#",".######.","..####..","...##...","..####..",".######."],
'mail':["........","########","##....##","#.#..#.#","#..##..#","#......#","########","........"]}
def title_screen():
    c=LW/2
    s=f'<rect x="2.5" y="2.5" width="{LW-5}" height="{LH-5}" fill="none" stroke="{L3}"/>'
    s+=T(HANDLE+" "+TXT["presents"],0,14,L2,center=c)
    for i,w in enumerate(NAME):
        y=30+i*28
        s+=T(w,0,y+1,L2,3,center=c+1)+T(w,0,y,L3,3,center=c)
    s+=T(CLASS,0,92,L2,center=c)
    # Tiny explorable world: layered hills, a terminal landmark, and a roaming pixel adventurer.
    s+=f'<path d="M18 128 L18 122 L48 112 L72 119 L102 106 L130 117 L158 109 L190 120 L220 110 L250 119 L282 111 L302 120 L302 130 Z" fill="{L2}" opacity=".42"/>'
    s+=f'<path d="M18 129 L18 125 L52 119 L84 126 L118 116 L148 124 L184 117 L214 126 L250 118 L282 124 L302 121 L302 130 Z" fill="{L3}" opacity=".52"/>'
    s+=f'<path d="M18 130 H302" stroke="{L3}" stroke-width="1"/>'
    # Distant stars / data points.
    for sx,sy in [(34,105),(78,111),(142,103),(196,108),(232,103),(287,106)]:
        s+=f'<rect x="{sx}" y="{sy}" width="2" height="2" fill="{L3}">{blink(1.1+(sx%3)*.25,"1;0.25")}</rect>'
    # A tiny terminal on the horizon gives the scene a subtle tech signature.
    s+=f'<rect x="266" y="111" width="17" height="13" fill="{L1}" stroke="{L3}" stroke-width="1"/>'
    s+=f'<rect x="269" y="114" width="11" height="6" fill="{L3}" opacity=".75"/>'
    s+=f'<path d="M272 117 l2 -2 l2 2 l2 -2" fill="none" stroke="{L0}" stroke-width="1"/>'
    s+=f'<path d="M274 124 v3 M270 127 h9" stroke="{L3}" stroke-width="1"/>'
    # Small explorer walks across the landscape; two frames alternate for a subtle step cycle.
    explorer_a=["...##...","..####..",".######.","..#..#..",".######.","..#..#..",".##..##.","#......#"]
    explorer_b=["...##...","..####..",".######.","..#..#..",".######.","...##...","..#..#..",".##..##."]
    vals=';'.join(f"{v} 0" for v in range(24,250,4))
    s+=(f'<g><animateTransform attributeName="transform" type="translate" values="{vals}" calcMode="discrete" dur="12s" repeatCount="indefinite"/>'
        f'<g transform="translate(0,116)"><g>{bmp(explorer_a,0,0,1,L3)}{blink(.34,"1;0")}</g>'
        f'<g>{bmp(explorer_b,0,0,1,L3)}{blink(.34,"0;1")}</g></g></g>')
    s+=f'<g>{T(TXT["press"],0,LH-33,L3,center=c)}{blink(1.0,"1;0")}</g>'
    s+=T(TXT["copyright"]+" "+HANDLE,0,LH-16,L2,center=c)
    return s
def menu_screen():
    s=lcd_head(TXT["menu_title"],TXT["menu_ver"])
    hl=[[(0,4.4)],[(4.4,5.4)],[(5.4,7.2)],[]]
    for i,name in enumerate(MENU):
        y0=24+i*33
        s+=T(name,56,y0+2,L3,2)
        if hl[i]:
            s+=(f'<g opacity="0">{anim(hl[i])}<rect x="20" y="{y0-2}" width="{LW-40}" height="18" fill="{L3}"/>'
                f'{T(">",32,y0+2,L0,2)}{T(name,56,y0+2,L0,2)}</g>')
    s+=T(TXT["menu_hint"],0,LH-10,L2,center=LW/2)
    return s
def select_screen():
    s=lcd_head(TXT["select_title"],TXT["select_count"])
    box=SELECT_AVATAR_BOX; y0=17; h=box+10; ax=16; ay=y0+(h-box)//2
    s+=f'<rect x="10.5" y="{y0+.5}" width="{LW-21}" height="{h}" fill="{L1}" stroke="{L3}"/>'
    s+=avatar_framed("big",ax,ay,box)
    if SELECT_TAG: s+=f'<rect x="{ax-1}" y="{ay-1}" width="{tw(SELECT_TAG,1)+6}" height="11" fill="{L3}"/>'+T(SELECT_TAG,ax+2,ay+1,L0)
    tx=ax+box+14
    if tx+tw(SELECT_NAME,2)>LW-14: print("WARNING: SELECT_NAME too long")
    s+=T(SELECT_NAME,tx+1,y0+12,L2,2)+T(SELECT_NAME,tx,y0+11,L3,2)
    s+=f'<rect x="{tx}" y="{y0+30}" width="{LW-14-tx}" height="1" fill="{L2}"/>'
    for i,line in enumerate(SELECT_SUB[:4]): s+=T(line,tx,y0+38+i*11,L2 if i else L3)
    s+=f'<g><rect x="8.5" y="{y0-1.5}" width="{LW-17}" height="{h+3}" fill="none" stroke="{L3}" stroke-width="2"/>{blink(.6,"1;0.1")}</g>'
    # ---- quick menu: the sections below the console, as icon tiles (fills the screen)
    tiles=[t for t in SELECT_TILES if t[0]]
    if tiles:
        my=y0+h+8; ttl=TXT.get("select_menu","")
        s+=T(ttl,10,my,L3)+f'<rect x="{10+tw(ttl,1)+6}" y="{my+3}" width="{LW-20-tw(ttl,1)-6}" height="1" fill="{L2}"/>'
        ty=my+12; th=min(50,LH-20-ty); gap=6; k=len(tiles); w_=(LW-20-(k-1)*gap)//k
        if th<30: print("WARNING: select screen tiles are squashed (th=%d), lower SELECT_AVATAR_BOX"%th)
        for i,(lab,ic) in enumerate(tiles):
            x=10+i*(w_+gap); icx=x+(w_-16)//2; icy=ty+(th-30)//2+1
            def tile(bg,fg,fg2):
                r=f'<rect x="{x+.5}" y="{ty+.5}" width="{w_-1}" height="{th-1}" fill="{bg}" stroke="{L3}"/>'
                r+=bmp(TILE_ICONS[ic],icx,icy,2,fg)+T(lab,0,icy+20,fg,center=x+w_/2)+T("S%d"%(i+2),x+4,ty+4,fg2)
                return r
            s+=tile(L1,L3,L2)
            t0=3.1+i*0.85
            s+=f'<g opacity="0">{anim([(t0,t0+0.85)])}{tile(L3,L0,L0)}</g>'
    s+=T(TXT["select_hint"],0,LH-10,L2,center=LW/2)
    return s

def loading_screen():
    c=LW/2; t0,t1,N=10.7,12.2,18; dy=11
    s=T(TXT["loading_top"],0,48+dy,L2,center=c)+T(TXT["loading_name"],0,84+dy,L3,2,center=c)
    s+=f'<rect x="30.5" y="{62.5+dy}" width="{LW-61}" height="12" fill="none" stroke="{L3}"/>'
    kts=["0"]+[n(round((t0+(k+1)*(t1-t0)/N)/D,5)) for k in range(N)]; vs=["0"]+[str(14*(k+1)) for k in range(N)]
    s+=f'<rect x="33" y="{65+dy}" width="0" height="7" fill="{L3}"><animate attributeName="width" values="{";".join(vs)}" keyTimes="{";".join(kts)}" calcMode="discrete" dur="{D}s" repeatCount="indefinite"/></rect>'
    s+=f'<g>{T(TXT["loading_wait"],0,108+dy,L2,center=c)}{blink(.5)}</g>'
    return s
SCREENS_TL=[("title",title_screen,[(0,3.0),(27.4,D)]),("select",select_screen,[(3.0,6.6)]),("detail",None,[(6.6,27.4)])]
def timeline(force=None):
    out=''
    for i,(nm,fn,w) in enumerate(SCREENS_TL):
        body=fn() if fn else profile_screen()
        if force is None: out+=f'<g opacity="0">{anim(w)}{body}</g>'
        elif force==i: out+=f'<g>{body}</g>'
    return out

def press(wins,shape,dur=None):
    return f'<g opacity="0">{anim(wins,dur or D)}{shape}</g>'
def shell(inner,LWp,LHp,SCp,P,dur,title,desc):
    """Compact handheld: big 640x352 LCD, small side controls. inner = LCD content in logical px."""
    defs=GRID+f'''<clipPath id="lcd"><rect width="{LWp}" height="{LHp}"/></clipPath>
<linearGradient id="body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SHELL_TOP}"/><stop offset="1" stop-color="{SHELL_BOT}"/></linearGradient>
<linearGradient id="vig" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".22"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>
<radialGradient id="btn" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="{BTN_A}"/><stop offset="1" stop-color="{BTN_B}"/></radialGradient>'''
    pr=lambda k,shape: press(P[k],shape,dur) if P.get(k) else ''
    b='<rect x="0" y="8" width="960" height="440" rx="24" fill="#000" opacity=".16"/>'
    b+='<rect width="960" height="440" rx="24" fill="url(#body)"/><rect x="2" y="2" width="956" height="436" rx="22" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>'
    b+='<rect x="136" y="16" width="688" height="408" rx="14" fill="'+BEZEL+'"/><rect x="136" y="16" width="688" height="408" rx="14" fill="none" stroke="#3b3a4d" stroke-width="3"/>'
    b+='<rect x="152" y="26" width="110" height="2" fill="#b0346a"/><rect x="152" y="31" width="110" height="2" fill="#3e4fb8"/>'
    b+='<rect x="698" y="26" width="110" height="2" fill="#b0346a"/><rect x="698" y="31" width="110" height="2" fill="#3e4fb8"/>'
    b+=T(SHELL_TEXT,0,22,"#a3a1ba",2,center=480)
    b+='<circle cx="148" cy="226" r="4" fill="#ff2d4a"><animate attributeName="opacity" values="1;.55;1" dur="2.4s" repeatCount="indefinite"/></circle>'
    b+='<rect x="156" y="46" width="648" height="360" fill="#2a2933"/>'
    b+=f'<g transform="translate(160,{50+(352-LHp*SCp)/2:.2f}) scale({SCp})"><rect width="{LWp}" height="{LHp}" fill="{L0}"/><g clip-path="url(#lcd)">{inner}</g>'
    b+=f'<rect width="{LWp}" height="{LHp}" fill="url(#grid)"/><rect width="{LWp}" height="9" fill="url(#vig)"/></g>'
    cx,cy=76,212
    b+=f'<circle cx="{cx}" cy="{cy}" r="52" fill="#b3b0a2"/><circle cx="{cx}" cy="{cy}" r="52" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="2"/>'
    b+=f'<rect x="{cx-40}" y="{cy-13}" width="80" height="26" rx="5" fill="#2c2b36"/><rect x="{cx-13}" y="{cy-40}" width="26" height="80" rx="5" fill="#2c2b36"/>'
    dk="#121118"
    b+=pr('down',f'<rect x="{cx-13}" y="{cy+6}" width="26" height="34" rx="5" fill="{dk}"/>')+pr('up',f'<rect x="{cx-13}" y="{cy-40}" width="26" height="34" rx="5" fill="{dk}"/>')
    b+=pr('right',f'<rect x="{cx+6}" y="{cy-13}" width="34" height="26" rx="5" fill="{dk}"/>')+pr('left',f'<rect x="{cx-40}" y="{cy-13}" width="34" height="26" rx="5" fill="{dk}"/>')
    b+=f'<circle cx="{cx}" cy="{cy}" r="7" fill="#1f1e27"/>'
    for dx,dy,pts in [(0,-27,"-4,3 0,-3 4,3"),(0,27,"-4,-3 0,3 4,-3"),(-27,0,"3,-4 -3,0 3,4"),(27,0,"-3,-4 3,0 -3,4")]:
        b+=f'<polygon transform="translate({cx+dx},{cy+dy})" points="{pts}" fill="#5b5a70"/>'
    b+='<g transform="rotate(-25 892 212)"><rect x="830" y="180" width="124" height="64" rx="32" fill="#b3b0a2"/><rect x="830" y="180" width="124" height="64" rx="32" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="2"/></g>'
    for (x,y) in [(914,200),(870,224)]:
        b+=f'<circle cx="{x}" cy="{y+2}" r="21" fill="#5e1130"/><circle cx="{x}" cy="{y}" r="21" fill="url(#btn)"/>'
    b+=pr('a','<circle cx="914" cy="202" r="21" fill="#5e1130"/>')+pr('b','<circle cx="870" cy="226" r="21" fill="#5e1130"/>')
    b+=T("A",910,246,"#5a5870",1)+T("B",866,262,"#5a5870",1)
    for (x,l) in [(56,"SELECT"),(108,"START")]:
        b+=f'<g transform="translate({x},388) rotate(-25)"><rect x="-19" y="-5" width="38" height="10" rx="5" fill="#6e6c82"/></g>'+T(l,x-tw(l,1)/2,402,"#5a5870",1)
    b+=pr('start','<g transform="translate(108,388) rotate(-25)"><rect x="-19" y="-5" width="38" height="10" rx="5" fill="#34334a"/></g>')
    b+='<g transform="translate(868,368) rotate(-30)" stroke="#8f8c7f" stroke-width="5" stroke-linecap="round">'+''.join(f'<line x1="0" y1="{k*10}" x2="46" y2="{k*10}"/>' for k in range(5))+'</g>'
    return svg(960,450,b,defs,title,desc)
def console(force=None):
    P={'start':[(2.6,2.9)],'a':[(6.2,6.5)],'b':[(27.0,27.3)]}
    return shell(timeline(force),LW,LH,SC,P,D,f"{HANDLE} - handheld profile","Retro handheld: press start, pick the Vihaan Jain player slot, and the profile details open.")

ICONS={
'dawn':["...##...","#..##..#",".#.##.#.","..####..",".######.","########","........","########"],
'db':[".######.","#......#",".######.","#......#",".######.","#......#",".######.","########"],
'chip':["#.#..#.#",".######.","##....##",".#.##.#.",".#.##.#.","##....##",".######.","#.#..#.#"],
'graph':["#.......","#......#","#.....#.","#.##.#..","##..##..","#.......","#.......","########"],
'net':[".##..##.",".##..##.","..####..",".######.","..####..",".##..##.",".##..##.","........"],
'maze':["########","#......#","#.####.#","#.#..#.#","#.#.##.#","#.#....#","#.######","########"],
'cal':["########","#......#","########","#.#.#.##","#......#","#.#.#.##","#......#","########"]}

# ================================================================== SECTIONS
import json, re, math, datetime, urllib.request
PAL5=[L1,'#6b9a15','#4a7d1c',L2,L3]
def svg2(w,h,body,defs='',title=''): return svg(w,h,body,defs+GRID.replace('id="grid"','id="grid"'),title)
def scan(w,h,rx=10):
    return (f'<pattern id="g2" width="3" height="3" patternUnits="userSpaceOnUse"><path d="M3 0V3H0" stroke="{L3}" stroke-opacity=".08" stroke-width=".5" fill="none"/></pattern>',
            f'<rect x="1.5" y="1.5" width="{w-3}" height="{h-3}" rx="{rx}" fill="url(#g2)"/>')
def seq(i,total,dur):
    a,b=i/total,(i+1)/total
    if i==0: kt,v="0;"+n(b),"1;0"
    elif i==total-1: kt,v="0;"+n(a),"0;1"
    else: kt,v="0;%s;%s"%(n(a),n(b)),"0;1;0"
    return f'<animate attributeName="opacity" values="{v}" keyTimes="{kt}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/>'
# ---- section banner
def section(tag,title,w=640,h=None):
    h=h or HDR_HEIGHT; sc=HDR_SCALE; th=7*sc; ty=(h-th)//2
    d,ov=scan(w,h); tb=tw(tag,sc)+20
    b=f'<rect x="1.5" y="1.5" width="{w-3}" height="{h-3}" rx="9" fill="{L0}" stroke="{L3}" stroke-width="3"/>'
    b+=f'<rect x="8" y="7" width="{tb}" height="{h-14}" fill="{L3}"/>'+T(tag,8+(tb-tw(tag,sc))//2,ty,L0,sc)
    b+=T(title,8+tb+17,ty+1,L2,sc)+T(title,8+tb+16,ty,L3,sc)
    if HDR_ARROW: b+=f'<g>{T(HDR_ARROW,w-22-tw(HDR_ARROW,sc),ty,L3,sc)}{blink(.8,"1;0.15")}</g>'
    return svg(w,h,b+ov,d,title)

# ---- cartridge + info plate
# Cartridge tech chips use a larger pixel font and wrap within the plate.
CHIP_SCALE,CHIP_PAD,CHIP_GAP=1.5,10,4
CHIP_H,CHIP_ROW_GAP=16,3
def chip_rows(techs,maxw=256):
    rows=[[]]; x=0
    for t in techs:
        w=tw(t,CHIP_SCALE)+CHIP_PAD
        if x+w>maxw and rows[-1]: rows.append([]); x=0
        rows[-1].append((t,w)); x+=w+CHIP_GAP
    return rows
PLATE_Y=350
def plate_h(maxrows): return 55+maxrows*(CHIP_H+CHIP_ROW_GAP)
def fit_text_scale(text,max_width,preferred=2):
    return min(preferred, max_width/max(1,tw(text,1)))
def cart_h(maxrows): return PLATE_Y+plate_h(maxrows)+8
def cart(title,l1,l2,color,icon,d1,d2,techs,maxrows,locked=False,blurb=""):
    d=GRID+f'''<linearGradient id="cb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#bdbbc8"/><stop offset="1" stop-color="#8b899c"/></linearGradient>
<clipPath id="lab"><rect x="34" y="62" width="212" height="206" rx="8"/></clipPath>'''
    b='<path d="M8 38 L34 12 H246 L272 38 V318 H8 Z" fill="#000" opacity=".16" transform="translate(0,6)"/>'
    b+='<path d="M8 32 L32 8 H248 L272 32 V312 H8 Z" fill="url(#cb)" stroke="#575569" stroke-width="3" stroke-linejoin="round"/>'
    b+='<rect x="44" y="18" width="192" height="30" rx="5" fill="#7a788c"/>'+''.join(f'<rect x="56" y="{23+k*6}" width="168" height="2" fill="#575569"/>' for k in range(4))
    b+=f'<rect x="34" y="62" width="212" height="206" rx="8" fill="{color}" stroke="#1d1c26" stroke-opacity=".6" stroke-width="3"/>'
    b+=f'<rect x="34" y="62" width="212" height="206" rx="8" fill="#fff" opacity=".07"/><rect x="34" y="62" width="212" height="4" fill="#fff" opacity=".18"/>'
    b+='<rect x="42" y="70" width="196" height="28" fill="#17171f"/>'
    title_sc=fit_text_scale(title,184,2)
    b+=T(title,0,77,"#ffffff",title_sc,center=140)
    b+=f'<rect x="50" y="108" width="180" height="88" fill="{L0}" stroke="{L3}" stroke-width="3"/>'
    ic=bmp(ICONS[icon],112,124,7,L3)
    b+=(f'<g>{ic}{blink(1.6,"1;0.35")}</g>' if locked else ic)+f'<rect x="50" y="108" width="180" height="88" fill="url(#grid)"/>'
    b+=T("SOON" if locked else "PLAY",172 if not locked else 168,181,L3,1)+f'<g>{T(">",206,181,L3,1)}{blink(.7)}</g>'
    # Fit long subtitles to the 212px cartridge face instead of letting them spill outside.
    l1_sc=fit_text_scale(l1,204,2); l2_sc=fit_text_scale(l2,204,2)
    b+=T(l1,0,208,"#1d1c26",l1_sc,center=141)+T(l1,0,207,"#ffffff",l1_sc,center=140)
    b+=T(l2,0,232,"#1d1c26",l2_sc,center=141,extra='opacity=".7"')+T(l2,0,231,"#ffffff",l2_sc,center=140,extra='opacity=".85"')
    b+=f'<g clip-path="url(#lab)"><polygon points="0,0 36,0 6,206 -30,206" fill="#fff" opacity=".18"><animateTransform attributeName="transform" type="translate" values="-60 62;320 62;320 62" keyTimes="0;.35;1" dur="5s" repeatCount="indefinite"/></polygon></g>'
    b+='<rect x="40" y="312" width="200" height="22" fill="#2b2a36"/>'+''.join(f'<rect x="{48+k*8}" y="316" width="4" height="14" fill="#d9b84a"/>' for k in range(24))
    # Compact info plate: prominent tagline and tech chips only. Full copy is in More info.
    py=PLATE_Y; ph=plate_h(maxrows)
    b+=f'<rect x="6.5" y="{py+.5}" width="267" height="{ph}" rx="8" fill="{L0}" stroke="{L3}" stroke-width="3"/>'
    b+=T(d1,0,py+13,L2,2,center=141)+T(d1,0,py+12,L3,2,center=140)+T(d2,0,py+31,L2,2,center=141)+T(d2,0,py+30,L3,2,center=140)
    b+=f'<rect x="12" y="{py+48}" width="256" height="1" fill="{L2}"/>'
    for r,row in enumerate(chip_rows(techs)):
        x=12+(256-(sum(w for _,w in row)+CHIP_GAP*(len(row)-1)))/2
        y=py+51+r*(CHIP_H+CHIP_ROW_GAP)
        for t,w in row:
            b+=f'<rect x="{round(x)+.5}" y="{y+.5}" width="{w-1}" height="{CHIP_H-1}" rx="1" fill="{L1}" stroke="{L3}"/>'
            b+=T(t,round(x)+5,y+2,L3,CHIP_SCALE)
            x+=w+CHIP_GAP
    dd,ov=scan(280,ph); b+=f'<rect x="7" y="{py+1}" width="266" height="{ph}" rx="8" fill="url(#g2)"/>'
    return svg(280,cart_h(maxrows),b,d+dd,title)
def cart_empty(maxrows):
    """Empty cartridge slot (dashed outline) - same 280 x cart_h box as a real cartridge."""
    H=cart_h(maxrows); st='#8b899c'
    b=f'<path d="M8 32 L32 8 H248 L272 32 V{H-8} H8 Z" fill="{st}" fill-opacity=".07" stroke="{st}" stroke-width="3" stroke-dasharray="10 7" stroke-linejoin="round"/>'
    b+=f'<rect x="44" y="18" width="192" height="30" rx="5" fill="none" stroke="{st}" stroke-width="2" stroke-dasharray="6 5" opacity=".7"/>'
    b+=f'<rect x="34" y="62" width="212" height="206" rx="8" fill="none" stroke="{st}" stroke-width="2" stroke-dasharray="6 5" opacity=".7"/>'
    plus=["...##...","...##...","...##...","########","########","...##...","...##...","...##..."]
    b+=f'<g>{bmp(plus,112,120,7,st)}{blink(1.6,"1;0.35")}</g>'
    b+=T("EMPTY SLOT",0,200,st,2,center=140)+T("NEXT PROJECT",0,226,st,1,center=140)+T("INSERT CARTRIDGE",0,240,st,1,center=140,extra='opacity=".7"')
    b+=''.join(f'<rect x="{48+k*8}" y="316" width="4" height="14" fill="{st}" opacity=".35"/>' for k in range(24))
    return svg(280,H,b,'',"Empty slot")

def maxrows_of(projects): return max(len(chip_rows(p[9])) for p in projects)
# ---- tech stack inventory
def stack(cats,w=960):
    d,_=scan(w,10)
    allc=[t for _,items in cats for t in items]; M=len(allc); dur=round(M*0.3,2)
    pad=22; lx=pad; cx0=pad+230; maxx=w-pad
    # layout
    blocks=[]; y=pad
    for name,items in cats:
        x=cx0; row=0; pos=[]
        for t in items:
            cw=tw(t,2)+18
            if x+cw>maxx: x=cx0; row+=1
            pos.append((t,x,row,cw)); x+=cw+8
        h=(row+1)*34+10; blocks.append((name,items,pos,y,h)); y+=h+14
    H=y-14+pad
    b=f'<rect x="1.5" y="1.5" width="{w-3}" height="{H-3}" rx="10" fill="{L0}" stroke="{L3}" stroke-width="3"/>'
    idx=0
    for bi,(name,items,pos,by,bh) in enumerate(blocks):
        b+=f'<rect x="{lx}" y="{by+5}" width="206" height="28" fill="{L3}"/>'+T(name,lx+10,by+12,L0,2)
        b+=T(f"ITEMS x{len(items)}",lx+4,by+40,L2,1)
        for t,x,row,cw in pos:
            y0=by+5+row*34; lock=(t=="???")
            fill=L1
            base=f'<rect x="{x+.5}" y="{y0+.5}" width="{cw-1}" height="27" fill="{fill}" stroke="{L3}"/>'
            txt=T(t,x+9,y0+7,L2 if lock else L3,2)
            b+=f'<g>{base}{txt}{blink(1.2,"1;0.25")}</g>' if lock else base+txt
            ov=f'<rect x="{x}" y="{y0}" width="{cw}" height="28" fill="{L3}"/>'+T(t,x+9,y0+7,L0,2)
            b+=f'<g opacity="0">{seq(idx,M,dur)}{ov}</g>'; idx+=1
        if bi<len(blocks)-1: b+=f'<rect x="{pad}" y="{by+bh+6}" width="{w-2*pad}" height="2" fill="{L2}" opacity=".5"/>'
    dd,ov2=scan(w,H); b+=ov2
    return svg(w,H,b,d+dd,"Tech stack")
# ---- activity / hi-score
def fetch_activity(user):
    h=urllib.request.urlopen(urllib.request.Request(f"https://github.com/users/{user}/contributions",headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read().decode('utf-8','ignore')
    cells=re.findall(r'data-date="([\d-]+)"[^>]*data-level="(\d)"',h)
    tips=re.findall(r'<tool-tip[^>]*>([^<]+)</tool-tip>',h)
    if not cells or len(cells)!=len(tips): raise RuntimeError("parse failed")
    out=[]
    for (dt,lv),tp in zip(cells,tips):
        m=re.match(r'(\d+) contribution',tp); out.append([dt,int(m.group(1)) if m else 0,int(lv)])
    return sorted(out)
def activity(days,w=960):
    first=datetime.date.fromisoformat(days[0][0]); off=(first.weekday()+1)%7
    ncol=(off+len(days)+6)//7
    total=sum(d[1] for d in days); best=max((d[1] for d in days),default=0); active=sum(1 for d in days if d[1]>0)
    cur=0
    for d in reversed(days[:-1] if days[-1][1]==0 else days):
        if d[1]>0: cur+=1
        else: break
    lng=run=0
    for d in days:
        run=run+1 if d[1]>0 else 0; lng=max(lng,run)
    cs,gp=14,3; pitch=cs+gp; x0=(w-(ncol*pitch-gp))//2; y0=122; H=292
    dd,_=scan(w,H)
    b=f'<rect x="1.5" y="1.5" width="{w-3}" height="{H-3}" rx="10" fill="{L0}" stroke="{L3}" stroke-width="3"/>'
    b+=T("PLAYER STATS",x0,18,L2,2)+T("PLAYER STATS",x0-1,17,L3,2)
    lg=w-x0-(5*(cs+3)+tw("MORE",1)+tw("LESS",1)+16)
    b+=T("LESS",lg,22,L2,1); 
    for k in range(5): b+=f'<rect x="{lg+tw("LESS",1)+6+k*(cs+3)}" y="19" width="{cs}" height="{cs-3}" fill="{PAL5[k]}"/>'
    b+=T("MORE",lg+tw("LESS",1)+10+5*(cs+3),22,L2,1)
    boxes=[(SCORE_LABELS["score"],str(total)),(SCORE_LABELS["best"],str(best)),(SCORE_LABELS["streak"],str(cur)),(SCORE_LABELS["maxstreak"],str(lng))]
    bw=(ncol*pitch-gp-3*18)//4
    for i,(k,v) in enumerate(boxes):
        x=x0+i*(bw+18)
        b+=f'<rect x="{x}" y="42" width="{bw}" height="58" fill="{L1}" stroke="{L3}" stroke-width="2"/>'+T(k,x+10,50,L2,2)+T(v,x+10,70,L3,3)
    # months
    last=-9
    for i,(dt,_,_) in enumerate(days):
        dte=datetime.date.fromisoformat(dt)
        if dte.day<=7 and (off+i)%7==0 or i==0:
            c=(off+i)//7
            if c-last>=3: b+=T(dte.strftime("%b"),x0+c*pitch,108,L2,1); last=c
    cells_static='';cells_anim=''
    for i,(dt,cnt,lv) in enumerate(days):
        c,r=(off+i)//7,(off+i)%7; x,y=x0+c*pitch,y0+r*pitch
        if lv==0: cells_static+=f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{L1}"/>'
        else: cells_anim+=(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{PAL5[lv]}">'
                           f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{n(round((c+1)/ncol*0.72,4))};0.95" calcMode="discrete" dur="16s" repeatCount="indefinite"/></rect>')
    b+=cells_static+cells_anim
    # runner
    ty=y0+7*pitch+4
    b+=f'<rect x="{x0}" y="{ty+14}" width="{ncol*pitch-gp}" height="2" fill="{L2}" opacity=".6"/>'
    fx=x0+(ncol-1)*pitch
    b+=f'<rect x="{fx+10}" y="{ty-2}" width="2" height="18" fill="{L3}"/><path d="M{fx+12} {ty-2}h8v6h-8z" fill="#c8443f"/>'
    A=["..####..","##.##.##","########",".######.","..#..#..",".##..##."]; B=["..####..","##.##.##","########",".######.","..####..","..#..#.."]
    kt=';'.join(n(round(c/ncol*0.72,4)) for c in range(ncol)); vals=';'.join(f"{x0+c*pitch} 0" for c in range(ncol))
    b+=(f'<g><animate attributeName="opacity" values="1;0" keyTimes="0;0.74" calcMode="discrete" dur="16s" repeatCount="indefinite"/>'
        f'<animateTransform attributeName="transform" type="translate" values="{vals}" keyTimes="{kt}" calcMode="discrete" dur="16s" repeatCount="indefinite"/>'
        f'<g transform="translate(0,{ty})"><g>{bmp(A,0,0,2,L3)}{blink(.3,"1;0")}</g><g>{bmp(B,0,0,2,L3)}{blink(.3,"0;1")}</g></g></g>')
    b+=T(f"{active} ACTIVE DAYS  -  SAVED {days[-1][0]}",x0,H-22,L2,1)
    dd2,ov=scan(w,H); b+=ov
    return svg(w,H,b,dd+dd2,"Contribution high-score")
# ---- contact buttons
def contact_cartridge(label):
    """Render one independently clickable contact cartridge."""
    masks = {
        "GITHUB": [
            "000000000111111000000000",
            "000000111111111110000000",
            "000001111111111111100000",
            "000011111111111111110000",
            "000111111111111111111000",
            "001111011111111110111100",
            "011111000100001000111100",
            "011111000000000000111110",
            "011111000000000000111110",
            "111110000000000000011111",
            "111110000000000000011111",
            "111110000000000000011111",
            "111110000000000000011111",
            "111110000000000000011111",
            "011111000000000000111110",
            "011111100000000001111110",
            "011101111100001111111110",
            "001110111000000111111100",
            "001111000000000111111100",
            "000111111000000111111000",
            "000011111000000111110000",
            "000001111000000111100000",
            "000000011000000110000000",
            "000000000000000000000000",
        ],
        "EMAIL": [
            "000000000000000000000000",
            "000000000000000000000000",
            "000000000000000000000000",
            "011111111111111111111110",
            "111111111111111111111111",
            "111000000000000000000111",
            "110000000000000000000011",
            "111000000000000000000111",
            "111100000000000000001111",
            "111110000000000000011111",
            "111111100000000001111111",
            "110011110000000011110011",
            "110001111000000111100011",
            "110000111100001111000011",
            "110000001111111100000011",
            "110000000111111000000011",
            "110000000001100000000011",
            "110000000000000000000011",
            "111000000000000000000111",
            "111111111111111111111111",
            "011111111111111111111110",
            "000000000000000000000000",
            "000000000000000000000000",
            "000000000000000000000000",
        ],
        "LINKEDIN": [
            "000000000000000000000000",
            "001111111111111111111100",
            "011111111111111111111110",
            "011111111111111111111110",
            "011111111111111111111110",
            "011110001111111111111110",
            "011110001111111111111110",
            "011110011111111111111110",
            "011111111111111111111110",
            "011111111111111001111110",
            "011110001100000000011110",
            "011110001100000000011110",
            "011110001100011100011110",
            "011110001100011110011110",
            "011110001100011110011110",
            "011110001100011110011110",
            "011110001100011110011110",
            "011110001100011110011110",
            "011110001100011110011110",
            "011111111111111111111110",
            "011111111111111111111110",
            "011111111111111111111110",
            "001111111111111111111100",
            "000000000000000000000000",
        ],
        "DISCORD": [
            "000000000000000000000000",
            "000000000000000000000000",
            "000000000000000000000000",
            "000000001000000100000000",
            "000001111111111111100000",
            "000011111111111111110000",
            "000111111111111111111000",
            "000111111111111111111000",
            "001111111111111111111100",
            "001111111111111111111100",
            "001111111111111111111100",
            "011111100011110001111110",
            "011111100011110001111110",
            "011111100011110001111110",
            "011111100111111001111110",
            "011111111111111111111110",
            "011111111111111111111110",
            "011111111111111111111110",
            "001111110011110011111100",
            "000011100000000001110000",
            "000000000000000000000000",
            "000000000000000000000000",
            "000000000000000000000000",
            "000000000000000000000000",
        ],
        "PORTFOLIO": [
            "000000000001100000000000",
            "000000110011110011000000",
            "000011110111111011110000",
            "000111110111111011111000",
            "001111101111111101111100",
            "001111101111111101111100",
            "011111101111111101111110",
            "011111001111111100111110",
            "000000000000000000000000",
            "111111011111111110111111",
            "111111011111111110111111",
            "111111011111111110111111",
            "111111011111111110111111",
            "111111011111111110111111",
            "111111011111111110111111",
            "000000000000000000000000",
            "011111001111111100111110",
            "011111101111111101111110",
            "001111101111111101111100",
            "001111101111111101111100",
            "000111110111111011111000",
            "000011110111111011110000",
            "000000110011110011000000",
            "000000000001100000000000",
        ],
    }
    w,h=176,132
    b=f'<path d="M12 2 H164 L174 14 V126 Q174 130 170 130 H6 Q2 130 2 126 V14 Z" fill="#7c7a8c" stroke="#343344" stroke-width="3"/>'
    b+=f'<rect x="10" y="14" width="156" height="68" rx="4" fill="{L1}" stroke="{L3}" stroke-width="2"/>'
    b+=f'<rect x="18" y="22" width="140" height="52" fill="{L0}" stroke="{L2}" stroke-width="1"/>'
    scale=2; ix=(w-24*scale)//2; iy=26
    for ry,row in enumerate(masks[label]):
        for rx,pixel in enumerate(row):
            if pixel=="1":
                b+=f'<rect x="{ix+rx*scale}" y="{iy+ry*scale}" width="{scale}" height="{scale}" fill="{L3}"/>'
    b+=f'<rect x="14" y="90" width="148" height="24" fill="{L3}"/>'
    b+=T(label, w//2, 95, L0, 1, center=w//2)
    for px in (22,146):
        b+=f'<rect x="{px}" y="119" width="8" height="3" fill="{L3}"/>'
    return svg(w,h,b,title=label.title()+" contact cartridge",desc=label.title()+" contact link cartridge with pixelated service logo.")


def button(label,icon):
    w,h=tw(label,2)+48+16+16+22,56
    d,ov=scan(w,h,12)
    b=f'<rect x="3" y="6" width="{w-3}" height="{h-6}" rx="12" fill="{L3}" opacity=".35"/>'
    b+=f'<rect x="1.5" y="1.5" width="{w-6}" height="{h-9}" rx="12" fill="{L0}" stroke="{L3}" stroke-width="3"/>'
    b+=f'<rect x="10" y="10" width="46" height="{h-27}" fill="{L3}"/>'+T(icon,0,(h-9-14)//2+0,L0,2,center=33)
    b+=T(label,68,(h-9-14)//2,L3,2)+f'<g>{T(">",w-28,(h-9-14)//2,L3,2)}{blink(.8,"1;0.1")}</g>'
    return svg(w,h,b,d,label)


# ================================================================== SECTION SHELLS (same handheld, different screen)
def stack_shell(cats, logos=None):
    """RPG loadout screen on the same 320x176 LCD (640x352 on screen) as the title/profile screens.
    One row per category: label tab + brand-coloured monogram chips that wrap inside their row."""
    LWs,LHs,SCs=LW,LH,SC
    logos=logos or {}
    CH,PITCH,LABW,X0=11,13,58,6
    cx0=X0+LABW+4; avail=LWs-X0-3-cx0          # chip area (x from cx0, width avail)
    rows=[]
    for name,items in cats:
        x=0; ln=0; pos=[]
        for it in items:
            cw=13+3+tw(it,1)+2
            if x+cw>avail and x>0: x=0; ln+=1
            pos.append((it,x,ln,cw)); x+=cw+2
        rows.append((name,items,pos,ln+1))
    top=15; bot=LHs-4; rh=[l*PITCH+3 for *_,l in rows]
    gap=min(5,(bot-top-sum(rh))//max(1,len(rows)-1))
    if sum(rh)+gap*(len(rows)-1)>bot-top: print("WARNING: loadout rows overflow the LCD - remove an item or category")
    dur=10.0; per=dur/len(rows)
    base=""; sel=""; P={"down":[]}
    y=top
    for i,(name,items,pos,lines) in enumerate(rows):
        h=rh[i]
        base+=f'<rect x="{X0+.5}" y="{y+.5}" width="{LWs-2*X0-1}" height="{h-1}" fill="{L1}" stroke="{L2}"/>'
        base+=f'<rect x="{X0+1}" y="{y+1}" width="{LABW-1}" height="{h-2}" fill="{L3}"/>'
        lab=STACK_SHORT.get(name,name)
        base+=T(lab,X0+1,y+(h-7)//2,L0,1,center=X0+1+(LABW-1)/2)
        for it,px,ln,cw in pos:
            mono,bg,fg=STACK_BRAND.get(it,(it[:1],L2,L0))
            x=cx0+px; yy=y+2+ln*PITCH
            base+=f'<rect x="{x+.5}" y="{yy+.5}" width="{cw-1}" height="{CH-1}" fill="{L0}" stroke="{L2}" stroke-width=".7"/>'
            base+=f'<rect x="{x+1}" y="{yy+1}" width="13" height="{CH-2}" fill="{bg}"/>'
            paths=logos.get(it,())
            if paths:
                base+=f'<g transform="translate({x+2.5} {yy+1.5}) scale(.38)" fill="{fg}">'+''.join(f'<path d="{d}"/>' for d in paths)+'</g>'
            else:
                base+=T(mono,x+1+(13-tw(mono,1))/2,yy+2,fg,1)
            base+=T(it,x+17,yy+2,L3,1)
        w0=i*per
        sel+=f'<g opacity="0">{anim([(w0,w0+per)],dur)}<rect x="{X0+.5}" y="{y+.5}" width="{LWs-2*X0-1}" height="{h-1}" fill="none" stroke="{L3}" stroke-width="2"/>{blink(.7,"1;0.4")}</g>'
        P["down"].append((w0+per-.2,w0+per))
        y+=h+gap
    n_items=sum(len(it) for _,it in cats)
    header=lcd_head("EQUIPPED",f"{n_items} ITEMS")
    P["down"]=P["down"][:-1]
    return shell(header+base+sel,LWs,LHs,SCs,P,dur,"Equipment loadout","RPG-style loadout screen listing languages, frontend, backend and databases, tools and platforms, and AI/ML and data tools.")

def activity_shell(days):
    LWa,LHa=366,201; SCa=640/LWa
    dur=16.0
    first=datetime.date.fromisoformat(days[0][0]); off=(first.weekday()+1)%7
    ncol=(off+len(days)+6)//7
    total=sum(d[1] for d in days); best=max((d[1] for d in days),default=0); active=sum(1 for d in days if d[1]>0)
    cur=0
    for d in reversed(days[:-1] if days[-1][1]==0 else days):
        if d[1]>0: cur+=1
        else: break
    lng=run=0
    for d in days:
        run=run+1 if d[1]>0 else 0; lng=max(lng,run)
    s=''
    gap=6; bw=(LWa-16-3*gap)//4; bx0=(LWa-(4*bw+3*gap))//2
    for i,(k,v) in enumerate([(SCORE_LABELS["score"],str(total)),(SCORE_LABELS["best"],str(best)),(SCORE_LABELS["streak"],str(cur)),(SCORE_LABELS["maxstreak"],str(lng))]):
        x=bx0+i*(bw+gap)
        s+=f'<rect x="{x+.5}" y="8.5" width="{bw-1}" height="29" fill="{L1}" stroke="{L3}"/>'+T(k,x+4,12,L2,1)+T(v,x+4,22,L3,2)
    pitch,cs=6,5; x0=(LWa-(ncol*pitch-1))//2; y0=55
    last=-9
    for i,(dt,_,_) in enumerate(days):
        dte=datetime.date.fromisoformat(dt)
        if (dte.day<=7 and (off+i)%7==0) or i==0:
            c=(off+i)//7
            if c-last>=5: s+=T(dte.strftime("%b"),x0+c*pitch,45,L2,1); last=c
    st='';an=''
    for i,(dt,cnt,lv) in enumerate(days):
        c,r=(off+i)//7,(off+i)%7; x,y=x0+c*pitch,y0+r*pitch
        if lv==0: st+=f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{L1}"/>'
        else: an+=(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{PAL5[lv]}"><animate attributeName="opacity" values="0;1;0" '
                   f'keyTimes="0;{n(round((c+1)/ncol*0.72,4))};0.95" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/></rect>')
    s+=st+an
    ty=y0+7*pitch+3
    s+=f'<rect x="{x0}" y="{ty+7}" width="{ncol*pitch-1}" height="1" fill="{L2}" opacity=".7"/>'
    fx=x0+(ncol-1)*pitch
    s+=f'<rect x="{fx+3}" y="{ty-1}" width="1" height="9" fill="{L3}"/><rect x="{fx+4}" y="{ty-1}" width="4" height="3" fill="#c8443f"/>'
    kt=';'.join(n(round(c/ncol*0.72,4)) for c in range(ncol)); vals=';'.join(f"{x0+c*pitch} 0" for c in range(ncol))
    s+=(f'<g><animate attributeName="opacity" values="1;0" keyTimes="0;0.74" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/>'
        f'<animateTransform attributeName="transform" type="translate" values="{vals}" keyTimes="{kt}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/>'
        f'<g transform="translate(0,{ty})"><g>{bmp(SPR_A,0,0,1,L3)}{blink(.3,"1;0")}</g><g>{bmp(SPR_B,0,0,1,L3)}{blink(.3,"0;1")}</g></g></g>')
    # monthly bars (last 12 months)
    months={}
    for dt,cnt,_ in days:
        m=dt[:7]; months[m]=months.get(m,0)+cnt
    keys=sorted(months)[-12:]; mx=max([months[k] for k in keys] or [1]) or 1
    s+=T(SCORE_LABELS["monthly"],x0,112,L2,1)
    base_y=168; bwid=18; mp=(ncol*pitch-1)/12
    for i,k in enumerate(keys):
        h=max(1,round(months[k]/mx*38)) if months[k] else 1
        x=round(x0+i*mp+(mp-bwid)/2)
        s+=f'<rect x="{x}" y="{base_y-h}" width="{bwid}" height="{h}" fill="{L3 if months[k] else L2}"/>'
        s+=T(datetime.date.fromisoformat(k+"-01").strftime("%b"),x+(bwid-17)/2,base_y+4,L2,1)
        if months[k]: s+=T(str(months[k]),x+(bwid-tw(str(months[k]),1))/2,base_y-h-8,L3,1)
    s+=T(f"{active} ACTIVE DAYS",0,LHa-12,L2,1,center=LWa/2)
    P={'a':[(0.2,0.5)],'right':[(0.5,11.5)]}
    return shell(s,LWa,LHa,SCa,P,dur,"GitHub contribution hi-score","Handheld screen with the contribution heatmap, a runner that unlocks each week, and monthly totals.")
