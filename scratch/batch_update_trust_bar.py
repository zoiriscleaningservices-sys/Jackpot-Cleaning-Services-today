import os
import glob
import re

def update_trust_bar(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extract location name from existing trust bar
    loc_match = re.search(r'Locally Owned &amp; Operated in ([^<]+)', content)
    if loc_match:
        loc_name = loc_match.group(1).strip()
    else:
        loc_match2 = re.search(r'Locally Owned.*?in ([^<]+)', content)
        if loc_match2:
            loc_name = loc_match2.group(1).strip()
        else:
            loc_name = "Cincinnati, OH"

    # Construct the ultra-modern 2x2 Mobile / 4-Col Desktop Trust & Credibility Matrix
    new_trust_bar = f'''<!-- ULTRA-MODERN TRUST & CREDIBILITY MATRIX -->
        <section class="relative bg-gradient-to-r from-[#142924] via-brand-green to-[#142924] py-7 sm:py-9 border-y border-emerald-900/40 shadow-inner overflow-hidden">
            <!-- Subtle ambient glow background -->
            <div class="absolute inset-0 pointer-events-none">
                <div class="absolute -top-24 left-1/4 w-72 h-72 bg-brand-orange/10 rounded-full blur-3xl"></div>
                <div class="absolute -bottom-24 right-1/4 w-72 h-72 bg-brand-gold/10 rounded-full blur-3xl"></div>
            </div>

            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <!-- Mobile 2x2 Grid / Desktop 4-Card Luxury Dock -->
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 lg:gap-6">
                    
                    <!-- Card 1: 5.0 Star Rating -->
                    <div class="bg-white/[0.06] hover:bg-white/[0.1] backdrop-blur-xl border border-white/10 hover:border-brand-gold/40 rounded-2xl p-3 sm:p-4 transition-all duration-300 flex items-center gap-2.5 sm:gap-3 group shadow-[0_4px_20px_rgba(0,0,0,0.2)]">
                        <div class="w-9 h-9 sm:w-11 sm:h-11 rounded-xl bg-brand-gold/15 text-brand-gold flex items-center justify-center text-base sm:text-lg shrink-0 group-hover:scale-110 transition-transform shadow-inner">
                            <i class="fa-solid fa-star"></i>
                        </div>
                        <div class="min-w-0">
                            <div class="text-white font-extrabold text-xs sm:text-sm tracking-tight truncate">5.0 Star Rating</div>
                            <div class="text-brand-gold/90 text-[10px] sm:text-xs font-medium truncate">148+ Reviews</div>
                        </div>
                    </div>

                    <!-- Card 2: Bonded & Insured -->
                    <div class="bg-white/[0.06] hover:bg-white/[0.1] backdrop-blur-xl border border-white/10 hover:border-brand-orange/40 rounded-2xl p-3 sm:p-4 transition-all duration-300 flex items-center gap-2.5 sm:gap-3 group shadow-[0_4px_20px_rgba(0,0,0,0.2)]">
                        <div class="w-9 h-9 sm:w-11 sm:h-11 rounded-xl bg-brand-orange/15 text-brand-orange flex items-center justify-center text-base sm:text-lg shrink-0 group-hover:scale-110 transition-transform shadow-inner">
                            <i class="fa-solid fa-shield-halved"></i>
                        </div>
                        <div class="min-w-0">
                            <div class="text-white font-extrabold text-xs sm:text-sm tracking-tight truncate">Bonded &amp; Insured</div>
                            <div class="text-emerald-300 text-[10px] sm:text-xs font-medium truncate">Full Protection</div>
                        </div>
                    </div>

                    <!-- Card 3: 100% Satisfaction -->
                    <div class="bg-white/[0.06] hover:bg-white/[0.1] backdrop-blur-xl border border-white/10 hover:border-emerald-400/40 rounded-2xl p-3 sm:p-4 transition-all duration-300 flex items-center gap-2.5 sm:gap-3 group shadow-[0_4px_20px_rgba(0,0,0,0.2)]">
                        <div class="w-9 h-9 sm:w-11 sm:h-11 rounded-xl bg-emerald-500/15 text-emerald-400 flex items-center justify-center text-base sm:text-lg shrink-0 group-hover:scale-110 transition-transform shadow-inner">
                            <i class="fa-solid fa-rotate-left"></i>
                        </div>
                        <div class="min-w-0">
                            <div class="text-white font-extrabold text-xs sm:text-sm tracking-tight truncate">100% Guarantee</div>
                            <div class="text-gray-300 text-[10px] sm:text-xs font-medium truncate">Free Re-Clean</div>
                        </div>
                    </div>

                    <!-- Card 4: Locally Owned in City -->
                    <div class="bg-white/[0.06] hover:bg-white/[0.1] backdrop-blur-xl border border-white/10 hover:border-brand-gold/40 rounded-2xl p-3 sm:p-4 transition-all duration-300 flex items-center gap-2.5 sm:gap-3 group shadow-[0_4px_20px_rgba(0,0,0,0.2)]">
                        <div class="w-9 h-9 sm:w-11 sm:h-11 rounded-xl bg-brand-gold/15 text-brand-gold flex items-center justify-center text-base sm:text-lg shrink-0 group-hover:scale-110 transition-transform shadow-inner">
                            <i class="fa-solid fa-map-pin"></i>
                        </div>
                        <div class="min-w-0">
                            <div class="text-white font-extrabold text-xs sm:text-sm tracking-tight truncate">Locally Owned</div>
                            <div class="text-gray-300 text-[10px] sm:text-xs font-medium truncate">{loc_name}</div>
                        </div>
                    </div>

                </div>
            </div>
        </section>'''

    # Pattern to replace existing trust bar
    trust_pattern = r'(<!-- TRUST BAR -->\s*<section.*?</section>|<!-- ULTRA-MODERN TRUST & CREDIBILITY MATRIX -->\s*<section.*?</section>)'
    if re.search(trust_pattern, content, re.DOTALL):
        content = re.sub(trust_pattern, new_trust_bar, content, count=1, flags=re.DOTALL)
    else:
        # Fallback search for section with py-6 bg-brand-green
        fallback = r'(<section class="py-6 bg-brand-green".*?</section>)'
        if re.search(fallback, content, re.DOTALL):
            content = re.sub(fallback, new_trust_bar, content, count=1, flags=re.DOTALL)
        else:
            return False, "No trust bar pattern matched"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True, "Trust bar updated"

if __name__ == '__main__':
    all_html = glob.glob('**/*.html', recursive=True)
    success = 0
    fail = 0
    for f in all_html:
        s, m = update_trust_bar(f)
        if s:
            success += 1
        else:
            print(f"Failed {f}: {m}")
            fail += 1
    print(f"Done! Updated {success} files. Failed: {fail}")
