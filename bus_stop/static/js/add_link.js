document.addEventListener('DOMContentLoaded', () => {
    const rows = document.querySelectorAll('.dynamic-table tbody tr');

    rows.forEach(row => {
        row.addEventListener('click', () => {
            const href = row.getAttribute('data-href');
            if (href) {
                window.location.href = href;
            }
        });
    });
});
