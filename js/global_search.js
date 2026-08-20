// Global search handler for Jackpot Cleaning Services city / neighborhood lookup
document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('heroSearchForm');
    const searchInput = document.getElementById('heroCitySearch');

    if (searchForm && searchInput) {
        searchForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const query = searchInput.value.trim().toLowerCase();
            if (!query) return;

            // List of supported Cincinnati / Northern KY service areas
            const serviceAreas = [
                'cincinnati', 'downtown cincinnati', 'oakley', 'hyde park', 
                'montgomery', 'blue ash', 'mason', 'west chester', 'milford', 
                'loveland', 'indian hill', 'kenwood', 'norwood', 'covington', 
                'newport', 'florence', 'anderson', 'clifton', 'mt adams', 'walnut hills'
            ];

            const match = serviceAreas.find(area => area.includes(query) || query.includes(area));

            if (match) {
                // Smooth scroll to service areas or quote form
                const quoteSection = document.getElementById('quote') || document.getElementById('services');
                if (quoteSection) {
                    quoteSection.scrollIntoView({ behavior: 'smooth' });
                }
            } else {
                // Smooth scroll to quote section for custom inquiry
                const quoteSection = document.getElementById('quote');
                if (quoteSection) {
                    quoteSection.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    }
});
