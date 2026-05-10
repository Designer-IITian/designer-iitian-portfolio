import glob

back_arrow_html = '''
    <!-- Back Arrow -->
    <a href="index.html#works" class="back-arrow-btn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
        BACK TO WORKS
    </a>
'''

files = glob.glob('work-*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '<!-- Back Arrow -->' not in content:
        content = content.replace('<body>', '<body>' + back_arrow_html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Injected back arrow into all work pages.")
