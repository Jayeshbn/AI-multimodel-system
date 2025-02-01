document.addEventListener('DOMContentLoaded', () => {
    const mainContent = document.getElementById('main-content');

    // Function to load content dynamically
    const loadContent = async (model) => {
        const response = await fetch(`/load_model/${model}`);
        if (response.ok) {
            const content = await response.text();
            mainContent.innerHTML = content;
        } else {
            mainContent.innerHTML = '<p>Error loading content. Please try again.</p>';
        }
    };

    // Sidebar navigation
    document.querySelectorAll('.sidebar a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const model = e.target.getAttribute('data-model');
            if (model) {
                if (model === 'index') {
                    location.reload(); // Reload homepage
                } else {
                    loadContent(model);
                }
            }
        });
    });

    // Homepage model cards
    document.querySelectorAll('.card button').forEach(button => {
        button.addEventListener('click', () => {
            const model = button.closest('.card').getAttribute('data-model');
            if (model) {
                loadContent(model);
            }
        });
    });
});
