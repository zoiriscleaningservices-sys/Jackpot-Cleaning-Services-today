import os
import glob
import re

CITY_MAP = {
    'downtown-cincinnati': 'Downtown Cincinnati, OH',
    'oakley': 'Oakley, OH',
    'hyde-park': 'Hyde Park, OH',
    'montgomery': 'Montgomery, OH',
    'blue-ash': 'Blue Ash, OH',
    'mason': 'Mason, OH',
    'west-chester': 'West Chester, OH',
    'indian-hill': 'Indian Hill, OH',
    'loveland': 'Loveland, OH',
    'milford': 'Milford, OH',
    'covington-ky': 'Covington, KY',
    'newport-ky': 'Newport, KY',
}

def get_loc_name(file_path):
    rel = os.path.relpath(file_path, '.').replace('\\', '/')
    parts = rel.split('/')
    if len(parts) > 1 and parts[0] in CITY_MAP:
        return CITY_MAP[parts[0]]
    return "Cincinnati, OH"

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    loc_name = get_loc_name(file_path)

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

    ticker_pattern = r'<!-- SLEEK INFINITE GLIDING TRUST TICKER -->\s*<section.*?</section>'
    if re.search(ticker_pattern, content, re.DOTALL):
        content = re.sub(ticker_pattern, new_ticker, content, count=1, flags=re.DOTALL)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

if __name__ == '__main__':
    all_html = glob.glob('**/*.html', recursive=True)
    count = 0
    for f in all_html:
        if fix_file(f):
            count += 1
    print(f"Fixed clean location names in {count} files.")
