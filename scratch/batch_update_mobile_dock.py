import os
import glob
import re

def get_depth_prefix(file_path):
    rel = os.path.relpath(file_path, '.').replace('\\', '/')
    depth = rel.count('/')
    if depth == 0:
        return ''
    return '../' * depth

def update_mobile_dock(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = get_depth_prefix(file_path)
    home_link = f"{prefix}" if prefix else "./"
    logo_src = f"{prefix}assets/images/logo.webp"

    # The Ultra-Clean Floating Island Dock with Center Logo
    new_dock = f'''<!-- FLOATING MOBILE SMART DOCK (Ultra-Modern Floating Island with Logo) -->
    <div class="lg:hidden fixed bottom-4 inset-x-4 z-50 max-w-xs sm:max-w-sm mx-auto">
        <div class="bg-white/95 backdrop-blur-2xl rounded-full shadow-[0_12px_35px_rgba(0,0,0,0.22)] border border-gray-200/80 p-2 flex items-center justify-between gap-2">
            <!-- Left: Call Button -->
            <a href="tel:+15135990399" class="flex-1 flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-full bg-brand-green text-white font-extrabold text-xs sm:text-sm shadow-sm active:scale-95 transition-all">
                <i class="fa-solid fa-phone text-brand-gold text-xs"></i>
                <span>Call</span>
            </a>

            <!-- Center: Floating Logo Button -->
            <a href="{home_link}" class="w-12 h-12 rounded-full bg-white shadow-[0_6px_20px_rgba(0,0,0,0.18)] border-2 border-brand-orange flex items-center justify-center p-1 shrink-0 -my-3 hover:scale-110 active:scale-95 transition-all duration-300" aria-label="Home">
                <img src="{logo_src}" alt="Jackpot Clean" class="w-full h-full object-contain rounded-full">
            </a>

            <!-- Right: Quote Button -->
            <a href="#quote" class="flex-1 flex items-center justify-center gap-1 py-2.5 px-3 rounded-full bg-gradient-to-r from-brand-orange to-[#D94E28] text-white font-extrabold text-xs sm:text-sm shadow-sm active:scale-95 transition-all">
                <span>Quote</span>
                <i class="fa-solid fa-arrow-right text-xs"></i>
            </a>
        </div>
    </div>'''

    # Patterns to match existing docks
    dock_patterns = [
        r'<!-- UNIQUE MOBILE FLOATING QUICK-ACTION BAR.*?-->\s*<div class="lg:hidden fixed bottom-0.*?</div>\s*</div>',
        r'<!-- MOBILE FLOATING SMART DOCK.*?-->\s*<div class="fixed bottom-0.*?</div>\s*</div>',
        r'<!-- FLOATING MOBILE SMART DOCK.*?-->\s*<div class="lg:hidden fixed bottom-4.*?</div>\s*</div>',
        r'<div class="lg:hidden fixed bottom-0.*?</div>\s*</div>',
        r'<div class="fixed bottom-0 inset-x-0 z-50 lg:hidden.*?</div>\s*</div>'
    ]

    matched = False
    for pat in dock_patterns:
        if re.search(pat, content, re.DOTALL):
            content = re.sub(pat, new_dock, content, count=1, flags=re.DOTALL)
            matched = True
            break

    if not matched:
        # If no dock pattern matched, insert before </body> or </main>
        if '</body>' in content:
            content = content.replace('</body>', f'{new_dock}\n</body>', 1)
            matched = True

    if matched:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Updated dock"
    return False, "Could not match dock"

if __name__ == '__main__':
    all_html = glob.glob('**/*.html', recursive=True)
    success = 0
    fail = 0
    for f in all_html:
        s, m = update_mobile_dock(f)
        if s:
            success += 1
        else:
            print(f"Failed {f}: {m}")
            fail += 1
    print(f"Completed! Updated mobile floating island dock on {success} files. Failed: {fail}")
