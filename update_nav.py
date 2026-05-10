import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Navigation Header
old_nav = """                <a href="#home" class="nav-link">HOME</a>
                <a href="#about" class="nav-link active">ABOUT</a>
                <a href="#works" class="nav-link">WORKS</a>
                <a href="#visual-language" class="nav-link">PROCESS</a>
                <a href="#cta" class="nav-link">CONTACT</a>"""

new_nav = """                <a href="#home" class="nav-link">HOME</a>
                <a href="#about" class="nav-link active">ABOUT</a>
                <a href="#skills" class="nav-link">PROCESS</a>
                <a href="#works" class="nav-link">WORKS</a>
                <a href="#cta" class="nav-link">CONTACT</a>"""

content = content.replace(old_nav, new_nav)

# 2. Update Footer Navigation
old_footer_nav = """                        <a href="#home" class="footer-link">Home</a>
                        <a href="#about" class="footer-link">About</a>
                        <a href="#works" class="footer-link">Works</a>
                        <a href="#visual-language" class="footer-link">Process</a>
                        <a href="#cta" class="footer-link">Contact</a>"""

new_footer_nav = """                        <a href="#home" class="footer-link">Home</a>
                        <a href="#about" class="footer-link">About</a>
                        <a href="#skills" class="footer-link">Process</a>
                        <a href="#works" class="footer-link">Works</a>
                        <a href="#cta" class="footer-link">Contact</a>"""

content = content.replace(old_footer_nav, new_footer_nav)

# 3. Extract and modify Visual Language Section
vl_pattern = re.compile(r'( {8}<!-- Visual Language Section -->\n.*?)( {8}<!-- Let\'s Work Together CTA Section -->)', re.DOTALL)
match = vl_pattern.search(content)

if match:
    vl_section = match.group(1)
    # Remove from old position
    content = content.replace(vl_section, '')
    
    # Modify vl_section
    vl_section = vl_section.replace('id="visual-language"', 'id="skills"')
    vl_section = vl_section.replace('Visual Language.', 'Skills.')
    vl_section = vl_section.replace('<!-- Visual Language Section -->', '<!-- Skills Section -->')
    
    # Replace the subtitle
    vl_section = re.sub(
        r'<p class="contact-text"[^>]*>.*?</p>', 
        '<p class="contact-text" style="margin-bottom: 0; max-width: none;">A comprehensive mastery of technical disciplines and design software.</p>', 
        vl_section, 
        flags=re.DOTALL
    )
    
    # Insert after #about
    about_end = '        </section>\n\n        <!-- Works Section -->'
    content = content.replace(about_end, '        </section>\n\n' + vl_section + '        <!-- Works Section -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html successfully")
