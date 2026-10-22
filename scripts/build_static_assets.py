"""Regenerates the hand-made SVGs in assets/ (hero, whoami, services). Run: python3 scripts/build_static_assets.py"""
T={"dark":dict(bg2="#06090f",panel="#161b22",fg="#ffffff",sub="#00b4ff",mut="#8b949e",grid="0,180,255",line="#30363d",k="#ff7b72",v="#d2a8ff",p="#ffa657",s="#a5d6ff",bar="#21262d",hi="#a5e3ff"),
   "light":dict(bg2="#f0f8ff",panel="#f6f8fa",fg="#0b2a4a",sub="#1f6feb",mut="#57606a",grid="31,111,235",line="#d0d7de",k="#cf222e",v="#8250df",p="#953800",s="#0a3069",bar="#eaeef2",hi="#1f6feb")}
FONT="'Segoe UI',Helvetica,Arial,sans-serif";MONO="'Fira Code',Consolas,Menlo,monospace"
def hero(c):
  vl="".join(f'<line x1="{450+(i-12)*18}" y1="140" x2="{450+(i-12)*140}" y2="260"/>' for i in range(25))
  hl="".join(f'<line x1="0" x2="900" y1="{y}" y2="{y}"/>' for y in (140,150,163,180,202,230,260))
  return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="240" viewBox="0 0 900 240" role="img" aria-label="Fred Kamm - Full-Stack Web Developer and IT Consultant">
<style>
.glow{{animation:pulse 6s ease-in-out infinite}}@keyframes pulse{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
.grid{{animation:scroll 3s linear infinite}}@keyframes scroll{{from{{transform:translateY(0)}}to{{transform:translateY(22px)}}}}
.name{{animation:rise 1.2s ease-out both}}.sub{{animation:rise 1.2s .4s ease-out both}}@keyframes rise{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
.scan{{animation:scan 5s linear infinite}}@keyframes scan{{from{{transform:translateX(-300px)}}to{{transform:translateX(1200px)}}}}
</style>
<defs>
<radialGradient id="a" cx="20%" cy="0%" r="70%"><stop offset="0" stop-color="#00b4ff" stop-opacity=".45"/><stop offset="1" stop-color="#00b4ff" stop-opacity="0"/></radialGradient>
<radialGradient id="b" cx="85%" cy="100%" r="60%"><stop offset="0" stop-color="#1f6feb" stop-opacity=".4"/><stop offset="1" stop-color="#1f6feb" stop-opacity="0"/></radialGradient>
<linearGradient id="t" x1="0" x2="1"><stop offset="0" stop-color="{c["fg"]}"/><stop offset=".6" stop-color="{c["hi"]}"/><stop offset="1" stop-color="#00b4ff"/></linearGradient>
<linearGradient id="s" x1="0" x2="1"><stop offset="0" stop-color="#00b4ff" stop-opacity="0"/><stop offset=".5" stop-color="#00b4ff" stop-opacity=".18"/><stop offset="1" stop-color="#00b4ff" stop-opacity="0"/></linearGradient>
<clipPath id="r"><rect width="900" height="240" rx="14"/></clipPath></defs>
<g clip-path="url(#r)"><rect width="900" height="240" fill="{c["bg2"]}"/>
<rect class="glow" width="900" height="240" fill="url(#a)"/><rect width="900" height="240" fill="url(#b)"/>
<g stroke="rgb({c["grid"]})" stroke-opacity=".22">{vl}<g class="grid">{hl}</g></g>
<rect class="scan" width="260" height="240" fill="url(#s)"/>
<text class="name" x="450" y="118" text-anchor="middle" font-family="{FONT}" font-size="62" font-weight="800" letter-spacing="8" fill="url(#t)">FRED KAMM</text>
<text class="sub" x="450" y="158" text-anchor="middle" font-family="{MONO}" font-size="16" letter-spacing="3" fill="{c["sub"]}">FULL-STACK WEB DEVELOPER · IT CONSULTANT</text>
</g><rect width="899" height="239" x=".5" y=".5" rx="14" fill="none" stroke="{c["line"]}"/></svg>'''
def term(c):
  L=[[("$ ","#00b4ff"),("whoami",c["fg"])],[("const ",c["k"]),("fred",c["v"]),(" = {",c["fg"])],
   [("  role",c["p"]),(": ",c["fg"]),('"Full-Stack Web Developer"',c["s"]),(",",c["fg"])],
   [("  company",c["p"]),(": ",c["fg"]),('"Proactive Performance Solutions Inc."',c["s"]),(",",c["fg"])],
   [("  location",c["p"]),(": ",c["fg"]),('"Pennsylvania"',c["s"]),(",",c["fg"])],
   [("  focus",c["p"]),(": [",c["fg"]),('"client websites", "IT consulting", "edge apps"',c["s"]),("],",c["fg"])],
   [("  stack",c["p"]),(": [",c["fg"]),('"React", "TypeScript", "Node", "Cloudflare"',c["s"]),("],",c["fg"])],
   [("  nerdingOut",c["p"]),(": ",c["fg"]),('"fantasy sports data"',c["s"]),(",",c["fg"])],
   [("  onGitHub",c["p"]),(": ",c["fg"]),('"since 2022"',c["s"])],[("};",c["fg"])]]
  rows=[];cw=8.6
  for i,l in enumerate(L):
    n=sum(len(x) for x,_ in l);y=72+i*24;d=0.3+i*0.45
    sp="".join(f'<tspan fill="{col}">{x}</tspan>' for x,col in l)
    rows.append(f'<clipPath id="c{i}"><rect x="24" y="{y-17}" height="24" width="0"><animate attributeName="width" from="0" to="{n*cw+6:.0f}" begin="{d:.2f}s" dur="{max(.25,n*0.012):.2f}s" fill="freeze"/></rect></clipPath><text x="28" y="{y}" clip-path="url(#c{i})" xml:space="preserve">{sp}</text>')
  last=72+(len(L)-1)*24;H=last+28
  return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{H}" viewBox="0 0 900 {H}" role="img" aria-label="whoami: Fred Kamm, Full-Stack Web Developer at Proactive Performance Solutions Inc., Pennsylvania">
<style>text{{font-family:{MONO};font-size:14px}}.cur{{animation:b 1s step-end infinite}}@keyframes b{{50%{{opacity:0}}}}</style>
<rect x=".5" y=".5" width="899" height="{H-1}" rx="10" fill="{c["panel"]}" stroke="{c["line"]}"/>
<path d="M1 11a10 10 0 0 1 10-10h878a10 10 0 0 1 10 10v27H1z" fill="{c["bar"]}"/>
<circle cx="22" cy="19" r="6" fill="#ff5f56"/><circle cx="42" cy="19" r="6" fill="#ffbd2e"/><circle cx="62" cy="19" r="6" fill="#27c93f"/>
<text x="84" y="24" fill="{c["mut"]}" style="font-size:12px">fred@kamm: ~</text>
{"".join(rows)}
<g opacity="0"><animate attributeName="opacity" to="1" begin="{0.3+(len(L)-1)*0.45+0.3:.2f}s" dur="0.01s" fill="freeze"/><rect class="cur" x="{28+2*cw+2:.0f}" y="{last-14}" width="9" height="18" fill="#00b4ff"/></g>
</svg>'''
def services(c):
  it=[("Full-Stack Web Apps","React &amp; TypeScript front ends,","Node and edge APIs"),("IT Consulting","Through Proactive Performance","Solutions Inc."),("Client Websites","Fast, SEO-ready sites for","small businesses"),("Edge &amp; Data","Cloudflare Workers, D1,","API integrations")]
  ic=['<rect x="0" y="2" width="28" height="19" rx="3"/><path d="M9 26h10M14 21v5"/>','<rect x="3" y="0" width="22" height="26" rx="2"/><path d="M8 6h4M16 6h4M8 12h4M16 12h4M12 26v-6h4v6"/>','<circle cx="14" cy="13" r="12"/><path d="M2 13h24M14 1c5 5 5 19 0 24M14 1c-5 5-5 19 0 24"/>','<path d="M16 0 4 15h10l-2 12 12-16h-10z"/>']
  g="".join(f'<g transform="translate({i*225},0)"><rect x=".5" y=".5" width="213" height="139" rx="10" fill="{c["panel"]}" stroke="{c["line"]}"/><rect x="16" width="181" height="2" fill="#00b4ff"><animate attributeName="opacity" values=".35;1;.35" dur="4s" begin="{i*.6}s" repeatCount="indefinite"/></rect><g transform="translate(18,20)" fill="none" stroke="#00b4ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">{ic[i]}</g><text x="18" y="80" font-family="{FONT}" font-weight="700" font-size="15" fill="{c["fg"]}">{a}</text><text x="18" y="102" font-family="{FONT}" font-size="12.5" fill="{c["mut"]}">{b}</text><text x="18" y="120" font-family="{FONT}" font-size="12.5" fill="{c["mut"]}">{d}</text></g>' for i,(a,b,d) in enumerate(it))
  return f'<svg xmlns="http://www.w3.org/2000/svg" width="889" height="140" viewBox="0 0 889 140" role="img" aria-label="What I do: full-stack web apps, IT consulting, client websites, edge and data">{g}</svg>'
if __name__=="__main__":
  import os;os.chdir(os.path.join(os.path.dirname(__file__),".."))
  for t,c in T.items():
    for n,f in [("hero",hero),("whoami",term),("services",services)]:
      open(f"assets/{n}-{t}.svg","w",encoding="utf-8").write(f(c))
