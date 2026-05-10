import glob
import re

# Read index.html to get the new block
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Pattern to capture everything from the FOLLOW heading down to the end of the footer-links div structure
pattern = re.compile(r'(<h4 class="footer-heading">FOLLOW</h4>.*?)(?=\s*</div>\s*</div>\s*</div>\s*<div class="footer-bottom">)', re.DOTALL)

match = pattern.search(index_content)
if match:
    follow_block = match.group(1)
    
    # Process all work files
    work_files = glob.glob('work-*.html')
    for file in work_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the old block with the new block
        new_content = pattern.sub(follow_block.replace('\\', '\\\\'), content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            print(f"No changes needed for {file}")
else:
    print("Could not find FOLLOW block in index.html")
