"""Draws a 31-day contribution activity graph (dark + light SVG) from GitHub's GraphQL API.
Uses only the Python standard library. Output: generated/activity-dark.svg, generated/activity-light.svg"""
import json, os, re, sys, urllib.request, datetime as dt

USER = os.environ.get("USERNAME", "fredkamm")
TOKEN = os.environ.get("GITHUB_TOKEN")
DAYS = 31

def fetch_public():
    """Token-free fallback: parse the public contributions calendar HTML."""
    req = urllib.request.Request(f"https://github.com/users/{USER}/contributions", headers={"User-Agent": "activity-graph"})
    html = urllib.request.urlopen(req).read().decode()
    ids = dict(re.findall(r'data-date="(\d{4}-\d{2}-\d{2})" id="([^"]+)"', html))
    tips = dict(re.findall(r'<tool-tip[^>]*for="([^"]+)"[^>]*>([^<]*)', html))
    days = []
    for date, cid in sorted(ids.items()):
        m = re.match(r"(\d+) contribution", tips.get(cid, ""))
        days.append({"date": date, "contributionCount": int(m.group(1)) if m else 0})
    if not days:
        sys.exit("could not parse public contributions calendar")
    return days[-DAYS:]

def fetch():
    if not TOKEN:
        return fetch_public()
    to = dt.datetime.now(dt.timezone.utc)
    frm = to - dt.timedelta(days=DAYS - 1)
    q = """query($u:String!,$f:DateTime!,$t:DateTime!){user(login:$u){contributionsCollection(from:$f,to:$t){
      contributionCalendar{weeks{contributionDays{date contributionCount}}}}}}"""
    body = json.dumps({"query": q, "variables": {"u": USER, "f": frm.isoformat(), "t": to.isoformat()}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", body,
                                 {"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"})
    data = json.load(urllib.request.urlopen(req))
    if "errors" in data:
        sys.exit(f"GraphQL error: {data['errors']}")
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    return days[-DAYS:]

THEMES = {
    "dark": dict(bg="#0d1117", panel="#161b22", border="#30363d", grid="#21262d", text="#8b949e", title="#e6edf3", line="#00b4ff", dot="#a5e3ff"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", border="#d0d7de", grid="#e6ebf1", text="#57606a", title="#0b2a4a", line="#1f6feb", dot="#0f4c8a"),
}

def svg(days, c):
    W, H, L, R, T, B = 900, 240, 50, 20, 50, 40
    counts = [d["contributionCount"] for d in days]
    top = max(4, max(counts))
    pw, ph = W - L - R, H - T - B
    xs = [L + i * pw / (len(days) - 1) for i in range(len(days))]
    ys = [T + ph - v / top * ph for v in counts]
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    grid = "".join(f'<line x1="{L}" x2="{W-R}" y1="{T+ph*k/4:.1f}" y2="{T+ph*k/4:.1f}" stroke="{c["grid"]}"/>'
                   f'<text x="{L-8}" y="{T+ph*k/4+4:.1f}" text-anchor="end">{round(top*(1-k/4))}</text>' for k in range(5))
    labels = "".join(f'<text x="{xs[i]:.1f}" y="{H-B+18}" text-anchor="middle">{days[i]["date"][5:]}</text>' for i in range(0, len(days), 5))
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{c["dot"]}"/>' for x, y in zip(xs, ys))
    total = sum(counts)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{USER} contributions, last {DAYS} days: {total}">
<style>text{{font-family:'Segoe UI',Helvetica,Arial,sans-serif;font-size:11px;fill:{c["text"]}}}.t{{font-size:15px;font-weight:700;fill:{c["title"]}}}
.ln{{stroke-dasharray:3000;stroke-dashoffset:3000;animation:d 2.5s ease-out forwards}}@keyframes d{{to{{stroke-dashoffset:0}}}}</style>
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c["line"]}" stop-opacity=".35"/><stop offset="1" stop-color="{c["line"]}" stop-opacity="0"/></linearGradient></defs>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="10" fill="{c["panel"]}" stroke="{c["border"]}"/>
<text class="t" x="{L}" y="30">Contributions · last {DAYS} days</text><text x="{W-R}" y="30" text-anchor="end">{total} total</text>
{grid}{labels}
<polygon points="{xs[0]:.1f},{T+ph} {pts} {xs[-1]:.1f},{T+ph}" fill="url(#g)"/>
<polyline class="ln" points="{pts}" fill="none" stroke="{c["line"]}" stroke-width="2.5" stroke-linejoin="round"/>{dots}
</svg>'''

if __name__ == "__main__":
    days = fetch()
    if len(days) < 2:
        sys.exit("not enough contribution data")
    os.makedirs("generated", exist_ok=True)
    for name, c in THEMES.items():
        with open(f"generated/activity-{name}.svg", "w", encoding="utf-8") as f:
            f.write(svg(days, c))
    print("wrote generated/activity-*.svg for", len(days), "days")
