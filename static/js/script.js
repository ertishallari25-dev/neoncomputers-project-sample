let currentCategory = 'All';

function toggleTheme() {
    document.body.classList.toggle('light-mode');
    const isLight = document.body.classList.contains('light-mode');
    const icon = document.querySelector('#theme-toggle i');
    if(isLight) {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
        document.querySelector('.navbar').classList.replace('navbar-dark', 'navbar-light');
    } else {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
        document.querySelector('.navbar').classList.replace('navbar-light', 'navbar-dark');
    }
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
}

if(localStorage.getItem('theme') === 'light') toggleTheme();

function navigateTo(pageId) {
    document.querySelectorAll('.page-section').forEach(s => s.classList.remove('active'));
    document.getElementById(pageId).classList.add('active');
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
    const link = document.getElementById('link-' + pageId);
    if(link) link.classList.add('active');
    window.scrollTo(0,0);
}

function scrollToProducts() {
    document.getElementById('products-area').scrollIntoView({behavior: 'smooth'});
}

function filterByCategory(cat, btn) {
    console.log("Filter requested for:", cat);
    // Frontend visual toggle only; Django does the real filtering
}

function handleSearch() { }

function resetFilters() { 
    window.location.href = "{% url 'home' %}";
}

function showToast(msg) {
    document.getElementById('toastMessage').textContent = msg;
    new bootstrap.Toast(document.getElementById('liveToast')).show();
}

function handleContactSubmit(e) {
    const f = document.getElementById('contactForm');
    if (!f.checkValidity()) {
        e.preventDefault();
        e.stopPropagation();
        f.classList.add('was-validated');
    }
}

// --- SEARCH FUNCTIONALITY (FIXED) ---
let searchTimeout;

function handleSearch() {
    clearTimeout(searchTimeout); // Reset timer
    
    searchTimeout = setTimeout(function() {
        const query = document.getElementById('searchInput').value;
        
        // ALWAYS redirect to Home page with search parameters
        if (query && query.trim() !== "") {
            window.location.href = "/?q=" + encodeURIComponent(query);
        } else {
            // If empty, just go to Home
            window.location.href = "/"; 
        }
    }, 500); // Wait 0.5 seconds before reloading
}