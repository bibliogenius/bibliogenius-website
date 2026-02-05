/**
 * The Green Librarian Map - Data Layer
 * Uses localStorage for persistence. Seeds with real Green Library data.
 * Categories aligned with EBLIDA "Green Librarian" tender requirements.
 */

const STORAGE_KEY = 'green_librarian_entries';

// Categories as per EBLIDA tender: Government Policies, Library Policies, Inspiring Initiatives
const CATEGORIES = {
    POLICY_GOV: 'policy_gov',
    POLICY_LIBRARY: 'policy_library',
    INITIATIVE: 'initiative'
};

const CATEGORY_LABELS = {
    [CATEGORIES.POLICY_GOV]: 'Government Policy',
    [CATEGORIES.POLICY_LIBRARY]: 'Library Policy',
    [CATEGORIES.INITIATIVE]: 'Inspiring Initiative'
};

const CATEGORY_ICONS = {
    [CATEGORIES.POLICY_GOV]: '🏛️',
    [CATEGORIES.POLICY_LIBRARY]: '📜',
    [CATEGORIES.INITIATIVE]: '🌱'
};

const CATEGORY_COLORS = {
    [CATEGORIES.POLICY_GOV]: '#8b5cf6',      // Purple for government
    [CATEGORIES.POLICY_LIBRARY]: '#3b82f6',  // Blue for library policies
    [CATEGORIES.INITIATIVE]: '#22c55e'       // Green for initiatives
};

// Real data from IFLA, EBLIDA, and European green library initiatives
const DEFAULT_ENTRIES = [
    // === GOVERNMENT POLICIES ===
    {
        id: 1,
        name: "Finland: Library Act & Sustainability Goals",
        city: "Helsinki",
        country: "Finland",
        lat: 60.1699,
        lng: 24.9384,
        category: CATEGORIES.POLICY_GOV,
        description: "Finland's Library Act (2016) integrates sustainability into public library missions. Libraries are recognized as key actors in achieving national climate goals and promoting sustainable lifestyles.",
        initiatives: [
            { name: "National Library Strategy 2021-2030", completed: true },
            { name: "Climate Education Mandate", completed: true },
            { name: "Green Building Standards for New Libraries", completed: true },
            { name: "Circular Economy Integration", completed: false }
        ],
        website: "https://minedu.fi/en/libraries"
    },
    {
        id: 2,
        name: "Germany: Agenda 2030 Library Framework",
        city: "Berlin",
        country: "Germany",
        lat: 52.5200,
        lng: 13.4050,
        category: CATEGORIES.POLICY_GOV,
        description: "German federal government's framework integrating libraries into national Agenda 2030 implementation. Libraries serve as 'Third Places' for sustainability education and community action.",
        initiatives: [
            { name: "SDG Documentation in Libraries", completed: true },
            { name: "Federal Funding for Green Renovations", completed: true },
            { name: "Staff Sustainability Training Program", completed: true },
            { name: "National Green Library Award", completed: true }
        ],
        website: "https://www.bibliotheksverband.de/"
    },
    {
        id: 3,
        name: "France: Climate & Resilience Law for Cultural Institutions",
        city: "Paris",
        country: "France",
        lat: 48.8566,
        lng: 2.3522,
        category: CATEGORIES.POLICY_GOV,
        description: "France's 2021 Climate & Resilience Law mandates carbon reduction for all public buildings including libraries. New construction must meet stringent environmental standards.",
        initiatives: [
            { name: "RE2020 Building Standards", completed: true },
            { name: "Carbon Footprint Reporting", completed: true },
            { name: "Renewable Energy Mandates", completed: false },
            { name: "Biodiversity Integration Requirements", completed: true }
        ],
        website: "https://www.culture.gouv.fr/"
    },
    {
        id: 4,
        name: "Netherlands: Green Deal for Libraries",
        city: "The Hague",
        country: "Netherlands",
        lat: 52.0705,
        lng: 4.3007,
        category: CATEGORIES.POLICY_GOV,
        description: "National agreement between Dutch government and library sector committing to carbon-neutral operations by 2030. Includes funding for solar panels and sustainable renovations.",
        initiatives: [
            { name: "Carbon Neutral 2030 Commitment", completed: false },
            { name: "Shared Services Platform", completed: true },
            { name: "Electric Vehicle Fleet", completed: true },
            { name: "Zero Waste Operations", completed: false }
        ],
        website: "https://www.kb.nl/"
    },

    // === LIBRARY POLICIES ===
    {
        id: 10,
        name: "Helsinki City Library: Climate Responsibility Policy",
        city: "Helsinki",
        country: "Finland",
        lat: 60.1740,
        lng: 24.9385,
        category: CATEGORIES.POLICY_LIBRARY,
        description: "Helsinki City Library's comprehensive sustainability policy covering all operations including Oodi Central Library. Focus on carbon neutrality, circular economy, and community engagement.",
        initiatives: [
            { name: "100% Renewable Energy", completed: true },
            { name: "Paperless Circulation", completed: true },
            { name: "Tool & Equipment Lending", completed: true },
            { name: "Repair Café Partnerships", completed: true },
            { name: "Staff Mobility Program", completed: true }
        ],
        website: "https://www.oodihelsinki.fi/en/"
    },
    {
        id: 11,
        name: "Dublin City Council Libraries: Climate Action Plan",
        city: "Dublin",
        country: "Ireland",
        lat: 53.3498,
        lng: -6.2603,
        category: CATEGORIES.POLICY_LIBRARY,
        description: "Dublin's library system adopted a Climate Action Plan making all branches centers for climate information, community resilience, and sustainable behavior change.",
        initiatives: [
            { name: "Climate Action Hub in Each Branch", completed: true },
            { name: "Home Energy Saving Kits Lending", completed: true },
            { name: "Seed Libraries", completed: true },
            { name: "Climate Book Clubs", completed: true },
            { name: "Public EV Charging Stations", completed: false }
        ],
        website: "https://www.dublincity.ie/library"
    },
    {
        id: 12,
        name: "Barcelona Public Libraries: Sustainability Charter",
        city: "Barcelona",
        country: "Spain",
        lat: 41.3851,
        lng: 2.1734,
        category: CATEGORIES.POLICY_LIBRARY,
        description: "Barcelona's library network adopted a Sustainability Charter committing all 40 branches to measurable environmental goals aligned with the city's Climate Emergency declaration.",
        initiatives: [
            { name: "Water Consumption Reduction (-20%)", completed: true },
            { name: "Single-Use Plastic Elimination", completed: true },
            { name: "Local & Organic Café Suppliers", completed: true },
            { name: "Rooftop Solar Installation", completed: false },
            { name: "Biodiversity Gardens", completed: true }
        ],
        website: "https://ajuntament.barcelona.cat/biblioteques/"
    },
    {
        id: 13,
        name: "Bücherhallen Hamburg: Green Library Strategy 2025",
        city: "Hamburg",
        country: "Germany",
        lat: 53.5511,
        lng: 9.9937,
        category: CATEGORIES.POLICY_LIBRARY,
        description: "Hamburg's public library system's comprehensive strategy covering 32 branches. Focus on sustainable logistics, green procurement, and community education.",
        initiatives: [
            { name: "Cargo Bike Delivery Network", completed: true },
            { name: "100% Recycled Paper", completed: true },
            { name: "Green IT Procurement Policy", completed: true },
            { name: "Climate Neutral Events", completed: false },
            { name: "Repair Café in Every Branch", completed: false }
        ],
        website: "https://www.buecherhallen.de/"
    },

    // === INSPIRING INITIATIVES ===
    {
        id: 20,
        name: "Oodi Central Library",
        city: "Helsinki",
        country: "Finland",
        lat: 60.1755,
        lng: 24.9380,
        category: CATEGORIES.INITIATIVE,
        description: "Award-winning sustainable library opened in 2018. Features extensive use of Finnish wood, energy-efficient design, rooftop solar panels, and fjord water cooling. IFLA Green Library Award finalist.",
        initiatives: [
            { name: "Sustainable Wood Construction", completed: true },
            { name: "Rooftop Urban Garden", completed: true },
            { name: "Public Maker Space", completed: true },
            { name: "Zero Food Waste Café", completed: true },
            { name: "Community Repair Hub", completed: true }
        ],
        website: "https://www.oodihelsinki.fi/en/"
    },
    {
        id: 21,
        name: "Šentvid Library 'Harmony with Nature'",
        city: "Ljubljana",
        country: "Slovenia",
        lat: 46.0876,
        lng: 14.4802,
        category: CATEGORIES.INITIATIVE,
        description: "IFLA Green Library Award 2019 recipient. 'We live in harmony with nature' concept. Located in a forested area with fully integrated nature programming and outdoor reading spaces.",
        initiatives: [
            { name: "Forest Integration Design", completed: true },
            { name: "Outdoor Story Trails", completed: true },
            { name: "Seed Library Exchange", completed: true },
            { name: "Beekeeping Program", completed: true },
            { name: "Nature Journaling Workshops", completed: true }
        ],
        website: "https://www.mklj.si/"
    },
    {
        id: 22,
        name: "James Baldwin Library Biodiverse Building",
        city: "Paris",
        country: "France",
        lat: 48.8936,
        lng: 2.3168,
        category: CATEGORIES.INITIATIVE,
        description: "IFLA recognized biodiverse city ecology project in Cité Clichy-Batignolles. 95% native Parisian plants, flower meadows on roofs, pond for aquatic biodiversity, low-carbon construction.",
        initiatives: [
            { name: "Biodiverse Roof Ecosystem", completed: true },
            { name: "95% Native Plant Selection", completed: true },
            { name: "Aquatic Biodiversity Pond", completed: true },
            { name: "Insect Hotels", completed: true },
            { name: "Butterfly Garden", completed: true }
        ],
        website: "https://www.paris.fr/"
    },
    {
        id: 23,
        name: "Deichman Bjørvika - Oslo's Sustainable Landmark",
        city: "Oslo",
        country: "Norway",
        lat: 59.9075,
        lng: 10.7528,
        category: CATEGORIES.INITIATIVE,
        description: "Oslo's stunning new main library (2020). BREEAM Excellent certified, innovative fjord water cooling, natural ventilation, and extensive public maker spaces focused on repair and reuse.",
        initiatives: [
            { name: "BREEAM Excellent Certification", completed: true },
            { name: "Fjord Water Cooling", completed: true },
            { name: "Passive Ventilation Design", completed: true },
            { name: "Public Sewing Workshop", completed: true },
            { name: "3D Printing for Repair", completed: true }
        ],
        website: "https://deichman.no/"
    },
    {
        id: 24,
        name: "Amsterdam OBA Tool Library",
        city: "Amsterdam",
        country: "Netherlands",
        lat: 52.3764,
        lng: 4.9077,
        category: CATEGORIES.INITIATIVE,
        description: "Pioneering 'Library of Things' initiative at Amsterdam's central library. Lending tools, sports equipment, and electronics to promote sharing economy and reduce consumption.",
        initiatives: [
            { name: "Tool Lending Collection (500+ items)", completed: true },
            { name: "Sports Equipment Sharing", completed: true },
            { name: "Electronics Lending", completed: true },
            { name: "Repair Workshop Events", completed: true },
            { name: "Toy Library", completed: true }
        ],
        website: "https://www.oba.nl/"
    },
    {
        id: 25,
        name: "Stuttgart City Library Sustainable Design",
        city: "Stuttgart",
        country: "Germany",
        lat: 48.7870,
        lng: 9.1823,
        category: CATEGORIES.INITIATIVE,
        description: "Iconic cube-shaped library (2011) designed for maximum natural light and energy efficiency. Pioneering example of sustainable architecture in public libraries.",
        initiatives: [
            { name: "Natural Light Maximization", completed: true },
            { name: "Rainwater Harvesting", completed: true },
            { name: "Energy-Efficient Facade", completed: true },
            { name: "Green Roof Installation", completed: true },
            { name: "Air Quality Monitoring", completed: true }
        ],
        website: "https://www.stuttgart.de/stadtbibliothek"
    },
    {
        id: 26,
        name: "Common Waste - Common Libraries (SE Europe)",
        city: "Zagreb",
        country: "Croatia",
        lat: 45.8150,
        lng: 15.9819,
        category: CATEGORIES.INITIATIVE,
        description: "Goethe Institute program across Southeast Europe exploring libraries as 'spaces of commoning' for eco-thinking, knowledge sharing, and recycling practices.",
        initiatives: [
            { name: "Multi-Country Network", completed: true },
            { name: "Waste Reduction Workshops", completed: true },
            { name: "Upcycling Art Programs", completed: true },
            { name: "Community Composting", completed: false },
            { name: "Plastic-Free Events", completed: true }
        ],
        website: "https://www.goethe.de/"
    },
    {
        id: 27,
        name: "Bibliothèque de la Part-Dieu",
        city: "Lyon",
        country: "France",
        lat: 45.7602,
        lng: 4.8590,
        category: CATEGORIES.INITIATIVE,
        description: "Lyon's flagship public library in the Part-Dieu district. A major cultural hub implementing sustainable practices and community-focused green initiatives.",
        initiatives: [
            { name: "Energy Efficiency Renovation", completed: true },
            { name: "Digital Resource Lending", completed: true },
            { name: "Community Repair Workshops", completed: false },
            { name: "Seed Exchange Program", completed: false },
            { name: "Zero Waste Events", completed: false }
        ],
        website: "https://www.bm-lyon.fr/"
    }
];

/**
 * Migrate data from old storage key if exists
 */
function migrateFromOldKey() {
    const OLD_KEY = 'green_libraries_data';
    const oldData = localStorage.getItem(OLD_KEY);

    if (oldData && !localStorage.getItem(STORAGE_KEY)) {
        try {
            const entries = JSON.parse(oldData);
            // Add category if missing (old entries won't have it)
            const migratedEntries = entries.map(entry => ({
                ...entry,
                category: entry.category || CATEGORIES.INITIATIVE
            }));
            localStorage.setItem(STORAGE_KEY, JSON.stringify(migratedEntries));
            console.log('Migrated data from old storage key');
            // Don't delete old key yet, in case of issues
        } catch (e) {
            console.error('Migration failed:', e);
        }
    }
}

/**
 * Initialize localStorage with default data if empty
 */
function seedDefaultData() {
    // First try to migrate from old key
    migrateFromOldKey();

    if (!localStorage.getItem(STORAGE_KEY)) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(DEFAULT_ENTRIES));
        console.log('Seeded default Green Librarian data');
    }
}

/**
 * Get all entries from localStorage
 * @returns {Array} Array of entry objects
 */
function getLibraries() {
    seedDefaultData();
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
}

/**
 * Get entries filtered by category
 * @param {string} category - Category to filter by
 * @returns {Array} Filtered array of entries
 */
function getLibrariesByCategory(category) {
    return getLibraries().filter(lib => lib.category === category);
}

/**
 * Get a single entry by ID
 * @param {number} id - Entry ID
 * @returns {Object|null} Entry object or null
 */
function getLibraryById(id) {
    const libraries = getLibraries();
    return libraries.find(lib => lib.id === parseInt(id)) || null;
}

/**
 * Save an entry (create or update)
 * @param {Object} library - Entry object
 * @returns {Object} Saved entry with ID
 */
function saveLibrary(library) {
    const libraries = getLibraries();

    if (library.id) {
        // Update existing
        const index = libraries.findIndex(lib => lib.id === library.id);
        if (index >= 0) {
            libraries[index] = { ...libraries[index], ...library };
        }
    } else {
        // Create new
        library.id = Date.now();
        library.initiatives = library.initiatives || [];
        libraries.push(library);
    }

    localStorage.setItem(STORAGE_KEY, JSON.stringify(libraries));
    return library;
}

/**
 * Delete an entry by ID
 * @param {number} id - Entry ID
 * @returns {boolean} Success status
 */
function deleteLibrary(id) {
    const libraries = getLibraries();
    const filtered = libraries.filter(lib => lib.id !== parseInt(id));
    localStorage.setItem(STORAGE_KEY, JSON.stringify(filtered));
    return filtered.length < libraries.length;
}

/**
 * Reset to default data
 */
function resetToDefaultData() {
    localStorage.removeItem(STORAGE_KEY);
    seedDefaultData();
}

/**
 * Get category metadata
 */
function getCategoryLabel(category) {
    return CATEGORY_LABELS[category] || category;
}

function getCategoryIcon(category) {
    return CATEGORY_ICONS[category] || '📍';
}

function getCategoryColor(category) {
    return CATEGORY_COLORS[category] || '#6b7280';
}

// Export for module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        getLibraries, getLibraryById, saveLibrary, deleteLibrary,
        resetToDefaultData, seedDefaultData, getLibrariesByCategory,
        getCategoryLabel, getCategoryIcon, getCategoryColor,
        CATEGORIES, CATEGORY_LABELS, CATEGORY_ICONS, CATEGORY_COLORS
    };
}
