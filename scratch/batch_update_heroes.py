import os
import glob
import re

def get_depth_prefix(file_path):
    rel = os.path.relpath(file_path, '.').replace('\\', '/')
    depth = rel.count('/')
    if depth == 0:
        return ''
    return '../' * depth

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = get_depth_prefix(file_path)
    
    # 1. Extract H1
    h1_match = re.search(r'(<h1[^>]*>.*?</h1>)', content, re.DOTALL)
    if not h1_match:
        return False, "No H1 found"
    
    h1_raw = h1_match.group(1)
    
    # Extract span and title parts
    span_match = re.search(r'<span class="[^"]*">(.*?)</span>', h1_raw, re.DOTALL)
    span_text = span_match.group(1).strip() if span_match else ""
    
    before_span = re.sub(r'<span class="[^"]*">.*?</span>', '', h1_raw, flags=re.DOTALL)
    before_span = re.sub(r'<h1[^>]*>', '', before_span)
    before_span = re.sub(r'</h1>', '', before_span)
    before_span = re.sub(r'<br[^>]*>', ' ', before_span).strip()

    if not span_text:
        h1_text = re.sub(r'<[^>]+>', ' ', h1_raw).strip()
        before_span = h1_text
        span_text = ""

    if span_text:
        new_h1 = f'''<h1 class="text-3xl sm:text-5xl md:text-6xl lg:text-7xl font-black tracking-tight leading-[1.14] drop-shadow-[0_4px_16px_rgba(0,0,0,0.9)] max-w-4xl" data-aos="fade-up" data-aos-delay="100">
                    {before_span}
                    <span class="block mt-1 sm:mt-2 orange-gradient-text drop-shadow-[0_2px_8px_rgba(0,0,0,0.8)]">
                        {span_text}
                    </span>
                </h1>'''
    else:
        new_h1 = f'''<h1 class="text-3xl sm:text-5xl md:text-6xl lg:text-7xl font-black tracking-tight leading-[1.14] drop-shadow-[0_4px_16px_rgba(0,0,0,0.9)] max-w-4xl" data-aos="fade-up" data-aos-delay="100">
                    {before_span}
                </h1>'''

    # 2. Extract Subtitle
    sub_match = re.search(r'<p class="[^"]*mt-[^"]*"[^>]*>(.*?)</p>', content, re.DOTALL)
    if sub_match:
        sub_raw = sub_match.group(1).strip()
        sub_clean = re.sub(r'\s+', ' ', sub_raw.replace('<br />', ' • ').replace('<br/>', ' • ').replace('<br>', ' • ')).strip()
        new_sub = f'''<p class="mt-4 sm:mt-6 text-sm sm:text-lg md:text-xl font-medium text-gray-200/95 max-w-2xl mx-auto leading-relaxed drop-shadow-[0_2px_8px_rgba(0,0,0,0.9)]" data-aos="fade-up" data-aos-delay="200">
                    {sub_clean}
                </p>'''
    else:
        new_sub = f'''<p class="mt-4 sm:mt-6 text-sm sm:text-lg md:text-xl font-medium text-gray-200/95 max-w-2xl mx-auto leading-relaxed drop-shadow-[0_2px_8px_rgba(0,0,0,0.9)]" data-aos="fade-up" data-aos-delay="200">
                    Premium Quality • Bonded &amp; Insured • Free Estimates • Home &amp; Office Cleaning
                </p>'''

    video_src = f"{prefix}assets/images/Cinematic_Website_Hero_—_Slow.mp4"

    # Construct the ultra-clean, minimal, luxury Hero (H1, Subtitle, 2 CTAs, Social Icons)
    new_hero = f'''<!-- MODERN HERO - Cinematic Video Background -->
        <section class="relative min-h-[540px] sm:min-h-[620px] lg:min-h-[700px] flex items-center justify-center overflow-hidden py-14 sm:py-18 lg:py-24">
            <video autoplay muted loop playsinline class="absolute inset-0 w-full h-full object-cover">
                <source src="{video_src}" type="video/mp4" />
            </video>
            <!-- Multi-layer gradient & depth overlay -->
            <div class="absolute inset-0 bg-gradient-to-b from-black/80 via-black/55 to-black/85"></div>

            <div class="relative z-10 w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center text-center text-white">
                
                <!-- MAIN HEADLINE -->
                {new_h1}

                <!-- VALUE PROPOSITION -->
                {new_sub}

                <!-- CALL TO ACTION CLUSTER -->
                <div class="mt-8 sm:mt-10 flex flex-col sm:flex-row gap-3.5 sm:gap-5 items-stretch sm:items-center justify-center w-full max-w-sm sm:max-w-none" data-aos="zoom-in" data-aos-delay="300">
                    <a href="#quote" class="group relative inline-flex items-center justify-center px-8 py-4 sm:px-9 sm:py-4 rounded-xl text-base sm:text-lg font-extrabold text-white bg-gradient-to-r from-brand-orange to-[#D94E28] shadow-[0_8px_25px_rgba(196,63,30,0.5)] hover:shadow-[0_12px_35px_rgba(196,63,30,0.7)] hover:scale-105 active:scale-98 transition-all duration-300 overflow-hidden">
                        <span class="relative z-10 flex items-center gap-2 drop-shadow-[0_2px_4px_rgba(0,0,0,0.6)]">
                            Get Free Quote
                            <i class="fa-solid fa-arrow-right text-sm transition-transform duration-300 group-hover:translate-x-1"></i>
                        </span>
                        <div class="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
                    </a>

                    <a href="tel:+15135990399" class="inline-flex items-center justify-center gap-2.5 px-7 py-4 sm:px-8 sm:py-4 rounded-xl text-base sm:text-lg font-extrabold text-white bg-white/15 backdrop-blur-xl border border-white/30 hover:bg-white/25 hover:border-white/50 shadow-[0_6px_20px_rgba(0,0,0,0.4)] hover:shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:scale-105 active:scale-98 transition-all duration-300">
                        <i class="fa-solid fa-phone text-brand-gold"></i>
                        <span class="drop-shadow-[0_2px_4px_rgba(0,0,0,0.6)]">Call (513) 599-0399</span>
                    </a>
                </div>

                <!-- SOCIAL MEDIA ICONS -->
                <div class="mt-8 sm:mt-12 flex items-center justify-center gap-6 sm:gap-8" data-aos="fade-up" data-aos-delay="400">
                    <a href="https://facebook.com/jackpotclean" target="_blank" rel="noopener" class="text-white/85 hover:text-white transition-all duration-300 hover:scale-110 drop-shadow-[0_3px_10px_rgba(0,0,0,0.75)]" aria-label="Facebook">
                        <svg class="w-8 h-8 sm:w-9 sm:h-9" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" /></svg>
                    </a>
                    <a href="https://instagram.com/jackpotclean" target="_blank" rel="noopener" class="text-white/85 hover:text-white transition-all duration-300 hover:scale-110 drop-shadow-[0_3px_10px_rgba(0,0,0,0.75)]" aria-label="Instagram">
                        <svg class="w-8 h-8 sm:w-9 sm:h-9" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.229.273 2.694.072 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.622 6.823 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.358-.2 6.823-2.622 6.98-6.98.058-1.28.072-1.689.072-4.948 0-3.259-.014-3.667-.072-4.947-.2-4.358-2.622-6.823-6.98-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zm0 10.162a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 11-2.881 0 1.44 0 012.881 0z" /></svg>
                    </a>
                    <a href="https://maps.google.com/?q=Jackpot+Cleaning+Services+Cincinnati+OH" target="_blank" rel="noopener" class="text-white/85 hover:text-white transition-all duration-300 hover:scale-110 drop-shadow-[0_3px_10px_rgba(0,0,0,0.75)]" aria-label="Google Maps">
                        <svg class="w-8 h-8 sm:w-9 sm:h-9" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" /></svg>
                    </a>
                </div>

            </div>
        </section>'''

    # Replace existing hero section
    hero_pattern = r'(<!-- MODERN HERO.*?-->\s*<section.*?</section>)'
    if re.search(hero_pattern, content, re.DOTALL):
        content = re.sub(hero_pattern, new_hero, content, count=1, flags=re.DOTALL)
    else:
        return False, "Hero pattern did not match"

    # Remove any leftover pill script
    content = re.sub(r'\s*// Interactive Hero Service Pills Logic.*?(?=</script>|\Z)', '', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True, "Updated successfully"

if __name__ == '__main__':
    all_html = glob.glob('**/*.html', recursive=True)
    success_count = 0
    fail_count = 0
    for f in all_html:
        success, msg = update_file(f)
        if success:
            success_count += 1
        else:
            print(f"Failed {f}: {msg}")
            fail_count += 1
    print(f"Completed! Updated {success_count} files. Failed: {fail_count}")
