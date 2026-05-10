import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    "Sacred Geometry": "work-sacred-geometry.html",
    "The Covenant Series": "work-covenant.html",
    "Divine Proportion": "work-divine.html",
    "Aura": "work-aura.html",
    "Lumina": "work-lumina.html",
    "Nexus": "work-nexus.html",
    "TITHES": "work-tithes.html",
    "ALTAR": "work-altar.html",
    "EPISTLE": "work-epistle.html",
}

for title, href in mapping.items():
    pattern = re.compile(rf'(<a href=")([^"]+)(" class="work-card">)(.*?<h3 class="work-title">{re.escape(title)}</h3>)', re.DOTALL)
    content = pattern.sub(rf'\1{href}\3\4', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html links.")
