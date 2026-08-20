import os
import glob
import re

CITY_MAP = {
    'downtown-cincinnati': ('Downtown Cincinnati, OH', 'Downtown Cincinnati'),
    'oakley': ('Oakley, OH', 'Oakley'),
    'hyde-park': ('Hyde Park, OH', 'Hyde Park'),
    'montgomery': ('Montgomery, OH', 'Montgomery'),
    'blue-ash': ('Blue Ash, OH', 'Blue Ash'),
    'mason': ('Mason, OH', 'Mason'),
    'west-chester': ('West Chester, OH', 'West Chester'),
    'indian-hill': ('Indian Hill, OH', 'Indian Hill'),
    'loveland': ('Loveland, OH', 'Loveland'),
    'milford': ('Milford, OH', 'Milford'),
    'covington-ky': ('Covington, KY', 'Covington'),
    'newport-ky': ('Newport, KY', 'Newport'),
}

def get_depth_prefix(file_path):
    rel = os.path.relpath(file_path, '.').replace('\\', '/')
    depth = rel.count('/')
    if depth == 0:
        return ''
    return '../' * depth

def get_loc_info(file_path):
    rel = os.path.relpath(file_path, '.').replace('\\', '/')
    parts = rel.split('/')
    if len(parts) > 1 and parts[0] in CITY_MAP:
        return CITY_MAP[parts[0]], parts[0]
    return ('Cincinnati, OH', 'Cincinnati'), 'services'

def update_services_section(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    (loc_full, loc_short), folder_slug = get_loc_info(file_path)
    prefix = get_depth_prefix(file_path)

    # Determine service link folder
    # If the page is inside a location (e.g. oakley/), we can link to that location's services if available or fallback to services/
    if folder_slug in CITY_MAP:
        base_service_dir = f"{folder_slug}/"
    else:
        base_service_dir = "services/"

    house_link = f"{prefix}{base_service_dir}house-cleaning/"
    deep_link = f"{prefix}{base_service_dir}deep-cleaning/"
    comm_link = f"{prefix}{base_service_dir}commercial-janitorial/"
    move_link = f"{prefix}{base_service_dir}move-out-cleaning/"
    post_link = f"{prefix}{base_service_dir}post-construction-cleaning/"
    carpet_link = f"{prefix}{base_service_dir}carpet-upholstery-cleaning/"
    window_link = f"{prefix}{base_service_dir}window-cleaning/"
    airbnb_link = f"{prefix}{base_service_dir}airbnb-turnover/"
    luxury_link = f"{prefix}{base_service_dir}luxury-estate-cleaning/"

    # Construct the exact reference Services Grid
    new_services_grid = f'''<!-- SERVICES GRID -->
        <section class="py-24 bg-white">
            <div class="max-w-7xl mx-auto px-5">
                <div class="text-center max-w-3xl mx-auto mb-16" data-aos="fade-up">
                    <h2 class="text-3xl lg:text-5xl font-bold text-brand-green mb-6">Cleaning Services in {loc_full}</h2>
                    <p class="text-lg text-gray-600">Expert cleaning services customized for your exact needs in {loc_short}. Trust our professionals to keep your space spotless.</p>
                </div>

                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <a href="{house_link}"
                        class="group bg-brand-sand p-8 rounded-3xl border border-gray-100 hover:border-brand-orange/30 transition-all duration-500 hover:shadow-xl"
                        data-aos="fade-up">
                        <div
                            class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-brand-orange text-2xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-house-chimney"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-brand-green mb-4">House Cleaning</h3>
                        <p class="text-gray-600 mb-6">Recurring maid service for {loc_short} homes — weekly, bi-weekly, or monthly. Consistent, reliable, and spotless every time.</p>
                        <span class="text-brand-orange font-bold flex items-center gap-2">Explore <i
                                class="fa-solid fa-chevron-right text-xs"></i></span>
                    </a>
                    <a href="{deep_link}"
                        class="group bg-brand-sand p-8 rounded-3xl border border-gray-100 hover:border-brand-orange/30 transition-all duration-500 hover:shadow-xl"
                        data-aos="fade-up" data-aos-delay="100">
                        <div
                            class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-brand-orange text-2xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-soap"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-brand-green mb-4">Deep Cleaning</h3>
                        <p class="text-gray-600 mb-6">A top-to-bottom intensive clean for kitchens, bathrooms, and living spaces. Perfect for first-time clients or seasonal resets.</p>
                        <span class="text-brand-orange font-bold flex items-center gap-2">Explore <i
                                class="fa-solid fa-chevron-right text-xs"></i></span>
                    </a>
                    <a href="{comm_link}"
                        class="group bg-brand-sand p-8 rounded-3xl border border-gray-100 hover:border-brand-orange/30 transition-all duration-500 hover:shadow-xl"
                        data-aos="fade-up" data-aos-delay="200">
                        <div
                            class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-brand-orange text-2xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-building"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-brand-green mb-4">Commercial Cleaning</h3>
                        <p class="text-gray-600 mb-6">Professional janitorial services for {loc_short} offices, gyms, daycares, medical facilities, and warehouses.</p>
                        <span class="text-brand-orange font-bold flex items-center gap-2">Explore <i
                                class="fa-solid fa-chevron-right text-xs"></i></span>
                    </a>
                    <a href="{move_link}"
                        class="group bg-brand-sand p-8 rounded-3xl border border-gray-100 hover:border-brand-orange/30 transition-all duration-500 hover:shadow-xl"
                        data-aos="fade-up" data-aos-delay="100">
                        <div
                            class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-brand-orange text-2xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-box-open"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-brand-green mb-4">Move-In / Move-Out</h3>
                        <p class="text-gray-600 mb-6">Get your full deposit back! Our {loc_short} move-out cleaning is thorough enough to satisfy even the strictest landlords.</p>
                        <span class="text-brand-orange font-bold flex items-center gap-2">Explore <i
                                class="fa-solid fa-chevron-right text-xs"></i></span>
                    </a>
                    <a href="{post_link}"
                        class="group bg-brand-sand p-8 rounded-3xl border border-gray-100 hover:border-brand-orange/30 transition-all duration-500 hover:shadow-xl"
                        data-aos="fade-up" data-aos-delay="200">
                        <div
                            class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-brand-orange text-2xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-helmet-safety"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-brand-green mb-4">Post-Construction</h3>
                        <p class="text-gray-600 mb-6">Remove construction dust, debris, and residue from new builds and remodels. We make your {loc_short} property move-in ready.</p>
                        <span class="text-brand-orange font-bold flex items-center gap-2">Explore <i
                                class="fa-solid fa-chevron-right text-xs"></i></span>
                    </a>
                    <a href="{carpet_link}"
                        class="group bg-brand-sand p-8 rounded-3xl border border-gray-100 hover:border-brand-orange/30 transition-all duration-500 hover:shadow-xl"
                        data-aos="fade-up" data-aos-delay="300">
                        <div
                            class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-brand-orange text-2xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-couch"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-brand-green mb-4">Carpet &amp; Upholstery</h3>
                        <p class="text-gray-600 mb-6">Deep-clean carpets and upholstery to remove stains, odors, and allergens. Great for {loc_short} homes with kids and pets.</p>
                        <span class="text-brand-orange font-bold flex items-center gap-2">Explore <i
                                class="fa-solid fa-chevron-right text-xs"></i></span>
                    </a>
                    <a href="{window_link}"
                        class="group bg-brand-sand p-8 rounded-3xl border border-gray-100 hover:border-brand-orange/30 transition-all duration-500 hover:shadow-xl"
                        data-aos="fade-up">
                        <div
                            class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-brand-orange text-2xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-window-maximize"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-brand-green mb-4">Window Cleaning</h3>
                        <p class="text-gray-600 mb-6">Crystal-clear windows inside and out. We tackle Ohio Valley pollen, water spots, and dust that coat every surface.</p>
                        <span class="text-brand-orange font-bold flex items-center gap-2">Explore <i
                                class="fa-solid fa-chevron-right text-xs"></i></span>
                    </a>
                    <a href="{airbnb_link}"
                        class="group bg-brand-sand p-8 rounded-3xl border border-gray-100 hover:border-brand-orange/30 transition-all duration-500 hover:shadow-xl"
                        data-aos="fade-up" data-aos-delay="100">
                        <div
                            class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-brand-orange text-2xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                            <i class="fa-brands fa-airbnb"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-brand-green mb-4">Airbnb Turnover</h3>
                        <p class="text-gray-600 mb-6">Fast, reliable turnovers between guests. We keep your {loc_short} short-term rental 5-star ready every single time.</p>
                        <span class="text-brand-orange font-bold flex items-center gap-2">Explore <i
                                class="fa-solid fa-chevron-right text-xs"></i></span>
                    </a>
                    <a href="{luxury_link}"
                        class="group bg-brand-sand p-8 rounded-3xl border border-gray-100 hover:border-brand-orange/30 transition-all duration-500 hover:shadow-xl"
                        data-aos="fade-up" data-aos-delay="200">
                        <div
                            class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-brand-orange text-2xl mb-6 shadow-sm group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-crown"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-brand-green mb-4">Luxury Estate Cleaning</h3>
                        <p class="text-gray-600 mb-6">White-glove residential cleaning for {loc_short}'s finest homes, estates, and luxury properties.</p>
                        <span class="text-brand-orange font-bold flex items-center gap-2">Explore <i
                                class="fa-solid fa-chevron-right text-xs"></i></span>
                    </a>
                </div>
            </div>
        </section>'''

    # Replace old services section
    pattern = r'(<!-- ===================================================== -->\s*<!--\s*SERVICES SECTION.*?-->\s*<!-- ===================================================== -->\s*<section.*?</section>|<!-- SERVICES GRID -->\s*<section.*?</section>)'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_services_grid, content, count=1, flags=re.DOTALL)
    else:
        # Fallback search for section with py-24 bg-[#FAF7F2] or py-24 bg-white
        fallback = r'(<section class="py-24 bg-\[#FAF7F2\].*?</section>)'
        if re.search(fallback, content, re.DOTALL):
            content = re.sub(fallback, new_services_grid, content, count=1, flags=re.DOTALL)
        else:
            return False, "Services section not found"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True, "Updated services grid"

if __name__ == '__main__':
    all_html = glob.glob('**/*.html', recursive=True)
    success = 0
    fail = 0
    for f in all_html:
        s, m = update_services_section(f)
        if s:
            success += 1
        else:
            # Check if it was about or blog where services grid might not exist
            print(f"Note on {f}: {m}")
            fail += 1
    print(f"Completed! Updated services grid on {success} files. (Other files: {fail})")
