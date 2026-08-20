import os
import glob
import re

CITY_DATA = {
    'downtown-cincinnati': {
        'name': 'Downtown Cincinnati, OH',
        'short': 'Downtown Cincinnati',
        'tagline': 'Urban Condos, Lofts & Commercial Facilities',
        'keywords': 'Downtown Cincinnati cleaning service, loft cleaning Cincinnati, CBD office cleaning',
        'state': 'OH',
        'zip': '45202',
        'lat': '39.103118',
        'lng': '-84.512020'
    },
    'oakley': {
        'name': 'Oakley, OH',
        'short': 'Oakley',
        'tagline': "Oakley's Premier Residential & Commercial Maids",
        'keywords': 'Oakley OH cleaning service, house cleaning Oakley Cincinnati, maid service Oakley',
        'state': 'OH',
        'zip': '45209',
        'lat': '39.1558',
        'lng': '-84.4327'
    },
    'hyde-park': {
        'name': 'Hyde Park, OH',
        'short': 'Hyde Park',
        'tagline': 'Historic Homes & Luxury Estate Cleaning',
        'keywords': 'Hyde Park Cincinnati cleaning services, house cleaning Hyde Park OH, luxury maid service',
        'state': 'OH',
        'zip': '45208',
        'lat': '39.1414',
        'lng': '-84.4449'
    },
    'montgomery': {
        'name': 'Montgomery, OH',
        'short': 'Montgomery',
        'tagline': "Montgomery's Top-Rated Home & Office Cleaners",
        'keywords': 'Montgomery OH house cleaning, maid service Montgomery Cincinnati, deep cleaning',
        'state': 'OH',
        'zip': '45242',
        'lat': '39.2278',
        'lng': '-84.3541'
    },
    'blue-ash': {
        'name': 'Blue Ash, OH',
        'short': 'Blue Ash',
        'tagline': 'Corporate Offices & Suburban Home Cleaning',
        'keywords': 'Blue Ash OH cleaning service, office janitorial Blue Ash, house cleaners Blue Ash',
        'state': 'OH',
        'zip': '45242',
        'lat': '39.2320',
        'lng': '-84.3783'
    },
    'mason': {
        'name': 'Mason, OH',
        'short': 'Mason',
        'tagline': "Mason & Deerfield Township's Finest Cleaners",
        'keywords': 'Mason OH house cleaning, maid service Mason Ohio, commercial cleaning Mason OH',
        'state': 'OH',
        'zip': '45040',
        'lat': '39.3601',
        'lng': '-84.3099'
    },
    'west-chester': {
        'name': 'West Chester, OH',
        'short': 'West Chester',
        'tagline': 'Trusted Home & Commercial Cleaning Specialists',
        'keywords': 'West Chester OH cleaning services, maid service West Chester Ohio, deep clean',
        'state': 'OH',
        'zip': '45069',
        'lat': '39.3323',
        'lng': '-84.4099'
    },
    'indian-hill': {
        'name': 'Indian Hill, OH',
        'short': 'Indian Hill',
        'tagline': 'White-Glove Luxury Estate & House Cleaning',
        'keywords': 'Indian Hill cleaning service, luxury estate cleaning Indian Hill OH, private maid service',
        'state': 'OH',
        'zip': '45243',
        'lat': '39.1895',
        'lng': '-84.3438'
    },
    'loveland': {
        'name': 'Loveland, OH',
        'short': 'Loveland',
        'tagline': "Loveland & Clermont County's Trusted Maids",
        'keywords': 'Loveland OH house cleaning, maid service Loveland Ohio, move out clean Loveland',
        'state': 'OH',
        'zip': '45140',
        'lat': '39.2689',
        'lng': '-84.2638'
    },
    'milford': {
        'name': 'Milford, OH',
        'short': 'Milford',
        'tagline': "Milford's Reliable Home & Facility Cleaning",
        'keywords': 'Milford OH cleaning company, house cleaning Milford Ohio, office cleaning',
        'state': 'OH',
        'zip': '45150',
        'lat': '39.1748',
        'lng': '-84.2947'
    },
    'covington-ky': {
        'name': 'Covington, KY',
        'short': 'Covington',
        'tagline': 'Northern Kentucky Commercial & Residential Cleaning',
        'keywords': 'Covington KY cleaning service, house cleaning Covington Kentucky, office janitorial NKY',
        'state': 'KY',
        'zip': '41011',
        'lat': '39.0837',
        'lng': '-84.5086'
    },
    'newport-ky': {
        'name': 'Newport, KY',
        'short': 'Newport',
        'tagline': 'Newport & Northern Kentucky Cleaning Specialists',
        'keywords': 'Newport KY cleaning service, house cleaning Newport Kentucky, maid service NKY',
        'state': 'KY',
        'zip': '41071',
        'lat': '39.0917',
        'lng': '-84.4958'
    },
}

SERVICES_DATA = {
    'house-cleaning': ('House Cleaning & Maid Service', 'Top-Rated Residential Maid Services', 'recurring house cleaning, vacuuming, mopping, bathroom sanitization, and kitchen care'),
    'deep-cleaning': ('Deep Cleaning Services', 'Top-to-Bottom Intensive Deep Cleans', 'detailed scrub-down of baseboards, appliances, tile grout, vents, and living spaces'),
    'commercial-janitorial': ('Commercial Janitorial & Office Cleaning', 'Professional Facility Sanitization', 'daily & weekly office janitorial, workstation sanitization, floor buffing, and restroom care'),
    'move-out-cleaning': ('Move-In / Move-Out Cleaning', '100% Full Deposit Guarantee Cleans', 'exhaustive move-out cleans for renters, realtors, and homeowners guaranteeing spotless results'),
    'post-construction-cleaning': ('Post-Construction Cleaning', 'Post-Build Dust & Debris Removal', 'drywall dust elimination, adhesive removal, window detailing, and move-in preparation'),
    'carpet-upholstery-cleaning': ('Carpet & Upholstery Cleaning', 'Deep Steam Stain & Odor Extraction', 'hot water extraction, pet stain removal, and fabric revitalization'),
    'window-cleaning': ('Window Cleaning Services', 'Streak-Free Interior & Exterior Windows', 'interior/exterior window washing, track scrubbing, and screen detailing'),
    'airbnb-turnover': ('Airbnb & Short-Term Rental Turnover', '5-Star Hospitality Turnover Cleaning', 'same-day guest turnovers, linen service, restocking, and 5-star sanitization'),
    'luxury-estate-cleaning': ('Luxury Estate Cleaning', 'White-Glove Private Residence Care', 'white-glove cleaning tailored for luxury estates, fine surfaces, and marble care'),
    'luxury-estate-management': ('Luxury Estate Management & Housekeeping', 'Full-Scale Estate Oversight', 'custom housekeeping schedules, vendor management, and routine estate care'),
    'property-management-janitorial': ('Property Management Cleaning', 'Multi-Unit Building Maintenance', 'turnover cleaning and common-area janitorial for apartment complexes and PM firms'),
    'property-maintenance': ('Property Maintenance & Turnover', 'Complete Property Care Solutions', 'interior turnaround cleaning, seasonal maintenance, and property upkeep'),
    'home-watch-services': ('Home Watch Services', 'Vacation & Absentee Home Care', 'visual property checks, storm inspections, and pre-arrival home cleaning'),
    'medical-dental-facility-cleaning': ('Medical & Dental Facility Cleaning', 'Terminal Clean & Healthcare Sanitization', 'hospital-grade disinfection, waiting room sanitization, and HIPAA compliant care'),
    'industrial-warehouse-cleaning': ('Industrial & Warehouse Cleaning', 'Heavy-Duty Facility Janitorial', 'warehouse floor scrubbing, breakroom janitorial, and industrial debris removal'),
    'gym-fitness-center-cleaning': ('Gym & Fitness Center Cleaning', 'Antimicrobial Sanitization & Equipment Care', 'workout floor disinfection, locker room descaling, and high-touch equipment wipe-down'),
    'school-daycare-cleaning': ('School & Daycare Cleaning', 'Safe Non-Toxic Sanitization for Kids', 'EPA certified green cleaning, toy disinfection, and classroom sanitization'),
    'church-worship-center-cleaning': ('Church & Worship Center Cleaning', 'Sanctuary & Community Facility Care', 'sanctuary detailing, pew polishing, fellowship hall cleaning, and Sunday prep'),
    'floor-stripping-waxing': ('Floor Stripping & Waxing', 'High-Gloss Commercial Floor Refinishing', 'VCT floor stripping, premium wax sealing, and high-speed buffing'),
    'solar-panel-cleaning': ('Solar Panel Cleaning', 'Efficiency-Boosting Panel Washing', 'pure deionized water solar panel washing to maximize energy output'),
    'gutter-cleaning': ('Gutter Cleaning Services', 'Debris Removal & Downspout Flushing', 'thorough roof gutter cleaning, downspout flushing, and drainage inspection'),
}

def optimize_file_seo(file_path):
    # Skip non-html or root/special pages handled separately
    rel = os.path.relpath(file_path, '.').replace('\\', '/')
    if rel in ['index.html', 'about/index.html', 'blog/index.html', 'gallery/index.html']:
        return True, "Root page preserved"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = rel.split('/')
    
    # Check if page is a location root (e.g. oakley/index.html) or service subpage (e.g. oakley/house-cleaning/index.html)
    city_slug = parts[0] if len(parts) > 1 and parts[0] in CITY_DATA else 'cincinnati'
    city_info = CITY_DATA.get(city_slug, {
        'name': 'Cincinnati, OH',
        'short': 'Cincinnati',
        'tagline': "Queen City's Top-Rated Cleaners",
        'keywords': 'Cincinnati cleaning services, house cleaning Cincinnati OH, maid service',
        'state': 'OH',
        'zip': '45202',
        'lat': '39.103118',
        'lng': '-84.512020'
    })

    service_slug = None
    if len(parts) >= 3:
        service_slug = parts[1]
    elif len(parts) == 2 and parts[0] == 'services':
        service_slug = None # services root
    elif len(parts) == 3 and parts[0] == 'services':
        service_slug = parts[1]

    # Generate unique Title & Meta Description
    if service_slug and service_slug in SERVICES_DATA:
        serv_name, serv_heading, serv_desc = SERVICES_DATA[service_slug]
        if city_slug != 'cincinnati':
            unique_title = f"{serv_name} in {city_info['name']} | Jackpot Cleaning Services"
            unique_desc = f"Top-rated {serv_name.lower()} in {city_info['name']} by Jackpot Cleaning Services. Bonded, insured, eco-friendly {serv_desc}. Call (513) 599-0399 for a free quote!"
        else:
            unique_title = f"{serv_name} in Cincinnati, OH | Jackpot Cleaning Services"
            unique_desc = f"Premier {serv_name.lower()} in Cincinnati, OH by Jackpot Clean. Bonded, insured professionals providing {serv_desc}. Get your free quote at (513) 599-0399!"
        unique_kw = f"{serv_name} {city_info['short']}, {city_info['keywords']}, Jackpot Cleaning Services"
    else:
        # Location root page (e.g. oakley/index.html)
        unique_title = f"Top Cleaning Services in {city_info['name']} | Jackpot Clean"
        unique_desc = f"Looking for trusted cleaning services in {city_info['name']}? Jackpot Cleaning Services provides 5-star house cleaning, deep cleaning & commercial janitorial. Call (513) 599-0399!"
        unique_kw = f"cleaning services {city_info['short']} OH, house cleaning {city_info['short']}, maid service {city_info['short']}, {city_info['keywords']}"

    # Replace Title
    content = re.sub(r'<title>.*?</title>', f'<title>{unique_title}</title>', content, count=1, flags=re.DOTALL)
    
    # Replace Meta Description
    content = re.sub(r'<meta\s+name="description"\s+content=".*?"\s*/>', f'<meta name="description" content="{unique_desc}" />', content, count=1, flags=re.DOTALL)
    
    # Replace Meta Keywords
    content = re.sub(r'<meta\s+name="keywords"\s+content=".*?"\s*/>', f'<meta name="keywords" content="{unique_kw}" />', content, count=1, flags=re.DOTALL)

    # Replace OG Title and Description
    content = re.sub(r'<meta\s+property="og:title"\s+content=".*?"\s*>', f'<meta property="og:title" content="{unique_title}">', content, count=1, flags=re.DOTALL)
    content = re.sub(r'<meta\s+property="og:description"\s+content=".*?"\s*>', f'<meta property="og:description" content="{unique_desc}">', content, count=1, flags=re.DOTALL)

    # Save
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, unique_title

if __name__ == '__main__':
    all_html = glob.glob('**/*.html', recursive=True)
    count = 0
    for f in all_html:
        s, m = optimize_file_seo(f)
        if s:
            count += 1
    print(f"SEO Uniqueness Engine applied across {count} files successfully!")
