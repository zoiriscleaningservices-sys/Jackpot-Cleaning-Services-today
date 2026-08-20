import os
import glob
import re

def update_marquee(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extract location name
    loc_match = re.search(r'Locally Owned.*?in ([^<]+)', content)
    if loc_match:
        loc_name = loc_match.group(1).replace('</div>', '').replace('</span>', '').strip()
    else:
        loc_name = "Cincinnati, OH"

    # 2. Add Marquee CSS to style block if not present
    if '@keyframes marqueeScroll' not in content:
        marquee_css = '''
        /* Sleek Continuous Infinite Gliding Marquee */
        @keyframes marqueeScroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .animate-marquee {
            display: flex;
            width: max-content;
            animation: marqueeScroll 28s linear infinite;
        }
        .animate-marquee:hover {
            animation-play-state: paused;
        }
    </style>'''
        content = content.replace('</style>', marquee_css, 1)

    # 3. Construct the Infinite Gliding Ticker
    new_ticker = f'''<!-- SLEEK INFINITE GLIDING TRUST TICKER -->
        <section class="py-3.5 sm:py-4 bg-brand-green border-y border-emerald-900/50 overflow-hidden relative shadow-inner">
            <!-- Left & Right Fade Masks for Smooth Infinite Look -->
            <div class="absolute left-0 top-0 bottom-0 w-12 sm:w-20 bg-gradient-to-r from-brand-green to-transparent z-10 pointer-events-none"></div>
            <div class="absolute right-0 top-0 bottom-0 w-12 sm:w-20 bg-gradient-to-l from-brand-green to-transparent z-10 pointer-events-none"></div>

            <div class="flex overflow-hidden select-none">
                <div class="animate-marquee flex items-center gap-6 sm:gap-10 text-white text-xs sm:text-sm font-semibold tracking-wide shrink-0">
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-map-pin text-brand-orange"></i> Locally Owned &amp; Operated in {loc_name}</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-star text-brand-gold"></i> 5.0-Star Rated (148+ Reviews)</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-shield-halved text-brand-orange"></i> Licensed, Bonded &amp; Insured</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-rotate-left text-brand-orange"></i> 100% Satisfaction Guarantee</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-leaf text-emerald-400"></i> Eco-Friendly Supplies</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-calendar-check text-brand-gold"></i> Flexible 7-Day Scheduling</span>
                    <span class="text-white/30">•</span>

                    <!-- Track 2 (Duplicate for Seamless Infinite Loop) -->
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-map-pin text-brand-orange"></i> Locally Owned &amp; Operated in {loc_name}</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-star text-brand-gold"></i> 5.0-Star Rated (148+ Reviews)</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-shield-halved text-brand-orange"></i> Licensed, Bonded &amp; Insured</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-rotate-left text-brand-orange"></i> 100% Satisfaction Guarantee</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-leaf text-emerald-400"></i> Eco-Friendly Supplies</span>
                    <span class="text-white/30">•</span>
                    <span class="inline-flex items-center gap-2 whitespace-nowrap"><i class="fa-solid fa-calendar-check text-brand-gold"></i> Flexible 7-Day Scheduling</span>
                    <span class="text-white/30">•</span>
                </div>
            </div>
        </section>'''

    # Pattern to replace existing trust bar or matrix
    trust_pattern = r'(<!-- ULTRA-MODERN TRUST & CREDIBILITY MATRIX -->\s*<section.*?</section>|<!-- TRUST BAR -->\s*<section.*?</section>|<!-- SLEEK INFINITE GLIDING TRUST TICKER -->\s*<section.*?</section>)'
    if re.search(trust_pattern, content, re.DOTALL):
        content = re.sub(trust_pattern, new_ticker, content, count=1, flags=re.DOTALL)
    else:
        fallback = r'(<section class="[^"]*bg-gradient-to-r from-\[#142924\].*?</section>|<section class="py-6 bg-brand-green".*?</section>)'
        if re.search(fallback, content, re.DOTALL):
            content = re.sub(fallback, new_ticker, content, count=1, flags=re.DOTALL)
        else:
            return False, "No trust section found"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True, "Updated to Infinite Gliding Marquee"

if __name__ == '__main__':
    all_html = glob.glob('**/*.html', recursive=True)
    success = 0
    fail = 0
    for f in all_html:
        s, m = update_marquee(f)
        if s:
            success += 1
        else:
            print(f"Failed {f}: {m}")
            fail += 1
    print(f"Completed! Updated {success} files. Failed: {fail}")
