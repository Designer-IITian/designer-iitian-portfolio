// Comprehensive Scroll Animation (Intersection Observer)
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Select all major elements to animate
const animatedElements = document.querySelectorAll(`
    .hero-title, .hero-subtitle, .hero-description, .hero-actions, .floating-card,
    .section-label, .belief-title, .belief-text, .stat-item, .belief-actions,
    .contact-heading, .works-grid > *, .marquee-container, .cta-content > *,
    .contact-left > *, .contact-right, .footer-col
`);

animatedElements.forEach((el, index) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(40px)';
    
    // Add staggered delay based on DOM order or parent
    let delay = 0;
    if (el.classList.contains('floating-card')) {
        delay = (index % 3) * 0.2; // Stagger hero cards
    } else if (el.classList.contains('stat-item')) {
        delay = (index % 3) * 0.15; // Stagger stats
    } else if (el.classList.contains('work-card')) {
        delay = (index % 3) * 0.15; // Stagger grid items row by row
    } else {
        delay = 0.1; // Default slight delay
    }

    el.style.transition = `opacity 0.8s ease-out ${delay}s, transform 0.8s cubic-bezier(0.16, 1, 0.3, 1) ${delay}s`;
    observer.observe(el);
});

// Update active state in navigation based on scroll
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').includes(current)) {
            link.classList.add('active');
        }
    });
});

// Textarea Character Count
const messageTextarea = document.getElementById('message');
const currentCharSpan = document.getElementById('current-char');

if (messageTextarea && currentCharSpan) {
    messageTextarea.addEventListener('input', function() {
        const currentLength = this.value.length;
        currentCharSpan.textContent = currentLength;
    });
}

// Scroll to top functionality
const scrollTopBtn = document.querySelector('.scroll-top-btn');

if (scrollTopBtn) {
    // Show button when scrolled down
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 500) {
            scrollTopBtn.style.opacity = '1';
            scrollTopBtn.style.pointerEvents = 'auto';
        } else {
            scrollTopBtn.style.opacity = '0';
            scrollTopBtn.style.pointerEvents = 'none';
        }
    });

    scrollTopBtn.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Marquee Infinite Scroll with dynamic speed
const marqueeTrack = document.querySelector('.marquee-track');
if (marqueeTrack) {
    let currentX = 0;
    // Lower baseline speed
    let defaultSpeed = 0.5;
    let hoverSpeed = 0.15; // Slow down significantly, but don't stop
    let speed = defaultSpeed; 

    marqueeTrack.addEventListener('mouseenter', () => speed = hoverSpeed);
    marqueeTrack.addEventListener('mouseleave', () => speed = defaultSpeed);

    function animateMarquee() {
        currentX -= speed;
        // The reset point is the width of half the items + the gap
        // Since there are 12 items and 11 gaps, we add 1 gap (30px) to scrollWidth to get the exact halfway distance
        const resetPoint = (marqueeTrack.scrollWidth + 30) / 2;
        
        if (Math.abs(currentX) >= resetPoint) {
            currentX = 0;
        }
        marqueeTrack.style.transform = `translateX(${currentX}px)`;
        requestAnimationFrame(animateMarquee);
    }
    
    // Start animation
    animateMarquee();
}

// Custom Cursor Logic
const cursor = document.querySelector('.custom-cursor');
const workCards = document.querySelectorAll('.work-card');

if (cursor && workCards.length > 0) {
    // Track mouse movement
    document.addEventListener('mousemove', (e) => {
        // Use requestAnimationFrame for smoother performance
        requestAnimationFrame(() => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });
    });

    // Add hover effect for work cards
    workCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            cursor.classList.add('active');
        });
        
        card.addEventListener('mouseleave', () => {
            cursor.classList.remove('active');
        });
    });
}

// Contact Form Submission (Web3Forms)
const contactForm = document.getElementById('contactForm');
const formResult = document.getElementById('formResult');

if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(contactForm);
        const object = Object.fromEntries(formData);
        const json = JSON.stringify(object);

        formResult.innerHTML = "Sending message...";
        formResult.style.display = "block";
        formResult.style.color = "var(--text-secondary)";

        fetch('https://api.web3forms.com/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: json
        })
        .then(async (response) => {
            let json = await response.json();
            if (response.status == 200) {
                formResult.innerHTML = '<span style="color: #4CAF50;">Message sent successfully!</span> We will get back to you soon.';
                formResult.style.color = "var(--accent-gold)";
                contactForm.reset();
                const currentCharSpan = document.getElementById('current-char');
                if (currentCharSpan) currentCharSpan.textContent = '0';
            } else {
                console.log(response);
                formResult.innerHTML = json.message || "Something went wrong!";
                formResult.style.color = "red";
            }
        })
        .catch(error => {
            console.log(error);
            formResult.innerHTML = "Something went wrong!";
            formResult.style.color = "red";
        })
        .then(function() {
            setTimeout(() => {
                formResult.style.display = "none";
            }, 5000);
        });
    });
}
