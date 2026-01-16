// YEP VOTING 2025 - Main JavaScript Utilities

// Smooth scroll behavior
document.documentElement.style.scrollBehavior = 'smooth';

// Add sparkle effect on page load
window.addEventListener('load', () => {
    createPageSparkles();
});

function createPageSparkles() {
    const count = 15;
    for (let i = 0; i < count; i++) {
        setTimeout(() => {
            const sparkle = document.createElement('div');
            sparkle.style.cssText = `
                position: fixed;
                width: 4px;
                height: 4px;
                background: white;
                border-radius: 50%;
                pointer-events: none;
                z-index: 9999;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                box-shadow: 0 0 10px white;
                animation: twinkle 1.5s ease-in-out;
            `;
            document.body.appendChild(sparkle);
            
            setTimeout(() => sparkle.remove(), 1500);
        }, i * 100);
    }
}

// Add twinkle animation
const style = document.createElement('style');
style.textContent = `
    @keyframes twinkle {
        0%, 100% { opacity: 0; transform: scale(0); }
        50% { opacity: 1; transform: scale(1); }
    }
`;
document.head.appendChild(style);

// Form validation helper
function validateForm(formId, rules) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    form.addEventListener('submit', (e) => {
        let isValid = true;
        
        for (const [fieldName, rule] of Object.entries(rules)) {
            const field = form.querySelector(`[name="${fieldName}"]`);
            if (!field) continue;
            
            if (rule.required && !field.value.trim()) {
                showError(field, rule.message || 'Trường này là bắt buộc');
                isValid = false;
            }
        }
        
        if (!isValid) {
            e.preventDefault();
        }
    });
}

function showError(field, message) {
    // Remove existing error
    const existingError = field.parentElement.querySelector('.field-error');
    if (existingError) existingError.remove();
    
    // Add new error
    const error = document.createElement('div');
    error.className = 'field-error';
    error.style.cssText = 'color: #fca5a5; font-size: 0.85em; margin-top: 6px;';
    error.textContent = message;
    field.parentElement.appendChild(error);
    
    // Highlight field
    field.style.borderColor = '#ef4444';
    
    // Remove error on input
    field.addEventListener('input', () => {
        error.remove();
        field.style.borderColor = '';
    }, { once: true });
}

// Lazy load images
function lazyLoadImages() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Call lazy load if images exist
if (document.querySelector('img[data-src]')) {
    lazyLoadImages();
}

// Keyboard navigation for vote cards
document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
        if (document.activeElement.classList.contains('vote-card') ||
            document.activeElement.classList.contains('employee-item')) {
            e.preventDefault();
            document.activeElement.click();
        }
    }
});

// Add focus styles for accessibility
const focusableElements = document.querySelectorAll(
    'button, a, input, .vote-card, .employee-item, .dept-card'
);

focusableElements.forEach(el => {
    el.addEventListener('focus', () => {
        el.style.outline = '2px solid #6366f1';
        el.style.outlineOffset = '3px';
    });
    
    el.addEventListener('blur', () => {
        el.style.outline = '';
        el.style.outlineOffset = '';
    });
});

// Prevent double submission
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn && !submitBtn.disabled) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loader"></span> Đang xử lý...';
            
            // Re-enable after 3 seconds as fallback
            setTimeout(() => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = submitBtn.dataset.originalText || 'Gửi';
            }, 3000);
        }
    });
});

// Save original button text
document.querySelectorAll('button[type="submit"]').forEach(btn => {
    btn.dataset.originalText = btn.innerHTML;
});

// Auto-refresh admin results every 10 seconds
if (window.location.pathname.includes('/admin/results/')) {
    setInterval(() => {
        // Only refresh if user hasn't scrolled
        if (window.scrollY < 100) {
            location.reload();
        }
    }, 10000);
}

// Console easter egg
console.log('%c🎉 YEP VOTING 2025', 'font-size: 24px; font-weight: bold; color: #6366f1;');
console.log('%cLuxury Digital Spotlight Design', 'font-size: 14px; color: #8b5cf6;');
console.log('%cDeveloped with ❤️', 'font-size: 12px; color: #ec4899;');