import os
import glob
import re

def get_depth_prefix(file_path):
    rel = os.path.relpath(file_path, '.').replace('\\', '/')
    depth = rel.count('/')
    if depth == 0:
        return ''
    return '../' * depth

def update_center_button(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = get_depth_prefix(file_path)
    logo_src = f"{prefix}assets/images/logo.webp"

    # Replace the center logo button to scroll smoothly to the top of the current page
    old_logo_pattern = r'<!-- Center: Floating Logo Button -->\s*<a href="[^"]*".*?</a>'
    new_logo_button = f'''<!-- Center: Floating Logo Button (Scroll to Top) -->
            <button type="button" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" class="w-12 h-12 rounded-full bg-white shadow-[0_6px_20px_rgba(0,0,0,0.18)] border-2 border-brand-orange flex items-center justify-center p-1 shrink-0 -my-3 hover:scale-110 active:scale-95 transition-all duration-300 cursor-pointer" aria-label="Scroll to top">
                <img src="{logo_src}" alt="Jackpot Clean" class="w-full h-full object-contain rounded-full pointer-events-none">
            </button>'''

    if re.search(old_logo_pattern, content, re.DOTALL):
        content = re.sub(old_logo_pattern, new_logo_button, content, count=1, flags=re.DOTALL)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Updated to Scroll-to-Top"
    else:
        # Fallback search if already modified or formatted differently
        fallback_pattern = r'(<a href="[^"]*"\s+class="w-12 h-12 rounded-full.*?</a>)'
        if re.search(fallback_pattern, content, re.DOTALL):
            content = re.sub(fallback_pattern, new_logo_button, content, count=1, flags=re.DOTALL)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Updated via fallback"
        return False, "Pattern not found"

if __name__ == '__main__':
    all_html = glob.glob('**/*.html', recursive=True)
    success = 0
    fail = 0
    for f in all_html:
        s, m = update_center_button(f)
        if s:
            success += 1
        else:
            print(f"Failed {f}: {m}")
            fail += 1
    print(f"Completed! Updated scroll-to-top center logo on {success} files. Failed: {fail}")
