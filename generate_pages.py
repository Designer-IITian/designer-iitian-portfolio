import os

projects = [
    {"file": "work-sacred-geometry.html", "title": "Sacred Geometry", "category": "BRAND IDENTITY", "year": "2024"},
    {"file": "work-covenant.html", "title": "The Covenant Series", "category": "EDITORIAL DESIGN", "year": "2024"},
    {"file": "work-divine.html", "title": "Divine Proportion", "category": "VISUAL SYSTEM", "year": "2023"},
    {"file": "work-aura.html", "title": "Aura", "category": "BRAND STRATEGY", "year": "2023"},
    {"file": "work-lumina.html", "title": "Lumina", "category": "PRINT LAYOUT", "year": "2022"},
    {"file": "work-nexus.html", "title": "Nexus", "category": "DIGITAL IDENTITY", "year": "2024"},
    {"file": "work-tithes.html", "title": "TITHES", "category": "PACKAGING DESIGN", "year": "2023"},
    {"file": "work-altar.html", "title": "ALTAR", "category": "SPATIAL BRANDING", "year": "2023"},
    {"file": "work-epistle.html", "title": "EPISTLE", "category": "PRINT DESIGN", "year": "2022"},
]

with open('work-detail.html', 'r', encoding='utf-8') as f:
    template = f.read()

for p in projects:
    new_content = template
    
    # Replace title
    new_content = new_content.replace(
        '<title>Sacred Geometry - Designer IITian</title>',
        f'<title>{p["title"]} - Designer IITian</title>'
    )
    
    # Replace Hero Title
    new_content = new_content.replace(
        '<h1 class="hero-title" style="font-size: 88px; margin-bottom: 24px;">Sacred Geometry<span class="dot">.</span></h1>',
        f'<h1 class="hero-title" style="font-size: 88px; margin-bottom: 24px;">{p["title"]}<span class="dot">.</span></h1>'
    )
    
    # Replace status badge category
    new_content = new_content.replace(
        'BRAND IDENTITY\n            </div>',
        f'{p["category"]}\n            </div>'
    )
    
    # Replace year
    new_content = new_content.replace(
        '2024 &mdash; CREATIVE DIRECTION',
        f'{p["year"]} &mdash; CREATIVE DIRECTION'
    )
    
    with open(p["file"], 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Created {p['file']}")
