/**
 * Clinic Legacy App - JavaScript
 * Handles interactivity and UX enhancements
 */

document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 5 seconds
    initAlertDismiss();
    
    // Initialize delete confirmations
    initDeleteConfirmations();
    
    // Set active nav link
    setActiveNavLink();
});

/**
 * Auto-dismiss alert messages after delay
 */
function initAlertDismiss() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        // Auto dismiss after 5 seconds
        setTimeout(() => {
            dismissAlert(alert);
        }, 5000);
        
        // Manual dismiss on click
        const closeBtn = alert.querySelector('.alert-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                dismissAlert(alert);
            });
        }
    });
}

function dismissAlert(alert) {
    alert.style.opacity = '0';
    alert.style.transform = 'translateY(-10px)';
    setTimeout(() => {
        alert.remove();
    }, 300);
}

/**
 * Confirm before delete actions
 */
function initDeleteConfirmations() {
    const deleteLinks = document.querySelectorAll('.delete-link, [data-confirm]');
    
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const message = this.dataset.confirm || 'Are you sure you want to delete this item?';
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });
}

/**
 * Set active navigation link based on current URL
 */
function setActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (currentPath === href || 
            (href !== '/' && currentPath.startsWith(href))) {
            link.classList.add('active');
        }
    });
}

/**
 * Form validation helper (optional enhancement)
 */
function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('[required]');
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.style.borderColor = 'var(--danger)';
        } else {
            input.style.borderColor = '';
        }
    });
    
    return isValid;
}
