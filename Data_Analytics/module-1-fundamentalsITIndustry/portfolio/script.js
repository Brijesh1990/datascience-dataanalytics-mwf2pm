// Mobile Menu Toggle
const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');

if (menuBtn) {
    menuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });

    // Close menu when a link is clicked
    const menuLinks = mobileMenu.querySelectorAll('a');
    menuLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
        });
    });
}

// Form Handling
const contactForm = document.getElementById('contactForm');

if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // Get form data
        const formData = {
            name: this.querySelector('input[type="text"]').value,
            email: this.querySelector('input[type="email"]').value,
            subject: this.querySelector('input[type="text"]:nth-of-type(2)').value,
            message: this.querySelector('textarea').value
        };

        // Basic validation
        if (!formData.name || !formData.email || !formData.subject || !formData.message) {
            showMessage('Please fill in all fields', 'error');
            return;
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(formData.email)) {
            showMessage('Please enter a valid email address', 'error');
            return;
        }

        // Show success message
        showMessage('Thank you! Your message has been sent successfully. I\'ll get back to you soon!', 'success');

        // Reset form
        this.reset();

        // Log the data (in a real application, you would send this to a server)
        console.log('Form submitted:', formData);

        // You can send the form data to a server using fetch or XMLHttpRequest
        // Example:
        /*
        fetch('/api/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            showMessage('Message sent successfully!', 'success');
        })
        .catch(error => {
            showMessage('Error sending message. Please try again.', 'error');
            console.error('Error:', error);
        });
        */
    });
}

// Show message function
function showMessage(message, type) {
    // Create message element
    const messageDiv = document.createElement('div');
    messageDiv.className = type === 'success' ? 'success-message' : 'error-message';
    messageDiv.textContent = message;

    // Add to form container
    const formContainer = document.querySelector('#contactForm').parentElement;
    formContainer.insertBefore(messageDiv, document.querySelector('#contactForm'));

    // Remove message after 5 seconds
    setTimeout(() => {
        messageDiv.style.animation = 'fadeOutUp 0.5s ease-out forwards';
        setTimeout(() => messageDiv.remove(), 500);
    }, 5000);
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Intersection Observer for animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all elements with animation classes
document.querySelectorAll('.fade-in-up, .fade-in-left, .fade-in-right').forEach(el => {
    observer.observe(el);
});

// Add animation delay to skill bars on scroll
const skillBarsObserver = new IntersectionObserver(function(entries) {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            entry.target.style.setProperty('--animation-delay', (index * 0.1) + 's');
            entry.target.style.opacity = '1';
            entry.target.style.width = entry.target.getAttribute('style').match(/width:\s*(\d+%)/)[1];
        }
    });
}, observerOptions);

document.querySelectorAll('.skill-bar').forEach(bar => {
    skillBarsObserver.observe(bar);
});

// Add typing effect to hero title
function typeWriter(element, text, speed = 50) {
    let i = 0;
    element.textContent = '';

    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }

    type();
}

// Check if element exists before calling typeWriter
const heroTitle = document.querySelector('h1 span');
if (heroTitle) {
    // Only apply typewriter effect on desktop
    if (window.innerWidth > 768) {
        const originalText = heroTitle.textContent;
        typeWriter(heroTitle, originalText, 30);
    }
}

// Add hover effect to tool boxes
document.querySelectorAll('.tool-box').forEach(box => {
    box.addEventListener('mouseenter', function() {
        this.style.animation = 'pulse 0.6s ease-in-out';
    });

    box.addEventListener('mouseleave', function() {
        this.style.animation = 'none';
    });
});

// Handle stat counter animation
const statBoxes = document.querySelectorAll('.stat-box');
const counterObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
            const numberElement = entry.target.querySelector('.text-3xl');
            if (numberElement) {
                const finalNumber = parseInt(numberElement.textContent);
                countUp(numberElement, finalNumber);
                entry.target.classList.add('counted');
            }
            counterObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

statBoxes.forEach(box => counterObserver.observe(box));

// Count up animation function
function countUp(element, finalNumber, duration = 2000) {
    let currentNumber = 0;
    const increment = finalNumber / (duration / 16);
    const originalText = element.textContent;
    const suffix = originalText.match(/[^\d]/g)?.join('') || '';

    function updateNumber() {
        currentNumber += increment;
        if (currentNumber >= finalNumber) {
            element.textContent = finalNumber + suffix;
        } else {
            element.textContent = Math.floor(currentNumber) + suffix;
            requestAnimationFrame(updateNumber);
        }
    }

    updateNumber();
}

// Add parallax effect to hero section
window.addEventListener('scroll', function() {
    const scrollPosition = window.scrollY;
    const heroSection = document.getElementById('home');

    if (heroSection) {
        heroSection.style.backgroundPosition = `0 ${scrollPosition * 0.5}px`;
    }
});

// Active navigation link on scroll
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('a[href^="#"]');

    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('text-cyan-400');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('text-cyan-400');
        }
    });
});

// Lazy loading for images
if ('IntersectionObserver' in window) {
    const images = document.querySelectorAll('img');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.src || img.dataset.src;
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
    // Press 'M' to scroll to menu
    if (event.key === 'm' || event.key === 'M') {
        document.getElementById('home').scrollIntoView({ behavior: 'smooth' });
    }

    // Press 'C' to scroll to contact
    if (event.key === 'c' || event.key === 'C') {
        document.getElementById('contact').scrollIntoView({ behavior: 'smooth' });
    }
});

// Add loading animation to images
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.addEventListener('load', function() {
            this.style.opacity = '1';
        });
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.3s ease-in';
    });
});

// Prevent form submission errors
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        const submitBtn = this.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner spinner mr-2"></i>Sending...';

        // Simulate sending (replace with actual API call)
        setTimeout(() => {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Send Message';
        }, 1500);
    });
}

// Responsive adjustments
window.addEventListener('resize', function() {
    const mobileMenu = document.getElementById('mobileMenu');
    if (window.innerWidth > 768) {
        mobileMenu.classList.add('hidden');
    }
});

// Add click ripple effect to buttons
document.querySelectorAll('button, a[class*="btn"]').forEach(element => {
    element.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');

        this.appendChild(ripple);

        setTimeout(() => ripple.remove(), 600);
    });
});

// Add ripple CSS
const style = document.createElement('style');
style.textContent = `
    button, a[class*="btn"] {
        position: relative;
        overflow: hidden;
    }

    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s ease-out;
        pointer-events: none;
    }

    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Check if running on mobile
const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
if (isMobile) {
    document.body.classList.add('mobile');
}

console.log('Portfolio script loaded successfully!');
